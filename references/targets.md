# Where to post (targets) and cadence

Pick by **project type**, not by biggest subreddit. The "home" sub is where the topic is
central; that's where the post belongs. Numbers are real subscriber counts, checked.

## Home by project type

| Project type | Home sub | Secondary | Format | Notes |
|---|---|---|---|---|
| Visual filter / pixel-art tool (game-inspired) | r/milkinsideabagofmilk (24k) | r/androidapps (580k) for the app, r/retrogaming (520k) | video/GIF first | Home sub has rule **"No AI content"**. r/PixelArt bans self-promo, avoid it. |
| eBay / auction tooling | r/Ebay (290k) or r/eBaySellers (46k) | r/footballcards, r/pokemoncardcollectors, r/baseballcards, r/gamecollecting | text + GitHub/PyPI link | Ask where the user actually collects; that sub is best. |
| Music library / YouTube Music tooling | r/YoutubeMusic (149k) | r/Python (1.5M), r/coolgithubprojects (127k), r/SideProject (871k) | text + link + screenshot | If the README is not in English, translate before global subs. |
| Graphics / OpenGL / rendering | r/opengl (41k), r/graphicsprogramming (97k) | r/C_Programming (241k), r/coolgithubprojects | video/GIF of the render | The demo video is essential. |
| Game (engine-specific) | r/godot (379k) if Godot | r/coolgithubprojects, r/SideProject | gameplay video | |
| Dev library / CLI (general) | r/Python (1.5M, self-post) or the language sub | r/coolgithubprojects, r/opensource (389k), r/SideProject | text + link | r/programming (6.9M) has strict rules; read them first. |
| Vibe-coded anything | r/vibecoding | (the topic sub) | text with process/tools | **Only sub where AI may be mentioned.** Dev tools need prior mod approval. |

## Rules to check every time
Run `python3 scripts/reddit.py subinfo <sub>` before posting and read the rule names.
Common blockers: "No Self-Promotion", "No AI content", link-only vs self-only, mandatory flair.

Known specifics:
- r/milkinsideabagofmilk: **No AI content**. Post must relate to the game.
- r/PixelArt: **No Self-Promotion**.
- r/vibecoding: no shilling (must include process), dev tools need approval, no low-effort.
- r/Python: self-post only.
- r/coolgithubprojects: link posts ok.

## Cadence
- 9:1: the user participates genuinely ~9 times in a sub before promoting there.
- One promo per sub; do not repeat the same text across subs.
- Never two promos the same day.
- Suggested order for the user's current repos:
  1. Milk Filter (home sub) -> 2. gixenpy (r/Ebay + a collector sub) ->
  3. YTMSplitter (r/YoutubeMusic) -> 4. SolarSystemOGL (r/opengl) -> 5. go/Godot (r/godot).

## Do not promote
Forks and university/homework repos (they are not the user's own work). Only promote repos the
user actually built and would stand behind.
