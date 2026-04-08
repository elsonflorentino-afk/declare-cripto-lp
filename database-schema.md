# Banco de Dados — Lead Scoring & Inteligência

Arquitetura e schema do banco de dados para cruzar **leads**, **anúncios** e **comportamento** com um modelo de **lead scoring** inteligente.

---

## 🎯 Objetivo

Criar uma fonte única da verdade (single source of truth) que:

1. **Consolida dados** de múltiplas fontes (RD Station, Meta Ads, GA4, LPs)
2. **Rastreia a jornada completa** do lead (criativo → clique → LP → form → qualificação → conversão)
3. **Calcula lead scoring automaticamente** baseado em múltiplos sinais
4. **Permite dashboards em tempo real** com Metabase/Retool
5. **Alimenta decisões de mídia** — quais criativos geram leads qualificados

---

## 🏗️ Stack recomendada

### Supabase (recomendado ⭐)

**Por quê:**
- PostgreSQL gerenciado (free tier: 500MB + 2GB bandwidth/mês)
- API REST automática (gerada a partir do schema)
- Interface web para visualizar dados (Table Editor + SQL Editor)
- Autenticação + Row Level Security nativos
- Webhooks + Edge Functions (Deno)
- Realtime subscriptions
- Integração fácil com Retool, Metabase, Google Sheets

**Alternativas:**
| Opção | Prós | Contras |
|-------|------|---------|
| **Cloudflare D1** | Grátis, SQLite serverless, integra com Workers | SQLite tem limitações vs Postgres |
| **Airtable** | Visual, fácil para não-técnicos | Caro ao escalar, limite de rows |
| **Google Sheets + Apps Script** | Grátis, familiar | Performance ruim >10k rows |
| **PlanetScale** | MySQL serverless | Free tier limitado agora |
| **Neon** | Postgres serverless | Menos features vs Supabase |

### Arquitetura completa

```
┌─────────────────────────────────────────────────────┐
│  FONTES DE DADOS                                    │
├─────────────────────────────────────────────────────┤
│  RD Station API ───┐                                │
│  Meta Ads API  ────┤                                │
│  GA4 API       ────┼──► ETL / Webhooks              │
│  LP Forms      ────┤                                │
│  WhatsApp API  ────┘                                │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  SUPABASE (PostgreSQL)                              │
├─────────────────────────────────────────────────────┤
│  Tabelas:                                           │
│  - leads                                            │
│  - campaigns                                        │
│  - ads                                              │
│  - lead_events                                      │
│  - lead_scoring                                     │
│  - conversions                                      │
│                                                     │
│  Views materializadas:                              │
│  - v_lead_journey                                   │
│  - v_campaign_performance                           │
│  - v_creative_performance                           │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  CONSUMIDORES                                       │
├─────────────────────────────────────────────────────┤
│  - Metabase / Retool (dashboards)                   │
│  - Slack / Email (alertas de leads quentes)         │
│  - Meta Ads API (feedback de lead quality → CAPI)   │
│  - Comercial (priorização de follow-up)             │
└─────────────────────────────────────────────────────┘
```

---

## 📋 Schema SQL completo

### Tabela: `leads`

Armazena dados identificadores de cada lead.

