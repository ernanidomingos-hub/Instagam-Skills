# Histórico completo: TikTok Shop do Ernani (@ernanidepaula84)

Resumo de tudo que foi feito e combinado na conversa "Combinação de Vídeos TikTok Shop" (23/10 a
01/11/2026). Use para continuar em qualquer sessão nova, na nuvem (celular/iPad) ou no Mac.

## 1. Quem é e como falar
- Ernani de Paula, criador de TikTok Shop (afiliado), conta TikTok **@ernanidepaula84**.
- Me chama de **"migo"**. Responder em português, próximo e direto, sem enrolação.
- Regra de ouro: **sempre mostrar o resultado antes de considerar pronto**. Na edição, **um vídeo por
  vez**: só seguir quando ele disser "próximo" ou "ficou bom".

## 2. Contas e ferramentas conectadas
| Ferramenta | Para quê | Situação |
|---|---|---|
| Google Drive (conector) | ler e criar arquivos, renomear, criar pastas | ok; só envia arquivo pequeno (~5 MB) |
| Google Planilhas (conector) | ler e atualizar planilhas | ok |
| Windsor.ai (`tiktok_organic`) | métricas dos vídeos do TikTok (views, retenção por segundo, legendas) | ok; a 1ª consulta às vezes estoura o tempo, é só repetir |
| Metricool (marca `6422603`, fuso America/Sao_Paulo) | agendar posts no TikTok | TikTok conectado; falta ligar o Google Drive dentro do Metricool |
| Higgsfield | postar ou deixar rascunho no TikTok | TikTok NÃO conectado; o envio de mídia exige liberar `upload.higgsfield.ai` |
| GitHub `ernanidomingos-hub/Instagam-Skills` | guarda a skill, a fila e este histórico | branch `claude/inspiring-hawking-xdknyz` (ainda não está na `main`) |

## 3. Pastas e arquivos no Google Drive
Pasta principal: **Video Tiktok Shop** (ID `1h-vkl4kBUQX9maquwPCCwKtKH2uQO0vU`)
- **editar** (`1yt73uBeH-lx0UVtWy3jjCS5CCZxw2yYf`): vídeos brutos, compartilhada por link (leitor)
- **editados** (`1FRvYX4i8mO_ujOED2vncrOXr0E9i1YmX`): vídeos prontos. Por enquanto só tem `IMG_8401_editado.mp4`
- **Ulanzi MA60** (`1wb1L0pCqp90qhHaiyqBcVMlQHJYzAelM`), subpastas Gancho/Corpo/CTA, clipes renomeados
  para `MA60_Gancho_01..13`, `MA60_Corpo_01..03` e `MA60_CTA_01..08`
- Planilha **MA60 - Combinações Gancho x Corpo x CTA (312 vídeos)** (`1pU5545tj9QaQ86yJnFMgg-cpohhgXbVyPMf5TTv7clk`)
- Planilha "[ERRO - pode apagar] MA60 - Combinações (versão antiga)", que pode ser apagada
- Planilha **Fila de Postagem TikTok Shop** (`10rliQE4R-3ODKKd3arDzaH0BRLbztFhPaZdsn0NsG1U`)

Pasta **Kit Granado** (em Meu Drive, `1k7W8ZKMimgJ7i3Thh-O3TBtA5eWQQJnu`): Gancho (9), Corpo (3) e Cta (6),
compartilhada por link durante o trabalho; pode voltar para Restrito.

Download na nuvem (pasta compartilhada por link):
`curl -L "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"`

## 4. Rede do ambiente na nuvem (Allowed domains)
`drive.google.com`, `drive.usercontent.google.com`, `huggingface.co`, `cas-server.xethub.hf.co`,
`cdn-lfs.huggingface.co`, `us.aws.cdn.hf.co` (ou `*.hf.co` e `*.huggingface.co`).
Opcional: `upload.higgsfield.ai` (rascunho via Higgsfield).
Script de setup sugerido:
```bash
pip install faster-whisper
HF_HUB_DISABLE_XET=1 python3 -c "from faster_whisper import WhisperModel; WhisperModel('medium')"
```

## 5. Edição simples de TikTok Shop (skill `tiktok-shop-edit`)
Arquivos: `skills/tiktok-shop-edit/` (SKILL.md, scripts/, references/aprovados.md, references/fila.md).
Regras aprovadas:
1. Tirar tentativas erradas, repetições, gaguejadas e palavras abandonadas; fica a **última versão completa**.
2. **Manter pausas naturais**: só encurtar pausa de 0,6 s ou mais, deixando ~0,24 s. Cortar 0,1–0,3 s dá
   tranco na imagem. Isso foi reprovado.
3. Todo corte em silêncio (`checkcuts.py`); poucos cortes (1 a 6 nos vídeos aprovados).
4. Nada de cor, texto, música ou efeito. Áudio em -14 LUFS, saída 1080x1920 30 fps.
5. Transcrever com o Whisper **medium**; conferir cada erro em trechos curtos; depois de renderizar,
   transcrever o vídeo final inteiro em janelas que passem por cada emenda.
6. Vídeos do iPhone vêm em 4K HEVC rotacionado: rodar `prepare.sh` antes (cortar direto do 4K estoura a memória).
7. Entregar com: produto, duração antes→depois, nº de cortes, tabela "o que cortei / o que ficou", fala final.

Aprovados (referência): IMG_8401 (sérum Shiseido Men, 58→46 s), IMG_8391 (espuma Shiseido, 83→50 s) e
IMG_8406 (kit Shiseido, 83→63 s). Os detalhes estão em `aprovados.md`.

