# মাত্র ১০০০ ("Only 1000") — Team plan to finish the film

**Read this first.** This document lists every piece of work still needed to turn the current rough cut into the finished film we submit. Each task says who does it (suggested), what to make, exactly where to save it, and how to know it is done.

- **Today:** Thursday 29 October 2026.
- **Submission deadline:** Sunday 1 November 2026, 11:59 PM (from the production notebook, step "Export and submit"). Plan to submit on Sunday afternoon, not at midnight.

---

## 1. Background: what we are making

- **What it is.** A short three-dimensional (3D) animated film in Bangla for the CyberFrames 2026 Finale competition. The theme is online job-offer fraud and why you should check before you trust or pay.
- **Picture size.** Widescreen landscape, 1920 pixels wide by 1080 pixels tall.
- **Length.** The script was written for 3 minutes 27 seconds. The current rough cut is 3 minutes 18 seconds, because one clip was shorter than planned (explained in section 3).
- **How it was made.** The animated clips were generated in Google Vids, the still pictures in Gemini, and the screens will be made in Canva. The final edit happens in CapCut.

### The story in one paragraph
Iqbal, a 56-year-old college teacher, wipes "VERIFY FIRST" off his blackboard just as an unknown number calls. A polite woman's voice says she is "Ahona", his former student, now in a company's human resources department, and asks if anyone he knows needs a job. Iqbal says his daughter Mehrin is looking, and he forwards the application link she sends. Mehrin fills in the form and uploads her CV (résumé). Meanwhile the same "Ahona" voice is heard calling a farmer, a mother, a shopkeeper and a young job-seeker. The site then asks Mehrin for a 1,000 taka "application processing fee". Before she pays, her father calls: a colleague got the same call, and the college register shows no "Ahona" in that batch. Mehrin does not pay. We then see the truth: "Ahona" is an ordinary man using voice-changing software, his phone's balance rising with other victims' money. He calmly leaves for the evening, gives some coins to a beggar without looking, and disappears into the Dhaka crowd. Mehrin hesitates over whether to report it, opens her laptop with a firm click, and reports it to the Bangladesh Police with evidence. The film ends on his house of playing cards falling, and three end messages.

### The characters
| Character | Who they are | On screen? |
|---|---|---|
| Iqbal | 56, college teacher, grey beard, glasses, pale blue shirt | Yes |
| Mehrin | 26, Iqbal's daughter, mint-green kameez, white dupatta | Yes |
| "Ahona" | The fake former student. **Voice only**, the scammer's voice changed to a woman's voice | Never shown |
| The scammer | About 30, charcoal shirt. **His face must never be shown** (only back, hands, mouth and microphone) | Partly |
| The colleague | Another teacher, about 50, one line | Yes |
| Inner voices 1 to 6 | The doubts in Mehrin's head in Scene 9 | Voice only |

---

## 2. Where everything is (full file paths)

The project lives on **the editor's computer** in the folder `D:\Matro1000_Edit\`. Everyone else shares files through **the team's shared Google Drive folder for this film**. That folder must have subfolders with exactly these names: `clips`, `stills`, `screens`, `audio`, `sfx`, `music`. Upload into the matching subfolder, and the editor copies each file into the same subfolder on their computer.