```sql
CREATE TABLE leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rd_uuid TEXT UNIQUE,                  -- ID do RD Station
  email TEXT UNIQUE NOT NULL,
  name TEXT,
  phone TEXT,
  whatsapp TEXT,

  -- Perfil (do formulário da LP)
  investe_cripto BOOLEAN,
  patrimonio_cripto TEXT,               -- "Até R$ 10 mil", "Entre R$ 50 mil a R$ 200 mil", etc
  patrimonio_cripto_min_k NUMERIC,      -- 0, 10, 50, 200, 500, 1000 (em k)
  investe_tradicional BOOLEAN,
  patrimonio_tradicional TEXT,
  patrimonio_tradicional_min_k NUMERIC,

  -- Origem
  first_source TEXT,                    -- facebook, organic, direct, etc
  first_medium TEXT,
  first_campaign TEXT,
  first_content TEXT,                   -- ad_name
  first_term TEXT,

  -- Última interação
  last_source TEXT,
  last_medium TEXT,
  last_campaign TEXT,
  last_activity_at TIMESTAMPTZ,

  -- Scoring
  score INTEGER DEFAULT 0,              -- 0-100
  score_tier TEXT,                      -- cold, warm, hot, qualified
  score_updated_at TIMESTAMPTZ,

  -- Funnel
  funnel_stage TEXT DEFAULT 'lead',     -- lead, mql, sql, opportunity, customer
  is_qualified BOOLEAN DEFAULT FALSE,   -- ≥R$50k em qualquer (cripto OR trad)

  -- Timestamps
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_leads_email ON leads(email);
CREATE INDEX idx_leads_score ON leads(score DESC);
CREATE INDEX idx_leads_qualified ON leads(is_qualified);
CREATE INDEX idx_leads_created ON leads(created_at DESC);
CREATE INDEX idx_leads_rd_uuid ON leads(rd_uuid);
```

### Tabela: `campaigns`

Campanhas do Meta Ads (sincronizadas diariamente).

```sql
CREATE TABLE campaigns (
  id TEXT PRIMARY KEY,                  -- campaign_id do Meta
  name TEXT NOT NULL,
  status TEXT,                          -- ACTIVE, PAUSED, DELETED
  objective TEXT,
  daily_budget NUMERIC,
  lifetime_budget NUMERIC,
  start_date DATE,

  -- Métricas agregadas (atualizadas pelo ETL diário)
  total_spend NUMERIC DEFAULT 0,
  total_impressions INTEGER DEFAULT 0,
  total_clicks INTEGER DEFAULT 0,
  total_leads_meta INTEGER DEFAULT 0,   -- o que o Meta reporta
  total_leads_real INTEGER DEFAULT 0,   -- o que o RD efetivamente recebe

  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_campaigns_status ON campaigns(status);
```

### Tabela: `ads`

Anúncios individuais dentro de campanhas.

```sql
CREATE TABLE ads (
  id TEXT PRIMARY KEY,                  -- ad_id do Meta
  campaign_id TEXT REFERENCES campaigns(id),
  adset_id TEXT,
  name TEXT NOT NULL,                   -- ex: VID-METODO-NAOSORTE-LP-ANALISE
  creative_id TEXT,
  status TEXT,

  -- Tipo e formato
  ad_type TEXT,                         -- video, image, carousel, dynamic
  format TEXT,                          -- feed, stories, reels, etc

  -- Métricas agregadas (últimos 30 dias)
  spend_30d NUMERIC DEFAULT 0,
  impressions_30d INTEGER DEFAULT 0,
  clicks_30d INTEGER DEFAULT 0,
  leads_30d INTEGER DEFAULT 0,
  cpl_30d NUMERIC,
  ctr_30d NUMERIC,

  -- Lead quality (via cruzamento com leads qualificados)
  qualified_leads_30d INTEGER DEFAULT 0,
  qualified_rate NUMERIC,               -- % de qualificados
  cost_per_qualified_lead NUMERIC,

  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_ads_campaign ON ads(campaign_id);
CREATE INDEX idx_ads_name ON ads(name);
CREATE INDEX idx_ads_qualified_rate ON ads(qualified_rate DESC);
```

### Tabela: `lead_events`

Timeline de cada interação do lead (jornada completa).

```sql
CREATE TABLE lead_events (
  id BIGSERIAL PRIMARY KEY,
  lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,

  event_type TEXT NOT NULL,             -- pageview, cta_click, form_submit, whatsapp_click, ebook_download, etc
  event_source TEXT,                    -- lp_analise, lp_ir_cripto, webinar, ebook_pdf, etc

  -- Atribuição
  utm_source TEXT,
  utm_medium TEXT,
  utm_campaign TEXT,
  utm_content TEXT,                     -- ad_name
  utm_term TEXT,
  ad_id TEXT REFERENCES ads(id),
  campaign_id TEXT REFERENCES campaigns(id),

  -- Metadados adicionais
  page_url TEXT,
  referrer TEXT,
  user_agent TEXT,
  ip_address INET,

  -- Timestamp
  occurred_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_events_lead ON lead_events(lead_id, occurred_at DESC);
CREATE INDEX idx_events_type ON lead_events(event_type);
CREATE INDEX idx_events_ad ON lead_events(ad_id);
CREATE INDEX idx_events_occurred ON lead_events(occurred_at DESC);
```

