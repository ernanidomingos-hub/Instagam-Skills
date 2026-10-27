#!/usr/bin/env bash
# Converte o vídeo do celular (4K/HEVC/rotacionado) num master 1080x1920 30fps
# e extrai o áudio cru (16 kHz mono) usado para medir silêncios.
# Uso: prepare.sh <video> <pasta_saida>
set -euo pipefail
src="$1"; out="$2"; mkdir -p "$out"
ffmpeg -v error -y -i "$src" -map 0:v:0 -map 0:a:0 \
  -vf "scale=1080:1920:flags=lanczos,setsar=1" -c:v libx264 -preset fast -crf 15 \
  -pix_fmt yuv420p -r 30 -c:a pcm_s16le -ar 44100 "$out/src1080.mov"
ffmpeg -v error -y -i "$out/src1080.mov" -vn -ac 1 -ar 16000 -f s16le "$out/a.raw"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$out/src1080.mov"