| What | Full path on the editor's computer | Notes |
|---|---|---|
| Master script | `D:\Matro1000_Edit\Matro1000_FINAL_Package_3D.txt` | **Part 1** = every shot with its time. **Part 2** = video prompts and, at the very end, "UI SCREEN DESIGN SPECIFICATIONS" (how each screen should look, sections A to I). **Part 3** = all dialogue and sounds |
| Production notebook | `D:\Matro1000_Edit\Matro1000_Google_Vids_Notebook.md` | How the clips were made, who made what, the Canva screen list (step 34) and editing steps (steps 38 to 40) |
| Video clips | `D:\Matro1000_Edit\clips\` | `G1-G7.mp4`, `G4.mp4` (new), `G8.mp4` … `G20.mp4`, `G16b.mp4` |
| Editor's clip notes | `D:\Matro1000_Edit\clips\NOTES.txt` | Which seconds of each clip become which shot. **Two of its entries were wrong**, see section 3 |
| Still pictures | `D:\Matro1000_Edit\stills\` | `2.3.jpg`, `5.3.jpg`, `5.4.jpg`, `5.5.jpg`, `5.6.jpg`, `8.4.jpg`, `8.5.jpg` (all done) |
| Reference pictures | `D:\Matro1000_Edit\refs\` | Character boards and rooms, for reference only; not used in the film |
| **Screens and text overlays** (to make) | `D:\Matro1000_Edit\screens\` | Empty now. Canva graphics, phone and laptop screens, text overlays go here |
| **Voice recordings** (to make) | `D:\Matro1000_Edit\audio\` | Empty now |
| **Sound effects** (to collect) | `D:\Matro1000_Edit\sfx\` | Empty now |
| **Music** (to choose) | `D:\Matro1000_Edit\music\` | Empty now |
| **Current rough cut** | `D:\Matro1000_Edit\output\rough_cut_v2.mp4` | Picture only, no sound. **This is the timing reference for everyone.** |
| Older rough cut | `D:\Matro1000_Edit\output\rough_cut_v1.mp4` | Outdated (it contained repeated footage). Ignore it |
| Rough-cut build script | `D:\Matro1000_Edit\output\build_rough_cut.py` | Editor only. Rebuilds the rough cut automatically |
| Detailed screen list | `D:\Matro1000_Edit\output\tasks\screens_tasks.md` | Exact text for every screen, with a reference picture of each phone or laptop screen |
| Reference pictures of the green screens | `D:\Matro1000_Edit\output\tasks\green_screen_frames\` | `shot_2.3.png`, `shot_4.1.png` and so on: a frame from the rough cut showing the screen's angle |
| Detailed voice list | `D:\Matro1000_Edit\output\tasks\voice_tasks.md` | Every line, who says it, where it goes, acting notes |
| Detailed sound effects and music list | `D:\Matro1000_Edit\output\tasks\sfx_music_tasks.md` | Every sound effect with its exact moment, plus the music rules |

### How to read the rough cut
- **Top-left label.** For example `7.2   00:01:40:05` means you are watching **shot 7.2** at **0 hours, 1 minute, 40 seconds and 5 frames**. There are 25 frames in every second, so the last number runs from 00 to 24. Every time in this plan and in the detailed lists uses this same clock.
- **Grey cards with white writing** are screens nobody has made yet (Canva graphics, end cards). They name the shot, its length and what belongs there.
- **Bright green screens** on phones, laptops and the scammer's monitor are left green on purpose. The editor replaces them with the screen pictures made in workstreams 2 and 3 (this is called "chroma key").
- **Short fades to black** happen at five scene changes, to soften them.
- **Grey blurred rectangles on the laptop lid** hide a real brand logo. They are rough; the editor makes them neat in CapCut.

---

## 3. What changed since the first plan (please read)

1. **The old G4 clip was a copy.** Inside `D:\Matro1000_Edit\clips\G1-G7.mp4`, seconds 28 to 38 were an exact copy of seconds 18 to 28. When the clip was extended in Google Vids, the repeated part was never cut off. The real new part was only 2.6 seconds long and unusable: he walks off and his books disappear. **The new `D:\Matro1000_Edit\clips\G4.mp4` (10 seconds) replaces it and is now in the rough cut as shots 3.2 and 3.3.** It is 4 seconds shorter than the script planned, which is the main reason the film is now 3:18.
2. **Repeated moments and jumps removed.** Mehrin's long phone take now plays once, in order. Shots no longer end on a frozen picture of the next shot.
3. **Fades to black** were added at the scene changes into Scenes 2, 6, 8 and 9 and into the end cards. Scene changes the script wants as hard cuts stay hard cuts: the "send" sound into Mehrin's notification, the laptop click, and the "submit" click.
4. **All times in the detailed lists were updated to the new rough cut** (`rough_cut_v2.mp4`). Do not use times from older messages.

---

## 4. Rules for everyone (breaking these can disqualify the film)

- **No real brands.** No real bank, mobile wallet, police, government or company logos, and no real brand names on any screen. Invented names only.
- **No real people's details.** No real phone numbers (write `01XXXXXXXXX`), no real names of team members, no university or college names or logos anywhere in the film.
- **The scammer's face is never shown.** Only his back, hands, shoulders down, and his mouth with the microphone.
- **Mehrin never pays.** No screen may show a completed payment.
- **Bangla text** must be typed in Canva (or made as a picture file), never generated by artificial intelligence, so the letters are correct.
- **Name files by shot number**, exactly as described in each task (for example `5.1.mp4`, `3.1_Iqbal_take1.wav`).
- **Music and sound effects must be free to use** (royalty-free). Write down the website and licence for every file in a text file named `sources.txt` in the same folder.

---

## 5. The tasks

Names in the notebook were left blank, so roles are written as "Person A" and so on, matching notebook step 1:
- **Person A** made Iqbal's clips.
- **Person B** made Mehrin's clips.
- **Person C** made the scammer's clips and the stills for shots 8.4 and 8.5.
- **Person D** made the other stills and was planned for screens and sound.
- **The Editor** puts everything together.

A, B and C have finished their clips, so the remaining work is spread across everyone. **This split is a suggestion: change it if you like, but make sure every task has one owner.**

Write names here: Person A = ________ · Person B = ________ · Person C = ________ · Person D = ________ · Editor = ________

---

### Workstream 1 — Fake careers website (Person B)
**Why one person:** the script requires the same fictional careers website, with the same colours and layout, everywhere it appears (Scenes 4, 5 and 6). One designer keeps it consistent.

**Make these**, with exact wording from `D:\Matro1000_Edit\output\tasks\screens_tasks.md` and design rules C, D and E at the end of Part 2 of the master script:

| Shot | What | Shape | Save as |
|---|---|---|---|
| 4.1 | "Career Search" page with three job cards | Wide laptop screen, 1920 × 1080 | `screens\4.1.png` |
| 4.3 | "Job Application — Junior Executive — Apply Now" page | Wide, 1920 × 1080 | `screens\4.3.png` |
| 5.1 | Application form being filled in (full-screen, 3 seconds, animated) | Wide, 1920 × 1080 | `screens\5.1.mp4` |
| 5.2 | Mehrin_CV.pdf uploading, progress 10% to 35% (3 seconds, animated) | Wide | `screens\5.2.mp4` |
| 5.7 | Progress 100%, "CV Uploaded Successfully" (3 seconds) | Wide | `screens\5.7.mp4` |
| 6.1 | "APPLICATION PROCESSING FEE — ৳1,000 — PAY NOW" (3 seconds) | Wide | `screens\6.1.mp4` |
| 6.2 to 6.4 | The same fee page, to go on Mehrin's laptop. The cursor in the footage hovers at the **centre** of the screen, so put the PAY NOW button there | Wide | `screens\6.2_fee_page.png` |
| 7.1 to 7.5 | The same fee page, **blurred** | Wide | `screens\7.1_fee_page_blurred.png` |

**Done when:** all eight files are in the shared `screens` folder, the wording matches the detailed list letter for letter, and no real company appears anywhere.

### Workstream 2 — Phone screens and classroom text (Person A)
**Make these** (exact text in `screens_tasks.md`, design rules A and B in Part 2 of the master script):

| Shot | What | Shape | Save as |
|---|---|---|---|
| 2.3 | Incoming call: "Unknown Number", green answer button | Tall phone screen, 1080 × 1920 | `screens\2.3.png` |
| 3.6 | Message from Unknown: “স্যার, আবেদন করার লিংকটা পাঠালাম।” plus the link `jobs.example.invalid` | Tall phone | `screens\3.6.png` |
| 3.7 | Forward to Mehrin, with Iqbal's message and a link preview | Tall phone | `screens\3.7.png` |
| 4.2 | Chat from "Baba" with the same message and link | Tall phone | `screens\4.2.png` |
| 6.3 | "Baba Calling" incoming call | Tall phone | `screens\6.3_baba_calling.png` |
| 2.1 to 2.2 | Blackboard text: DIGITAL HYGIENE / VERIFY FIRST / Unknown Links • Fake Offers, white chalk style, **transparent background** | Wide | `screens\overlays\2.1_board_text.png` and `screens\overlays\2.2_verify_first.png` (VERIFY FIRST alone, so the editor can wipe it away) |
| 3.5 | Door sign: রেজিস্টার কক্ষ | Transparent background | `screens\overlays\3.5_register_room_sign.png` |
| 7.3 | ২০১৮ · বি সেকশন (over the register pages) | Transparent background | `screens\overlays\7.3_batch_label.png` |

**Two known problems to know about:**
- In shot 3.6 the phone screen is never visible in the footage, so the editor will show your 3.6 picture as a pop-up phone.
- In shot 6.3 the phone screen is black, not green, so the editor tracks your picture onto it by hand.

**Done when:** all files are uploaded and the Bangla text has been checked by a second person.

### Workstream 3 — Scammer's screens and the "ghost" layer (Person C)
| Shot | What | Shape | Save as |
|---|---|---|---|
| 8.3 | "VOICE CONVERSION": a sound wave that changes shape after a mouse click, with no real software name (4 seconds). A screen recording of any free audio editor works if all names are hidden | Wide monitor, 1920 × 1080 | `screens\8.3.mp4` |
| 8.4 | Four windows titled FAKE JOB / LOAN APPLICATION / SCHOLARSHIP / TRAVEL BOOKING | Wide monitor | `screens\8.4.png` |
| 8.5 | Fictional wallet app "Account Overview" → "Available Balance". Starts at ৳12,400, then +৳500 → ৳12,900, +৳1,000 → ৳13,900, +৳800 → ৳14,700. **6 seconds, animated.** The three changes happen 0.7, 2.5 and 4.3 seconds into the video, and the final balance stays readable to the end | Tall phone, 1080 × 1920 | `screens\8.5.mp4` |
| 8.9 to 8.10 | "Ghost" layer: the 8.4 windows, the 8.5 balance and the faces from stills 5.3 to 5.6, drifting softly. The editor lays it over the street scene at 20–30% visibility (6 seconds) | Wide | `screens\overlays\8.9_ghost_layer.mp4` |
| 9.2 | Floating Bangla phrases: টাকা যায়নি / মানুষ হাসবে / এত ঝামেলা / অভিযোগ করে কী হবে? as **four separate transparent pictures** | Transparent background | `screens\overlays\9.2_phrase1.png` to `9.2_phrase4.png` |

**Done when:** all files are uploaded and the wallet numbers add up exactly.

### Workstream 4 — Reporting screens and end cards (Person D)
| Shot | What | Length | Save as |
|---|---|---|---|
| 10.1 | Search box: "How to report cybercrime in Bangladesh", typed in | 3 s | `screens\10.1.mp4` |
| 10.2 | Search results: Bangladesh Police Online GD (General Diary) — gd.police.gov.bd, and Police Cyber Support for Women — cybersupport.women@police.gov.bd | 3 s | `screens\10.2.mp4` |
| 10.3 | Files dragged into a folder named EVIDENCE: call-log.png, message-screenshot.png, fake-job-page.png, suspicious-url.txt | 4 s | `screens\10.3.mp4` |
| 10.4 | Simple complaint form: Complaint details / Supporting evidence attached / SUBMIT | 3 s | `screens\10.4.mp4` |
| 10.5 | Cursor clicks SUBMIT, then "REPORT SUBMITTED" (**not** "case solved" and **not** "suspect arrested") | 2 s | `screens\10.5.mp4` |
| 12.1 | Black screen: “আপনার কাছে মাত্র ১,০০০ টাকা।” | 3 s | `screens\12.1.mp4` |
| 12.2 | Black screen: “তার কাছে হাজার মানুষের ১,০০০ টাকা।” | 3 s | `screens\12.2.mp4` |
| 12.3 | যাচাই করুন। প্রমাণ রাখুন। রিপোর্ট করুন। with a small line below: PCSW (Police Cyber Support for Women): cybersupport.women@police.gov.bd | 3 s | `screens\12.3.mp4` |
| 12.4 | Title: মাত্র ১০০০ | 2 s | `screens\12.4.mp4` |

The police screens are a **simplified illustration**, not a copy of the real police website, and use no police logo. **Fact-check** the email address on the official Bangladesh Police website before the final export.

**Done when:** all nine files are uploaded, and the end cards are large and readable for their full time.

### Workstream 5 — Voice casting and recording (Person D runs the sessions; actors as cast)
- **Background.** Part 3 of the master script has 33 spoken lines. The detailed list `D:\Matro1000_Edit\output\tasks\voice_tasks.md` gives every line in Bangla, who says it, how to say it, and the exact time slot it must fit in the rough cut.
- **Cast first.** Decide who voices Iqbal, Mehrin, the colleague and the scammer. The scammer's actor also records all of Ahona's lines (see workstream 6). Scene 9 needs **six different people** for inner voices 1 to 6; friends or family are fine.
- **Record.**
  - Use a quiet room, a phone is fine, and record **3 takes of every line**.
  - Before each take, say its file name out loud.
  - Watch `D:\Matro1000_Edit\output\rough_cut_v2.mp4` while recording so each line fits its slot. **Never speed a line up afterwards.** If a line cannot fit, tell the editor.
- **Save as** `audio\[shot]_[character]_take[number].wav`, for example `audio\3.1_Iqbal_take1.wav`, `audio\9.2_Voice4_take2.wav`.
- **Done when:** all 33 lines × 3 takes (99 files) are uploaded, and a second person has listened to one take of each line.

### Workstream 6 — Turning the scammer's voice into "Ahona" (Person C)
- **Background.**
  - "Ahona" does not exist. The film reveals in Scene 8 that her voice was the scammer's voice run through voice-changing software.
  - So the scammer's actor records Ahona's 9 lines (shots 3.1 to 3.5 and 5.3 to 5.6) in his own voice. Each line is then changed into **one consistent woman's voice**, the same setting every time.
  - The scammer's own line in shot 8.2 is also converted. Shot 8.3 plays that converted take, the same words with the same timing.
- **Do.** Pick one free voice-changer tool and keep its settings fixed. Convert the best take of each of the 9 Ahona lines and of shot 8.2.
- **Save as** `audio\ahona_converted\3.1_Ahona.wav` … `audio\ahona_converted\5.6_Ahona.wav`, plus `audio\ahona_converted\8.3_Ahona_from_8.2.wav`.
- **Done when:** all 10 files sound like the same woman and none has the phone filter (the editor adds that).

### Workstream 7 — Sound effects (Person D)
- **Do.**
  - Collect every sound in `D:\Matro1000_Edit\output\tasks\sfx_music_tasks.md` (section 1) from free sound libraries: birds, the cat's meow, the bell, phone buzzes, message "ting"s, mouse clicks, the laptop "clack", street sounds, card rustles and the rest.
  - The list gives the exact moment for the important ones. The laptop click that silences Mehrin's inner voices is at **00:02:46:13** in the current rough cut.
- **Save as** `sfx\[shot]_[sound].wav`, for example `sfx\9.4_laptop_clack.wav`, and list the sources in `sfx\sources.txt`.
- **Done when:** every row in section 1 of the list has a file.

### Workstream 8 — Music (Person A)
- **Background.** The script never says where the music starts. It only says where music must **stop** or stay out (section 2 of `sfx_music_tasks.md`):
  - **Music cuts dead** on Iqbal's line “এক টাকাও দিবা না।” at the start of shot 7.2.
  - **No villain music** in Scene 8.
  - **No music** at the start of Scene 9.
  - **Everything goes silent** at the laptop click.
  - **Quiet** during the reporting screens.
- **Do.** Choose one or two royalty-free tracks (for example from the YouTube Audio Library): quiet tension for Scenes 4 to 7 and an optional low note for the end cards. Mark where you suggest they start.
- **Save as** `music\[number]_[track name].mp3`, plus `music\sources.txt` with the licence for each track and a suggested start time.
- **Done when:** the editor has the files and the sources list.

### Workstream 9 — Final edit in CapCut (Editor)
Work in this order:
1. **Start from the rough-cut timing.** Use `D:\Matro1000_Edit\output\rough_cut_v2.mp4` as the reference: same shot order, same source seconds, same speed changes. The exact source seconds for every shot are in `D:\Matro1000_Edit\output\build_rough_cut.py` (the list called PIECES).
2. **Replace the grey cards** with the Canva videos from workstreams 1 and 4.
3. **Green screens.** Use CapCut's chroma key to remove the green, then lay each screen picture on top and match its corners to the screen angle (reference frames are in `D:\Matro1000_Edit\output\tasks\green_screen_frames\`). This includes shots 6.4, 7.1, 7.2, 7.4 and 7.5, which show Mehrin's green laptop and are not in the notebook's list.
4. **Text overlays** from workstreams 2 and 3: the board text (wipe VERIFY FIRST away with the duster), the door sign, the batch label, the floating phrases, and the ghost layer at 20–30% visibility.
5. **Logo blurs.** Replace the rough grey rectangles with tracked blurs over the laptop logo in shot 4.2, shot 9.1 (first 2.4 seconds) and shot 9.4 (once the lid lifts).
6. **Voices.**
   - Place the best takes in their slots.
   - Phone-filter every line marked with a phone in `voice_tasks.md`.
   - **No** filter on the converted line in 8.3: it plays from the monitor.
7. **Sound effects and music.** Place them as listed. Cut all music on “এক টাকাও দিবা না।”, and cut **every** sound to silence on the laptop-click frame, with no fade and no echo.
8. **Balance the sound** so every line is clear over the music. Keep the five fades to black.
9. **Check the look of G4** (shots 3.2 and 3.3). Its classroom looks slightly different from the test clip before it; adjust the colour if it is noticeable.
10. **Export.** MP4 video, 1920 × 1080, 25 frames per second, standard H.264 video with AAC sound. Save as `D:\Matro1000_Edit\output\final\Team Name Finale__CyberFrames 2026.mp4`, replacing "Team Name" with the real team name and checking the spacing the upload form asks for.

### Workstream 10 — Final check and submission (the Editor plus one other person who has not seen the film for a day)
Watch the exported file from start to finish once with sound and once without, and tick each item:
- [ ] Length is within the competition's limit. **Check the organizers' email or rules PDF.** The master script says the official range is 3:00 to 3:30, and we are currently at 3:18 before sound.
- [ ] No team names, university or college names or logos, and no real brand logos (including the laptop logo in shots 4.2, 9.1 and 9.4).
- [ ] The small four-pointed sparkle mark in the bottom-right corner of the Google Vids clips was left in. **Agree as a team** whether the rules allow it.
- [ ] The scammer's face is never visible.
- [ ] No real phone numbers. The wallet is clearly fictional and its numbers add up.
- [ ] Mehrin never presses PAY NOW and no payment is shown.
- [ ] The police contact details are correct (checked on the official website).
- [ ] Every Bangla word on screen is spelled correctly.
- [ ] The sound goes completely silent on the laptop click, and the music stops on “এক টাকাও দিবা না।”.
- [ ] The file name is correct.

Then upload through the **Google Form link in the organizers' email**.

---

## 6. Schedule (suggested)

| When | What must be finished | Who |
|---|---|---|
| Friday 30 October, 10:00 PM | Workstreams 1, 2, 3 and 4 (all screens and overlays) uploaded. Workstream 5 casting done and at least Iqbal's and Mehrin's lines recorded | A, B, C, D |
| Saturday 31 October, 12:00 PM | All voice lines recorded (workstream 5), Ahona converted (workstream 6), sound effects (workstream 7) and music (workstream 8) uploaded | C, D, A |
| Saturday 31 October, 10:00 PM | Editor shares a first complete version with sound in the shared folder for everyone to watch | Editor |
| Sunday 1 November, 12:00 PM | Everyone's notes sent to the editor; fixes done; final export | Everyone, Editor |
| Sunday 1 November, by 5:00 PM | Final check (workstream 10) and upload. **Hard deadline 11:59 PM** | Editor + checker |

---

## 7. Open questions for the team
1. **Length.** Confirm the allowed length in the organizers' rules before the film grows past 3:30.
2. **Google Vids sparkle mark.** Keep or not, depending on the rules about marks on artificial-intelligence-generated video.
3. **Shot 3.6.** The footage never shows the phone screen. Agree: a pop-up phone graphic (current plan), or a quick cut to a phone close-up?
4. **Shot 6.3.** "Baba Calling" must be tracked onto a black phone screen by hand. If that looks bad, the editor may cut to the 6.3 picture full-screen instead.
5. **G4 classroom.** It looks slightly different from the test clip. Is it acceptable, or should Person A regenerate it closer to the test clip's framing?

If anything in this plan is unclear, ask the editor before guessing. A wrong file name or a wrong time costs more time than a question.