### Tabela: `lead_scoring`

Histórico e componentes do score.

```sql
CREATE TABLE lead_scoring (
  id BIGSERIAL PRIMARY KEY,
  lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,

  -- Score total e componentes
  total_score INTEGER NOT NULL,
  patrimony_score INTEGER DEFAULT 0,    -- 0-40 (patrimônio declarado)
  engagement_score INTEGER DEFAULT 0,   -- 0-20 (cliques, pageviews, tempo)
  intent_score INTEGER DEFAULT 0,       -- 0-20 (WhatsApp, forms repetidos)
  source_score INTEGER DEFAULT 0,       -- 0-10 (qualidade da origem)
  recency_score INTEGER DEFAULT 0,      -- 0-10 (quão recente é a última interação)

  -- Razão do score
  reason JSONB,                         -- breakdown detalhado

  calculated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_scoring_lead ON lead_scoring(lead_id, calculated_at DESC);
```

### Tabela: `conversions`

Conversões chave do lead (form submitted, e-book baixado, análise agendada, vendido).

```sql
CREATE TABLE conversions (
  id BIGSERIAL PRIMARY KEY,
  lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,

  conversion_type TEXT NOT NULL,        -- form_submit, ebook_download, analysis_scheduled, customer, churned
  conversion_source TEXT,               -- lp_analise, webinar, etc
  conversion_value NUMERIC,             -- R$ (para customer)

  -- Atribuição do first touch
  first_touch_source TEXT,
  first_touch_campaign TEXT,
  first_touch_ad_id TEXT,

  -- Atribuição do last touch
  last_touch_source TEXT,
  last_touch_campaign TEXT,
  last_touch_ad_id TEXT,

  -- Tempo até conversão
  days_to_conversion INTEGER,           -- dias desde o primeiro evento

  converted_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_conversions_lead ON conversions(lead_id);
CREATE INDEX idx_conversions_type ON conversions(conversion_type);
CREATE INDEX idx_conversions_at ON conversions(converted_at DESC);
```

---

## 🧮 Algoritmo de Lead Scoring

### Componentes (total 0-100)

| Componente | Peso | Cálculo |
|------------|------|---------|
| **Patrimônio** | 0-40 | Baseado em faixa declarada no form |
| **Engajamento** | 0-20 | Pageviews, tempo na LP, cliques |
| **Intenção** | 0-20 | WhatsApp click, múltiplos forms, ebook download |
| **Origem** | 0-10 | Qualidade do canal (paid > organic > direct) |
| **Recência** | 0-10 | Quão recente é a última interação |

### Tabela de patrimônio (componente mais importante)

```sql
-- Função PL/pgSQL para calcular patrimony_score
CREATE OR REPLACE FUNCTION calc_patrimony_score(
  p_cripto_min_k NUMERIC,
  p_trad_min_k NUMERIC
) RETURNS INTEGER AS $$
DECLARE
  max_patrimony NUMERIC;
  score INTEGER;
BEGIN
  max_patrimony := GREATEST(COALESCE(p_cripto_min_k, 0), COALESCE(p_trad_min_k, 0));

  IF max_patrimony >= 1000 THEN score := 40;       -- ≥R$1M
  ELSIF max_patrimony >= 500 THEN score := 35;     -- R$500k-1M
  ELSIF max_patrimony >= 200 THEN score := 28;     -- R$200k-500k
  ELSIF max_patrimony >= 100 THEN score := 22;     -- R$100k-200k (MÍNIMO QUALIFICADO)
  ELSIF max_patrimony >= 50 THEN score := 15;      -- R$50k-100k
  ELSIF max_patrimony >= 10 THEN score := 8;       -- R$10k-50k
  ELSE score := 2;                                 -- <R$10k
  END IF;

  RETURN score;
END;
$$ LANGUAGE plpgsql;
```

### Tiers de classificação

