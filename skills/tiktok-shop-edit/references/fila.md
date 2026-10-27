# Fila de edição: pasta "Video Tiktok Shop/editar" (Google Drive)

Usada pela sessão na nuvem (celular/iPad) e pela sessão no Mac. Fonte da verdade sobre o que já está
pronto: a pasta **editados**. Antes de editar um vídeo, veja se `<original>_editado.mp4` já está lá; se
estiver, pule para o próximo.

- Pasta editar (brutos): ID `1yt73uBeH-lx0UVtWy3jjCS5CCZxw2yYf`, compartilhada por link (leitor)
- Pasta editados (prontos): ID `1FRvYX4i8mO_ujOED2vncrOXr0E9i1YmX`
- Na nuvem, o download é feito por
  `https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`.
  O vídeo pronto é entregue no chat, e o usuário sobe em "editados".

| # | Arquivo | ID no Drive | Produto | Status | Janelas (tempos do src1080) |
|---|---|---|---|---|---|
| 1 | IMG_8417 | 16M_OKqq1aqyQU0FkJDeo5UpkBeR7oRaN | Desodorante antitranspirante Principia | aprovado | 30.90-36.30,47.94-59.52,63.42-69.10,72.72-89.10 |
| 2 | IMG_8411 | 1EvEx43hVQjxJLRRGXLCpmvSdAFjxFL8V | Creme calmante multirreparador Principia | aguardando aprovação | 0.90-30.18,33.22-35.60 |
| 3 | IMG_8409 | 1cPY3qJ_kszwOAQq-K08Ha0uWk-8E9hRx | | a editar | |
| 4 | IMG_8301 | 1RPA3f5ArGbff_jJHG_7bQA_psG_z-AQl | | a editar | |
| 5 | IMG_8294 | 1Kjj56pfwe0WYsGG69D4dELfS2ONace5F | | a editar | |
| 6 | IMG_8010 | 1fGMMO0quy_BrIBv-5XefP1KnQm6oaUZg | | a editar | |
| 7 | IMG_8001 | 1_Yteko6AkuztdaI1VrzkxHzqlF5FLxhE | | a editar | |
| 8 | IMG_7967 | 1u303vliNq14ya-PBYYdJdm9SW4JCg0UT | | a editar | |
| 9 | IMG_7852 | 1UtYhSmILIvNVikiJo7fPWnUeX3r6BCRf | | a editar | |
| 10 | IMG_6975 | 1S6Zgk-ZQiLqTPXJkKAAGbhfxFLnLahgv | | a editar | |
| 11 | IMG_6971 | 1OK16jAqjPIUAtRdTzmQeLdHO7zw9pAW6 | | a editar | |
| 12 | IMG_6161 | 1atoNrjZmKVfxSQZbzPzVIPRoBYbrCo0_ | | a editar | |
| 13 | IMG_6141 | 1qFvI4caBigeNkOrCg3iS3yWyIQqrCQrg | | a editar | |

## Preparar o ambiente na nuvem (container novo)

```bash
python3 -m venv venv && ./venv/bin/pip install -q faster-whisper
HF_HUB_DISABLE_XET=1 ./venv/bin/python -c "from faster_whisper import WhisperModel; WhisperModel('medium')"
```

Domínios liberados na rede: `drive.google.com`, `drive.usercontent.google.com`, `huggingface.co`,
`*.hf.co`, `cdn-lfs.huggingface.co`. Se `transcribe.py` falhar com `av`, o script já decodifica o
áudio pelo ffmpeg, então não depende do PyAV.
