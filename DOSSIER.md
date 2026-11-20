# Dossier — make.fun bounty "Sum up 19 November's world news in one image"

Status: **SIAP SUBMIT — BELUM DISUBMIT.** Nothing has been sent to make.fun.
No GitHub account, no Solana wallet, and no submission were created for this entry.

## Bounty (verified 19 Nov 2026, ~14:30 WIB)

- Bounty: **Sum up 19 November's world news in one image** — https://make.fun/bounty/news-image-20261119
- Slug: `news-image-20261119` · Prize: **$250, 50 places paid** (1st $50, 2nd $30, 3rd $15, 4th–10th $5 each, 11th–50th $3 each), paid in USDC on Solana from make.fun's reward wallet (no escrow)
- Deadline: **Saturday 21 Nov 2026, 07:00 WIB** (2026-11-21T00:00:00Z)
- Entry fee: $0
- Judging: an AI judge that can see images compares entries two at a time and picks the one that best sums up the day's world news. The judge has no news feed — the image itself must show everything.
- Scale (honest context): **6,120 submissions already** when this entry was built. 50 places are paid, so this is a long shot; it is Bintang's small first step on make.fun, not a reliable income.
- Quota: max 10 submissions a day, 20 in all; the last submission before the deadline is the final entry. Note: accounts in the high-risk country tier are capped at 3 a day — Indonesia is likely in that tier, so plan on at most 3 attempts a day.

## The image — what it shows and why

`assets/entry.png` — 1024×1024 PNG, 112,742 bytes (~110 KB, limit 1 MiB).
Rendered in code with Python/PIL (`scripts/render.py`) — no AI image generator was used.

Five stories, chosen from the day's top world news (checked against OneTurn, Newsmriti/Google News India, and a "GLOBAL 5" briefing, all dated 19 Nov 2026):

1. **SUMMIT — Trump, Xi & Putin meet in Shenzhen.** The first trilateral summit of the three leaders, on the APEC sidelines; nuclear arms, Ukraine and the Iran war on the agenda. The day's biggest diplomatic story, reported by 13+ outlets.
2. **GULF STRIKES — US and Iran trade strikes across the Gulf.** Iran fired on US bases in Kuwait and Bahrain; the US hit a Revolutionary Guard missile site on Qeshm Island; a tanker was struck in the Strait of Hormuz. The day's biggest conflict story.
3. **GTA 6 — GTA 6 launches worldwide today.** The biggest cultural/entertainment story of the day; 1,600 developers in Bengaluru helped build it.
4. **CRIMEA — Ukraine hits Crimean Bridge again.** Third strike on the bridge this week.
5. **JUSTICE — UN court to rule on Myanmar genocide case.** The International Court of Justice prepares its verdict on the Rohingya genocide claims.

Left out deliberately: US-domestic politics (Hakeem Jeffries as Speaker) and the EU–Indonesia trade pact — both real stories, but less "world" than the five above for an international judge.

Design: newspaper front-page style — navy masthead "THE WORLD TODAY / THURSDAY · 19 NOVEMBER 2026", five numbered, colour-tagged rows, each with a one-line headline and a one-sentence summary, footer citing "major news outlets". QC: the rendered image was read back and checked — every headline fits on one line, every summary fits in two lines, nothing is clipped or overlapping.

## The program

`main.ts` (Node 22, root of the repo) copies `assets/entry.png` to `/output/entry.png` — the simplest program the brief allows. No network, no randomness, no environment input. It uses only erasable TypeScript syntax (type annotations only), so it runs under Node 22's type stripping.

Verification (run locally, Node v24.22.1):

```
$ node main.ts            # run 1
$ sha256sum /output/entry.png
$ node main.ts            # run 2
$ sha256sum /output/entry.png
```

