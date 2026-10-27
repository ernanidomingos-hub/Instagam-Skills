"""Confere cada emenda: volume nos primeiros/últimos 60 ms de cada trecho no original.
Borda acima de -35 dB = corte caiu dentro da fala (palavra comida). Revise antes de renderizar.
Uso: checkcuts.py <a.raw> "a1-b1,a2-b2,..."
"""
import sys
import numpy as np

a = np.fromfile(sys.argv[1], np.int16).astype(np.float32) / 32768
db = lambda t0, t1: 20 * np.log10(np.sqrt((a[int(t0 * 16000):int(t1 * 16000)] ** 2).mean()) + 1e-9)
out = 0.0
for i, (s, e) in enumerate(tuple(map(float, p.split("-"))) for p in sys.argv[2].split(",")):
    ins, oute = db(s, s + 0.06), db(e - 0.06, e)
    flag = ("  <-- INICIO NA FALA" if ins > -35 else "") + ("  <-- FIM NA FALA" if oute > -35 else "")
    print(f"#{i:2d} original {s:6.2f}-{e:6.2f}  editado {out:6.2f}  in={ins:4.0f}dB fim={oute:4.0f}dB{flag}")
    out += e - s
