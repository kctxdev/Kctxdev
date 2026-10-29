#!/usr/bin/env python3
"""Gera assets/stats.svg e assets/activity.svg a partir da API do GitHub.
Sem dependências (só stdlib). Uso: GITHUB_TOKEN=... GH_USER=kctxdev python scripts/gen_stats.py
Sem token, gera placeholders ("sync pendente"). Com --mock, gera dados falsos para testar o visual."""
import os, sys, json, random, datetime, urllib.request
from pathlib import Path

USER = os.environ.get("GH_USER", "kctxdev")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = Path(__file__).resolve().parent.parent / "assets"
G, C, R, A, P = "#00FF41", "#00E5FF", "#FF3366", "#FFC857", "#B388FF"
PANE, TXT, DIM = "#070D0B", "#CFFFE0", "#5E8A6E"
FONT = "'JetBrains Mono','Fira Code','Courier New',monospace"
esc = lambda s: str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

QUERY = """query($login:String!){ user(login:$login){
 followers{totalCount}
 repositories(first:100, ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC){ totalCount nodes{ stargazerCount forkCount
   languages(first:6, orderBy:{field:SIZE,direction:DESC}){ edges{ size node{ name } } } } }
 contributionsCollection{ totalCommitContributions totalPullRequestContributions totalIssueContributions
   contributionCalendar{ totalContributions weeks{ contributionDays{ contributionCount date weekday } } } } } }"""

def fetch():
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json", "User-Agent": "kctxdev-stats"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    if "errors" in d: raise SystemExit(f"GraphQL: {d['errors']}")
    u = d["data"]["user"]
    langs = {}
    stars = forks = 0
    for n in u["repositories"]["nodes"]:
        stars += n["stargazerCount"]; forks += n["forkCount"]
        for e in n["languages"]["edges"]:
            langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
    cc = u["contributionsCollection"]
    weeks = [[(day["date"], day["contributionCount"], day["weekday"]) for day in w["contributionDays"]]
             for w in cc["contributionCalendar"]["weeks"]]
    return dict(repos=u["repositories"]["totalCount"], stars=stars, forks=forks, followers=u["followers"]["totalCount"],
                commits=cc["totalCommitContributions"], prs=cc["totalPullRequestContributions"], issues=cc["totalIssueContributions"],
                total=cc["contributionCalendar"]["totalContributions"], langs=langs, weeks=weeks)

def mock():
    random.seed(3)
    start = datetime.date.today() - datetime.timedelta(days=370)
    start -= datetime.timedelta(days=(start.weekday() + 1) % 7)
    weeks = []
    d = start
    for _ in range(53):
        w = []
        for wd in range(7):
            w.append((d.isoformat(), random.choice([0, 0, 0, 1, 2, 3, 5, 8, 12]), wd)); d += datetime.timedelta(days=1)
        weeks.append(w)
    return dict(repos=12, stars=7, forks=2, followers=9, commits=412, prs=18, issues=6,
                total=sum(c for w in weeks for _, c, _ in w), langs={"Python": 52000, "HCL": 31000, "Java": 14000, "Shell": 6000, "HTML": 3000}, weeks=weeks)

def placeholder():
    weeks = [[("", 0, wd) for wd in range(7)] for _ in range(53)]
    return dict(repos="--", stars="--", forks="--", followers="--", commits="--", prs="--", issues="--", total="--", langs={}, weeks=weeks, pending=True)

BASE = ("text{font-family:" + FONT + "}@media (prefers-reduced-motion:reduce){*{animation:none!important}}")

def pane(x, y, w, h, title):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{PANE}" stroke="{G}" stroke-opacity=".55" stroke-width="2"/>'
            f'<circle cx="{x+18}" cy="{y+17}" r="3.5" fill="{G}"/><text x="{x+30}" y="{y+21}" font-size="12" fill="{TXT}">{esc(title)}</text>'
            f'<line x1="{x+10}" y1="{y+30}" x2="{x+w-10}" y2="{y+30}" stroke="{G}" stroke-opacity=".2"/>')

