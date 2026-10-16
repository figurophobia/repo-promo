#!/usr/bin/env python3
"""
reddit.py — publica en Reddit usando la sesión ya iniciada en tu Firefox.

No necesita registrar una app ni pedir acceso a la API oficial: reutiliza las
cookies (reddit_session + token_v2) del perfil de Firefox indicado.

Uso:
  python3 reddit.py whoami
  python3 reddit.py subinfo test
  python3 reddit.py post --sr test --title "Hola" --text "cuerpo"        # dry-run
  python3 reddit.py post --sr test --title "Hola" --url https://... --yes
  python3 reddit.py del t3_xxxxx
  python3 reddit.py recent --sr test --limit 5
"""
import argparse, glob, json, os, shutil, sqlite3, sys, urllib.error, urllib.parse, urllib.request

PROFILE = os.environ.get(
    "REDDIT_FF_PROFILE",
    os.path.expanduser("~/.mozilla/firefox/3tkpr7gf.default-release"),
)
JAR = "/tmp/opencode/reddit/cookies.sqlite"
UA = os.environ.get(
    "REDDIT_UA",
    "Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
)
BASE = "https://www.reddit.com"
OAUTH = "https://oauth.reddit.com"


def load_cookies():
    src = os.path.join(PROFILE, "cookies.sqlite")
    if not os.path.exists(src):
        sys.exit(f"No encuentro {src} (¿perfil de Firefox correcto?)")
    os.makedirs(os.path.dirname(JAR), exist_ok=True)
    shutil.copy(src, JAR)
    for ext in ("-wal", "-shm"):
        if os.path.exists(src + ext):
            try:
                shutil.copy(src + ext, JAR + ext)
            except Exception:
                pass
    con = sqlite3.connect(JAR)
    rows = con.execute(
        "SELECT name,value FROM moz_cookies WHERE host LIKE '%reddit.com'"
    ).fetchall()
    con.close()
    return dict(rows)


def call(url, data=None, token=None, cookie=None, referer=None):
    body = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=body)
    req.add_header("User-Agent", UA)
    if token:
        req.add_header("Authorization", "bearer " + token)
    if cookie:
        req.add_header("Cookie", cookie)
    if data:
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
    if referer:
        req.add_header("Referer", referer)
        req.add_header("Origin", BASE)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode("utf-8", "replace")
            try:
                return r.status, json.loads(raw)
            except json.JSONDecodeError:
                return r.status, raw
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, raw
    except Exception as e:
        return -1, str(e)


def session():
    c = load_cookies()
    cookie = "; ".join(f"{k}={v}" for k, v in c.items())
    return c, cookie


def modhash(cookie):
    s, j = call(f"{BASE}/api/me.json", cookie=cookie)
    if isinstance(j, dict) and j.get("data"):
        return j["data"].get("modhash")
    return None


# ---------- comandos ----------
def cmd_whoami(a):
    c, cookie = session()
    s, j = call(f"{OAUTH}/api/v1/me", token=c.get("token_v2"), )
    if s == 200 and isinstance(j, dict):
        print(f"usuario   : {j.get('name')}")
        print(f"karma     : link={j.get('link_karma')} comment={j.get('comment_karma')}")
        print(f"is_mod    : {j.get('is_mod')}")
    else:
        print("error:", s, j)


def cmd_subinfo(a):
    s, j = call(f"{BASE}/r/{a.sr}/about.json", cookie=session()[1])
    if s != 200 or not isinstance(j, dict):
        print("error:", s, str(j)[:200]); return
    d = j["data"]
    print(f"r/{d.get('display_name')}")
    print(f"  suscriptores : {d.get('subscribers')}")
    print(f"  permitir link: {not d.get('user_flair_text') is None} | tipo: {d.get('submission_type')}")
    print(f"  over18       : {d.get('over18')}")
    rj = call(f"{OAUTH}/r/{a.sr}/about/rules", token=session()[0].get("token_v2"))
    if rj[0] == 200 and isinstance(rj[1], dict):
        print("  reglas:")
        for r in rj[1].get("rules", [])[:8]:
            print("   -", r.get("short_name"), "—", (r.get("description") or "")[:70])


def cmd_post(a):
    c, cookie = session()
    uh = modhash(cookie)
    data = {"api_type": "json", "sr": a.sr, "title": a.title, "uh": uh}
    if a.url:
        data["kind"] = "link"; data["url"] = a.url
    else:
        data["kind"] = "self"; data["text"] = a.text or ""
    print(f"[{'LINK' if a.url else 'SELF'}] r/{a.sr} :: {a.title}")
    if not a.yes:
        print("(dry-run) añade --yes para publicar de verdad.")
        return
    s, j = call(f"{BASE}/api/submit", data, cookie=cookie, referer=f"{BASE}/r/{a.sr}/submit")
    if s == 200 and isinstance(j, dict):
        errs = j.get("json", {}).get("errors")
        if errs:
            print("ERROR Reddit:", errs); return
        d = j["json"]["data"]
        print("publicado:", d.get("url") or d.get("name"))
    else:
        print("status:", s, str(j)[:300])


def cmd_del(a):
    c, cookie = session()
    s, j = call(f"{BASE}/api/del", {"id": a.id, "uh": modhash(cookie)}, cookie=cookie, referer=f"{BASE}/")
    print("borrado" if s == 200 else f"status {s}: {j}")


def cmd_recent(a):
    s, j = call(f"{BASE}/user/me/submitted.json?limit={a.limit}&raw_json=1", cookie=session()[1])
    if s != 200 or not isinstance(j, dict):
        print("error:", s, str(j)[:200]); return
    for ch in j["data"]["children"]:
        d = ch["data"]
        print(f"  {d.get('name')}  r/{d.get('subreddit')}  {d.get('title')[:60]}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    sp.add_parser("whoami", help="muestra la cuenta").set_defaults(fn=cmd_whoami)

    si = sp.add_parser("subinfo", help="info y reglas de un subreddit")
    si.add_argument("sr"); si.set_defaults(fn=cmd_subinfo)

    po = sp.add_parser("post", help="crea un post (dry-run por defecto)")
    po.add_argument("--sr", required=True)
    po.add_argument("--title", required=True)
    po.add_argument("--text", default="")
    po.add_argument("--url", default="")
    po.add_argument("--yes", action="store_true")
    po.set_defaults(fn=cmd_post)

    de = sp.add_parser("del", help="borra un post/comentario por fullname (t3_/t1_)")
    de.add_argument("id"); de.set_defaults(fn=cmd_del)

    re_ = sp.add_parser("recent", help="tus últimos posts")
    re_.add_argument("--sr", default=""); re_.add_argument("--limit", type=int, default=10)
    re_.set_defaults(fn=cmd_recent)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