### Fila atual (pasta "editar", 13 vídeos)
| # | Vídeo | Produto | Status | Janelas de corte (tempos do src1080) |
|---|---|---|---|---|
| 1 | IMG_8417 | Desodorante antitranspirante Principia | aprovado (90→39 s) | 30.90-36.30,47.94-59.52,63.42-69.10,72.72-89.10 |
| 2 | IMG_8411 | Creme calmante multirreparador Principia | aguardando aprovação (37→32 s) | 0.90-30.18,33.22-35.60 |
| 3–13 | IMG_8409, 8301, 8294, 8010, 8001, 7967, 7852, 6975, 6971, 6161, 6141 | — | a editar | — |
IDs no Drive de cada um: em `fila.md`.

## 6. Postagem no TikTok (combinado em 01/11)
- Preferência: **rascunho**. O vídeo e a legenda chegam prontos; o Ernani só anexa o link do produto e publica.
- Nenhuma ferramenta disponível anexa produto do TikTok Shop pela API.
- Com dia e hora na planilha: Metricool com `autoPublish: false`. Na hora marcada chega uma notificação
  no celular, e o TikTok abre com o vídeo e a legenda.
- Melhores horários do perfil (Metricool): **10h, 12h e 18h**; quarta e quinta às 10h são os mais fortes.
- Fluxo: editar → aprovar → subir em "editados" → preencher na planilha o link do vídeo, o link do produto
  e o dia/hora → "agenda" → Claude escreve a legenda (para aprovar), agenda e muda o Status.
- Legenda sugerida para o IMG_8417 (já na planilha): "96 horas de proteção de verdade 💪 Testei o
  antitranspirante da Principia com niacinamida e ele protege e ainda hidrata a axila. Comprando junto com
  outro produto Principia, sai com quase 20% de desconto 👇 #principia #desodorante #antitranspirante
  #skincaremasculino #tiktokshopbr"

## 7. Combinações Gancho + Corpo + CTA
Método: listar clipes por pasta, ignorar os `._*` (lixo do Mac), gerar todas as combinações sem
repetir e organizar em lotes em que cada gancho aparece uma vez. Para escolher as melhores: cruzar a
duração de cada post do TikTok com a soma gancho+corpo+CTA para descobrir quais clipes foram usados,
puxar a retenção por segundo no Windsor e olhar quadros dos clipes.

### Ulanzi MA60 (Mini Tripé Magnético)
- 13 ganchos × 3 corpos × 8 CTAs = **312 combinações** (24 lotes de 13).
- Análise do TikTok: 16 posts, ~22,8 mil views; 70–80% saem antes de 3 s (o gancho decide); só 1–5%
  chegam ao CTA. O melhor post (31/08, 9,2 mil) foi às 8h.
- 10 vídeos montados (gancho/corpo/CTA): V01 01/02/04, V02 05/01/01, V03 07/03/04, V04 04/02/01,
  V05 09/01/08, V06 03/03/01, V07 11/02/08, V08 02/01/02, V09 08/03/02, V10 12/02/03.

### Kit Granado Mala Bossa
- 9 ganchos × 3 corpos × 6 CTAs = **162 combinações**.
- Análise (25 posts, ~63 mil views): o corpo 0711 2 (19,7 s) é o melhor e o 0711 3 (46 s) é longo demais;
  ganchos fortes: 0711 6, 0711 3, 0711 4 e 0711 7; fracos: 0711, 0711 2 e 0711 (2)(1).
- 12 vídeos montados (gancho/corpo/CTA, nomes do Drive): V01 0711 6/0711 2/0711 2, V02 0711 6/0711/0711 4,
  V03 0711 3/0711 2/0711 6, V04 0711 4/0711 2/0711 3, V05 0711 7/0711 2/0711 4, V06 0711 8/0711 2/0711 6,
  V07 0711 3/0711/0711 3, V08 0711 4/0711/0711 6, V09 0711 7/0711/0711 2, V10 0711 8/0711/0711 4,
  V11 0711 5/0711 2/0711 3, V12 0711/0711 2/0711 6.

## 8. Mac
- Já configurado em outra sessão (Claude Desktop → Code → ambiente local): `~/CLAUDE.md`,
  `~/.claude/skills/tiktok-shop-edit`, `~/.tiktok-edit-venv` (Python + ffmpeg 7.1; sem ffprobe),
  modelo medium em `~/.cache/huggingface`. As pastas editar/editados ficam em
  `~/Library/CloudStorage/GoogleDrive-ernanidomingos84@gmail.com/Meu Drive/Video Tiktok Shop/`.
- No Mac, o vídeo pronto vai direto para "editados" (sincroniza com o Drive). Na nuvem, ele é entregue
  no chat e o Ernani sobe na mão.
- Sessão na nuvem: não enxerga as pastas do Mac. Para isso, conectar a pasta via Remote Control ou usar
  a sessão local.

## 9. Pendências
1. Aprovar o IMG_8411; depois editar os 11 restantes, um por vez.
2. Subir em "editados" os aprovados que ainda não estão lá (IMG_8417, 8391, 8406 e o 8411 quando aprovar).
3. Ligar o Google Drive no Metricool; preencher a planilha de postagem e pedir "agenda".
4. Voltar as pastas Kit Granado e Ulanzi MA60 para "Restrito" se não forem mais usadas.
5. Opcional: abrir um PR para levar a skill para a `main` do Instagam-Skills.
6. Opcional: apagar a planilha "[ERRO - pode apagar]" e os arquivos `._*` das pastas do MA60.