```sql
CREATE OR REPLACE FUNCTION calc_score_tier(p_total_score INTEGER)
RETURNS TEXT AS $$
BEGIN
  IF p_total_score >= 75 THEN RETURN 'qualified';   -- Lead quente qualificado
  ELSIF p_total_score >= 50 THEN RETURN 'hot';      -- Lead quente
  ELSIF p_total_score >= 30 THEN RETURN 'warm';     -- Lead morno
  ELSE RETURN 'cold';                                -- Lead frio
  END IF;
END;
$$ LANGUAGE plpgsql;
```

### Trigger para recalcular score automaticamente

```sql
CREATE OR REPLACE FUNCTION update_lead_score()
RETURNS TRIGGER AS $$
DECLARE
  v_patrimony_score INTEGER;
  v_engagement_score INTEGER;
  v_intent_score INTEGER;
  v_source_score INTEGER;
  v_recency_score INTEGER;
  v_total_score INTEGER;
BEGIN
  -- Patrimônio
  v_patrimony_score := calc_patrimony_score(
    NEW.patrimonio_cripto_min_k,
    NEW.patrimonio_tradicional_min_k
  );

  -- Engajamento (count eventos)
  SELECT LEAST(20, COUNT(*) * 2) INTO v_engagement_score
  FROM lead_events
  WHERE lead_id = NEW.id AND event_type IN ('pageview', 'cta_click');

  -- Intenção (ações de alto valor)
  SELECT LEAST(20,
    (COUNT(*) FILTER (WHERE event_type = 'whatsapp_click')) * 5 +
    (COUNT(*) FILTER (WHERE event_type = 'ebook_download')) * 5 +
    (COUNT(*) FILTER (WHERE event_type = 'form_submit')) * 3
  ) INTO v_intent_score
  FROM lead_events WHERE lead_id = NEW.id;

  -- Origem (paid > organic > direct)
  v_source_score := CASE
    WHEN NEW.first_source = 'facebook' THEN 10
    WHEN NEW.first_source = 'google' THEN 9
    WHEN NEW.first_source = 'organic' THEN 6
    WHEN NEW.first_source = 'direct' THEN 4
    ELSE 5
  END;

  -- Recência
  v_recency_score := CASE
    WHEN NEW.last_activity_at >= NOW() - INTERVAL '1 day' THEN 10
    WHEN NEW.last_activity_at >= NOW() - INTERVAL '7 days' THEN 7
    WHEN NEW.last_activity_at >= NOW() - INTERVAL '30 days' THEN 4
    ELSE 1
  END;

  -- Total
  v_total_score := v_patrimony_score + v_engagement_score + v_intent_score + v_source_score + v_recency_score;

  NEW.score := v_total_score;
  NEW.score_tier := calc_score_tier(v_total_score);
  NEW.score_updated_at := NOW();
  NEW.is_qualified := (COALESCE(NEW.patrimonio_cripto_min_k, 0) >= 50 OR COALESCE(NEW.patrimonio_tradicional_min_k, 0) >= 50);

  -- Salvar histórico
  INSERT INTO lead_scoring (
    lead_id, total_score,
    patrimony_score, engagement_score, intent_score, source_score, recency_score,
    reason
  ) VALUES (
    NEW.id, v_total_score,
    v_patrimony_score, v_engagement_score, v_intent_score, v_source_score, v_recency_score,
    jsonb_build_object(
      'patrimony', v_patrimony_score,
      'engagement', v_engagement_score,
      'intent', v_intent_score,
      'source', v_source_score,
      'recency', v_recency_score
    )
  );

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_lead_score
BEFORE UPDATE ON leads
FOR EACH ROW
EXECUTE FUNCTION update_lead_score();
```

---

## 📊 Views para dashboards

### Jornada completa do lead

