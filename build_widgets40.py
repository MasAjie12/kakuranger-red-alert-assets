# -*- coding: utf-8 -*-
"""Tema 40 widgets. Port structure stable t31, palette/artwork Kakuranger Merah."""
from pathlib import Path
from PIL import Image, ImageOps
BASE = Path(__file__).parent
SRC = BASE.parent / "31-pikachu-pokemon" / "widgets"
DST = BASE / "widgets"
DST.mkdir(exist_ok=True)
RAW = "https://raw.githubusercontent.com/MasAjie12/kakuranger-red-alert-assets/refs/heads/main/"
LEFT = RAW + "hiasan.png"
RIGHT = RAW + "hiasan-kanan.png"
BG = RAW + "bg.png"
SAKURA = RAW + "sakura.png"
# Bake mirrored asset: no CSS scaleX dependency in production widgets.
source = Path(r"C:/Users/NASRU/Downloads/hiasan.png")
if source.exists(): ImageOps.mirror(Image.open(source)).save(BASE / "hiasan-kanan.png")
SWAPS = [
 ("https://raw.githubusercontent.com/MasAjie12/pikachu-alert-assets/main/pikachubg.png", BG),
 ("https://raw.githubusercontent.com/MasAjie12/pikachu-alert-assets/main/pikachukirinobg.png", LEFT),
 ("pikachu-alert-assets", "kakuranger-red-alert-assets"), ("pikachubg.png", "bg.png"), ("pikachukirinobg.png", "hiasan.png"), ("pikachubg", "bg"), ("pikachukirinobg", "hiasan"),
 ("#FFD92F", "#D92B35"), ("#FFF176", "#F6D58A"), ("#FFFDE7", "#FFF3E3"), ("#FFF59D", "#F9E2A7"), ("#EF3D4E", "#B91F2A"), ("#6A1B9A", "#7F151B"), ("#3D0B5C", "#4A0D12"), ("#2A0846", "#26070B"), ("#16052B", "#190205"), ("#F2EAFF", "#FFE9DE"),
 ("%23EF3D4E", "%23D92B35"), ("%23FFD92F", "%23D8AA45"), ("%236A1B9A", "%237F151B"),
 ("255,217,47", "217,43,53"), ("255, 217, 47", "217, 43, 53"), ("106,27,154", "127,21,27"), ("106, 27, 154", "127, 21, 27"), ("42,8,70", "38,7,11"), ("42, 8, 70", "38, 7, 11"), ("61,11,92", "74,13,18"), ("61, 11, 92", "74, 13, 18"), ("239,61,78", "185,31,42"), ("239, 61, 78", "185, 31, 42"), ("22,6,46", "25,2,5"), ("22, 6, 46", "25, 2, 5"),
 ("PIKACHU LEADERBOARD", "KAKURANGER LEADERBOARD"), ("PIKACHU", "KAKURANGER"), ("GENGAR", "RED"), ("Pokemon", "Kakuranger"), ("POKEMON", "KAKURANGER"), ("✨", "✦"), ("pk31-", "kr40-"), ("t31", "t40"),
]
DECOR = f'''\n/* t40 Kakuranger: bg + sakura overlay + mirrored hiasan above layer */\n.card,.subathon-container{{position:relative!important;overflow:hidden!important;background-image:linear-gradient(rgba(25,2,5,.38),rgba(25,2,5,.58)),url("{SAKURA}"),url("{BG}")!important;background-size:cover,cover,cover!important;background-position:center,center,center!important;background-blend-mode:normal,screen,normal!important;}}\n.card .card-header,.subathon-container .sub_judul{{position:relative!important;padding-left:3.7em!important;padding-right:3.7em!important;z-index:4!important}}\n.card .card-header::before,.card .card-header::after,.subathon-container .sub_judul::before,.subathon-container .sub_judul::after{{content:""!important;position:absolute!important;top:50%!important;width:3.05em!important;height:3.6em!important;background-position:center!important;background-repeat:no-repeat!important;background-size:contain!important;pointer-events:none!important;z-index:8!important;filter:drop-shadow(0 3px 8px rgba(217,43,53,.62))!important;animation:kr40-wglow 3.8s ease-in-out infinite alternate!important}}\n.card .card-header::before,.subathon-container .sub_judul::before{{left:.22em!important;background-image:url("{LEFT}")!important;transform:translateY(-50%)!important}}\n.card .card-header::after,.subathon-container .sub_judul::after{{right:.22em!important;background-image:url("{RIGHT}")!important;transform:translateY(-50%)!important}}\n.card .card-header h4,.card .card-header h4 strong,.sub_judul,.sub_judul strong{{color:#FFF3E3!important;text-shadow:0 2px 8px #190205!important}}\n@keyframes kr40-wglow{{0%{{filter:drop-shadow(0 3px 8px rgba(217,43,53,.48)) brightness(.96)}}100%{{filter:drop-shadow(0 8px 15px rgba(246,213,138,.82)) brightness(1.1)}}}}\n#ms_container{{position:relative!important;overflow:hidden!important;background-image:linear-gradient(rgba(25,2,5,.42),rgba(25,2,5,.62)),url("{SAKURA}"),url("{BG}")!important;background-size:cover,cover,cover!important;background-position:center,center,center!important;background-blend-mode:normal,screen,normal!important}}\n#ms_container .text-container{{position:relative!important;z-index:4!important}}\n#ms_container .text-container::before,#ms_container .text-container::after{{background-image:url("{LEFT}")!important;background-position:center!important;background-size:contain!important;background-repeat:no-repeat!important;filter:drop-shadow(0 3px 8px rgba(217,43,53,.62))!important}}\n#ms_container .text-container::after{{background-image:url("{RIGHT}")!important;transform:translateY(-50%)!important}}\n'''

def transform(text):
    for a,b in SWAPS: text=text.replace(a,b)
    # Some older widget variants contain legacy names/colors outside standard swaps.
    cleanup = {
        "https://raw.githubusercontent.com/MasAjie12/pikachu-alert-assets/main/pikachubg.png": BG,
        "https://raw.githubusercontent.com/MasAjie12/pikachu-alert-assets/main/pikachukirinobg.png": LEFT,
        "pikachu-alert-assets": "kakuranger-red-alert-assets",
        "pikachubg.png": "bg.png", "pikachukirinobg.png": "hiasan.png",
        "pikachubg": "bg", "pikachukirinobg": "hiasan",
        "#FFD92F": "#D92B35", "#FFF176": "#F6D58A", "#FFFDE7": "#FFF3E3",
        "#FFF59D": "#F9E2A7", "#EF3D4E": "#B91F2A", "#6A1B9A": "#7F151B",
        "#3D0B5C": "#4A0D12", "#2A0846": "#26070B", "#16052B": "#190205",
        "#F2EAFF": "#FFE9DE", "pk31": "kr40", "t31": "t40",
        "PIKACHU": "KAKURANGER", "Pikachu": "Kakuranger", "pikachu": "kakuranger",
        "GENGAR": "RED", "Pokemon": "Kakuranger", "POKEMON": "KAKURANGER",
        "✨": "✦",
    }
    for a,b in cleanup.items(): text=text.replace(a,b)
    return text.replace("\r\n","\n")

for src in sorted(SRC.glob("*.css")):
    text = transform(src.read_text(encoding="utf-8")) + DECOR
    assert not any(x in text for x in ("pikachu", "PIKACHU", "Pikachu", "pk31-", "t31")), src.name
    assert text.count("{")==text.count("}"), src.name
    (DST/src.name).write_text(text, encoding="utf-8")
print("OK widgets", len(list(DST.glob("*.css"))))