def stats_svg(s):
    W, H = 1000, 250
    o = [pane(0, 0, 490, H, f"git shortlog — {USER}"), pane(510, 0, 490, H, "languages — por bytes")]
    rows = [("repos públicos", s["repos"], G), ("stars recebidas", s["stars"], A), ("forks", s["forks"], C),
            ("commits (12 meses)", s["commits"], G), ("pull requests", s["prs"], P), ("issues", s["issues"], R), ("seguidores", s["followers"], C)]
    for i, (k, v, c) in enumerate(rows):
        y = 64 + i * 25
        o.append(f'<text x="24" y="{y}" font-size="14" fill="{TXT}">{esc(k)}</text>')
        o.append(f'<text x="466" y="{y}" font-size="14" font-weight="700" fill="{c}" text-anchor="end">{esc(v)}</text>')
        x1 = 24 + len(k) * 8.6 + 8; x2 = 466 - len(str(v)) * 8.6 - 8
        o.append(f'<line x1="{x1:.0f}" y1="{y-4}" x2="{x2:.0f}" y2="{y-4}" stroke="{G}" stroke-opacity=".3" stroke-dasharray="2 4"/>')
    langs = sorted(s["langs"].items(), key=lambda kv: -kv[1])[:6]
    tot = sum(v for _, v in langs) or 1
    cols = [G, C, P, A, R, "#7CFFB2"]
    if not langs:
        o.append(f'<text x="534" y="110" font-size="13" fill="{DIM}">// sync pendente</text><text x="534" y="132" font-size="12" fill="{DIM}">rode o workflow "Atualizar stats" na aba Actions</text>')
    for i, (n, v) in enumerate(langs):
        y = 56 + i * 30; pct = v / tot; fw = 250 * pct
        o.append(f'<text x="534" y="{y+11}" font-size="13" fill="{TXT}">{esc(n)}</text>')
        o.append(f'<rect x="640" y="{y}" width="250" height="14" rx="3" fill="#0d1a14" stroke="{G}" stroke-opacity=".25"/>')
        o.append(f'<rect x="640" y="{y}" width="0" height="14" rx="3" fill="{cols[i]}"><animate attributeName="width" values="0;{fw:.0f};{fw:.0f};0" keyTimes="0;.12;.92;1" dur="14s" repeatCount="indefinite"/></rect>')
        o.append(f'<rect x="640" y="{y}" width="250" height="14" rx="3" fill="url(#seg)"/>')
        o.append(f'<text x="966" y="{y+11}" font-size="12" fill="{cols[i]}" text-anchor="end">{pct*100:.1f}%</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Estatísticas e linguagens do GitHub">'
            f'<defs><pattern id="seg" width="7" height="14" patternUnits="userSpaceOnUse"><rect x="5" width="2" height="14" fill="{PANE}"/></pattern></defs>'
            f'<style>{BASE}</style>{"".join(o)}</svg>')

def streaks(days):
    best = run = 0
    for c in days:
        run = run + 1 if c > 0 else 0
        best = max(best, run)
    d = list(days)
    if d and d[-1] == 0:  # hoje ainda sem commit não quebra a sequência
        d = d[:-1]
    cur = 0
    for c in reversed(d):
        if c > 0: cur += 1
        else: break
    return best, cur

def activity_svg(s):
    W, H = 1000, 236
    weeks = s["weeks"]; cell, step = 14, 18
    x0 = (W - len(weeks) * step + 4) / 2; y0 = 62
    mx = max([c for w in weeks for _, c, _ in w] + [1])
    def lvl(c):
        if c == 0: return 0
        r = c / mx
        return 1 if r <= .25 else 2 if r <= .5 else 3 if r <= .75 else 4
    fills = ["#0d1a14", "#0a4a20", "#008f2d", "#00c83a", G]
    o = [pane(0, 0, W, H, "contribution matrix — últimos 12 meses")]
    months = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]; last = -1
    for i, w in enumerate(weeks):
        if w and w[0][0]:
            m = int(w[0][0][5:7]) - 1
            if m != last: o.append(f'<text x="{x0+i*step:.0f}" y="{y0-8}" font-size="10" fill="{DIM}">{months[m]}</text>'); last = m
        for d, c, wd in w:
            l = lvl(c); x = x0 + i * step; y = y0 + wd * step
            extra = f' stroke="{G}" stroke-opacity=".9" stroke-width="1"' if l == 4 else ""
            o.append(f'<rect x="{x:.0f}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{fills[l]}"{extra}><title>{esc(d)}: {c}</title></rect>')
    gw = len(weeks) * step
    o.append(f'<g style="animation:scan 7s linear infinite"><rect x="{x0-30:.0f}" y="{y0-4}" width="36" height="{7*step+4}" fill="url(#sg)"/><rect x="{x0+4:.0f}" y="{y0-4}" width="2" height="{7*step+4}" fill="{G}" opacity=".9"/></g>')
    days = [c for w in weeks for _, c, _ in w]
    best, cur = streaks(days)
    tot = s["total"]
    foot = (f"{tot} contribuições · maior sequência: {best} dias · sequência atual: {cur} dias" if not s.get("pending") else "// sync pendente — rode o workflow \"Atualizar stats\"")
    o.append(f'<text x="24" y="{H-16}" font-size="12" fill="{G}">{esc(foot)}</text>')
    lx = W - 24 - 5 * 18 - 70
    o.append(f'<text x="{lx}" y="{H-16}" font-size="10" fill="{DIM}">menos</text>')
    for i, f in enumerate(fills): o.append(f'<rect x="{lx+40+i*18}" y="{H-26}" width="12" height="12" rx="3" fill="{f}"/>')
    o.append(f'<text x="{lx+40+5*18+4}" y="{H-16}" font-size="10" fill="{DIM}">mais</text>')
    css = BASE + f"@keyframes scan{{from{{transform:translateX(0)}}to{{transform:translateX({gw}px)}}}}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Matriz de contribuições do GitHub">'
            f'<defs><linearGradient id="sg" x1="0" x2="1"><stop offset="0" stop-color="{G}" stop-opacity="0"/><stop offset="1" stop-color="{G}" stop-opacity=".35"/></linearGradient></defs>'
            f'<style>{css}</style>{"".join(o)}</svg>')

if __name__ == "__main__":
    data = mock() if "--mock" in sys.argv else (fetch() if TOKEN else placeholder())
    OUT.mkdir(exist_ok=True)
    (OUT / "stats.svg").write_text(stats_svg(data), encoding="utf-8")
    (OUT / "activity.svg").write_text(activity_svg(data), encoding="utf-8")
    print("ok:", "mock" if "--mock" in sys.argv else ("api" if TOKEN else "placeholder"))
