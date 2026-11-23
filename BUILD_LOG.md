# BUILD_LOG — u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 ("A Day of One-Line Pitches")

- Contest: u-ronigrv-a-day-of-one-line-pitches-12cd9bb3, prize $5 (top three $2/$2/$1)
- Deadline: 00:20 WIB 25 Nov 2026 (17:20 UTC 24 Nov 2026)
- Kit: downloaded from https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/kit
- Kit level: 39 (`node cli/makefun.mjs --version` → 0.1.0, kit level 39, build 3bfc69b8c4d0)
- Gate: /output/entry.txt, UTF-8, 1–240 chars, not only whitespace
- Judge: pairwise, persuasiveness > clarity > truth > warmth/craft, one read, friend who never coded
- Repo (planned): verren044/makefun-u-ronigrv-a-day-of-one-line-pitches-12cd9bb3

## Candidates (12, all ≤ 240 chars)

1. (180) "Tell it your idea in plain words and watch it become a real app you can tap, share, and show off tonight — free to try, no code, no risk, just the idea you've been carrying around."
2. (165) "You don't need to code — just describe the app you've been imagining, and an AI agent on make.fun will build it for you today, free, while you watch it come to life."
3. (174) "That app idea you've been telling everyone about? Describe it in one sentence and an AI agent on make.fun will build a working version for you today — free, no code, no risk."
4. (172) "If you can describe it, you can have it: tell an AI agent on make.fun your app idea in plain English and get a real, working app back today — free to try, no coding needed."
5. (182) "You've had the idea for months — now just say it out loud: an AI agent on make.fun turns your words into a working app today, free, and you don't need to write a single line of code."
6. (170) "Stop dreaming about your app and let an AI agent on make.fun build it: describe it in plain words, get a working app back today, free — no code, no cost, nothing to lose."
7. (168) "Your idea deserves more than a note on your phone — describe it to an AI agent on make.fun and watch it become a real app today, free, built while you have your coffee."
8. (168) "No code, no cost, no waiting months: tell an AI agent on make.fun what you want your app to do, and it builds a working version for you today — your idea, finally real."
9. (183) "The app you've been imagining is one sentence away: describe it to an AI agent on make.fun and it will build it for you, free, today — no coding, no risk, just your idea come to life."
10. (163) "You already have the hard part — the idea. Just describe it in plain words and an AI agent on make.fun will build your first app for free, today, no code required."
11. (166) "Imagine telling a friend your app idea over coffee and having a working app in your hands by tonight — that's what an AI agent on make.fun does, free, no code needed."
12. (163) "That idea in your head could be an app on your phone by tonight: just describe it to an AI agent on make.fun — free, no code, and you stay in charge the whole way."

## Pairwise self-judging (brief: persuade a non-coder friend, one read)

- First cut — sentence-count rule: the brief asks for ONE sentence. #3 opens with a
  question ("...about?") then a second sentence, and #10 is two sentences joined by a
  period. Both are strong but risk reading as two sentences to a strict judge, so both
  are cut despite their hooks.
- #9 vs #5: both concrete (describe → working app today), free, no code. #9 wins on
  warmth/craft: "one sentence away" is a fresh turn that mirrors the contest itself
  (the pitch IS one sentence), and "just your idea come to life" ends warm; #5's
  "you don't need to write a single line of code" is plainer and slightly longer.
- #9 vs #2: #2 is clear but generic ("while you watch it come to life"); #9 names the
  mechanism (describe it → it builds it) and stacks free/today/no-coding/no-risk.
- #9 vs #8: #8's triple opening ("No code, no cost, no waiting months") is punchy but
  slogan-like; #9 sounds more like a person talking to a friend.
- #9 vs #11: #11's coffee image is warm but hypothetical ("Imagine telling..."), while
  #9 speaks directly to the friend's own idea and gives the concrete next step.
- #9 vs #1: #1 is warm ("the idea you've been carrying around") but its payoff is
  vague ("tap, share, show off"); #9 promises a built app, free, today.
- #9 vs #4/#6/#7/#12: #4 is solid but "in plain English" is narrower than needed;
  #6's "Stop dreaming" is mildly scolding; #7's coffee line is cute but the payoff
  ("built while you have your coffee") overpromises on speed; #12's "stay in charge"
  is a weaker closer than "your idea come to life".

## Pick

#9 — "The app you've been imagining is one sentence away: describe it to an AI agent on make.fun and it will build it for you, free, today — no coding, no risk, just your idea come to life." (183 chars)

Rationale: single sentence; speaks directly to the friend's own idea; concrete
action (describe it) → concrete outcome (it builds it, free, today); low-risk
stack (free, no coding, no risk); truthful (no promise beyond a built first
version, free to enter); freshest turn of phrase in the set ("one sentence away").

## Verification

- `python3 main.py` run twice with MAKEFUN_OUTPUT_DIR to a temp dir; outputs
  byte-identical (sha256 compared), 183 chars, valid UTF-8, no trailing newline.
- Files: main.py (stdlib only, deterministic), README.md (readme_template followed,
  badges + bounty link, referral k7cmczfx, no placeholders), LICENSE (MIT, SPDX
  first line), .makefun/owner.json (wallet 5dzkJVQkKc2V2mMuQDsfv8EJwtw3uLDMARNVHkjmByaX).
- NOT done here (per task): bundle, kit check, submit, GitHub repo creation, push.
