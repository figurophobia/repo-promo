# Borradores de ejemplo (mensajes de prueba)

> Nada de esto se ha publicado. Tono natural, sin guiones largos de IA.
> Regla clave: **solo en r/vibecoding se menciona el uso de IA.** En el resto, nunca.

---

## Tells de IA que hay que evitar (esto delata)
- Guion largo `—` a mitad de frase o para abrir ("Hey —").
- Abrir con "Hey", "So,", "Basically,".
- Negritas por todas partes y listas perfectas con ":" en cada línea.
- "Curious:", "Happy to answer questions.", "Would love to see what you make."
- Frases tipo "no es solo X, es Y", "de A a B", triple adjetivo ("rápido, limpio y simple").
- Emojis decorativos gratuitos (deja solo el ⭐ si quieres).
- Cierre con pregunta demasiado pulida.

Cómo suena natural: frases cortas, contracciones, alguna imperfección, hablar como
le explicarías algo a un colega. Menos adornos, más concreción.

---

## Ejemplo 1. Reescritura de tu promo de gixenpy

**Malo (lo que publicaste, 1 up):**
```
GitHub - figurophobia/gixenpy: Unofficial Python client for Gixen.com (eBay sniping)
```

**Bueno (para r/footballcards, r/pokemoncardcollectors, r/Ebay...):**

**Título:**
```
I got tired of sniping eBay auctions by hand so I made a Python client for Gixen
```

**Cuerpo:**
```
Like a lot of you I use Gixen to snipe eBay auctions, but I wanted it hooked into a search
tool I'm building and their API isn't public anymore. So I wrote gixenpy. It logs into your
Gixen account and submits the same web forms the site itself uses. Instead of hardcoding
the field names it reads the real HTML form, so when they change their markup it usually
keeps working.

What it does:
- add / edit / remove: schedule, change or cancel a snipe
- list: your active and finished snipes with their status
- groups and offset: Gixen bid groups and the offset-before-close option
- purge: clear finished snipes
- works as a normal library too (GixenClient), not only a CLI

pip install gixenpy
Source: https://github.com/figurophobia/gixenpy

It's unofficial, nothing to do with Gixen. It's early so bug reports and PRs are welcome.
If you already snipe, what would you want it to do?
```

---

## Ejemplo 2. Post para r/vibecoding (aquí SÍ se habla de IA)

Ahí es obligatorio contar tools y proceso, si no te lo borran.

**Título:**
```
I let Claude Code drive a site's login and form flow because its API was dead. Here's the loop.
```

**Cuerpo:**
```
I'm building a small auction tool and needed to talk to a site whose public API got killed.
Instead of digging for a private JSON endpoint I let the agent drive the actual web forms,
which turned out to be way more durable.

Tools: Claude Code (Opus) for everything, Playwright to poke the flow, Python for the wrapper.

The loop that worked:
1. Record one manual run in DevTools and export the HAR.
2. Hand the HAR to the agent and ask it to explain the flow step by step.
3. Have it write a client that reuses the page's own form fields instead of hardcoded names.
4. One failing test per step, let it iterate until green.

What actually broke:
- Auth was the hard part, not parsing. Cookies plus a CSRF token pulled from the form.
- The agent kept hardcoding field names until I told it, explicitly, to query the DOM.
- The "resilient to markup changes" abstraction paid off, it's survived two redesigns.

Repo is in the first comment. How do you deal with a site that has no API, do you scrape,
drive the UI, or proxy the mobile app?
```

---

## Ejemplo 3. Update en una comunidad que ya te conoce (tu mejor patrón)

**Título:**
```
Milk Filter Mobile now has GIF export and a new film grain look
```

**Cuerpo:**
```
Some of you might remember the Milk Filter app I posted a while back. Quick update since a
few people asked for it.

What's new:
- GIF export, pick a video and get a looping GIF straight from your gallery
- a new film grain preset on top of the Pixel Art filter
- faster processing, a 10s clip renders in a couple of seconds on my phone

The Milk Filter itself is still a port of the one u/DarkShadowYT21 made, none of it is my
idea, I just made it run native.

Download APK: <link releases>
Source: <link github> (star if you like it)

If you make something with the new grain, drop a clip in the comments.
```

---

## Ejemplo 4. Plantilla para un repo futuro

**Títulos posibles (elige uno):**
```
I built <cosa> because <dolor concreto>
I spent <tiempo> making <tool> so you don't have to <tarea>
<tool> does <X> in <Y>
```

**Cuerpo:**
```
<Una línea de contexto: qué hacías antes y por qué te molestaba.>

<Qué construiste y el detalle honesto que da credibilidad: cuánto tardó, qué te costó,
qué todavía no funciona.>

What it does:
- <feature 1>
- <feature 2>
- <feature 3>

Try it: <link demo>
Source: <link github> (MIT)

<Cierre: una pregunta normal, o simplemente invitarlos a probarlo.>
```

---

## Recordatorios
- Solo en r/vibecoding se menciona la IA. En cualquier otro sub, ni una palabra.
- Fuera guiones largos y fuera "Hey".
- Publica primero donde se discute el problema, no donde hay más gente.
- 9:1, y no copies el mismo texto tal cual en varios subs.
