#!/usr/bin/env python3
"""Matro1000 rough cut: picture only, 1920x1080, 25 fps, 3:27, burned-in shot + timecode labels.

Re-run when screens/stills arrive:  python output/build_rough_cut.py -o output/rough_cut_v2.mp4
Every step is one of the ffmpeg-skill scripts. Shot times = PART 1 of Matro1000_FINAL_Package_3D.txt,
source ranges = clips/NOTES.txt (+ the changes agreed for v1, see comments).
"""
import argparse, json, os, subprocess, sys, tempfile
from pathlib import Path

SKILL = Path(os.environ.get("FFMPEG_SKILL_SCRIPTS") or next(Path.home().glob("*/skills/ffmpeg-skill/scripts")))
ROOT = Path(__file__).resolve().parent.parent
FPS = 25
FLOOR = 0.85  # slowest speed before the last frame is held

# PART 1 master shot list: (shot, seconds). Labels and placeholder cards come from here.
SHOTS = [("1.1", 2), ("1.2", 2), ("1.3", 3), ("1.4", 2), ("1.5", 2), ("2.1", 3), ("2.2", 3), ("2.3", 2), ("2.4", 2),
         ("3.1", 6), ("3.2", 6), ("3.3", 8), ("3.4", 6), ("3.5", 4), ("3.6", 2), ("3.7", 2),
         ("4.1", 4), ("4.2", 3), ("4.3", 4), ("5.1", 3), ("5.2", 3), ("5.3", 3), ("5.4", 2), ("5.5", 3), ("5.6", 2),
         ("5.7", 3), ("5.8", 3), ("6.1", 3), ("6.2", 3), ("6.3", 3), ("6.4", 2),
         ("7.1", 6), ("7.2", 6), ("7.3", 5), ("7.4", 5), ("7.5", 3),
         ("8.1", 3), ("8.2", 4), ("8.3", 4), ("8.4", 3), ("8.5", 6), ("8.6", 2), ("8.7", 2), ("8.8", 2), ("8.9", 3), ("8.10", 3),
         ("9.1", 4), ("9.2", 8), ("9.3", 4), ("9.4", 4),
         ("10.1", 3), ("10.2", 3), ("10.3", 4), ("10.4", 3), ("10.5", 2), ("11.1", 3), ("11.2", 2),
         ("12.1", 3), ("12.2", 3), ("12.3", 3), ("12.4", 2)]

CARDS = {  # placeholder text for shots with no footage yet
    "5.1": "CANVA SCREEN - Job form\\NFull Name, Phone, Education: MBA, CV: Mehrin_CV.pdf",
    "5.2": "CANVA SCREEN - CV upload\\NUploading Mehrin_CV.pdf, progress 10% -> 35%",
    "5.7": "CANVA SCREEN - CV upload done\\N100% - CV Uploaded Successfully",
    "6.1": "CANVA SCREEN - Fee page\\NAPPLICATION PROCESSING FEE - BDT 1,000 - PAY NOW",
    "10.1": "CANVA SCREEN - Search\\NHow to report cybercrime in Bangladesh",
    "10.2": "CANVA SCREEN - Search results\\NBangladesh Police Online GD + Police Cyber Support for Women",
    "10.3": "CANVA SCREEN - Evidence folder\\NFiles dragged into EVIDENCE",
    "10.4": "CANVA SCREEN - Complaint form\\NComplaint details, evidence attached, SUBMIT",
    "10.5": "CANVA SCREEN - Submit\\NCursor clicks SUBMIT -> REPORT SUBMITTED",
    "12.1": "END CARD 1 - black screen\\NTagline part 1 (Bangla text)",
    "12.2": "END CARD 2 - black screen\\NTagline part 2 (Bangla text)",
    "12.3": "END CARD 3\\NVerify. Keep proof. Report. + PCSW contact line",
    "12.4": "END CARD 4\\NTitle: Matro 1000 (Bangla)",
}

# Blur boxes (x, y, w, h), 1920x1080, found on frames of each clip
G9_LOGO = (165, 820, 190, 180)    # lid logo, fixed for all of shot 4.2
G13_LID = (270, 800, 360, 280)    # pale mark on the closed lid, path while it drifts out of frame (0-2.4 s)
G15_LOGO = (490, 790, 300, 290)   # logo rising with the lid as it opens (12.6 s on)

