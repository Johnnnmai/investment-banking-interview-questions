#!/usr/bin/env python3
"""Generate /questions/ SEO pages (Jekyll), the questions index, sitemap.xml and robots.txt.

Run from the repo root:  python3 _tools/build_question_pages.py
The call-to-action lives in one place: `qpage_cta` in _config.yml, rendered by _includes/qpage-cta.html.
(_tools/ is ignored by Jekyll because it starts with an underscore.)
"""
import html, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from question_pages_data import PAGES
AC_URL = "https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib"
# Every page has a rubric in the self-check (AIE repo tools/answer_check_data.py IB keys), so each links with its own q.
SELFCHECK = '<p class=selfcheck><b>Practiced one out loud?</b> <a href="{url}">Paste your answer into the free self-check and get a score in 30 seconds</a></p>'
LVL = {"Easy": "E", "Medium": "M", "Hard": "S", "Fit": "F"}
ARROW = '<span class=dot aria-hidden=true>&rarr;</span>'
e = html.escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://johnnnmai.github.io/investment-banking-interview-questions"
LASTMOD = "2026-11-01"
BY_SLUG = {p["slug"]: p for p in PAGES}


def y(v):  # JSON strings are valid YAML scalars
    return json.dumps(v, ensure_ascii=True)


def front(d):
    return "---\n" + "".join(f"{k}: {y(v)}\n" for k, v in d.items()) + "---\n\n"


def page(p):
    faq = [{"@type": "Question", "name": p["q"], "acceptedAnswer": {"@type": "Answer", "text": " ".join(p["sample"])}}]
    faq += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["followups"]]
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq}, ensure_ascii=True).replace("</", "<\\/")
    fm = {"layout": "question", "title": p["q"], "description": p["desc"], "permalink": f"/questions/{p['slug']}/",
          "slug": p["slug"], "level": p["level"], "faq_jsonld": ld}
    ac = e(f"{AC_URL}&q={p['slug']}")
    o = [front(fm)]
    # Raw HTML body (kramdown passes block HTML through); layout adds nav, sticky bar and footer.
    o.append(f'<header class=qhero data-hero><div class=wrap><div class="crumb label"><a href="../../">Investment Banking Interview Questions</a> / <a href="../">Questions</a></div>'
             f'<span class="lvl {LVL[p["level"]]}">{p["level"]}</span><h1>{e(p["q"])}</h1>'
             '<p class=lead>How to answer it in an investment banking interview: what is being tested, a step-by-step framework, a sample answer and the mistakes to avoid.</p>'
             f'{{% include hero-buy.html campaign="{p["slug"]}" ghost_href="{ac}" ghost_text="Score my answer free" %}}</div></header>\n\n')
    o.append('<main id=main class=body><div class=read>\n')
    o.append(SELFCHECK.format(url=ac) + "\n")
    o.append(f'<h2>What the interviewer is testing</h2><p>{e(p["testing"])}</p>\n')
    o.append('<h2>Answer framework</h2><ol class=steps>' + "".join(f"<li>{e(s)}</li>" for s in p["steps"]) + "</ol>\n")
    o.append('<h2>Sample answer</h2><div class=sample>' + "".join(f"<p class=ans>{e(s)}</p>" for s in p["sample"]) + "</div>\n")
    if p["followups"]:
        o.append('<h2>Likely follow-ups</h2>' + "".join(f'<div class=fu><b>{e(q)}</b> {e(a)}</div>' for q, a in p["followups"]) + "\n")
    o.append('<h2>Common mistakes</h2><ul class=mist>' + "".join(f"<li>{e(m)}</li>" for m in p["mistakes"]) + "</ul>\n")
    o.append("{% include qpage-cta.html %}\n")
    o.append('<h2>Related questions</h2><ul class=related>' +
             "".join(f'<li><a href="../{r}/">{e(BY_SLUG[r]["q"])}</a></li>' for r in p["related"]) +
             '<li><a href="../">All question deep dives</a></li><li><a href="../../">All 100 investment banking interview questions with answers</a></li></ul>\n')
    if p["src"]:
        o.append("<p class=muted>Based on question" + ("s " if len(p["src"]) > 1 else " ") + ", ".join(f"#{n}" for n in p["src"]) + ' in the <a href="../../">full question bank</a>.</p>\n')
    else:
        o.append('<p class=muted>Based on the fit questions section of the <a href="../../">full question bank</a>.</p>\n')
    o.append("</div></main>\n")
    return "".join(o)


