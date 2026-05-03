# Briefing LinkedIn Ads — Fenix DFA (Prioridade 1: CIO/CISO)

**Data:** 03/maio/2026
**Cliente:** Fenix DFA (fenixdfa.com)
**Canal:** LinkedIn Ads — Sponsored Content com Lead Gen Form
**Audiência:** CIOs, CISOs, VPs of Infrastructure, Heads of IT Security
**Conversão:** Download do Executive One-Pager (Lead Gen Form)
**Budget:** Limitado — otimizar para menor CPL possível
**Entregas:** 3 peças estáticas (1200x628px)

---

## Estratégia — Otimização de budget

O cliente tem pouco orçamento. Para maximizar cada real:

**Formato:** LinkedIn Lead Gen Form (NÃO landing page)
- Lead preenche dentro do LinkedIn (sem sair da plataforma)
- Campos pré-preenchidos pelo LinkedIn (nome, email, cargo, empresa)
- Material para download: Executive One-Pager (PDF)
- CPL estimado: R$30-80 (vs R$100-200 com LP)

**Fluxo:**
```
Anúncio no feed → Lead Gen Form (nome, email, cargo, empresa)
→ Download automático do One-Pager → Follow-up por email (nurture)
→ Resilience Assessment (call com vendas)
```

**Por que Lead Gen Form e não LP:**
- Taxa de conversão 2-5x maior (campos pré-preenchidos)
- Sem fricção de carregamento de página
- Ideal para budget limitado

---

## Mensagem central (do OnePager)

> "Most companies discover their backup doesn't work during a ransomware attack. Fenix DFA finds that out first."

**Tradução para os criativos:** A empresa acha que está protegida. Não está. A Fenix DFA mostra onde estão as falhas ANTES do incidente.

---

## Identidade Visual

