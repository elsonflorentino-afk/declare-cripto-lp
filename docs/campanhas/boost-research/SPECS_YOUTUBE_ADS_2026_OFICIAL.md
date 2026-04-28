# Especificacoes Tecnicas e Melhores Praticas - YouTube Ads 2026

**Autor:** @greg (Google Ads Specialist)
**Data:** 28/abr/2026
**Fontes:** Google Ads Help, YouTube Help, Think with Google (todas oficiais)

---

## 1. Especificacoes Tecnicas por Formato de Anuncio

### 1.1 Configuracoes Gerais de Upload (YouTube)

| Parametro | Especificacao |
|-----------|---------------|
| **Container recomendado** | MP4 |
| **Codec de video** | H.264, High Profile, 2 B-frames consecutivos, Closed GOP (metade do frame rate), CABAC |
| **Codec de audio** | AAC-LC |
| **Canais de audio** | Stereo ou Stereo + 5.1 |
| **Bitrate de audio** | 128 kbps ou superior |
| **Frame rate** | Manter o nativo da gravacao (24, 25, 30, 48, 50, 60 fps aceitos) |
| **Bitrate de video** | Variable Bitrate (VBR), sem limite minimo obrigatorio |
| **Tamanho maximo** | 256 GB ou 12 horas (o que for menor) |
| **Formatos aceitos** | .MOV, .MP4, .MPEG-1, .MPEG-2, .MPEG4, .MPG, .AVI, .WMV, .MPEGPS, .FLV, .3GPP, .WebM, .DNxHR, .ProRes, .CineForm, .HEVC (H.265) |

