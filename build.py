"""Regenerate both static language pages using Python 3 standard library."""
import json
from pathlib import Path
from html import escape
ROOT = Path(__file__).resolve().parent
content = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
ids = ['about', 'experience', 'skills', 'project', 'education', 'contact']
def e(value):
    return escape(str(value))
def lines(value):
    return '<br>'.join(e(value).split('\n'))
def heading(number, label, title):
    return f'<div class="section-heading"><p class="eyebrow"><span>{number}</span> {e(label)}</p><h2>{lines(title)}</h2></div>'
for lang, c in content.items():
    other = 'en.html' if lang == 'ar' else 'index.html'
    toggle = 'English' if lang == 'ar' else 'العربية'
    otherlang = 'en' if lang == 'ar' else 'ar'
    nav = ''.join(f'<a href="#{i}">{e(t)}</a>' for i,t in zip(ids,c['nav']))
    duties = ''.join(f'<article class="duty"><span class="item-number" aria-hidden="true">0{n+1}</span><h4>{e(d["title"])}</h4><ul>'+''.join(f'<li>{e(v)}</li>' for v in d['items'])+'</ul></article>' for n,d in enumerate(c['duties']))
    skills = ''.join(f'<article class="skill"><h3>{e(d["title"])}</h3><ul>'+''.join(f'<li>{e(v)}</li>' for v in d['items'])+'</ul></article>' for d in c['skills'])
    courses = ''.join(f'<li><div><h4>{e(t)}</h4><p>{e(p)}</p></div><time datetime="{y}">{y}</time></li>' for t,p,y in c['courses'])
    languages = ''.join(f'<li>{e(v)}</li>' for v in c['languages'])
    name = 'محمود أحمد<br><span>الزناتي.</span>' if lang == 'ar' else 'Mahmoud Ahmed<br><span>El Zanaty.</span>'
    html = f'''<!doctype html>
<html lang="{lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c['name'])} — {e(c['title'])}</title>
<meta name="description" content="{e(c['description'])}">
<meta name="theme-color" content="#161918">
<meta property="og:type" content="website"><meta property="og:title" content="{e(c['name'])} — {e(c['title'])}">
<meta property="og:description" content="{e(c['description'])}"><meta property="og:locale" content="{'ar_SA' if lang == 'ar' else 'en_US'}">
<link rel="alternate" hreflang="ar" href="./index.html"><link rel="alternate" hreflang="en" href="./en.html"><link rel="alternate" hreflang="x-default" href="./index.html">
<link rel="icon" href="./assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="./assets/style.css"><script src="./assets/app.js" defer></script>
</head>
<body id="top">
<a class="skip" href="#main">{e(c['skip'])}</a>
<header class="header"><div class="header-inner">
<a class="brand" href="#top" aria-label="{e(c['name'])}"><span class="brand-mark" aria-hidden="true">MZ<span>.</span></span></a>
<nav class="desktop-nav" aria-label="{e(c['navigation'])}">{nav}</nav>
<div class="header-actions"><a class="language" href="./{other}" lang="{otherlang}" hreflang="{otherlang}" data-language="{otherlang}">{toggle}</a>
<details class="mobile-menu"><summary>{e(c['menu'])}<span aria-hidden="true"> ☰</span></summary><nav aria-label="{e(c['navigation'])}">{nav}</nav></details></div>
</div></header>
<main id="main" tabindex="-1">
<section class="hero container" aria-labelledby="hero-title">
<div class="hero-copy"><p class="eyebrow"><span class="short-rule"></span>{e(c['heroLabel'])}</p><p class="hello">{e(c['hello'])}</p>
<h1 id="hero-title">{name}</h1><p class="role">{e(c['title'])}</p><p class="direction">{e(c['direction'])}</p><p class="hero-summary">{e(c['summary'])}</p>
<div class="actions"><a class="button primary" href="#experience">{e(c['experienceCta'])}<span aria-hidden="true">↙</span></a><a class="button secondary" href="#contact">{e(c['contactCta'])}</a></div>
<p class="location"><span aria-hidden="true">⌖</span> {e(c['location'])}</p></div>
<div class="identity-panel"><div class="panel-top"><span dir="ltr">M / Z</span><span>{e(c['heroLabel'])}</span></div><div class="monogram" aria-hidden="true">M<span>Z</span><i>.</i></div><div class="panel-bottom"><p>{e(c['monogramCaption'])}</p><span>{e(c['monogramSmall'])}</span></div></div>
</section>
<section id="about" class="section container">
{heading('01',c['nav'][0],c['aboutTitle'])}<div class="about-grid"><p class="lead">{e(c['about'])}</p><aside class="focus-panel"><p class="eyebrow">{e(c['focusLabel'])}</p><h3>{e(c['focus'])}</h3><p>{e(c['focusText'])}</p></aside></div>
</section>
<section id="experience" class="section section-tinted"><div class="container">
{heading('02',c['nav'][1],c['experienceTitle'])}<div class="timeline">
<article class="timeline-item"><p class="period">{e(c['currentDate'])}</p><div><h3>{e(c['currentTitle'])}</h3><p class="company">{e(c['currentCompany'])}</p><p>{e(c['currentText'])}</p></div></article>
<article class="timeline-item"><p class="period">{e(c['previousDate'])}</p><div><h3>{e(c['previousTitle'])}</h3><p class="company">{e(c['previousCompany'])}</p><p>{e(c['previousText'])}</p></div></article>
</div><div class="duties-intro"><h3>{e(c['dutiesTitle'])}</h3><p>{e(c['dutiesNote'])}</p></div><div class="duties-grid">{duties}</div></div>
</section>
<section id="skills" class="section container">{heading('03',c['nav'][2],c['skillsTitle'])}<div class="skills-grid">{skills}</div></section>
<section id="project" class="section container">{heading('04',c['nav'][3],c['projectTitle'])}<article class="project-card"><div class="project-index" aria-hidden="true">01<span>2024</span></div><div class="project-copy"><p class="eyebrow">{e(c['projectLabel'])}</p><h3>{lines(c['projectName'])}</h3><p>{e(c['projectText'])}</p><details class="project-details"><summary>{e(c['projectMore'])}</summary><p>{e(c['projectDetail'])}</p></details></div></article></section>
<section id="education" class="section section-tinted"><div class="container">{heading('05',c['nav'][4],c['educationTitle'])}<div class="education-grid"><div><article class="degree"><p class="eyebrow"><bdi>2020–2024</bdi></p><h3>{e(c['degree'])}</h3><p>{e(c['school'])}</p><p class="grade">{e(c['grade'])}</p><p>{e(c['finalGrade'])}</p></article><div class="languages"><h3>{e(c['languagesLabel'])}</h3><ul>{languages}</ul></div></div><div class="courses"><h3>{e(c['coursesLabel'])}</h3><ul>{courses}</ul></div></div></div></section>
<section id="contact" class="section container contact">{heading('06',c['nav'][5],c['contactTitle'])}<p>{e(c['contactText'])}</p><a class="email-link" href="mailto:acc.m.zanaty@gmail.com" aria-label="{e(c['emailLabel'])}: acc.m.zanaty@gmail.com"><bdi>acc.m.zanaty@gmail.com</bdi><span aria-hidden="true">↗</span></a><div class="contact-bottom"><p>{e(c['location'])}</p><button class="button secondary print-button" hidden>{e(c['print'])}<span aria-hidden="true">↓</span></button></div><noscript><p>{e(c['noJs'])}</p></noscript></section>
</main><footer class="container footer"><p>{e(c['footer'])}</p><a href="#top">{e(c['backTop'])} ↑</a></footer>
</body></html>'''
    (ROOT / ('index.html' if lang == 'ar' else 'en.html')).write_text(html, encoding='utf-8')
print('Built index.html and en.html')
