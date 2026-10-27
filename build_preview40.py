# -*- coding: utf-8 -*-
"""Offline full preview for Kakuranger Red alerts + all widgets."""
from pathlib import Path
BASE=Path(__file__).parent
RAW="https://raw.githubusercontent.com/MasAjie12/kakuranger-red-alert-assets/refs/heads/main/"
LOCAL={RAW+"bg.png":"bg.png",RAW+"sakura.png":"sakura.png",RAW+"hiasan.png":"hiasan.png",RAW+"hiasan-kanan.png":"hiasan-kanan.png"}
NAMES=["Kakuranger Red","Takeshi","Sasuke","Ryu","Miya","Akimaru"]
WIDGETS=[p.stem for p in sorted((BASE/"widgets").glob("*.css")) if not p.stem.endswith("-obs") or p.stem in {"sociabuzz-milestone","sociabuzz-queue","sociabuzz-subathon","sociabuzz-top-donator"}]

def local(s):
    for a,b in LOCAL.items():s=s.replace(a,"../40-kakuranger-red/"+b)
    return s

def mock(name):
    l=name.lower()
    if "mediashare-video" in l:return '<div id="ms_container"><div class="wrapper"><div class="media-container"><div class="fake-video">▶ KAKURANGER VIDEO</div><div class="loadingbar"></div><div class="style-1 text-container"><div class="title"><span id="sender">Kakuranger Red</span><span class="dari"></span><span id="nominal">Rp 50.000</span></div><div id="message">NINPOH: FIRE SPIN!</div></div></div></div></div>'
    if "mediashare" in l:return '<div id="ms_container"><div class="wrapper"><div class="loadingbar"></div><div class="media-container"><div class="style-1 text-container"><div class="title"><span id="sender">Takeshi</span><span class="dari"></span><span id="nominal">Rp 50.000</span></div><div id="message">Kakuranger, fight!</div></div></div></div></div>'
    if "subathon" in l:return '<div class="w-sub"><div class="subathon-container"><div class="sub_judul"><strong>SUBATHON TIMER</strong></div><div class="sub_timer"><span>12</span>:<span>34</span>:<span>56</span></div></div></div>'
    if "milestone" in l:return '<div class="w-mile"><div class="card"><div class="card-header"><h4><strong>MILESTONE</strong></h4></div><div class="card-body"><div class="center_progress"><h4><strong>Rp 680.000 / Rp 1.000.000</strong></h4></div><div class="progress"><div class="progress-bar" style="width:68%"></div></div></div></div></div>'
    if "queue" in l:return '<div class="w-queue"><div class="card"><div class="card-header"><h4><strong>QUEUE LIST</strong></h4></div><table class="show_donate">'+''.join(f'<tr><td>{i+1}</td><td class="text-limit">{n}</td><td class="text-limit-r">Rp {(5-i)*50000:,}</td></tr>' for i,n in enumerate(NAMES[:5]))+'</table></div></div>'
    return '<div class="w-top"><div class="card"><div class="card-header"><h4><strong>TOP DONATOR</strong></h4></div><table class="show_donate">'+''.join(f'<tr><td>{i+1}</td><td class="text-limit">{n}</td><td class="text-limit-r">Rp {(6-i)*50000:,}</td></tr>' for i,n in enumerate(NAMES[:5]))+'</table></div></div>'

parts=[]
for slug,label in (("sociabuzz","SOCIABUZZ ALERT"),("saweria","SAWERIA ALERT")):
 h=(BASE/f"{slug}-alert.html").read_text(encoding="utf-8")
 for a,b in (("{amount}","Rp 250.000"),("{from_text}","Sociabuzz"),("{supporter}","Takeshi"),("{donator}","Sasuke"),("{message}","NINPOH! KAKURANGER RED ATTACK!")):h=h.replace(a,b)
 c=local((BASE/f"{slug}-alert.css").read_text(encoding="utf-8"));parts.append(f'<section><h2>{label}</h2><div class="alert">{h}<style>{c}</style></div></section>')
for n in WIDGETS:
 c=local((BASE/"widgets"/f"{n}.css").read_text(encoding="utf-8"));parts.append(f'<section class="widget"><h3>{n}</h3><style>{c}</style>{mock(n)}</section>')
html='''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kakuranger Red — Full Preview</title><style>body{margin:0;padding:20px;background:#190205;color:#fff3e3;font-family:Segoe UI,sans-serif}h1{text-align:center;color:#f6d58a;letter-spacing:3px}h2,h3{color:#d92b35}.alert{max-width:720px;margin:auto}.widget{display:inline-block;vertical-align:top;width:min(430px,100%);margin:10px;min-height:190px;background:rgba(38,7,11,.72);border:1px solid #7f151b;border-radius:16px;padding:12px;box-sizing:border-box}.widget h3{font-size:12px;letter-spacing:1px;margin:0 0 8px}section{margin:0 auto 30px;max-width:1400px}@media(max-width:600px){body{padding:10px}.widget{width:100%;margin:8px 0}}</style></head><body><h1>赤 KAKURANGER MERAH 赤</h1>'''+''.join(parts)+'''</body></html>'''
(BASE/"preview-kakuranger-red.html").write_text(html,encoding="utf-8")
assert "{amount}" not in html and "pikachu" not in html.lower()
print("OK preview",len(parts),"sections")
