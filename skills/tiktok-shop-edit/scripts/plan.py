"""Gera os trechos a manter dentro das janelas permitidas (janelas = vídeo sem os erros).

Só encurta pausas longas (>= 0,6 s), deixando ~0,24 s, como uma respiração. Pausas
naturais da fala ficam: cortar 0,1-0,3 s faz a imagem dar um tranco.
Uso: plan.py <src1080.mov> "a1-b1,a2-b2,..."
"""
import re, sys, subprocess

MIN_PAUSE, PAD = 0.6, 0.12
src = sys.argv[1]
win = [tuple(map(float, p.split("-"))) for p in sys.argv[2].split(",")]
log = subprocess.run(["ffmpeg", "-v", "info", "-i", src, "-af",
                      f"highpass=f=80,silencedetect=n=-38dB:d={MIN_PAUSE}", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
en += [1e9] * (len(st) - len(en))
keep = []
for a, b in win:
    cur = a
    for s, e in zip(st, en):
        if e <= a or s >= b:
            continue
        if s > cur:
            keep.append((cur, min(s + PAD, b)))
        cur = max(cur, e - PAD)
    if cur < b:
        keep.append((cur, b))
keep = [(round(a, 2), round(b, 2)) for a, b in keep if b - a > 0.12]
print(",".join(f"{a}-{b}" for a, b in keep))
print("total", round(sum(b - a for a, b in keep), 2), file=sys.stderr)