G = "clips/G1-G7.mp4"
# Picture pieces in order: (source, in, out, seconds, options). Durations must add up to SHOTS.
PIECES = [
    (G, 0.00, 2.47, 2, {}), (G, 2.47, 5.03, 2, {}), (G, 5.03, 7.97, 3, {}), (G, 7.97, 9.97, 2, {}),
    (G, 9.97, 12.37, 2, {}),                                     # 12.37-12.67 black gap skipped
    (G, 12.67, 15.50, 3, {}), (G, 15.50, 17.97, 3, {}),
    ("stills/2.3.jpg", 0, 0, 2, {}),
    (G, 17.97, 19.97, 2, {}), (G, 19.97, 25.97, 6, {}),           # test clip: 2.4, 3.1
    (G, 25.97, 38.00, 14, {}),                                   # 3.2-3.3: test-clip leftover + G4, cut before he turns (~38 s)
    (G, 40.63, 48.00, 10, {"floor": 0.70}),                      # 3.4-3.5: ~74% instead of a long freeze
    (G, 48.00, 50.47, 2, {}), (G, 50.47, 52.00, 2, {}),           # 3.6, 3.7; 52-53 white gap skipped
    ("clips/G9.mp4", 0, 3.50, 4, {}), ("clips/G9.mp4", 3.50, 6.38, 3, {"blur": G9_LOGO}),
    ("clips/G9.mp4", 6.38, 10.00, 4, {}),
    ("card", 0, 0, 3, {}), ("card", 0, 0, 3, {}),
    ("stills/5.3.jpg", 0, 0, 3, {}), ("stills/5.4.jpg", 0, 0, 2, {}), ("stills/5.5.jpg", 0, 0, 3, {}),
    ("stills/5.6.jpg", 0, 0, 2, {}),
    ("card", 0, 0, 3, {}),
    (G, 53.00, 56.05, 3, {}),                                    # 5.8 (G7)
    ("card", 0, 0, 3, {}),
    ("clips/G10.mp4", 0, 2.46, 3, {}), ("clips/G10.mp4", 2.46, 4.38, 3, {}), ("clips/G10.mp4", 4.38, 6.38, 2, {}),
    ("clips/G11.mp4", 8.00, 14.00, 6, {}),                       # 7.1 (G11 0-8 = G10 repeat)
    ("clips/G8.mp4", 0, 3.46, 4.08, {"floor": 0.84}),            # 7.2 cross-cut: Iqbal in register room...
    ("clips/G10.mp4", 6.38, 8.00, 1.92, {"floor": 0.84}),        # ...then Mehrin on the phone (unused G10 tail)
    ("clips/G8.mp4", 3.46, 6.92, 5, {}),                         # 7.3
    ("clips/G11.mp4", 14.00, 16.00, 2, {}), ("clips/G8.mp4", 6.92, 9.92, 3, {}),  # 7.4 = 7.4a + 7.4b
    ("clips/G12.mp4", 11.00, 14.00, 3, {}),                      # 7.5 (G12 0-10 = repeat), ends on closed lid
    ("clips/G16.mp4", 0, 3.00, 3, {}),                           # 8.1: face appears at 3.46, never used
    ("clips/G16b.mp4", 0, 4.00, 4, {}), ("clips/G17.mp4", 0, 4.00, 4, {}),
    ("stills/8.4.jpg", 0, 0, 3, {}), ("stills/8.5.jpg", 0, 0, 6, {}),
    ("clips/G18.mp4", 0, 2, 2, {}), ("clips/G18.mp4", 2, 4, 2, {}), ("clips/G18.mp4", 4, 6, 2, {}),
    ("clips/G19.mp4", 0, 3.46, 3, {}), ("clips/G19.mp4", 3.46, 6.016, 3, {}),
    ("clips/G13.mp4", 0, 2.40, 2.40, {"blur": G13_LID}), ("clips/G13.mp4", 2.40, 4.00, 1.60, {}),  # 9.1
    ("clips/G14.mp4", 4.00, 14.016, 12, {}),                     # 9.2-9.3 (G14 0-4 = repeat)
    ("clips/G15.mp4", 10.00, 12.60, 2.60, {}), ("clips/G15.mp4", 12.60, 14.00, 1.40, {"blur": G15_LOGO}),  # 9.4
    ("card", 0, 0, 3, {}), ("card", 0, 0, 3, {}), ("card", 0, 0, 4, {}), ("card", 0, 0, 3, {}), ("card", 0, 0, 2, {}),
    ("clips/G20.mp4", 0, 2.46, 3, {}), ("clips/G20.mp4", 2.46, 5.013, 2, {}),
    ("card", 0, 0, 3, {}), ("card", 0, 0, 3, {}), ("card", 0, 0, 3, {}), ("card", 0, 0, 2, {}),
]


def run(script, *args):
    cmd = [sys.executable, str(SKILL / script), *map(str, args), "--json"]
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if p.returncode:
        sys.exit(f"FAILED: {' '.join(cmd)}\n{p.stdout[-2000:]}\n{p.stderr[-2000:]}")
    return json.loads(p.stdout)


def frames(path):
    v = run("probe.py", path)["video"]
    return v["nb_frames"] or round(v["duration"] * FPS)


