"""Transcreve a fala com tempo por palavra (faster-whisper, modelo medium).

Uso:
  transcribe.py <video> <saida.json>            # vídeo inteiro -> JSON de palavras
  transcribe.py <video> --ranges a-b a-b ...    # cada trecho separado (para conferir emendas)
Trechos curtos isolados ajudam a achar repetições que o vídeo inteiro esconde.
"""
import os, sys, json, subprocess
import numpy as np
from faster_whisper import WhisperModel

MODEL = os.environ.get("WM", "medium")

def load(path, a=None, b=None):
    cmd = ["ffmpeg", "-v", "error"]
    if a is not None:
        cmd += ["-ss", str(a), "-to", str(b)]
    cmd += ["-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768

model = WhisperModel(MODEL, device="cpu", compute_type="int8")
video = sys.argv[1]
if sys.argv[2] == "--ranges":
    for r in sys.argv[3:]:
        a, b = map(float, r.split("-"))
        segs = model.transcribe(load(video, a, b), language="pt", word_timestamps=True,
                                condition_on_previous_text=False)[0]
        print(f"{r}: " + " | ".join(" ".join(f"{w.start + a:.2f}:{w.word.strip()}" for w in s.words)
                                    for s in segs), flush=True)
else:
    words = []
    for s in model.transcribe(load(video), language="pt", word_timestamps=True)[0]:
        words += [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)} for w in s.words]
        print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text.strip()}", flush=True)
    json.dump(words, open(sys.argv[2], "w"), ensure_ascii=False)