```sql
CREATE MATERIALIZED VIEW v_lead_journey AS
SELECT
  l.id,
  l.email,
  l.name,
  l.score,
  l.score_tier,
  l.is_qualified,
  l.patrimonio_cripto,
  l.patrimonio_tradicional,

  -- First touch
  l.first_source,
  l.first_campaign,
  l.first_content AS first_ad_name,

  -- Timeline
  MIN(e.occurred_at) AS first_event_at,
  MAX(e.occurred_at) AS last_event_at,
  COUNT(e.id) AS total_events,

  -- Conversões
  bool_or(c.conversion_type = 'form_submit') AS submitted_form,
  bool_or(c.conversion_type = 'ebook_download') AS downloaded_ebook,
  bool_or(c.conversion_type = 'analysis_scheduled') AS scheduled_analysis,
  bool_or(c.conversion_type = 'customer') AS became_customer,

  l.created_at AS lead_created_at
FROM leads l
LEFT JOIN lead_events e ON e.lead_id = l.id
LEFT JOIN conversions c ON c.lead_id = l.id
GROUP BY l.id;

CREATE UNIQUE INDEX ON v_lead_journey (id);
```

### Performance por criativo

```sql
CREATE MATERIALIZED VIEW v_creative_performance AS
SELECT
  a.id,
  a.name,
  a.campaign_id,
  a.spend_30d,
  a.leads_30d,
  a.cpl_30d,
  a.ctr_30d,

  -- Cruzamento com leads qualificados (via cf_utm_content)
  COUNT(DISTINCT l.id) FILTER (WHERE l.is_qualified) AS qualified_leads,
  COUNT(DISTINCT l.id) AS total_leads_tracked,

  -- Taxa de qualificação real
  ROUND(
    COUNT(DISTINCT l.id) FILTER (WHERE l.is_qualified)::NUMERIC
    / NULLIF(COUNT(DISTINCT l.id), 0) * 100,
    2
  ) AS qualified_rate_pct,

  -- CPL qualificado
  ROUND(
    a.spend_30d / NULLIF(COUNT(DISTINCT l.id) FILTER (WHERE l.is_qualified), 0),
    2
  ) AS cost_per_qualified_lead

FROM ads a
LEFT JOIN leads l ON l.first_content = a.name
GROUP BY a.id, a.name, a.campaign_id, a.spend_30d, a.leads_30d, a.cpl_30d, a.ctr_30d;

CREATE UNIQUE INDEX ON v_creative_performance (id);
```

---

## 🔄 ETL (Sincronização de dados)

### Fontes e frequência

| Fonte | Dados | Frequência | Método |
|-------|-------|------------|--------|
| **RD Station API** | Leads + eventos | A cada 15 min | Cron + API |
| **Meta Ads API** | Campanhas, ads, métricas | A cada 1 hora | Cron + API |
| **GA4 API** | Pageviews, sessions | Diário | Cron + API |
| **Webhook LPs** | Form submits | Tempo real | Webhook → Supabase Edge Function |

### Edge Function exemplo (Supabase)

```typescript
// supabase/functions/sync-rd-station/index.ts
import { serve } from 'https://deno.land/std/http/server.ts'
import { createClient } from '@supabase/supabase-js'

serve(async (req) => {
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
  )

  // 1. Buscar token RD (refresh)
  const rdToken = await refreshRdToken()

  // 2. Listar contatos últimos 15 min
  const contacts = await fetchRdContacts(rdToken, new Date(Date.now() - 15*60*1000))

  // 3. Para cada contato, buscar detalhes (cf_utm_*, cf_patrimonio_*)
  for (const c of contacts) {
    const details = await fetchContactDetails(rdToken, c.uuid)

    // 4. Upsert no Supabase
    await supabase.from('leads').upsert({
      rd_uuid: details.uuid,
      email: details.email,
      name: details.name,
      phone: details.mobile_phone,
      investe_cripto: details.cf_voce_ja_possui_investimentos_em_bitcoin_cripto === 'sim',
      patrimonio_cripto: details.cf_que_otimo_agora_preciso_entender_qual_seu_patrimonio_ho,
      patrimonio_cripto_min_k: parsePatrimony(details.cf_que_otimo_agora_preciso_entender_qual_seu_patrimonio_ho),
      first_source: details.cf_utm_source,
      first_campaign: details.cf_utm_campaign,
      first_content: details.cf_utm_content,
    }, { onConflict: 'email' })
  }

  return new Response('OK', { status: 200 })
})

function parsePatrimony(faixa: string): number {
  if (!faixa) return 0
  if (faixa.includes('Até R$ 10 mil')) return 0
  if (faixa.includes('Entre R$ 10 mil e R$ 50 mil')) return 10
  if (faixa.includes('Entre R$ 50 mil a R$ 200 mil')) return 50
  if (faixa.includes('Entre R$ 200 mil e R$500 mil')) return 200
  if (faixa.includes('Acima de R$500 mil')) return 500
  if (faixa.includes('1 milhão')) return 1000
  return 0
}
```

