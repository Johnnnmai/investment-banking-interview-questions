#!/usr/bin/env python3
"""Generate /questions/ SEO pages (Jekyll), the questions index, sitemap.xml and robots.txt.

Run from the repo root:  python3 _tools/build_question_pages.py
The call-to-action lives in one place: `qpage_cta` in _config.yml, rendered by _includes/qpage-cta.html.
(_tools/ is ignored by Jekyll because it starts with an underscore.)
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from question_pages_data import PAGES

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
          "slug": p["slug"], "tagline": f"Investment banking interview question ({p['level']}): how to answer it", "faq_jsonld": ld}
    o = [front(fm)]
    o.append("[100 IB Interview Questions](../../) › [Questions](../) › This question\n\n")
    o.append("{% include qpage-cta.html %}\n\n")
    o.append("## What the interviewer is testing\n\n" + p["testing"] + "\n\n")
    o.append("## Answer framework\n\n" + "".join(f"{i}. {s}\n" for i, s in enumerate(p["steps"], 1)) + "\n")
    o.append("## Sample answer\n\n" + "".join(f"> {s}\n>\n" for s in p["sample"]).rstrip(">\n") + "\n\n")
    if p["followups"]:
        o.append("## Likely follow-ups\n\n" + "".join(f"**{q}** {a}\n\n" for q, a in p["followups"]))
    o.append("## Common mistakes\n\n" + "".join(f"- {m}\n" for m in p["mistakes"]) + "\n")
    o.append("## Related questions\n\n" + "".join(f"- [{BY_SLUG[r]['q']}](../{r}/)\n" for r in p["related"]))
    o.append("- [All question deep dives](../)\n- [All 100 investment banking interview questions with answers](../../)\n\n")
    if p["src"]:
        o.append("_Based on question" + ("s " if len(p["src"]) > 1 else " ") + ", ".join(f"#{n}" for n in p["src"]) + " in the [full question bank](../../)._\n\n")
    else:
        o.append("_Based on the fit questions section of the [full question bank](../../)._\n\n")
    o.append("{% include qpage-cta.html %}\n")
    return "".join(o)


def index():
    fm = {"layout": "question", "title": "Investment Banking Interview Questions: Answer Frameworks and Sample Answers",
          "description": "Deep dives on the most-asked IB interview questions: DCF, three statements, EV vs equity value, WACC, LBO, merger model and why investment banking.",
          "permalink": "/questions/", "slug": "questions-index", "tagline": "One page per question: what is tested, a framework, a sample answer and common mistakes"}
    o = [front(fm), "[100 IB Interview Questions](../) › Questions\n\n"]
    for p in PAGES:
        o.append(f"### [{p['q']}]({p['slug']}/)\n\n_{p['level']}_ · {p['desc']}\n\n")
    o.append("**Practice tool:** [Check your interview answer with the free Answer Self-Check](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib) (score, missed concepts and tips).\n\n")
    o.append("[See all 100 investment banking interview questions with answers](../)\n\n{% include qpage-cta.html %}\n")
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
