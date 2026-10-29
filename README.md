# মাত্র ১০০০ ("Only 1000") — short film project

A short three-dimensional (3D) animated film in Bangla for the **CyberFrames 2026 Finale**, about a fake job offer that asks for a 1,000 taka "processing fee", and why you should check before you trust or pay.

- **Submission deadline:** Sunday 1 November 2026, 11:59 PM. We aim to submit on **Sunday afternoon**.
- **Where we are:** all animated clips and still pictures are made. A picture-only rough cut exists ([`output/rough_cut_v2.mp4`](output/rough_cut_v2.mp4), 3 minutes 18 seconds). Still missing: the screens, text overlays, voices, sound effects and music, then the final edit.
- **Full task list:** [`output/tasks/Team_Plan_Finish_The_Film.md`](output/tasks/Team_Plan_Finish_The_Film.md). **Read it before you start.**

---

## 1. What is in this repository

| Path | What it is |
|---|---|
| [`Matro1000_FINAL_Package_3D.txt`](Matro1000_FINAL_Package_3D.txt) | Master script. **Part 1** = every shot with its time. **Part 2** = video prompts, and at the very end "UI SCREEN DESIGN SPECIFICATIONS" (how each screen should look). **Part 3** = all dialogue and sounds |
| [`Matro1000_Google_Vids_Notebook.md`](Matro1000_Google_Vids_Notebook.md) | Production notebook: how the clips were made and who made what |
| `clips\` | The animated video clips (`G1-G7.mp4`, `G4.mp4`, `G8.mp4` … `G20.mp4`) and [`clips/NOTES.txt`](clips/NOTES.txt) (which seconds of each clip become which shot) |
| `stills\` | Still pictures for shots 2.3, 5.3 to 5.6, 8.4 and 8.5 |
| `refs\` | Character and room reference pictures (not used in the film) |
| [`output/rough_cut_v2.mp4`](output/rough_cut_v2.mp4) | **Current rough cut, the timing reference for everyone.** No sound yet |
| `output\rough_cut_v1.mp4` | Old rough cut with repeated footage. Ignore it |
| [`output/tasks/Team_Plan_Finish_The_Film.md`](output/tasks/Team_Plan_Finish_The_Film.md) | **The team plan:** every remaining task, who does it, file names, where to save, schedule |
| [`output/tasks/screens_tasks.md`](output/tasks/screens_tasks.md) | Exact text for every screen and text overlay |
| [`output/tasks/voice_tasks.md`](output/tasks/voice_tasks.md) | Every spoken line, who says it, acting notes, time slot |
| [`output/tasks/sfx_music_tasks.md`](output/tasks/sfx_music_tasks.md) | Every sound effect with its exact moment, plus the music rules |
| `output\tasks\green_screen_frames\` | A frame from the rough cut for each green phone or laptop screen, showing its angle |
| `screens\`, `audio\`, `sfx\`, `music\` | **Where your finished work goes.** These folders don't exist yet: create them when you add your first file (see step 8) |

### How to read the rough cut
- **Top-left label.** For example `7.2   00:01:40:05` means shot 7.2 at 0 hours, 1 minute, 40 seconds and 5 frames. There are 25 frames in a second, and every time in our task lists uses this clock.
- **Grey cards with white writing** are screens nobody has made yet.
- **Bright green phone, laptop and monitor screens** are left green on purpose. The editor replaces them with your screen pictures.

---

## 2. Getting started (Windows PowerShell, once)

The videos are stored with **Git Large File Storage**: Git keeps a small note for each video and downloads the real file separately. On 29 October the repository's history was rewritten to set this up, so **any copy downloaded before then no longer works. Download it again.**

1. Open **PowerShell** (Start menu, type "PowerShell").

2. Turn on Large File Storage and tell Git who you are. Use your own name and the email address of your GitHub account:
   ```powershell
   git lfs install
   git config --global user.name "Your Name"
   git config --global user.email "your-github-email@example.com"
   ```

3. **If you downloaded this repository before**, set the old copy aside (skip this if you never did). If it has files you haven't uploaded yet, copy them somewhere else first. If you don't remember where it is, find it:
   ```powershell
   Get-ChildItem -Path $HOME, D:\ -Directory -Recurse -Filter "short-film*" -ErrorAction SilentlyContinue | Select-Object FullName
   ```
   Then rename it, using the path the command showed:
   ```powershell
   Rename-Item "C:\Users\YourName\Documents\short-film" "short-film-OLD"
   ```

4. Download a fresh copy (about 400 MB):
   ```powershell
   cd "$HOME\Documents"
   git clone https://github.com/fatema-hossain/short-film.git
   cd short-film
   ```
   If a browser window asks you to sign in to GitHub, sign in. If you're refused access, ask Fatema to add you as a collaborator.

5. Open [`output/tasks/Team_Plan_Finish_The_Film.md`](output/tasks/Team_Plan_Finish_The_Film.md) and find your tasks.

6. Once you've checked nothing is missing, you can delete `short-film-OLD`.

---

## 3. Every time you work

7. **Before you start**, get everyone's latest changes:
   ```powershell
   cd "$HOME\Documents\short-film"
   git pull
   ```

8. **Put your finished file in the right folder**, named exactly as the team plan says. If the folder doesn't exist yet, create it first. Example:
   ```powershell
   New-Item -ItemType Directory -Force screens
   Copy-Item "$HOME\Downloads\5.1.mp4" screens\
   ```

9. **Upload it**, with a short description of what you added:
   ```powershell
   git add screens\5.1.mp4
   git commit -m "Add Canva screen 5.1 (job form)"
   git push
   ```

10. **If `git push` is rejected** because someone else uploaded first, run these two and you're done:
    ```powershell
    git pull
    git push
    ```

11. **To see what you've changed** but not uploaded yet:
    ```powershell
    git status
    ```

### Rules
- **Never run `git push --force` or `git push -f`.** It can delete other people's work. If a push is rejected, use step 10 or ask.
- **One owner per file.** Git can't merge two people's edits to the same video or image; one of them gets lost. Only change files you own.
- **Only upload finished files** to `screens`, `audio`, `sfx` and `music`. Leave out drafts and test exports.
- **Name files exactly** as the team plan says, for example `screens\5.1.mp4`, `audio\3.1_Iqbal_take1.wav`, `sfx\9.4_laptop_clack.wav`.

---

## 4. Remaining tasks

The split below is a suggestion from the team plan, using the role names from the notebook:
- **Person A** made Iqbal's clips.
- **Person B** made Mehrin's clips.
- **Person C** made the scammer's clips.
- **Person D** made the other stills.
- **The Editor** assembles the film.

Change owners if you like, but every task needs exactly one owner. **The details for each task (exact text, sizes, file names, times) are in the [team plan](output/tasks/Team_Plan_Finish_The_Film.md) and the three task lists in `output\tasks\`.**

| # | Task | Owner (suggested) | What to make | Save to |
|---|---|---|---|---|
| 1 | Fake careers website | Person B | Career Search page (4.1), Job Application page (4.3), application form (5.1), CV upload 10–35% (5.2) and 100% (5.7), fee screen (6.1), fee page for the laptop (6.2–6.4) and its blurred version (7.1–7.5). Same colours and layout everywhere | `screens\` |
| 2 | Phone screens and classroom text | Person A | Incoming call (2.3), message from Unknown (3.6), forward to Mehrin (3.7), chat from Baba (4.2), Baba Calling (6.3), blackboard text (2.1–2.2), door sign রেজিস্টার কক্ষ (3.5), batch label ২০১৮ · বি সেকশন (7.3) | `screens\` and `screens\overlays\` |
| 3 | Scammer's screens | Person C | Voice-conversion sound wave (8.3), four scam windows (8.4), animated fictional wallet balance (8.5), "ghost" layer for the street scene (8.9–8.10), floating Bangla doubt phrases (9.2) | `screens\` and `screens\overlays\` |
| 4 | Reporting screens and end cards | Person D | Search, results, evidence folder, complaint form, REPORT SUBMITTED (10.1–10.5); the four end cards (12.1–12.4) | `screens\` |
| 5 | Voice recording | Person D runs it; actors as cast | 33 lines, 3 takes each. Cast Iqbal, Mehrin, the colleague, the scammer, and **six different people** for the inner voices in Scene 9. See [`voice_tasks.md`](output/tasks/voice_tasks.md) | `audio\` |
| 6 | "Ahona" voice | Person C | Run the scammer actor's 9 Ahona lines and his shot 8.2 line through one voice changer, so it's one consistent woman's voice | `audio\ahona_converted\` |
| 7 | Sound effects | Person D | Every sound in [`sfx_music_tasks.md`](output/tasks/sfx_music_tasks.md) section 1, from free libraries, with sources listed in `sfx\sources.txt` | `sfx\` |
| 8 | Music | Person A | One or two royalty-free tracks following the music rules (it must stop dead on “এক টাকাও দিবা না।” and at the laptop click), with sources listed in `music\sources.txt` | `music\` |
| 9 | Final edit in CapCut | Editor | Assemble from the rough-cut timing, swap in the screens, key the green screens, add overlays, tidy logo blurs, voices, sound, music; export 1920 × 1080, 25 frames per second, MP4 | `output\final\` |
| 10 | Final check and submission | Editor + one other person | Watch the whole film twice and tick the checklist in the team plan, then upload through the Google Form link in the organizers' email | — |

### Schedule
| When | Finished |
|---|---|
| **Friday 30 October, 10:00 PM** | Tasks 1–4 (all screens and overlays) uploaded. Voice casting done; Iqbal's and Mehrin's lines recorded |
| **Saturday 31 October, 12:00 PM** | Tasks 5–8 (all voices, Ahona voice, sound effects, music) uploaded |
| **Saturday 31 October, 10:00 PM** | Editor shares the first complete version with sound |
| **Sunday 1 November, 12:00 PM** | Everyone's notes in; fixes done; final export |
| **Sunday 1 November, by 5:00 PM** | Final check and upload. **Hard deadline 11:59 PM** |

### Rules for the film itself
- No real brand, bank, wallet, police or government logos or names on any screen.
- No team names, no university or college names, no real phone numbers (write `01XXXXXXXXX`).
- The scammer's face is never shown.
- Mehrin never presses PAY NOW, and no payment is ever shown.
- Bangla text is typed in Canva, never generated.

### Open questions for the team
1. **Length.** The master script says the official range is 3:00 to 3:30. Confirm it in the organizers' rules.
2. **Sparkle mark.** The small four-pointed sparkle in the bottom-right corner of the Google Vids clips: keep it or not?
3. **Shot 3.6.** The phone screen is never visible: a pop-up phone graphic, or a cut to a phone close-up?
4. **Shot 6.3.** "Baba Calling" must be tracked onto a black phone screen. If it looks bad, show the graphic full-screen instead?
5. **New G4 clip (shots 3.2–3.3).** The classroom looks slightly different from the clip before it. Acceptable, or regenerate?