---

## 📈 Dashboards recomendados

### 1. Panorama geral (CEO)
- Total leads / qualificados / customers
- ROI por canal
- Funil de conversão (lead → qualified → customer)
- Cohort retention

### 2. Performance de mídia (@cris)
- Ads ordenados por `cost_per_qualified_lead`
- Criativos vencedores vs perdedores
- Comparativo de campanhas (C4 vs C5)
- Alertas: CPL subindo, CTR caindo

### 3. Lead quality (@pm)
- Distribuição de leads por tier (cold/warm/hot/qualified)
- Tempo médio de jornada até conversão
- Drop-off por etapa do funil
- Taxa de qualificação por origem

### 4. Comercial
- Leads `qualified` ordenados por score (priorização)
- Alertas de leads com `score >= 75` que não foram contatados
- Timeline completa de cada lead
- SLA de contato

---

## 🚀 Como começar (setup passo a passo)

### 1. Criar conta Supabase
1. Acesse [supabase.com](https://supabase.com)
2. Sign up com GitHub
3. **New project** → nome: `boost-leads`
4. Escolha região: **São Paulo (sa-east-1)**
5. Defina senha do banco e salve

### 2. Criar o schema
1. Vai em **SQL Editor** no menu lateral
2. Cole o SQL completo desse documento (tabelas + funções + triggers)
3. Run

### 3. Obter credenciais
- Vai em **Project Settings** → **API**
- Copia:
  - `URL` (ex: `https://abcxyz.supabase.co`)
  - `anon key` (pública)
  - `service_role key` (secreta — NÃO expor no front)

### 4. Configurar ETL
**Opção A — Supabase Edge Functions** (recomendado)
- Deploy via dashboard Supabase
- Cron via [cron.hookdeck.com](https://cron.hookdeck.com)

**Opção B — GitHub Actions**
- Workflow `.github/workflows/sync-rd.yml` rodando a cada 15 min
- Chama script Python que sincroniza RD → Supabase

### 5. Conectar dashboards
- **Metabase Cloud** (grátis para 5 usuários)
  - Dashboard → Add Data Source → PostgreSQL
  - URL, user, password do Supabase
- **Retool** — mais polido, $10/usuário
- **Supabase Dashboard** — já vem básico gratuito

---

## 💰 Custos estimados

| Serviço | Free tier | Paid se precisar |
|---------|-----------|------------------|
| **Supabase** | 500MB + 2GB bw | $25/mês (Pro: 8GB + 50GB bw) |
| **Metabase Cloud** | 5 usuários | $85/mês |
| **Cron (Hookdeck)** | 100k requests/mês | Grátis até escalar |
| **GitHub Actions** | 2000 min/mês | Grátis |
| **Total mensal (start)** | **R$ 0** | ~R$ 600/mês ao escalar |

---

## 📋 Próximos passos

1. **[ ]** Criar conta no Supabase
2. **[ ]** Rodar o schema SQL completo
3. **[ ]** Criar Edge Function para sincronizar RD Station
4. **[ ]** Criar Edge Function para sincronizar Meta Ads
5. **[ ]** Configurar cron de 15 min
6. **[ ]** Conectar Metabase
7. **[ ]** Criar 4 dashboards principais
8. **[ ]** Backfill histórico (últimos 90 dias)
9. **[ ]** Validar lead scoring com amostra manual
10. **[ ]** Treinar equipe comercial

**Tempo estimado:** 3-5 dias de implementação, +1 semana de ajuste fino.

---

*Documento criado em 08/abr/2026 — Boost Research Creative Squad*
