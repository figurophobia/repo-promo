# repo-promo

A small toolkit and OpenCode skill to prepare and publish promo posts for your GitHub
projects on Reddit.

It uses the Reddit session already logged in on your Firefox profile, so there is **no need to
register an app or get Reddit API access**. It reads the cookies, talks to the same endpoints
the web client uses, and posts on your behalf.

## What's inside

```
repo-promo/
├── SKILL.md              # OpenCode skill: the full promo workflow
├── references/
│   ├── writing-rules.md  # natural tone, AI tells to avoid, templates
│   └── targets.md        # project type -> subreddit mapping + cadence
├── scripts/
│   └── reddit.py         # the posting tool
├── guides/
│   ├── promo-guide.md    # lessons learned (what worked / what didn't)
│   └── plan.md           # per-project publishing plan
└── examples/
    └── drafts.md         # worked example posts
```

## Requirements

- Linux with Firefox, logged into the Reddit account you want to post from.
- Python 3 (uses only the standard library).
- `sqlite3` available (usually is).

## Use the tool directly

```sh
python3 scripts/reddit.py whoami
python3 scripts/reddit.py subinfo test                 # subscribers + rules of a sub
python3 scripts/reddit.py post --sr test --title "x" --text "y"   # dry-run
python3 scripts/reddit.py post --sr test --title "x" --url https://github.com/... --yes
python3 scripts/reddit.py del t3_xxxxxxx
python3 scripts/reddit.py recent --limit 10
```

`post` is dry-run by default; only `--yes` actually publishes. Override the Firefox profile or
User-Agent with the `REDDIT_FF_PROFILE` / `REDDIT_UA` env vars.

## Install as an OpenCode skill

Copy (or symlink) this folder into your skills directory:

```sh
cp -r repo-promo ~/.config/opencode/skills/repo-promo
# or: ln -s "$PWD/repo-promo" ~/.config/opencode/skills/repo-promo
```

Then just tell your agent you finished something and want promo. The skill handles the rest:
it researches the repo, picks target subreddits, checks their rules, drafts a natural post,
renders a test post in `r/test`, and only publishes to the real subreddit after you approve.

## Rules the skill enforces

- **Never mention AI** in a post, except in `r/vibecoding` (where their rules actually require
  talking about the tools and process used).
- **Natural tone**: no em dash openers, no "Hey —", no AI tells.
- **Check the subreddit rules** before posting and drop any that forbid self-promo or links.
- **One promo per subreddit**, never the same text pasted across subs, and respect the 9:1
  self-promotion ratio.

## Disclaimer

This tool posts using your own Reddit session. Use it responsibly: follow Reddit's content
policy and each subreddit's rules, and don't spam. You are responsible for what gets posted.

## License

MIT