def tc(f):
    s, ff = divmod(f, FPS)
    return f"{s // 3600:02d}:{s // 60 % 60:02d}:{s % 60:02d}:{ff:02d}"


def ass_time(f):  # 25 fps frame -> h:mm:ss.cc (one frame = 4 cs exactly)
    cs = f * 4
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def build_piece(i, piece, work):
    src, a, b, dur, opt = piece
    n = round(dur * FPS)
    out = work / f"p{i:02d}.mp4"
    if src == "card":
        run("background.py", "-o", out, "--duration", n / FPS, "--width", 1920, "--height", 1080,
            "--fps", FPS, "--color", "0x2b2b2b")
        return out
    if src.startswith("stills/"):
        run("insert.py", src, "-o", out, "--duration", n / FPS, "--width", 1920, "--height", 1080,
            "--fps", FPS, "--zoom", "in", "--zoom-amount", 1.1)
        return out
    length = b - a
    speed = 1.0 if length >= dur else max(length / dur, opt.get("floor", FLOOR))
    cut = work / f"p{i:02d}_cut.mp4"
    run("cut.py", src, "--start", a, "--end", a + min(length, dur), "--accurate", "-o", cut)
    if "blur" in opt:
        x, y, w, h = opt["blur"]
        run("redact.py", cut, "--x", x, "--y", y, "--width", w, "--height", h, "--mode", "blur",
            "--blur-strength", 30, "-o", (cut := cut.with_name(cut.stem + "_blur.mp4")))
    fit = work / f"p{i:02d}_fit.mp4"
    extra = ["--duration", round(length / speed, 3), "--method", "speed"] if speed < 1 else []
    run("fit.py", cut, "--fps", FPS, "--width", 1920, "--height", 1080, *extra, "-o", fit)
    have = frames(fit)  # conform to the exact frame count so every shot lands on its PART 1 time
    if have < n:
        run("freeze.py", fit, "--hold", (n - have) / FPS, "--mode", "extend", "-o", out)
    elif have > n:
        run("fit.py", fit, "--duration", n / FPS, "--method", "trim", "-o", out)
    else:
        fit.rename(out)
    got = frames(out)
    print(f"  piece {i:02d} {src} {a}-{b} -> {got} f ({speed:.0%})" + (" BLUR" if "blur" in opt else ""))
    if got != n:
        sys.exit(f"piece {i} has {got} frames, wanted {n}")
    return out


def write_ass(path):
    lines = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1920", "PlayResY: 1080", "WrapStyle: 2", "",
             "[V4+ Styles]",
             "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
             "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
             "Alignment, MarginL, MarginR, MarginV, Encoding",
             "Style: Label,Consolas,30,&H00FFFFFF,&H00FFFFFF,&H80000000,&H80000000,0,0,0,0,100,100,0,0,3,6,0,7,24,24,20,1",
             "Style: Card,Arial,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,120,120,0,1",
             "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    f0 = 0
    for shot, sec in SHOTS:
        f1 = f0 + sec * FPS
        if shot in CARDS:
            lines.append(f"Dialogue: 0,{ass_time(f0)},{ass_time(f1)},Card,,0,0,0,,"
                         f"{{\\fs96\\b1}}{shot}  |  {sec} s{{\\fs64\\b0}}\\N\\N{CARDS[shot]}")
        for f in range(f0, f1):
            lines.append(f"Dialogue: 1,{ass_time(f)},{ass_time(f + 1)},Label,,0,0,0,,{shot}   {tc(f)}")
        f0 = f1
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return f0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", default="output/rough_cut_v1.mp4")
    ap.add_argument("--work", help="folder for intermediates (default: a temp folder)")
    args = ap.parse_args()
    total = sum(d for *_, d, _ in PIECES)
    assert round(total * FPS) == sum(s for _, s in SHOTS) * FPS == 207 * FPS, total
    work = Path(args.work or tempfile.mkdtemp(prefix="matro_rc_")).resolve()
    work.mkdir(parents=True, exist_ok=True)
    print(f"work: {work}")
    parts = [build_piece(i, p, work) for i, p in enumerate(PIECES)]
    (work / "parts.txt").write_text("".join(f"{p.name}\n" for p in parts))
    joined, muted, ass = work / "joined.mp4", work / "muted.mp4", work / "labels.ass"
    run("join.py", "--list", work / "parts.txt", "--transition", "none", "--width", 1920, "--height", 1080,
        "--fps", FPS, "-o", joined)
    run("audio.py", joined, "--gain", -150, "-o", muted)  # mute all clip audio, keep a silent track for later
    n = write_ass(ass)
    run("caption.py", muted, "--ass", ass, "-o", ROOT / args.output)
    got = frames(ROOT / args.output)
    print(f"done: {args.output}  {got} frames (want {n})")
    if got != n:
        sys.exit("frame count mismatch")


if __name__ == "__main__":
    main()
