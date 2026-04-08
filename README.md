# Boost Research — Projetos Digitais

Repositório central de landing pages, dashboards e assets digitais da **Boost Research**.

## 🌐 Painel Central

📊 **[Acessar painel de LPs →](./lps-index.html)**

---

## 📂 Estrutura do Repositório

### Landing Pages
| LP | URL | Status | Pasta |
|----|-----|--------|-------|
| LP Análise de Carteira | analise.boostresearch.com.br | 🟢 Ativa | (produção direta) |
| LP IR Cripto 2026 | lp-ir-cripto.boostresearch.com.br | 🟢 Ativa | (produção direta) |
| Quiz Patrimônio | diagnostico.boostresearch.com.br | 🟢 Ativa | (produção direta) |
| LP Patrimônio | patrimonio.boostresearch.com.br | 🟢 Ativa | (produção direta) |
| Site Institucional | boostresearch.com.br | 🟢 Ativa | (produção direta) |
| **Webinar R$1 Milhão** | webinar.boostresearch.com.br | 🟡 Staging | `/webinar-1milhao/` |

### Dashboards
- `relatorio_marco_2026_boost.html` — Relatório completo de performance Meta Ads
- `apresentacao_marco_2026.html` — Slides visuais da apresentação
- `otimizacao_c4_abril_2026.html` — Diagnóstico e otimização C4
- `dashboard_ir_cripto.html` — Dashboard campanha IR Cripto
- `dashboard_consultoria_boost.html` — Dashboard consultoria
- `dashboard_top_criativos.html` — Top criativos

### Documentação
- `copys_c4_renovacao_abril_2026.md` — Copys @vera para C4 abril
- `apresentacao_marco_2026.md` — Roteiro de apresentação

---

## 🎯 Tracking

Todas as LPs usam a mesma infraestrutura:

| Sistema | ID |
|---------|-----|
| **GTM** | `GTM-K2HT6HBX` |
| **Meta Pixel** | `1062572485162288` |
| **GA4** | `G-CWXD04LK39` |
| **sGTM + CAPI** | `sgtm.boostresearch.com.br` |
| **RD Station** | Via API pública |

### Eventos padrão no dataLayer
- `generate_lead` — conversão de formulário
- `cta_click` — cliques em CTAs
- `whatsapp_click` — cliques no WhatsApp flutuante
- `youtube_click` — cliques no canal
- `ebook_cta_click` — cliques em CTAs dentro de PDFs

---

## 🎨 Design System

### Cores oficiais
```css
:root {
  --bg: #000000;
  --bg2: #0A0A14;
  --bg3: #0D1020;
  --green: #00B37E;      /* Accent principal */
  --green-bright: #00D195;
  --white: #FFFFFF;
  --gray: #A0A0C0;
  --gray-dim: #3A3A5C;
  --red: #FF4444;
}
```

### Tipografia
- **Inter** (400, 500, 600, 700, 800, 900) via Google Fonts
- Preload non-blocking para performance

### Logo
- Arquivo oficial: `boost-logo-horizontal.svg`
- Variações: Light (branco), Dark (preto), Small (ícone apenas)

---

## 🚀 Deploy

### Cloudflare Pages (via navegador)

1. Acesse [dash.cloudflare.com](https://dash.cloudflare.com)
2. Vai em **Workers & Pages** → **Create application** → **Pages**
3. **Connect to Git** → selecione este repositório
4. Configurações:
   - **Build command:** (vazio)
   - **Build output directory:** `/`
   - **Production branch:** `main`
5. **Save and Deploy**

### Custom domains
Cada LP tem seu subdomínio configurado como CNAME:
- `webinar.boostresearch.com.br` → Pages project `webinar-1milhao`
- `analise.boostresearch.com.br` → Pages project `analise`
- etc.

---

## 🏗️ Arquitetura de Banco de Dados (planejado)

Ver documento: [`database-schema.md`](./database-schema.md)

**Stack recomendada:**
- **Supabase** (PostgreSQL gerenciado + API REST automática)
- **Conexões:** RD Station (leads) + Meta Ads API (campanhas) + GA4 (comportamento)
- **Lead scoring:** algoritmo multi-variável baseado em patrimônio, origem, engajamento

---

## 📋 Convenções

### Nomenclatura de arquivos
- LPs: `index.html` dentro de pasta com nome-kebab-case
- Dashboards: `dashboard_{tema}_{data}.html`
- Relatórios: `relatorio_{mes}_{ano}_boost.html`
- Copys: `copys_{campanha}_{mes}_{ano}.md`

### Commits
- `feat:` nova feature/LP
- `fix:` correção de bug
- `docs:` mudanças de documentação
- `design:` mudanças visuais
- `perf:` otimização de performance

---

## 📞 Contato

**Boost Research** — Casa de análise de criptoativos
- Site: [boostresearch.com.br](https://boostresearch.com.br)
- WhatsApp: (21) 96562-2891
- YouTube: [@boostresearch](https://www.youtube.com/@boostresearch)
