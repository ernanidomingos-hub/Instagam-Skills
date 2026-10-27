"""Lista silêncios e o volume (dB) em janelas finas, para achar pontos de corte seguros.

Uso:
  silences.py <a.raw>                    # silêncios >= 0,22s (-38 dB)
  silences.py <a.raw> --env t0-t1 ...    # volume a cada 40 ms nesses trechos
"""
import sys
import numpy as np

a = np.fromfile(sys.argv[1], np.int16).astype(np.float32) / 32768
db = lambda t0, t1: 20 * np.log10(np.sqrt((a[int(t0 * 16000):int(t1 * 16000)] ** 2).mean()) + 1e-9)

if len(sys.argv) > 2 and sys.argv[2] == "--env":
    for r in sys.argv[3:]:
        t0, t1 = map(float, r.split("-"))
        print(r, " ".join(f"{t:.2f}:{db(t, t + 0.04):.0f}" for t in np.arange(t0, t1, 0.04)))
else:
    step, quiet, start = 0.02, [], None
    for i, t in enumerate(np.arange(0, len(a) / 16000, step)):
        q = db(t, t + step) < -38
        if q and start is None:
            start = t
        if not q and start is not None:
            if t - start >= 0.22:
                quiet.append((start, t))
            start = None
    if start is not None:
        quiet.append((start, len(a) / 16000))
    print("  ".join(f"{s:.2f}-{e:.2f} ({e - s:.2f})" for s, e in quiet))