| Item | Valor |
|------|-------|
| Logo | Fenix DFA (arquivo: `~/Downloads/Fenix-DFA-Logo.svg` e `.png`) |
| Logo fundo azul | `~/Downloads/Fenix-Logo-Preview-FundoAzul.png` |
| Logo transparente | `~/Downloads/Fenix-DFA-Logo-Transparente.png` |
| Cor primária | Laranja Fenix (#E8551B — extraído do OnePager) |
| Cor fundo | Escuro (#1A1A2E) ou branco (testar ambos) |
| Cor texto | Branco (fundo escuro) ou preto (fundo claro) |
| Accent | Amber (#F59E0B) para badges/CTAs |
| Font | Sans-serif enterprise (Inter, Helvetica Neue) |

---

## Specs LinkedIn Ads

| Item | Spec |
|------|------|
| Dimensão imagem | 1200 x 628px (landscape) |
| Formato | JPG ou PNG |
| Tamanho máximo | 5MB |
| Headline do anúncio | Máx 70 caracteres |
| Texto introdutório | Máx 150 palavras (recomendado curto) |
| CTA do Lead Gen Form | "Download" |

---

## CRIATIVO 1 — Silent Failures

### Conceito visual
**FALHA SILENCIOSA.** Tudo parece ok na superfície, mas por dentro está quebrado. A imagem transmite falsa normalidade — o console mostra verde, mas o recovery já falhou. Tons escuros, iluminação vermelha, atmosfera de data center em alerta silencioso.

### Imagens para o designer baixar (gratuitas)

| # | Imagem | URL | Como usar |
|---|--------|-----|-----------|
| 1 | Sala de servidores com luz vermelha | [Unsplash — Server room red](https://unsplash.com/photos/a-red-server-room-GNcCXtQ5oxk) | Fundo com overlay escuro 70%. Texto headline por cima |
| 2 | Data center com luzes vermelhas | [Unsplash — Red lights room](https://unsplash.com/photos/a-room-that-has-red-lights-in-it-TaTSi2ljyPA) | Alternativa mais dramática. Mesmo uso |
| 3 | Data center futurista azul | [Unsplash — Blue server room](https://unsplash.com/photos/futuristic-server-room-lit-with-blue-lights-CuZ8VdwRpyk) | Para versão mais fria/tech. Contraste com alerta vermelho no texto |
| 4 | Vidro rachado fundo preto | [Unsplash — Cracked glass](https://unsplash.com/photos/a-cracked-glass-window-with-a-black-background-_5e0bUpum24) | Metáfora: parece inteiro mas está rachado. Overlay com headline |
| 5 | Iceberg (risco oculto) | [Unsplash — Iceberg](https://unsplash.com/photos/a-large-iceberg-in-the-middle-of-the-ocean-n2qV323Fitc) | Metáfora clássica: o problema visível é pequeno, o real está submerso |

**Coleções extras:** [Server room dark (Pexels)](https://www.pexels.com/search/server%20room%20dark/) · [Cracked glass (Unsplash)](https://unsplash.com/s/photos/cracked-glass)

### Referências de LinkedIn Ads (ver na Ad Library)
- **CrowdStrike** → [Ad Library](https://www.linkedin.com/ad-library/?q=CrowdStrike) — Fundo dark, tipografia bold branca, dados de ameaça em destaque, vermelho como alerta
- **Datadog** → [Ad Library](https://www.linkedin.com/ad-library/?q=Datadog) — Dashboard de observabilidade como elemento central, fundo escuro
- **Splunk** → [Ad Library](https://www.linkedin.com/ad-library/?q=Splunk) — Infográficos de segurança, fundo degradê escuro

### Texto do post LinkedIn
**Headline:** Seus backups estão quebrando em silêncio.

**Texto introdutório:**
Assets saem de cobertura. Schedulers suspendem e nunca retomam. Retenção encolhe sem aprovação. O console mostra verde — mas o recovery já está quebrado.

A maioria das empresas descobre isso durante o incidente. A Fenix DFA descobre antes.

Baixe o Executive One-Pager e veja os 3 riscos que executivos não podem ignorar.

### Imagem (1200x628)

**Layout sugerido — opção A (fundo escuro):**
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  ⚠  SEUS BACKUPS ESTÃO                             │
│     QUEBRANDO EM SILÊNCIO.                          │
│                                                     │
│  O console mostra verde.                            │
│  O recovery já está quebrado.                       │
│                                                     │
│  ┌──────────────────────┐                           │
│  │ DOWNLOAD ONE-PAGER → │  (badge laranja)          │
│  └──────────────────────┘                           │
│                                                     │
│  FENIX DFA                        fenixdfa.com      │
└─────────────────────────────────────────────────────┘
```

**Elementos visuais:**
- Fundo: escuro (#1A1A2E) com gradiente sutil
- Ícone de alerta (⚠) em laranja Fenix grande no topo
- Headline em branco, bold, 2 linhas
- Subtítulo em cinza claro, 2 linhas
- Badge "DOWNLOAD ONE-PAGER →" em laranja (#E8551B)
- Logo Fenix DFA canto inferior esquerdo
- URL canto inferior direito
- SEM foto, SEM imagem de banco — apenas tipografia + ícone (mais limpo, mais enterprise)

**Layout sugerido — opção B (com imagem):**
- Lado esquerdo (55%): texto sobre fundo escuro
- Lado direito (45%): imagem de dashboard/monitoramento com indicadores verdes mas um alerta vermelho escondido
- Imagem: buscar "monitoring dashboard false positive", "server monitoring green status"

### Lead Gen Form
- Headline: "Baixe o Executive One-Pager"
- Descrição: "Veja os 3 riscos que CIOs e CISOs não podem ignorar sobre operações de backup."
- Campos: Nome (pré-preenchido), Email (pré-preenchido), Cargo (pré-preenchido), Empresa (pré-preenchido)
- CTA: "Download"
- Política de privacidade: fenixdfa.com/privacy
- Thank you: link para o PDF do One-Pager

---

## CRIATIVO 2 — Regulatory Exposure

### Conceito visual
**PRESSÃO REGULATÓRIA.** Peso institucional, seriedade, consequência legal. Transmitir a sensação de "auditoria iminente" — o regulador pede provas e você precisa tê-las na hora. Tons sóbrios (preto, cinza, dourado/bronze para autoridade). Elementos: martelo de juiz, documentos, badges de regulação.

### Imagens para o designer baixar (gratuitas)

| # | Imagem | URL | Como usar |
|---|--------|-----|-----------|
| 1 | Martelo de juiz + livro (fundo escuro) | [Unsplash — Gavel dark](https://unsplash.com/photos/wooden-gavel-resting-on-a-dark-surface-next-to-book-FaTLrG5-ViE) | Lado direito da composição. Texto + badges regulatórios à esquerda |
| 2 | Martelo minimalista fundo escuro | [Unsplash — Gavel minimal](https://unsplash.com/photos/a-wooden-gavel-rests-on-a-dark-surface-T69Smz0SJ6w) | Mais limpo, ideal para composição com muito texto |
| 3 | Martelo sobre livro fechado | [Unsplash — Gavel book](https://unsplash.com/photos/a-wooden-gavel-rests-on-a-closed-book-NB1dUts3ROU) | Autoridade + conhecimento |

**Coleções extras:** [Legal compliance (Unsplash)](https://unsplash.com/s/photos/legal-compliance) · [Compliance (Pexels)](https://www.pexels.com/search/compliance/) · [Digital law (Unsplash)](https://unsplash.com/s/photos/digital-law)

### Referências de LinkedIn Ads (ver na Ad Library)
- **OneTrust** → [Ad Library](https://www.linkedin.com/ad-library/?q=OneTrust) — Escudo/check em fundo azul-marinho, badges de certificação (SOC 2, ISO 27001, GDPR)
- **Vanta** → [Ad Library](https://www.linkedin.com/ad-library/?q=Vanta) — Minimalista, backgrounds escuros, checkmarks verdes de compliance automatizado
- **TrustArc** → [Ad Library](https://www.linkedin.com/ad-library/?q=TrustArc) — Gráficos de frameworks regulatórios, timelines de compliance

### Texto do post LinkedIn
**Headline:** Reguladores não aceitam screenshots. Exigem evidência contínua.

**Texto introdutório:**
DORA. NIS2. GDPR. ISO 27001. SOX.

Todos exigem evidência contínua e auditável de que seus dados podem ser recuperados. Não um relatório montado na véspera da auditoria.

A Fenix DFA gera documentação de compliance automatizada, timestamped e defensible. Disponível on demand — não reunida em pânico.

Baixe o Executive One-Pager.

### Imagem (1200x628)

**Layout sugerido:**
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  DORA · NIS2 · GDPR · ISO 27001 · SOX              │
│  (em laranja, espaçados, como badges)               │
│                                                     │
│  REGULADORES NÃO ACEITAM                            │
│  SCREENSHOTS.                                       │
│  EXIGEM EVIDÊNCIA CONTÍNUA.                         │
│                                                     │
│  ┌──────────────────────┐                           │
│  │ DOWNLOAD ONE-PAGER → │                           │
│  └──────────────────────┘                           │
│                                                     │
│  FENIX DFA                        fenixdfa.com      │
└─────────────────────────────────────────────────────┘
```

**Elementos visuais:**
- Topo: badges dos frameworks regulatórios em linha (DORA, NIS2, GDPR, ISO 27001, SOX) — cada um em caixa com borda laranja
- Headline em branco, bold, 3 linhas
- A palavra "SCREENSHOTS" pode ter um efeito de risco/tachado (strikethrough) sutil
- Badge download em laranja
- Fundo escuro
- Logo + URL no rodapé

**Alternativa com imagem:**
- Documento de compliance com carimbo "REJECTED" em vermelho
- Buscar: "compliance audit rejected", "regulatory document stamp failed"

---

## CRIATIVO 3 — Accountability

### Conceito visual
**ESCALAÇÃO DE RESPONSABILIDADE.** A responsabilidade sobe na hierarquia até o board. Tensão corporativa, peso da decisão. A imagem evoca "a reunião que ninguém quer ter" — quando o board pergunta "quem era responsável?" e não tem resposta. Sala vazia = alguém vai ser responsabilizado. Dominós = efeito cascata.

### Imagens para o designer baixar (gratuitas)

| # | Imagem | URL | Como usar |
|---|--------|-----|-----------|
| 1 | Sala de reunião vazia | [Unsplash — Empty meeting room](https://unsplash.com/photos/empty-meeting-room-6MtJ-y1hzTs) | Fundo com overlay escuro. A cadeira vazia = quem responde? |
| 2 | Coleção boardrooms vazias | [Unsplash — Empty boardroom](https://unsplash.com/s/photos/empty-boardroom) | 45 fotos. Escolher a mais tensa/corporativa |
| 3 | Dominós caindo | [Unsplash — Domino effect](https://unsplash.com/s/photos/domino-effect) | Metáfora de escalação. Efeito cascata |
| 4 | Reuniões executivas | [Unsplash — Board meeting](https://unsplash.com/s/photos/board-meeting) | Executivos com expressão séria, pressão |

**Coleções extras:** [Empty meeting room (Unsplash)](https://unsplash.com/s/photos/empty-meeting-room) · [Chain reaction (Unsplash)](https://unsplash.com/s/photos/chain-reaction)

### Referências de LinkedIn Ads (ver na Ad Library)
- **Rubrik** → [Ad Library](https://www.linkedin.com/ad-library/?q=Rubrik) — "Cyber resilience", gráficos de recovery time, tons escuros com verde
- **Veeam** → [Ad Library](https://www.linkedin.com/ad-library/?q=Veeam) — Mensagem direta sobre recovery, ângulo "o que acontece quando você NÃO tem backup"
- **ServiceNow** → [Ad Library](https://www.linkedin.com/ad-library/?q=ServiceNow) — Hierarquias visuais (org charts), "board-level visibility"
- **Diligent** → [Ad Library](https://www.linkedin.com/ad-library/?q=Diligent) — Governança corporativa, boardroom moderno, "risk oversight"

### Texto do post LinkedIn
**Headline:** Quando a recuperação falha, a responsabilidade escala.

**Texto introdutório:**
A cadeia de accountability precisa existir antes do incidente, não depois.

Cada finding com um owner. Cada risco atribuído. Cada decisão visível — do analista ao board. Quando o regulador perguntar "quem era responsável?", a resposta já existe.

A Fenix DFA constrói essa cadeia automaticamente. Baixe o Executive One-Pager.

### Imagem (1200x628)

**Layout sugerido:**
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  QUANDO A RECUPERAÇÃO FALHA,                        │
│  A RESPONSABILIDADE ESCALA.                         │
│                                                     │
│       Analyst                                       │
│          ↓                                          │
│       IT Manager                                    │
│          ↓                                          │
│       VP Infrastructure                             │
│          ↓                                          │
│       CISO / CIO                                    │
│          ↓                                          │
│       BOARD  ← (highlight em vermelho)              │
│                                                     │
│  ┌──────────────────────┐                           │
│  │ DOWNLOAD ONE-PAGER → │                           │
│  └──────────────────────┘                           │
│  FENIX DFA                        fenixdfa.com      │
└─────────────────────────────────────────────────────┘
```

**Elementos visuais:**
- Headline bold em branco
- Cadeia hierárquica visual: setas subindo de Analyst → IT Manager → VP → CISO → Board
- Cada nível é um retângulo/pill com o título do cargo
- A seta final (Board) fica em vermelho/laranja — é onde a pressão chega
- Visual clean, tipográfico, sem foto
- Logo + badge download + URL

**Alternativa com imagem:**
- Sala de board vazia, cadeira do CEO em destaque, tela com relatório de falha
- Buscar: "empty boardroom chair", "corporate board meeting pressure"

---

## Elementos obrigatórios — TODOS os criativos

- [ ] Logo Fenix DFA (usar SVG de `~/Downloads/Fenix-DFA-Logo.svg`)
- [ ] Badge "DOWNLOAD ONE-PAGER →" em laranja (#E8551B)
- [ ] URL fenixdfa.com no rodapé
- [ ] Fundo escuro (#1A1A2E) — preferencialmente sem foto (mais enterprise)
- [ ] Headline legível em tamanho de feed LinkedIn (~600px width)
- [ ] Pouco texto na imagem — LinkedIn penaliza excesso
- [ ] Dimensão: 1200x628px, JPG ou PNG, máx 5MB
- [ ] Tom: enterprise, sóbrio, técnico — público é C-level sob pressão regulatória

## O que NÃO fazer

- Nada colorido/vibrante
- Nada com pessoas sorrindo (público está sob pressão, não feliz)
- Nada com ícones genéricos de "segurança" (cadeado, escudo)
- Nada com "experimente grátis!" (tom de consumo, não enterprise)
- Nada em português se a campanha for para mercado internacional

## Idioma

- Se campanha Brasil: copys em português
- Se campanha global: copys em inglês (como estão acima)
- Definir com o cliente antes de produzir

---

## Referências visuais

**Enterprise SaaS security (dark mode, tipográfico):**
- CrowdStrike LinkedIn Ads
- Palo Alto Networks LinkedIn Ads
- Datadog LinkedIn Ads
- Wiz.io LinkedIn Ads

**Pesquisar no LinkedIn Ad Library:**
- linkedin.com/ad-library → buscar "CrowdStrike", "Datadog", "Rubrik"

---

## Fluxo completo da campanha

```
1. CRIATIVO no feed LinkedIn (3 variações)
      ↓
2. LEAD GEN FORM (campos pré-preenchidos pelo LinkedIn)
   - Nome, Email, Cargo, Empresa
   - CTA: "Download"
      ↓
3. DOWNLOAD automático do One-Pager (PDF)
      ↓
4. EMAIL de follow-up (automação)
   - Dia 0: "Aqui está seu One-Pager + link para Resilience Assessment"
   - Dia 3: "3 riscos que 78% das empresas ignoram"
   - Dia 7: "Como a Fenix DFA substitui 4 custos operacionais"
      ↓
5. RESILIENCE ASSESSMENT (call com vendas)
      ↓
6. TRIAL 30 dias
      ↓
7. CONTRATO
```

---

## Métricas esperadas (budget limitado)

| Métrica | Target |
|---------|--------|
| Budget/mês | R$3-5k |
| Impressões | 15.000-30.000 |
| CTR | 0,4-0,8% |
| CPL (Lead Gen Form) | R$30-80 |
| Leads/mês | 40-120 |
| Download One-Pager | 90%+ dos leads |
| Follow-up → Assessment | 10-20% |
| Assessment → Trial | 30-50% |

---

*Briefing baseado no Executive One-Pager oficial da Fenix DFA. Copys alinhadas com os 3 riscos do material: Silent Failures, Regulatory Exposure, Accountability Gaps.*
