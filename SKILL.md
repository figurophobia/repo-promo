---
name: Repo Promo
description: Use when the user finishes a project, repo, or tool and asks to promote it on Reddit (e.g. "ya está terminado", "hazme promo de esto", "promociona mi repo", "sácalo en reddit"). Researches the repo, picks target subreddits, checks their rules, drafts a natural post that does not sound AI-generated, renders a test post in r/test, and publishes to the real subreddit only after approval.
---

# Repo Promo

When the user says they finished something and wants promo, do the whole flow. Do not just
hand back a draft; prepare it, test it, and be ready to publish.

## Hard rules (never break these)

1. **Never mention AI/IA in the post** unless the target subreddit is `r/vibecoding`.
   No "vibe coded", "built with Claude", "AI-assisted", etc. anywhere else.
2. **Natural voice.** No em dash opener (`—`), no "Hey —", no "Hey", no "So,". Avoid the AI
   tells listed in `references/writing-rules.md`.
3. **Check the sub rules before posting** (`subinfo`). If a sub forbids self-promo, AI
   content, or link posts, drop it or adapt.
4. **One promo per subreddit**, and never the same text pasted across subs.
5. Respect the 9:1 rule: the user should have participated in the sub before promoting.

## Workflow

1. **Read the references first:** `references/writing-rules.md` (how to write it) and
   `references/targets.md` (where to post, and cadence).

2. **Get the repo facts.** If the user gives a repo name or URL:
   ```sh
   curl -s https://api.github.com/repos/<owner>/<name> | \
     python3 -c "import json,sys;d=json.load(sys.stdin);print(d['full_name'],d.get('description'),d.get('homepage'),d.get('topics'),d.get('language'),d.get('stargazers_count'))"
   ```
   If unclear which repo, list them:
   ```sh
   curl -s "https://api.github.com/users/<user>/repos?per_page=100&sort=updated"
   ```

3. **Pick targets** from `references/targets.md`. Prefer the project's "home" sub (where the
   topic is central). If more than one is reasonable, ask the user which they want.

4. **Verify each target and read its rules:**
   ```sh
   python3 scripts/reddit.py subinfo <subreddit>
   ```
   Skip or adapt any sub whose rules conflict (self-promo bans, AI bans, link-only, etc.).

5. **Draft the post** (title + body) using `references/writing-rules.md`. Keep the user's
   voice: personal, concrete, credits to others, no hype. Show the draft in chat and iterate.

6. **Render a test post** so the user sees it formatted, in the sandbox sub:
   ```sh
   python3 scripts/reddit.py post --sr test --title "<title>" --text "<body>" --yes
   ```
   Give them the permalink. After they've looked, delete it:
   ```sh
   python3 scripts/reddit.py del <t3_id>
   ```

7. **Publish to the real sub only after the user approves:**
   ```sh
   python3 scripts/reddit.py post --sr <subreddit> --title "<title>" --text "<body>" --yes
   # link post instead of text:
   python3 scripts/reddit.py post --sr <subreddit> --title "<title>" --url <url> --yes
   ```

8. **Report** the permalink and remind the cadence from `references/targets.md` (don't post
   again in that sub too soon; rotate subs).

## Notes

- The posting tool uses the user's existing Firefox session (no Reddit API key needed).
  Profile and UA can be overridden with `REDDIT_FF_PROFILE` / `REDDIT_UA`.
- `post` is dry-run by default; `--yes` actually publishes.
- The human-readable guides live in `guides/` (`promo-guide.md`, `plan.md`); worked
  examples are in `examples/drafts.md`.
- If the user wants a media/demo post (video or gallery), they must upload the media
  themselves; this tool only does text and link posts.
