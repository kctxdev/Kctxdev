#!/usr/bin/env python3
"""Gera assets/stats.svg e assets/activity.svg a partir da API do GitHub.
Sem dependências (só stdlib). Uso: GITHUB_TOKEN=... GH_USER=kctxdev python scripts/gen_stats.py
Funciona com ou sem token (sem token usa a API REST pública + página de contribuições).
Flags: --mock (dados falsos para testar o visual) e --placeholder (painéis vazios)."""
import os, re, sys, json, random, datetime, urllib.request
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

def http(url, data=None, headers=None, text=False):
    h = {"User-Agent": "kctxdev-stats", "Accept": "application/vnd.github+json"}
    h.update(headers or {})
    if TOKEN and "api.github.com" in url: h["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=30) as r:
        b = r.read().decode("utf-8", "replace")
    return b if text else json.loads(b)

def fetch_graphql():
    d = http("https://api.github.com/graphql", data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
             headers={"Content-Type": "application/json"})
    if d.get("errors") or not (d.get("data") or {}).get("user"): raise RuntimeError(f"GraphQL: {d.get('errors') or 'usuário sem dados'}")
    u = d["data"]["user"]
    langs = {}; stars = forks = 0
    for n in u["repositories"]["nodes"]:
        stars += n["stargazerCount"]; forks += n["forkCount"]
        for e in n["languages"]["edges"]:
            langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
    cc = u["contributionsCollection"]
    weeks = [[(x["date"], x["contributionCount"], x["weekday"], None) for x in w["contributionDays"]]
             for w in cc["contributionCalendar"]["weeks"]]
    return dict(repos=u["repositories"]["totalCount"], stars=stars, forks=forks, followers=u["followers"]["totalCount"],
                commits=cc["totalCommitContributions"], prs=cc["totalPullRequestContributions"], issues=cc["totalIssueContributions"],
                total=cc["contributionCalendar"]["totalContributions"], langs=langs, weeks=weeks)

def parse_calendar(h):
    cells = {}
    for m in re.finditer(r'<td\b[^>]*ContributionCalendar-day[^>]*>', h):
        t = m.group(0)
        d = re.search(r'data-date="([^"]+)"', t); i = re.search(r'id="([^"]+)"', t); l = re.search(r'data-level="(\d)"', t)
        if d: cells[i.group(1) if i else d.group(1)] = [d.group(1), int(l.group(1)) if l else 0, None]
    for m in re.finditer(r'<tool-tip[^>]*for="([^"]+)"[^>]*>(.*?)</tool-tip>', h, re.S):
        if m.group(1) in cells:
            n = re.match(r'\s*(\d[\d,.]*)\s+contribution', m.group(2))
            cells[m.group(1)][2] = int(re.sub(r"\D", "", n.group(1))) if n else 0
    if not cells: raise RuntimeError("não encontrei o calendário de contribuições na página")
    days = sorted(((datetime.date.fromisoformat(d), lv, c if c is not None else (1 if lv else 0)) for d, lv, c in cells.values()))
    first = days[0][0] - datetime.timedelta(days=(days[0][0].weekday() + 1) % 7)  # domingo da 1ª semana
    nweeks = (days[-1][0] - first).days // 7 + 1
    weeks = [[] for _ in range(nweeks)]
    for dt, lv, c in days:
        weeks[(dt - first).days // 7].append((dt.isoformat(), c, (dt.weekday() + 1) % 7, lv))
    m = re.search(r'([\d.,]+)\s+contributions?\s+in\s+the\s+last\s+year', h)
    total = int(re.sub(r"\D", "", m.group(1))) if m else sum(c for _, c, _ in [(0, x[2], 0) for x in days])
    return weeks, total

def search_total(q):
    try: return http("https://api.github.com/search/issues?q=" + q)["total_count"]
    except Exception: return "--"

def fetch_rest():
    u = http(f"https://api.github.com/users/{USER}")
    repos = [r for r in http(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]
    langs = {}
    for r in repos[:40]:
        try:
            for k, v in http(r["languages_url"]).items(): langs[k] = langs.get(k, 0) + v
        except Exception as e: print("aviso: linguagens de", r["name"], e, file=sys.stderr)
    weeks, total = parse_calendar(http(f"https://github.com/users/{USER}/contributions", text=True, headers={"Accept": "text/html"}))
    return dict(repos=u["public_repos"], stars=sum(r["stargazers_count"] for r in repos), forks=sum(r["forks_count"] for r in repos),
                followers=u["followers"], commits=total, commit_label="contribuições (12 meses)",
                prs=search_total(f"author:{USER}+type:pr+is:public"), issues=search_total(f"author:{USER}+type:issue+is:public"),
                total=total, langs=langs, weeks=weeks)

def collect():
    if TOKEN:
        try:
            d = fetch_graphql(); print("fonte: graphql"); return d
        except Exception as e:
            print("graphql falhou, usando REST:", e, file=sys.stderr)
    d = fetch_rest(); print("fonte: rest + página de contribuições"); return d

def mock():
    random.seed(3)
    start = datetime.date.today() - datetime.timedelta(days=370)
    start -= datetime.timedelta(days=(start.weekday() + 1) % 7)
    weeks = []; d = start
    for _ in range(53):
        w = []
        for wd in range(7):
            w.append((d.isoformat(), random.choice([0, 0, 0, 1, 2, 3, 5, 8, 12]), wd, None)); d += datetime.timedelta(days=1)
        weeks.append(w)
    return dict(repos=12, stars=7, forks=2, followers=9, commits=412, prs=18, issues=6,
                total=sum(c for w in weeks for _, c, _, _ in w), langs={"Python": 52000, "HCL": 31000, "Java": 14000, "Shell": 6000, "HTML": 3000}, weeks=weeks)

def placeholder():
    weeks = [[("", 0, wd, None) for wd in range(7)] for _ in range(53)]
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
            (s.get("commit_label","commits (12 meses)"), s["commits"], G), ("pull requests", s["prs"], P), ("issues", s["issues"], R), ("seguidores", s["followers"], C)]
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
    mx = max([c for w in weeks for _, c, _, _ in w] + [1])
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
        for d, c, wd, lv in w:
            l = lv if lv is not None else lvl(c); x = x0 + i * step; y = y0 + wd * step
            extra = f' stroke="{G}" stroke-opacity=".9" stroke-width="1"' if l == 4 else ""
            o.append(f'<rect x="{x:.0f}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{fills[l]}"{extra}><title>{esc(d)}: {c}</title></rect>')
    gw = len(weeks) * step
    o.append(f'<g style="animation:scan 7s linear infinite"><rect x="{x0-30:.0f}" y="{y0-4}" width="36" height="{7*step+4}" fill="url(#sg)"/><rect x="{x0+4:.0f}" y="{y0-4}" width="2" height="{7*step+4}" fill="{G}" opacity=".9"/></g>')
    days = [c for w in weeks for _, c, _, _ in w]
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
    try:
        data = mock() if "--mock" in sys.argv else placeholder() if "--placeholder" in sys.argv else collect()
    except Exception as e:
        sys.exit(f"ERRO ao coletar dados do GitHub: {e}")
    OUT.mkdir(exist_ok=True)
    (OUT / "stats.svg").write_text(stats_svg(data), encoding="utf-8")
    (OUT / "activity.svg").write_text(activity_svg(data), encoding="utf-8")
    print("ok")
