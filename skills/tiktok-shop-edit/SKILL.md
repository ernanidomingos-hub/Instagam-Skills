---
name: tiktok-shop-edit
description: >
  Edição simples de vídeo de TikTok Shop em português: tira respiros, pausas longas, frases repetidas
  e tentativas erradas, mantendo a fala natural. Não mexe em cor, texto, música nem efeitos. Use quando
  o usuário mandar um vídeo bruto (arquivo, pasta do Drive ou Downloads) e pedir "edita", "tira os
  erros", "tira os respiros", "deixa pronto pro TikTok Shop", ou mandar vídeos novos para editar no
  mesmo padrão dos anteriores.
user-invokable: true
argument-hint: "[vídeo bruto ou pasta com vídeos]"
license: MIT
metadata:
  author: Ernani de Paula
  version: "1.0.0"
  category: video
---

# TikTok Shop Edit — corte limpo, fala natural

O vídeo de TikTok Shop que performa é simples: a pessoa falando do produto, sem enrolação e sem erro.
Esta skill faz só isso. **Nada de cor, legenda, texto na tela, música ou efeito.**

## Regras que o usuário aprovou (não negociáveis)

1. **Erros e repetições saem inteiros.** Quando a pessoa repete uma frase, fica a **última versão
   completa** (é a certa). Gaguejadas ("o sérum ele… o sérum ele vai") e palavras abandonadas
   ("parcelar, tem… às vezes tem") também saem.
2. **Pausas naturais ficam.** Só encurte pausa **≥ 0,6 s**, deixando ~0,24 s (uma respiração).
   Cortar pausas de 0,1–0,3 s faz a imagem dar um **tranco** (cabeça e produto pulam) e a fala fica
   atropelada. Esse foi o erro que o usuário reprovou: "esse tipo de falha não pode existir".
3. **Todo corte cai em silêncio.** Nunca dentro de uma palavra. Confira com `checkcuts.py`.
4. **Poucos cortes.** Referência dos vídeos aprovados: 3 a 6 cortes num vídeo de ~60 s.
5. **Corte seco, sem transição.** Áudio com fade de 30 ms em cada emenda (sem estalo) e volume
   normalizado para −14 LUFS.
6. **Saída:** 1080×1920, 30 fps, H.264 + AAC. Ideal ≤ 60 s; se passar, avise e sugira o que tirar
   (normalmente o 1º chamado para o link, quando ele se repete no final).
7. **Sempre mostrar ao usuário antes de considerar pronto.** Mande o vídeo, a fala final transcrita e
   uma tabela do que foi cortado. Pergunte só o que é decisão dele (ex.: manter "Sim, sim").

## Ferramentas

Precisa de `ffmpeg` e de Python com `faster-whisper` (`pip install faster-whisper`). O modelo
`medium` é baixado do Hugging Face na primeira vez (~1,5 GB). Em ambiente na nuvem libere
`huggingface.co`, `*.hf.co` e `cdn-lfs.huggingface.co`; se der erro de "Xet", rode com
`HF_HUB_DISABLE_XET=1`. Use sempre o modelo **medium**: o `small` junta repetições rápidas numa frase
só e deixa erro passar ("clica pra você ver… clica pra você ver").

Scripts em `scripts/` (rode Python com `-I`):

| Script | Para quê |
|---|---|
| `prepare.sh <video> <pasta>` | Converte 4K/HEVC/rotacionado em `src1080.mov` + `a.raw` (áudio para medir silêncio). Sem isso o corte em 4K estoura a memória. |
| `transcribe.py <video> <saida.json>` | Fala inteira com tempo por palavra. |
| `transcribe.py <video> --ranges a-b …` | Transcreve trechos isolados. Use para tirar dúvida de erro e para conferir cada emenda. |
| `silences.py <a.raw>` / `--env t0-t1` | Lista silêncios / volume a cada 40 ms para achar o ponto exato do corte. |
| `plan.py <src1080.mov> "janelas"` | A partir das janelas sem erro, gera os trechos aplicando a regra 2. |
| `checkcuts.py <a.raw> "trechos"` | Marca emendas que caíram dentro da fala. |
| `cut.py <src1080.mov> <saida.mp4> "trechos"` | Renderiza. |

## Passo a passo

1. **Pegar o vídeo.** Drive: pasta com "Qualquer pessoa com o link" e
   `curl -L "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"`.
   Se vier HTML de login, a pasta ainda está restrita: peça para liberar só a pasta de edição.
2. `prepare.sh` e depois `transcribe.py` com o modelo medium.
3. **Ler a fala inteira** e marcar cada tentativa errada, repetição, gaguejada e palavra abandonada.
   O tempo por palavra do Whisper pode errar 1–2 s em volta de pausas: **confirme cada erro** com
   `--ranges` em pedaços de 1–3 s e com `silences.py`. Erros costumam vir em sequência (2–5 tentativas
   da mesma frase): ache todas, não só a primeira.
4. Montar as **janelas** = o vídeo todo menos os trechos com erro, com bordas nos silêncios.
   Se não houver silêncio entre duas palavras, use o vale de volume (`--env`) mais fundo (< −35 dB).
5. `plan.py` → `checkcuts.py` (corrija bordas marcadas) → `cut.py`.
6. **Conferir o resultado inteiro**: `transcribe.py --ranges` em janelas sobrepostas que passem por
   cada emenda (ex.: 0-12 10-24 22-36 …). Procure repetição, palavra comida, "assim/então" duplicado
   na emenda. Refaça até a leitura sair limpa. Veja também quadros (`ffmpeg … fps=1/5,tile`) para
   checar enquadramento.
7. Entregar ao usuário (regra 7).

## Exemplos aprovados

Veja `references/aprovados.md`: os 3 vídeos Shiseido aprovados, com o que foi cortado em cada um.