**Fonte:** [YouTube recommended upload encoding settings](https://support.google.com/youtube/answer/1722171?hl=en)

### 1.2 Resolucoes Recomendadas por Aspect Ratio

| Aspect Ratio | Resolucao Recomendada | Resolucao Minima | Uso Principal |
|--------------|----------------------|------------------|---------------|
| 16:9 (horizontal) | 1920x1080 (Full HD) | 1280x720 | In-stream, Discovery |
| 9:16 (vertical) | 1080x1920 | 720x1280 | Shorts, Demand Gen vertical |
| 1:1 (quadrado) | 1080x1080 | 720x720 | Demand Gen, feed |
| 4:3 | 640x480 (min) | 640x480 | Legacy, nao recomendado |

**Nota:** NUNCA usar letterboxing ou pillarboxing. O player do YouTube ajusta automaticamente ratios entre 16:9 e 9:16.

**Fonte:** [Video and audio formatting specifications](https://support.google.com/youtube/answer/4603579?hl=en)

---

### 1.3 In-Stream Skippable

| Parametro | Especificacao |
|-----------|---------------|
| **Duracao minima** | Sem minimo formal (recomendado >= 12s) |
| **Duracao maxima** | Sem limite (recomendado < 3 min) |
| **Skip disponivel** | Apos 5 segundos |
| **Cobranca** | CPV: viewer assiste 30s (ou video completo se < 30s) ou interage |
| **Aspect ratio** | 16:9 (horizontal), 9:16 (vertical), 1:1 (quadrado) aceitos |
| **Resolucao minima** | 1280x720 (16:9) |
| **Posicionamento** | Pre-roll, mid-roll, post-roll |
| **Melhor performance** | Videos < 3 minutos |

**Fonte:** [Skippable in-stream ads](https://support.google.com/google-ads/answer/6055025?hl=en)

### 1.4 In-Stream Non-Skippable

| Parametro | Especificacao |
|-----------|---------------|
| **Duracao maxima** | 15 segundos (padrao), ate 60 segundos em mercados selecionados |
| **Skip** | NAO disponivel |
| **Cobranca** | CPM (por mil impressoes) |
| **Aspect ratio** | 16:9 (horizontal) recomendado |
| **Resolucao minima** | 1280x720 |
| **Posicionamento** | Pre-roll, mid-roll, post-roll |

**Fonte:** [Non-skippable in-stream ads](https://support.google.com/google-ads/answer/11462260?hl=en)

### 1.5 Bumper Ads (6 segundos)

| Parametro | Especificacao |
|-----------|---------------|
| **Duracao maxima** | 6 segundos |
| **Skip** | NAO disponivel |
| **Cobranca** | CPM |
| **Aspect ratio** | 16:9 (horizontal) recomendado |
| **Resolucao minima** | 1280x720 |
| **Melhor uso** | Awareness, reforco de marca, remarketing |

**Fonte:** [About video ad formats](https://support.google.com/google-ads/answer/2375464?hl=en)

### 1.6 YouTube Shorts Ads

| Parametro | Especificacao |
|-----------|---------------|
| **Aspect ratio obrigatorio** | 9:16 (vertical) |
| **Resolucao recomendada** | 1080x1920 |
| **Duracao recomendada** | < 60 segundos (ideal: 10-30s para acao) |
| **Duracao maxima no feed** | 60s exibidos; overlay aparece aos 50s permitindo assistir o resto na watch page |
| **Duracao por tipo de campanha** | Video Reach: 6-60s / Video Action/App/PMax: 10-60s |
| **Som** | Padrao: ligado (sound-on) |
| **Skip** | Swipe up/down para pular |
| **CTA** | Overlay card com headline (40 chars) + descricao (90 chars) |
| **Estilo** | Social-first, autentico, creator-like |

**Dados de performance:** Som (musica/voiceover) aumenta conversoes em +20%.

**Fonte:** [YouTube Shorts ads: Asset specs and best practices](https://support.google.com/google-ads/answer/16041697?hl=en)

### 1.7 Discovery / In-Feed Video Ads

| Parametro | Especificacao |
|-----------|---------------|
| **Thumbnail** | Gerado automaticamente a partir do video (4 opcoes) |
| **Headline** | Ate 100 caracteres (recomendado <= 40) |
| **Descricao** | 2 linhas, ate 35 caracteres cada |
| **Video** | Qualquer duracao (hospedado no YouTube) |
| **Aspect ratio** | 16:9 recomendado |
| **Cobranca** | CPV (ao clicar e assistir) |
| **Posicionamento** | YouTube Home, resultados de busca, Watch Next |

**Fonte:** [In-feed video ads](https://support.google.com/google-ads/answer/6227733?hl=en)

---

## 2. Demand Gen - Especificacoes de Assets

### 2.1 Assets de Video

| Parametro | Especificacao |
|-----------|---------------|
| **Quantidade por asset group** | Ate 5 videos |
| **Aspect ratios aceitos** | 16:9 (horizontal), 9:16 (vertical), 1:1 (quadrado) |
| **Duracao maxima** | 3 minutos |
| **Shorts inventory** | Apenas primeiros 60s exibidos |
| **Som padrao por placement** | Discover feed: mudo/autoplay; YouTube Home: mudo/autoplay; In-stream: som pos-tap; Shorts: som ligado |

### 2.2 Assets de Imagem

| Tipo | Aspect Ratio | Resolucao Recomendada | Resolucao Minima | Tamanho Max |
|------|-------------|----------------------|------------------|-------------|
| Landscape | 1.91:1 | 1200 x 628 | 600 x 314 | 5120 KB |
| Portrait | 4:5 | 960 x 1200 | 480 x 600 | 5120 KB |
| Quadrado (logo) | 1:1 | 1200 x 1200 | 128 x 128 | 5120 KB |
| Vertical (Shorts) | 9:16 | 1080 x 1920 | — | 5120 KB |

### 2.3 Assets de Texto

| Tipo | Limite de Caracteres | Quantidade |
|------|---------------------|------------|
| Headline | Ate 40 caracteres | Ate 5 |
| Long Headline | Ate 90 caracteres | Ate 5 |
| Description | Ate 90 caracteres | Ate 5 |
| Business name | Ate 25 caracteres | 1 |
| CTA | Selecionado de lista predefinida | 1 |
| Logo | 1:1, min 128x128 | Ate 5 |

**Nota:** Shorts usa headline, long headline e description de forma intercambiavel como descricao do anuncio.

**Dado de performance:** Anunciantes que enviaram video + imagem no Demand Gen tiveram +20% de conversoes ao mesmo CPA vs. so video.

**Fonte:** [Demand Gen campaign creative: Asset specifications](https://support.google.com/google-ads/answer/13704860?hl=en)

---

## 3. ABCD Framework - Melhores Praticas Oficiais do Google

Baseado na analise de milhares de campanhas pelo Google. Ads que seguem o ABCD entregam:
- **+30% lift** em probabilidade de venda de curto prazo
- **+17% lift** em contribuicao de marca de longo prazo

### 3.1 A = ATTRACT (Atrair nos primeiros 5 segundos)

| Tecnica | Descricao | Aplicacao Boost |
|---------|-----------|-----------------|
| **Enquadramento fechado** | Comecar com close-up em rosto ou objeto | Andre Franco olhando para camera, close |
| **Multiplos cortes rapidos** | 2-3 shots nos primeiros 5s | Transicao grafico > Andre > numero |
| **Pergunta direta** | Abrir com pergunta que gera curiosidade | "Voce sabe quanto seu patrimonio perdeu esse mes?" |
| **Visual inesperado** | Algo que quebra o padrao do feed | Numero grande na tela (ex: "R$1.000.000") |
| **Audio forte** | Musica, efeito sonoro, voz impactante | Voz firme do Andre + sound effect |
| **Ritmo acelerado** | Pacing rapido nos primeiros segundos | Cortes a cada 1-2 segundos no inicio |

### 3.2 B = BRAND (Inserir a marca cedo)

| Tecnica | Descricao | Aplicacao Boost |
|---------|-----------|-----------------|
| **Marca nos primeiros 5s** | Branding precoce NAO prejudica performance | Logo Boost Research nos primeiros 3s |
| **Integracao natural** | Marca como parte da narrativa, nao interrupcao | Andre com camisa/cenario com marca visivel |
| **Audio branding** | Mencao verbal da marca | "Aqui na Boost Research..." |
| **Elementos graficos** | Lower third, watermark sutil | Lower third com "Boost Research" + cargo do Andre |
| **Produto em contexto** | Mostrar o produto sendo usado | Dashboard/tela de analise da Boost |

### 3.3 C = CONNECT (Criar conexao emocional)

| Tecnica | Descricao | Aplicacao Boost |
|---------|-----------|-----------------|
| **Pessoas reais** | Rostos humanos geram maior conexao | Andre Franco como protagonista |
| **Beneficio funcional + emocional** | Combinar dado concreto com sentimento | "Proteja seu patrimonio" (seguranca + dados) |
| **Storytelling** | Narrativa com inicio, meio, fim | Historia: problema > insight > solucao Boost |
| **Humor ou surpresa** | Quebra de expectativa | Dado surpreendente sobre cripto |
| **Tom conversacional** | Falar COM o viewer, nao PARA o viewer | Andre falando direto para camera |

### 3.4 D = DIRECT (Direcionar a acao)

| Tecnica | Descricao | Aplicacao Boost |
|---------|-----------|-----------------|
| **CTA especifico** | "Faca sua analise gratuita" vs. "Saiba mais" | "Agende sua analise de carteira" |
| **Urgencia** | Tempo limitado, vagas limitadas | "Vagas limitadas para abril" |
| **Texto + audio** | CTA visual E verbal simultaneamente | Andre fala + texto na tela |
| **Oferta clara** | O que a pessoa ganha ao clicar | "Analise gratuita do seu portfolio cripto" |
| **End card** | Tela final com CTA + logo | Logo Boost + CTA + URL |

**Fontes:**
- [YouTube ABCDs: Video ad best practices](https://www.thinkwithgoogle.com/future-of-marketing/creativity/youtube-video-ad-creative/)
- [ABCD Playbook PDF](https://www.thinkwithgoogle.com/_qs/documents/8472/ABCD_Complete_V7b_HR_1.pdf)
- [About the ABCDs of effective video ads](https://support.google.com/google-ads/answer/14783551?hl=en)

---

## 4. Legendas e Captions

### 4.1 Formatos de Arquivo Suportados

| Formato | Extensao | Recomendacao Google | Notas |
|---------|----------|---------------------|-------|
| **SubRip** | .srt | RECOMENDADO (simples) | Timing + texto, editavel em qualquer editor de texto |
| **SubViewer** | .sbv | RECOMENDADO (simples) | Similar ao SRT, formato de timestamp diferente |
| **Scenarist Closed Caption** | .scc | PREFERIDO (broadcast) | Padrao CEA-608, usado em TV |
| **TTML/DFXP** | .ttml/.dfxp | Suportado | Formato XML, suporta estilo e posicao |
| **SAMI** | .smi | Suportado | Formato Microsoft |
| **LRC** | .lrc | Suportado | Usado para letras de musica |
| **Auto-generated** | — | Disponivel | YouTube gera automaticamente via speech-to-text |

### 4.2 Boas Praticas para Legendas em Ads

| Aspecto | Recomendacao |
|---------|-------------|
| **Formato principal** | .SRT (mais universal e simples) |
| **Idioma** | Sempre adicionar no idioma do publico-alvo |
| **Auto-captions** | YouTube gera automaticamente, mas REVISAR sempre (erros em termos tecnicos/cripto) |
| **Acessibilidade** | Legendas expandem alcance para surdos/deficientes auditivos + ambientes sem som |
| **Performance** | Google Ads oferece "video enhancements" com legendas automaticas para PMax |
| **Burn-in vs. CC** | Para Shorts: burn-in (texto gravado no video) recomendado pois CC pode nao aparecer |

### 4.3 Impacto na Performance

- **80% dos videos** no YouTube sao assistidos sem som em dispositivos moveis (dado da industria)
- Legendas burned-in aumentam **watch time** em ambientes silenciosos
- Google Ads Video Enhancements gera versoes com legendas automaticas para ampliar alcance
- Para Shorts: **som ligado e padrao**, mas legendas reforcar a mensagem

**Fonte:** [Supported subtitle and closed caption files](https://support.google.com/youtube/answer/2734698?hl=en), [About video enhancements](https://support.google.com/google-ads/answer/13652431?hl=en)

---

## 5. Thumbnail para Discovery/In-Feed

### 5.1 Especificacoes Tecnicas

| Parametro | Especificacao |
|-----------|---------------|
| **Resolucao recomendada** | 1280 x 720 pixels |
| **Largura minima** | 640 pixels |
| **Aspect ratio** | 16:9 |
| **Formatos aceitos** | JPG, GIF, PNG |
| **Tamanho maximo** | 2 MB (videos) / 10 MB (podcasts) |
| **Origem** | Custom upload (conta verificada) ou auto-gerado pelo YouTube |

### 5.2 Boas Praticas para Thumbnails

| Regra | Descricao |
|-------|-----------|
| **Alta resolucao** | Sempre usar 1280x720; se qualquer thumb < 720p, TODAS sao rebaixadas para 480p |
| **Rosto visivel** | Thumbnails com rostos humanos tem maior CTR |
| **Texto legivel** | Maximo 3-5 palavras, fonte grande, contraste alto |
| **Cores vibrantes** | Contrastar com o fundo branco/cinza do YouTube |
| **Consistencia de marca** | Manter paleta Boost (escuro #12191D + verde #03E4D0) |
| **Sem clickbait** | Thumbnail deve refletir o conteudo real (policy do Google) |

**Fonte:** [Add custom thumbnails on YouTube](https://support.google.com/youtube/answer/72431?hl=en)

---

## 6. Safe Zones e Disclaimers para Financial Services

### 6.1 Safe Zones - Areas Seguras para Texto

**YouTube Shorts (9:16 vertical):**

```
+---------------------------+
|     TOP SAFE ZONE         |  <- Evitar: status bar, relogio
|  (manter texto abaixo)    |
|                           |
|   +-------------------+   |
|   |                   |   |
|   |   AREA SEGURA     |   |
|   |   para texto e    |   |
|   |   elementos-chave |   |
|   |                   |   |
|   +-------------------+   |
|                           |
|  BOTTOM: CTA overlay   |  <- Evitar: botoes like/share/subscribe
|  + navigation buttons  |  |
|  (aprox. 20% inferior) |  |
+---------------------------+
         ^                ^
         |                |
    Evitar laterais: icones de engajamento (like, comment, share)
    ficam na lateral direita (~15% da largura)
```

**Regra pratica para Shorts:**
- **Topo:** Manter 10-15% livre (barra de status)
- **Lateral direita:** Manter 15-20% livre (botoes like/share/comment)
- **Base:** Manter 20-25% livre (CTA card + descricao + controles)
- **Area util:** Centro do frame, ~60-65% da area total

**YouTube In-Stream (16:9 horizontal):**
- **Base:** Manter 20% inferior livre (lower third para CTA, banner companion)
- **Cantos:** Evitar texto nos cantos (botoes de skip, countdown, info)

### 6.2 Disclaimers para Financial Services (Cripto)

| Requisito | Especificacao | Obrigatorio? |
|-----------|---------------|-------------|
| **Endereco fisico** | Endereco comercial visivel no anuncio ou LP | SIM |
| **Acreditacao** | Links para orgaos reguladores (CVM, ANBIMA) quando aplicavel | SIM, se alegar afiliacao |
| **Disclosure** | NAO pode ser roll-over ou em outro link/aba | SIM |
| **Visibilidade** | Claramente visivel sem clicar ou hover | SIM |
| **Regulacao local** | Cumprir leis de TODOS os locais targetados | SIM |
| **Certificacao Google** | Necessaria para produtos financeiros restritos | SIM |

**Policy de Cripto (atualizada fev/2026):**
- Permitido anunciar servicos cripto em locais selecionados se cumprir leis locais
- PROIBIDO: ICOs, protocolos DeFi de trading, compra/venda direta de cripto
- Necessaria certificacao Google especifica por localizacao

### 6.3 Especificacoes Visuais de Disclaimer no Video

| Parametro | Recomendacao |
|-----------|-------------|
| **Tamanho minimo da fonte** | >= 24pt em 1080p (visivel em mobile) |
| **Duracao na tela** | Minimo 3 segundos OU duracao total do anuncio (bumper) |
| **Posicao** | Lower third ou rodape, dentro da safe zone |
| **Contraste** | Ratio minimo 4.5:1 (WCAG AA) contra o fundo |
| **Texto sugerido para Boost** | "Rentabilidade passada nao garante resultados futuros. Boost Research LTDA - CNPJ XX.XXX.XXX/0001-XX" |
| **Em bumpers (6s)** | Disclaimer deve ocupar os ultimos 1-2 segundos OU ser visivel durante todo o video |

**Fontes:**
- [Financial products and services](https://support.google.com/adspolicy/answer/2464998)
- [Cryptocurrencies and related products](https://support.google.com/adspolicy/answer/14009787?hl=en)
- [Updates to Cryptocurrencies policy (Jul 2025)](https://support.google.com/adspolicy/answer/16345928?hl=en)
- [Updates to Financial products policy (Feb 2026)](https://support.google.com/adspolicy/answer/16885619?hl=en)

---

## 7. Tabela Resumo - Todos os Formatos

| Formato | Duracao | Aspect Ratio | Skip | Cobranca | Melhor Uso |
|---------|---------|-------------|------|----------|------------|
| **In-stream Skippable** | Sem limite (rec < 3min) | 16:9, 9:16, 1:1 | Apos 5s | CPV | Awareness + Consideracao |
| **In-stream Non-skip** | Max 15s (60s em alguns mercados) | 16:9 | Nao | CPM | Mensagem completa garantida |
| **Bumper** | Max 6s | 16:9 | Nao | CPM | Reforco de marca, recall |
| **Shorts Ads** | Rec < 60s (ideal 10-30s) | 9:16 | Swipe | CPV/CPM | Mobile-first, geracao Z |
| **In-Feed/Discovery** | Sem limite | 16:9 | N/A (click-to-play) | CPV | Intencao, busca |
| **Demand Gen Video** | Max 3min (60s no Shorts) | 16:9, 9:16, 1:1 | Varia | CPA/ROAS | Conversao, mid-funnel |

---

## 8. Checklist de Producao para Boost Research

### Pre-Producao
- [ ] Definir formato (in-stream, shorts, bumper, demand gen)
- [ ] Gravar em resolucao nativa do formato (1080p min)
- [ ] Planejar hook nos primeiros 5 segundos (ABCD - Attract)
- [ ] Incluir branding Boost nos primeiros 5s (ABCD - Brand)
- [ ] Preparar disclaimer regulatorio

### Producao
- [ ] Gravar horizontal (16:9) E vertical (9:16) simultaneamente
- [ ] Manter elementos-chave na safe zone central
- [ ] Audio limpo (AAC-LC, 128kbps+)
- [ ] Frame rate nativo consistente

### Pos-Producao
- [ ] Exportar H.264, High Profile, MP4
- [ ] Criar versoes: horizontal + vertical + quadrado
- [ ] Burn-in legendas para Shorts
- [ ] Gerar arquivo .SRT para versoes in-stream
- [ ] Disclaimer visivel (24pt+, 3s+, contraste 4.5:1)
- [ ] Thumbnail custom 1280x720, JPG/PNG, < 2MB

### Upload e Configuracao
- [ ] Upload no YouTube primeiro (nunca direto no Google Ads)
- [ ] Adicionar captions .SRT
- [ ] Configurar thumbnail custom
- [ ] Verificar preview em mobile (safe zones ok?)
- [ ] Ativar video enhancements se PMax/Demand Gen

---

*Documento compilado por @greg a partir de fontes oficiais do Google em 28/abr/2026.*
*Todas as specs sao validas para a data de publicacao. Verificar atualizacoes em support.google.com/google-ads.*
