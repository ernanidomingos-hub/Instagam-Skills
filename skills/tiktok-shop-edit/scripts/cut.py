"""Renderiza só os trechos mantidos: corte seco no vídeo, fade de 30 ms no áudio
(sem estalo), volume normalizado para -14 LUFS (padrão TikTok). Nada de cor/texto/efeito.
Uso: cut.py <src1080.mov> <saida.mp4> "a1-b1,a2-b2,..."
"""
import sys, subprocess

src, out, spec = sys.argv[1], sys.argv[2], sys.argv[3]
rs = [tuple(map(float, p.split("-"))) for p in spec.split(",")]
f, cat = [], ""
for i, (a, b) in enumerate(rs):
    d = b - a
    fd = min(0.03, d / 4)
    f.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}]")
    f.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d={fd},afade=t=out:st={d - fd}:d={fd}[a{i}]")
    cat += f"[v{i}][a{i}]"
f.append(f"{cat}concat=n={len(rs)}:v=1:a=1[v][ac];[ac]loudnorm=I=-14:TP=-1.5:LRA=11[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", ";".join(f),
                "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "160k", "-ar", "44100",
                "-movflags", "+faststart", out], check=True)
print(out, round(sum(b - a for a, b in rs), 2))