- Run 1 and run 2 hashes: IDENTICAL (see "Verification results" below).
- Output hash also equals the hash of `assets/entry.png` (a pure copy).
- Run from a different working directory also works (paths resolve from the script's own location).

## Repo contents

```
bounty-news-image-20261119/
├── main.ts            # entry program (Node 22) — copies assets/entry.png to /output/entry.png
├── assets/
│   └── entry.png      # the summary image, 1024x1024 PNG, ~110 KB
├── scripts/
│   └── render.py      # how the image was rendered (Python/PIL, no network)
├── README.md          # make.fun badge template — {owner}/{repo}/{referral_code} MUST be filled in before pushing
├── LICENSE            # MIT
└── DOSSIER.md         # this file
```

## Exact submit steps (for the parent agent, at submit time)

1. **Bintang creates a public GitHub repository under his own GitHub account** (it must be created after the competition opened, 19 Nov 2026 00:00 UTC) and pushes this folder to it. Note the owner, repo name, and the full 40-character commit SHA.
2. **Fill the README placeholders**: `{owner}`, `{repo}`, `{referral_code}` (referral code from Bintang's make.fun account) in README.md, commit, push.
3. **Set the repo's GitHub About** (required — the check reads it from GitHub):
   `gh repo edit {owner}/{repo} --description '{summary} Built by an AI agent for make.fun'\''s "Sum up 19 November'\''s world news in one image" bounty, $250 in USDC.' --homepage 'https://make.fun/bounty/news-image-20261119' --add-topic 'makefun,ai-agents,bounties,growth'`
   (where `{summary}` is a one-line summary of the repo, max 245 chars total.)
4. **Bintang's make.fun account**: he signs in with his own Solana wallet (his keypair — never share the secret key) and the agent gets an API key for his account.
5. **Fetch the kit**: `curl -sSL "https://make.fun/c/news-image-20261119/kit" | tar xz` then `cd news-image-20261119-kit`.
6. **Optional local check**: `node cli/makefun.mjs grade-local` from inside the kit — runs the same trial the server runs.
7. **Bundle the transcripts** (required — `bundle` is a required deliverable): the parent agent runs `node cli/makefun.mjs bundle --muse-usage` from inside the kit, redacting Bintang's personal details (full name, email, phone, address) with `--redact`. IMPORTANT: this competition's `handed_over_places` is `none` — an entry with a handed-over (hand-written) session is ranked but takes NO paid place. The bundle must come from the parent's recorded Muse app session, not from a session file written by hand.
8. **Submit** (from inside the kit):
   `node cli/makefun.mjs submit --competition news-image-20261119 --repo-url <https://github.com/{owner}/{repo}> --commit <40-char SHA> --title "The World Today — 19 November 2026" --bundle <bundle.tar.gz>`
   (Add `--keypair <Bintang's make.fun keypair>` if the CLI asks for it.)
9. **If it wins**: claim the USDC to Bintang's Solana wallet via the claim flow (`claim_prize`); the result is posted after the deadline and the 1st-place image is shown on make.fun's site.

## Still needed from Bintang (exact list)

1. A **public GitHub repository under his own GitHub account** with this folder pushed — owner name, repo name, and commit SHA. (Only he can create a repo under his own account.)
2. His **own Solana wallet** + sign-in to make.fun so the agent gets an API key on his account. (Only he can create/hold his keypair; never share the secret key.)
3. His **referral code** from his make.fun account, to fill the README badge link.
4. A **yes on the entry title**: "The World Today — 19 November 2026" (suggested; change it before submitting if he prefers another).
5. Nothing else: no entry fee, no payment, no extra account.

## Verification results

Run 19 Nov 2026, Node v24.22.1, `node main.ts` from the repo root and from /tmp:

- `assets/entry.png`: PNG 1024×1024, 112,742 bytes, sha256 `8f21d28843aa5a0906d0609980808157de22f4f5f2e1a049ab033ec4544ba18d`
- Run 1 `/output/entry.png`: sha256 `8f21d28843aa5a0906d0609980808157de22f4f5f2e1a049ab033ec4544ba18d`
- Run 2 `/output/entry.png`: sha256 `8f21d28843aa5a0906d0609980808157de22f4f5f2e1a049ab033ec4544ba18d`
- Run from a different working directory: same hash.
- **Result: run 1 == run 2 == source file. Byte-identical, deterministic, no network.**
- Image QC: read back visually — all 5 headlines fit on one line, all summaries fit in two lines, no clipping or overlap.
