#!/usr/bin/env python3
"""Build static bilingual pages from JSON, using only the Python standard library."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
def E(value): return escape(str(value), quote=True)
def ul(items): return '<ul>' + ''.join('<li>'+E(v)+'</li>' for v in items) + '</ul>'
def img(n, alt=''): return f'<img src="../assets/mascot-{n:02d}.png" alt="{E(alt)}">'
def load(kind, lang): return json.loads((ROOT/'data'/f'{kind}.{lang}.json').read_text(encoding='utf-8'))

def shell(title, body, css, en, kind):
    alternate = f'{kind}.html' if en else f'{kind}.en.html'
    lang = 'en' if en else 'zh-CN'
    toolbar = ('Template home','Chinese','Print / PDF','Fictional example. Replace it with your own records.') if en else ('模板首页','English','打印 / PDF','示例人物与示例规划，请替换成自己的记录。')
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)} · Dopamine Life System</title><meta name="description" content="Colorful life systems and creator account planning templates by A Tian.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/{css}.css"><link rel="stylesheet" href="../assets/extras.css"></head>
<body><a class="skip-link" href="#main">{'Skip to content' if en else '跳到正文'}</a>
<div class="projectbar wrap"><a href="../{'index_en.html' if en else 'index.html'}">← {toolbar[0]}</a><a href="{alternate}">{toolbar[1]}</a><button onclick="window.print()">{toolbar[2]}</button></div>
<div class="wrap"><p class="example-badge">✦ {toolbar[3]}</p></div>{body}
<footer class="wrap">{'Open-source templates by A Tian · Example content · Update with your own evidence.' if en else '阿甜开源模板 · 内容为公开示例 · 请按自己的真实经历更新。'}<br><a href="../{'README_EN.md' if en else 'README.md'}">{'Documentation' if en else '使用说明'}</a></footer></body></html>'''

def life(en):
    lang='en' if en else 'zh-CN'; d=load('life',lang);t=lambda z,e:e if en else z
    nav=''.join(f'<a href="#{E(s["id"])}" style="--c:var(--{E(s["color"])})"><i></i>{E(s["title"])}</a>' for s in d['sections'])
    toc=''.join(f'<a href="#{E(s["id"])}" style="--c:var(--{E(s["color"])}L)"><b>{i+1:02d} · {E(s["title"])}</b><span>{E(s["description"])}</span></a>' for i,s in enumerate(d['sections']))
    identity=''.join(f'<div><b>{E(k)}</b>{E(v)}</div>' for k,v in d['identity'])
    h=f'''<header class="hero"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><div class="wrap"><div class="hero-in"><div><span class="kicker">LIFE SYSTEM · {t('使用说明书','A PERSONAL MANUAL')}</span><h1>{E(d['name'])}{t('的',"’s")}<br><span>{E(d['title'])}</span></h1><div class="motto box">{E(d['motto'])}</div></div><div class="hero-pic"><div class="ring"></div>{img(1,t('阿甜示例插画','Illustration from A Tian'))}</div></div><div class="idcard box">{identity}</div><div class="toc">{toc}</div></div></header><nav class="nav"><div class="wrap">{nav}</div></nav><main class="wrap" id="main">'''
    for i,s in enumerate(d['sections']):
        c=E(s['color']); h+=f'<section id="{E(s["id"])}" class="c-{c}"><div class="ch box"><div><span class="no">{i+1:02d}</span><h2>{E(s["title"])}</h2><p>{E(s["description"])}</p></div>{img(i+2)}</div>'
        if i==0:
            h+=f'<h3 class="sub" style="--c:var(--{c})">{t("我的做事循环","My making loop")}</h3><div class="loop">'+''.join(f'<div class="step"><div class="n">{j+1}</div><h4>{E(v)}</h4><p>{t("把这一小步做完，再开始下一步。","Finish this small step, then move on.")}</p></div>' for j,v in enumerate(d['loop']))+'</div>'
        h+='<div class="g2">'+''.join(f'<article class="card"><span class="lab">{E(card["label"])}</span><h3>{E(card["title"])}</h3><p>{E(card["body"])}</p><p class="so">→ {E(card["action"])}</p></article>' for card in s['cards'])+'</div>'
        if i==0:
            h+=f'<h3 class="sub" style="--c:var(--{c})">{t("我的能量表","My energy map")}</h3><div class="energy"><div class="card plus"><h3>＋ {t("充电","Recharges me")}</h3>{ul(d["energy"]["charge"])}</div><div class="card minus"><h3>－ {t("耗电","Drains me")}</h3>{ul(d["energy"]["drain"])}</div></div>'
        h+='</section>'
    h+=f'<div class="closing box"><h2>{t("人生系统，跟着生活一起更新。","Let your system evolve with your life.")}</h2><p>{t("它是一页持续修订的个人说明书。今天先从一件真实发生的小事开始。","A personal manual you keep revising. Start with one thing that actually happened today.")}</p></div></main>'
    return shell(d['title'],h,'life',en,'life-system')

def accounts(en):
    lang='en' if en else 'zh-CN';d=load('accounts',lang);t=lambda z,e:e if en else z
    nav=[('map',t('总图','Map'))]+[(a['id'],a['name']) for a in d['accounts']]+[('combo',t('联动','Angles')),('week',t('排期','Schedule')),('rules',t('规则','Guidelines'))]
    nav=''.join(f'<a href="#{E(k)}">{E(v)}</a>' for k,v in nav)
    h=f'''<header class="hero"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><div class="wrap"><div class="hero-in"><div><h1>{E(d['name'])}{t('的',"’s")}<br><span class="seven">{len(d['accounts'])}</span> {t('个号','accounts')}</h1><p class="sub">{E(d['subtitle'])}</p><div class="stickers"><span class="stk">{t('一人多面','One creator')}</span><span class="stk">{t('各有分工','Clear roles')}</span><span class="stk">{t('从生活开始','Start with life')}</span></div></div><div class="hero-pic"><div class="ring"></div>{img(11,t('阿甜示例插画','Illustration from A Tian'))}</div></div></div></header><nav class="nav"><div class="wrap">{nav}</div></nav><main class="wrap" id="main">'''
    def heading(no,title,desc=''):return f'<div class="sec-h"><span class="num">{E(no)}</span><h2>{E(title)}</h2><p>{E(desc)}</p></div>'
    h+='<section id="map">'+heading('01',t('四条线，七个号','Four lanes, seven accounts'),t('示例展示如何分工；账号数量可以按精力减少。','An example of clear roles. Reduce the number of accounts to fit your capacity.'))+'<div class="matrix">'
    for i,l in enumerate(d['lanes']):
        ahtml=''.join(f'<a class="acc" href="#{E(a["id"])}"><span class="dot" style="background:var(--{E(a["color"])})"></span>{E(a["name"])}</a>' for a in d['accounts'] if a['lane']==i)
        h+=f'<article class="lane box"><h3>{E(l["name"])}</h3><div class="what">{E(l["description"])}</div>{ahtml}</article>'
    h+='</div></section><section id="accounts">'+heading('02',t('每个号发什么','What each account posts'),t('定位、受众、栏目、制作方式和边界，都放在一张卡片里。','Purpose, audience, series, production and boundaries in a single card.'))
    for i,a in enumerate(d['accounts']):
        facts=[(t('给谁看','Audience'),a['audience']),(t('做什么','Purpose'),a['purpose']),(t('频率','Frequency'),a['frequency']),(t('来源','Source'),t('示例规划，无真实账号数据','Fictional plan; no real account metrics'))]
        facts=''.join(f'<div><b>{E(k)}</b>{E(v)}</div>' for k,v in facts)
        series=''.join(f'<div class="col"><div class="ct"><em>{j+1}</em>{E(s["name"])}</div>{ul(s["examples"])}</div>' for j,s in enumerate(a['series']))
        h+=f'<article id="{E(a["id"])}" class="acct box c-{E(a["color"])}"><div class="acct-top"><div class="acct-pic"><span class="no">{i+1}</span>{img(i+12)}</div><div class="acct-head"><div class="row1"><span class="role">{E(a["role"])}</span><span class="tag">{t("示例账号","Example account")}</span></div><h3>{E(a["name"])}</h3><p class="pitch">{E(a["audience"])}</p><div class="facts">{facts}</div></div></div><div class="cols">{series}</div><div class="howto"><div class="form"><h4>{t("怎么拍","How to make it")}</h4>{ul(a["production"])}</div><div class="dont"><h4>{t("不发什么","What stays out")}</h4>{ul(a["exclude"])}</div></div></article>'
    h+='</section><section id="combo">'+heading('03',t('一件事，讲不同的侧面','One story, different sides'))+f'<div class="combo-head box">{img(19)}<div><h3>{E(d["campaign"])}</h3><p>{t("让每个号都讲自己最适合的一面。","Give every account the angle that fits it.")}</p></div></div><div class="g2 public-grid">'
    for a,angle in zip(d['accounts'],d['angles']):h+=f'<article class="box public-card" style="--c:var(--{E(a["color"])})"><span class="tag">{E(a["name"])}</span><h3>{E(angle)}</h3></article>'
    h+='</div></section><section id="week">'+heading('04',t('一周怎么排','A weekly rhythm'),t('每周七条是演示，不是必须完成的目标。','Seven posts demonstrate the structure; they are not a required target.'))+'<div class="public-scroll box"><table class="public-table"><thead><tr>'
    days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'] if en else ['周一','周二','周三','周四','周五','周六','周日']
    h+=''.join('<th>'+E(day)+'</th>' for day in days)+'</tr></thead><tbody><tr>'+''.join(f'<td><b>{E(a["name"])}</b><br>{E(a["series"][0]["name"])}</td>' for a in d['accounts'])+'</tr></tbody></table></div></section>'
    h+='<section id="rules">'+heading('05',t('让计划保持清楚','Keep the plan clear'))+'<div class="g2 public-grid">'+''.join(f'<article class="box public-card"><span class="tag">{i+1:02d}</span><h3>{E(v)}</h3></article>' for i,v in enumerate(d['rules']))+'</div></section></main>'
    return shell(d['title'],h,'accounts',en,'account-planner')

def landing(en):
    t=lambda z,e:e if en else z
    template_suffix='.en' if en else ''
    alt='index.html' if en else 'index_en.html'
    return f'''<!doctype html><html lang="{'en' if en else 'zh-CN'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t('多巴胺人生系统','Dopamine Life System')}</title><link href="https://fonts.googleapis.com/css2?family=ZCOOL+KuaiLe&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/life.css"><link rel="stylesheet" href="assets/extras.css"></head><body><div class="projectbar wrap"><span>BY A TIAN · OPEN SOURCE</span><a href="{alt}">{t('English','中文')}</a></div><header class="hero"><div class="blob b1"></div><div class="blob b2"></div><div class="wrap"><div class="hero-in"><div><span class="kicker">{t('把生活变成一页好看的说明书','A COLORFUL MANUAL FOR YOUR LIFE')}</span><h1>{t('人生系统','Life systems')}<br><span>{t('多巴胺版','in full color')}</span></h1><div class="motto box">{t('认识自己，也让自己的内容更有方向。','Understand yourself. Give your creative work direction.')}</div></div><div class="hero-pic"><div class="ring"></div><img src="assets/mascot-01.png" alt="{t('阿甜示例插画','Illustration from A Tian')}"></div></div></div></header><main class="wrap"><div class="g2"><a class="box public-card template-link" href="templates/life-system{template_suffix}.html" style="--c:var(--pink)"><span class="tag">01 · LIFE SYSTEM</span><h2>{t('我的人生系统','My life system')} ↗</h2><p>{t('特点、能量、表达、边界、项目、卡点与生活节奏。','Traits, energy, voice, boundaries, projects, obstacles and rhythm.')}</p></a><a class="box public-card template-link" href="templates/account-planner{template_suffix}.html" style="--c:var(--blue)"><span class="tag">02 · ACCOUNT PLANNER</span><h2>{t('我的账号规划','My account planner')} ↗</h2><p>{t('账号分工、受众、固定栏目、内容联动和一周安排。','Roles, audiences, recurring series, shared themes and weekly scheduling.')}</p></a></div><section><div class="g3"><div class="card"><h3>{t('拿来就能打开','Open and explore')}</h3><p>{t('不用注册。下载后直接打开网页，看看两份完整示例。','No account required. Download and open the complete examples.')}</p></div><div class="card"><h3>{t('改成自己的版本','Make it yours')}</h3><p>{t('替换示例记录、插画和配色，也可以把提示词交给 AI。','Replace the records, illustrations and colors, or give the prompts to AI.')}</p></div><div class="card"><h3>{t('中文和英文','Chinese and English')}</h3><p>{t('网页和文档都提供双语，方便分享给不同的朋友。','Both pages and documentation are bilingual, ready to share.')}</p></div></div></section><p class="example-badge">{t('所有人物、指标和排期内容均为示例。人生系统用于自我记录，不是心理测评。','People, metrics and schedules are examples. The life system is for reflection, not psychological assessment.')}</p></main><footer class="wrap"><a href="{'README_EN.md' if en else 'README.md'}">{t('阅读使用说明','Read the guide')}</a> · MIT · Made by A Tian</footer></body></html>'''

for en in [False, True]:
    suffix='.en' if en else ''
    (ROOT/'templates'/f'life-system{suffix}.html').write_text(life(en),encoding='utf-8')
    (ROOT/'templates'/f'account-planner{suffix}.html').write_text(accounts(en),encoding='utf-8')
    (ROOT/('index_en.html' if en else 'index.html')).write_text(landing(en),encoding='utf-8')
print('Built four templates and two landing pages.')
