#!/usr/bin/env python3
"""Matro1000 rough cut: picture only, 1920x1080, 25 fps, burned-in shot + timecode labels.

Rebuild when screens/stills/clips arrive:  python output/build_rough_cut.py -o output/rough_cut_v3.mp4
Every step is one of the ffmpeg-skill scripts. Shot order and target lengths = PART 1 of
Matro1000_FINAL_Package_3D.txt; source ranges = clips/NOTES.txt, corrected where measured (see comments).
Length is not locked to 3:27: a shot whose footage runs short is slowed to FLOOR and then simply
ends early (only gaps up to MAX_HOLD are filled by holding the last frame).
"""
import argparse, json, os, subprocess, sys, tempfile
from pathlib import Path

SKILL = Path(os.environ.get("FFMPEG_SKILL_SCRIPTS") or next(Path.home().glob("*/skills/ffmpeg-skill/scripts")))
ROOT = Path(__file__).resolve().parent.parent
FPS = 25
FLOOR = 0.85     # slowest speed for a short source
MAX_HOLD = 0.25  # longest last-frame hold; a bigger gap shortens the shot instead
DIP = 0.6        # dip-to-black length at scene changes
DIP_AT = (11, 88, 124, 156, 196)  # PART 1 seconds: before 2.1, 6.1, 8.1, 9.1, 12.1

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
# Picture pieces in order: (source, in, out, PART 1 seconds, options). PART 1 seconds add up to 207.
PIECES = [
    (G, 0.00, 2.47, 2, {}), (G, 2.47, 5.03, 2, {}), (G, 5.03, 7.97, 3, {}), (G, 7.97, 9.97, 2, {}),
    (G, 9.97, 12.37, 2, {}),                                     # 12.37-12.67 black gap skipped
    (G, 12.67, 15.50, 3, {}), (G, 15.50, 17.97, 3, {}),
    ("stills/2.3.jpg", 0, 0, 2, {}),
    (G, 17.97, 19.97, 2, {}), (G, 19.97, 24.50, 6, {}),           # test clip: 2.4, 3.1 (ends before he lifts the books)
    # G1-G7 28-38 is the test clip again (untrimmed Extend repeat) and 38-40.63 unusable: G4.mp4 replaces both
    ("clips/G4.mp4", 0, 9.00, 14, {}),                           # 3.2-3.3, out before he stands up
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
    ("clips/G10.mp4", 0, 2.46, 3, {}), ("clips/G10.mp4", 2.46, 4.38, 3, {}),
    # Mehrin's phone take plays once, in order: 6.4 -> 7.1 -> 7.2 cutaway -> 7.4a (G11 0-8 = G10 repeat)
    ("clips/G10.mp4", 4.38, 6.38, 2, {}), ("clips/G10.mp4", 6.38, 8.00, 1.62, {}),
    ("clips/G11.mp4", 8.00, 12.00, 4.38, {}),
    ("clips/G8.mp4", 0, 3.46, 4, {}),                            # 7.2: Iqbal in the register room...
    ("clips/G11.mp4", 12.00, 14.00, 2, {}),                      # ...cut to Mehrin listening
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


def plan(i):
    """Frames this piece will have, and (speed, cut end) for clips."""
    src, a, b, span, opt = PIECES[i]
    if not src.startswith("clips/"):
        return round(span * FPS), 1.0, None
    nxt = PIECES[i + 1] if i + 1 < len(PIECES) else None
    seamless = nxt and nxt[0] == src and nxt[1] == b
    end = b if seamless else b - 0.02  # stop one frame short of the next shot's first frame
    if end - a >= span:
        return round(span * FPS), 1.0, a + span
    speed = max((end - a) / span, opt.get("floor", FLOOR))
    out = (end - a) / speed
    if span - out <= MAX_HOLD:
        out = span
    return round(out * FPS), speed, end


def build_piece(i, work):
    src, a, b, span, opt = PIECES[i]
    n, speed, end = plan(i)
    out = work / f"p{i:02d}.mp4"
    if src == "card":
        run("background.py", "-o", out, "--duration", n / FPS, "--width", 1920, "--height", 1080,
            "--fps", FPS, "--color", "0x2b2b2b")
        return out
    if src.startswith("stills/"):
        run("insert.py", src, "-o", out, "--duration", n / FPS, "--width", 1920, "--height", 1080,
            "--fps", FPS, "--zoom", "in", "--zoom-amount", 1.1)
        return out
    cut = work / f"p{i:02d}_cut.mp4"
    run("cut.py", src, "--start", a, "--end", end, "--accurate", "-o", cut)
    if "blur" in opt:
        x, y, w, h = opt["blur"]
        run("redact.py", cut, "--x", x, "--y", y, "--width", w, "--height", h, "--mode", "blur",
            "--blur-strength", 30, "-o", (cut := cut.with_name(cut.stem + "_blur.mp4")))
    fit = work / f"p{i:02d}_fit.mp4"
    extra = ["--duration", round((end - a) / speed, 3), "--method", "speed"] if speed < 1 else []
    run("fit.py", cut, "--fps", FPS, "--width", 1920, "--height", 1080, *extra, "-o", fit)
    have = frames(fit)  # conform to the planned frame count
    if have < n:
        run("freeze.py", fit, "--hold", (n - have) / FPS, "--mode", "extend", "-o", out)
    elif have > n:
        run("fit.py", fit, "--duration", n / FPS, "--method", "trim", "-o", out)
    else:
        fit.rename(out)
    got = frames(out)
    print(f"  piece {i:02d} {src} {a}-{end:.2f} -> {got} f ({speed:.0%})" + (" BLUR" if "blur" in opt else ""))
    if got != n:
        sys.exit(f"piece {i} has {got} frames, wanted {n}")
    return out


def timeline():
    """Map PART 1 seconds -> output frame: [(part1_start, span, out_start_frame, out_frames)] per piece."""
    rows, p1, f, k = [], 0.0, 0, 0
    dip = round(DIP * FPS)
    for i, piece in enumerate(PIECES):
        if i and round(p1, 3) in DIP_AT:
            k += 1
        n = plan(i)[0]
        rows.append((p1, piece[3], f - k * dip, n))
        p1, f = p1 + piece[3], f + n
    return rows, f - k * dip


def to_frame(t, rows):
    """Output frame for PART 1 time t; scene changes land in the middle of their dip."""
    for p1, span, f0, n in rows:
        if p1 <= t < p1 + span - 1e-9:
            mid = round(DIP * FPS / 2) if round(t, 3) == round(p1, 3) and round(t, 3) in DIP_AT else 0
            return f0 + mid + round((t - p1) / span * n)
    return rows[-1][2] + rows[-1][3]


def write_ass(path):
    rows, total = timeline()
    lines = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1920", "PlayResY: 1080", "WrapStyle: 2", "",
             "[V4+ Styles]",
             "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
             "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
             "Alignment, MarginL, MarginR, MarginV, Encoding",
             "Style: Label,Consolas,30,&H00FFFFFF,&H00FFFFFF,&H80000000,&H80000000,0,0,0,0,100,100,0,0,3,6,0,7,24,24,20,1",
             "Style: Card,Arial,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,120,120,0,1",
             "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    t = 0
    for shot, sec in SHOTS:
        f0, f1 = to_frame(t, rows), min(to_frame(t + sec, rows), total)
        if shot in CARDS:
            lines.append(f"Dialogue: 0,{ass_time(f0)},{ass_time(f1)},Card,,0,0,0,,"
                         f"{{\\fs96\\b1}}{shot}  |  {(f1 - f0) / FPS:.0f} s{{\\fs64\\b0}}\\N\\N{CARDS[shot]}")
        for f in range(f0, f1):
            lines.append(f"Dialogue: 1,{ass_time(f)},{ass_time(f + 1)},Label,,0,0,0,,{shot}   {tc(f)}")
        t += sec
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", default="output/rough_cut_v2.mp4")
    ap.add_argument("--work", help="folder for intermediates (default: a temp folder)")
    ap.add_argument("--shots", action="store_true", help="print the new shot start times and exit")
    args = ap.parse_args()
    assert round(sum(p[3] for p in PIECES), 3) == sum(s for _, s in SHOTS) == 207
    if args.shots:
        rows, total = timeline()
        t = 0
        for shot, sec in SHOTS:
            print(f"{shot}\t{tc(to_frame(t, rows))}\t{(min(to_frame(t + sec, rows), total) - to_frame(t, rows)) / FPS:.2f}")
            t += sec
        print(f"TOTAL\t{tc(total)}")
        return
    work = Path(args.work or tempfile.mkdtemp(prefix="matro_rc_")).resolve()
    work.mkdir(parents=True, exist_ok=True)
    print(f"work: {work}")
    parts = [build_piece(i, work) for i in range(len(PIECES))]
    # one block per scene group; dips to black between blocks
    blocks, cur, p1 = [], [], 0.0
    for i, part in enumerate(parts):
        if i and round(p1, 3) in DIP_AT:
            blocks.append(cur)
            cur = []
        cur.append(part)
        p1 += PIECES[i][3]
    blocks.append(cur)
    block_files = []
    for k, blk in enumerate(blocks):
        lst = work / f"block{k}.txt"
        lst.write_text("".join(f"{p.name}\n" for p in blk))
        bf = work / f"block{k}.mp4"
        run("join.py", "--list", lst, "--transition", "none", "--width", 1920, "--height", 1080, "--fps", FPS, "-o", bf)
        block_files.append(bf)
    joined, muted, ass = work / "joined.mp4", work / "muted.mp4", work / "labels.ass"
    run("join.py", *block_files, "--transition", "fadeblack", "--duration", DIP, "--width", 1920, "--height", 1080,
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