def index():
    title = "Investment Banking Interview Questions: Answer Frameworks and Sample Answers"
    fm = {"layout": "question", "title": title,
          "description": "Deep dives on the most-asked IB interview questions: DCF, three statements, EV vs equity value, WACC, LBO, merger model and why investment banking.",
          "permalink": "/questions/", "slug": "questions-index"}
    cnt = {k: sum(1 for p in PAGES if p["level"] == k) for k in LVL}
    o = [front(fm)]
    o.append(f'<header class="qhero idx" data-hero><div class=wrap><div class="crumb label"><a href="../">Investment Banking Interview Questions</a> / Questions</div>'
             f'<span class=bignum aria-hidden=true>{len(PAGES)}<em>deep dives</em></span><h1>{e(title)}</h1>'
             '<p class=lead>One page per question: what the interviewer is testing, an answer framework, a sample answer, follow-ups and common mistakes.</p>'
             f'{{% include hero-buy.html campaign="questions-index" ghost_href="{e(AC_URL)}" ghost_text="Score my answer free" %}}'
             '<div class=chips>' + "".join(f'<span class="lvl {LVL[k]}">{cnt[k]} {k}</span>' for k in LVL if cnt[k]) +
             '<span class=chip>Sample answer on every page</span></div></div></header>\n\n')
    o.append('<main id=main class=body><div class=read>\n' + SELFCHECK.format(url=e(AC_URL)) + "\n<ol class=qlist>\n")
    for i, p in enumerate(PAGES, 1):
        o.append(f'<li><a class=qcard href="{p["slug"]}/"><span class=n>{i:02d}</span><span class="lvl {LVL[p["level"]]}">{p["level"]}</span>'
                 f'<b>{e(p["q"])}</b><span class=d>{e(p["desc"])}</span></a></li>\n')
        if i == 3:
            o.append('{% include preview-card.html campaign="questions-index" %}\n')
    o.append("</ol>\n")
    o.append(f'<p><b>Practice tool:</b> <a href="{e(AC_URL)}">Check your interview answer with the free Answer Self-Check</a> (score, missed concepts and tips).</p>\n')
    o.append('<p><a href="../">See all 100 investment banking interview questions with answers</a></p>\n')
    o.append('{% include qpage-cta.html %}\n</div></main>\n')
    return "".join(o)


def main():
    os.makedirs(os.path.join(ROOT, "questions"), exist_ok=True)
    for p in PAGES:
        open(os.path.join(ROOT, "questions", p["slug"] + ".md"), "w").write(page(p))
    open(os.path.join(ROOT, "questions", "index.md"), "w").write(index())
    urls = [f"{SITE}/", f"{SITE}/questions/"] + [f"{SITE}/questions/{p['slug']}/" for p in PAGES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{u}</loc><lastmod>{LASTMOD}</lastmod></url>" for u in urls] + ["</urlset>"]
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    rb = os.path.join(ROOT, "robots.txt")
    r = open(rb).read() if os.path.exists(rb) else "User-agent: *\nAllow: /\n"
    line = f"Sitemap: {SITE}/sitemap.xml"
    if line not in r:
        r = r.rstrip("\n") + "\n" + line + "\n"
    open(rb, "w").write(r)
    print(f"built {len(PAGES)} pages + index, sitemap with {len(urls)} urls")


if __name__ == "__main__":
    main()
