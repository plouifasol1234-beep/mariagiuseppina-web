"""Maria Giuseppina · Chef privada — web multipàgina en Streamlit.

Executar:  streamlit run app.py
Fotos:     deixa les imatges a ./img amb els noms de IMAGES (jpg/png/webp).
Contacte:  canvia WHATSAPP pel teu número (format internacional, sense + ni espais).
"""
import base64
import urllib.parse
from pathlib import Path

import streamlit as st

WHATSAPP = "34XXXXXXXXX"  # <-- el teu número, p. ex. 34600111222
EMAIL = ""                # opcional: "hola@mariagiuseppina.cat"

IMG_DIR = Path(__file__).parent / "img"
IMAGES = ["tupper", "davantal", "plats", "retrat", "card1", "card2", "card3", "card4", "card5"]

PAGES = {
    "inici": "Inici",
    "serveis": "Serveis",
    "com-treballo": "Com treballo",
    "qui-soc": "Qui soc",
    "preguntes": "Preguntes",
    "contacte": "Contacte",
}

st.set_page_config(page_title="Maria Giuseppina · Chef privada", page_icon="🍲",
                   layout="wide", initial_sidebar_state="collapsed")


# ───────────────────────── utilitats ─────────────────────────
@st.cache_data
def img_uri(name: str) -> str | None:
    for ext in ("jpg", "jpeg", "png", "webp"):
        p = IMG_DIR / f"{name}.{ext}"
        if p.exists():
            mime = "jpeg" if ext in ("jpg", "jpeg") else ext
            return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"
    return None


def photo(name: str, height: int = 420, cls: str = "") -> str:
    uri = img_uri(name)
    if uri:
        return f'<img class="photo {cls}" src="{uri}" style="height:{height}px" alt="">'
    return f'<div class="photo ph {cls}" style="height:{height}px"><span>📷 img/{name}.jpg</span></div>'


def bg(name: str) -> str:
    uri = img_uri(name)
    return f"background-image:url('{uri}');" if uri else ""


def link(page: str) -> str:
    return f"?p={page}"


def btn(text: str, page: str = "contacte", style: str = "gold") -> str:
    return f'<a class="btn btn-{style}" href="{link(page)}" target="_self">{text}</a>'


def wa_url(text: str = "") -> str:
    url = f"https://wa.me/{WHATSAPP}"
    return url + ("?text=" + urllib.parse.quote(text) if text else "")


def render(html: str) -> None:
    # sense sagnats ni línies buides perquè el markdown de Streamlit no trenqui l'HTML
    st.markdown("\n".join(l.strip() for l in html.splitlines() if l.strip()), unsafe_allow_html=True)


# ───────────────────────── estils ─────────────────────────
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');
:root{--cream:#F6EFE1;--paper:#FCF9F2;--sage:#E3E8D4;--sage2:#D5DDC2;--green:#33432C;--green2:#425538;--ink:#1F2A1A;--muted:#5d6455;--gold:#E8B52E;--gold2:#D9A41C;--line:#d8d6c6;}
#MainMenu,header[data-testid="stHeader"],footer,[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="collapsedControl"]{display:none!important;}
.stApp{background:var(--paper);}
.block-container{padding:0!important;max-width:100%!important;}
[data-testid="stVerticalBlock"]{gap:0!important;}
.mg,.mg *{box-sizing:border-box;}
.mg{font-family:'DM Sans',sans-serif;color:var(--ink);}
.mg p,.mg li,.mg span,.mg em,.mg small,.mg a{font-family:inherit;}
.mg h1,.mg h2,.mg h3,.mg h4{padding:0;letter-spacing:normal;font-family:'Libre Baskerville',serif;color:var(--green);}
.mg .serif{font-family:'Libre Baskerville',serif;}
.mg a{text-decoration:none;}

/* layout */
.sec{padding:96px 24px;}
.wrap{max-width:1180px;margin:0 auto;}
.narrow{max-width:820px;margin:0 auto;}
.center{text-align:center;}
.bg-cream{background:var(--cream);} .bg-paper{background:var(--paper);} .bg-sage{background:var(--sage);} .bg-green{background:var(--green);}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;}
.photo{width:100%;object-fit:cover;border-radius:18px;display:block;box-shadow:0 24px 50px -24px rgba(40,50,30,.45);}
.ph{background:repeating-linear-gradient(45deg,#e8e0cf,#e8e0cf 12px,#efe8d9 12px,#efe8d9 24px);display:flex;align-items:center;justify-content:center;color:#8a8170;font-size:14px;}

/* tipografia */
.eyebrow{font-weight:700;font-size:14px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold2);margin:0 0 16px;display:flex;align-items:center;gap:12px;}
.eyebrow:before{content:"";width:28px;height:2px;background:var(--gold);}
.center .eyebrow{justify-content:center;}
.mg h2.title{font-size:42px;line-height:1.2;margin:0 0 22px;font-weight:700;}
.lead{font-size:20px;line-height:1.65;color:var(--muted);margin:0 0 18px;}
.body{font-size:18px;line-height:1.65;margin:0 0 16px;}

/* botons */
.btn{display:inline-flex;align-items:center;gap:10px;font-weight:700;font-size:16px;padding:16px 30px;border-radius:999px;transition:all .2s ease;border:2px solid transparent;}
.btn-gold{background:var(--gold);color:var(--ink)!important;box-shadow:0 10px 24px -10px rgba(217,164,28,.8);}
.btn-gold:hover{background:var(--gold2);transform:translateY(-2px);}
.btn-ghost{border-color:var(--green);color:var(--green)!important;}
.btn-ghost:hover{background:var(--green);color:var(--paper)!important;}
.btn-light{border-color:var(--paper);color:var(--paper)!important;}
.btn-light:hover{background:var(--paper);color:var(--green)!important;}
.btns{display:flex;gap:14px;flex-wrap:wrap;margin-top:34px;}
.center .btns{justify-content:center;}
.center .lead{margin-left:auto;margin-right:auto;max-width:720px;}

/* navegació */
.nav{position:fixed;top:0;left:0;right:0;z-index:999;background:rgba(246,239,225,.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid #e6dfcd;}
.nav .in{max-width:1180px;margin:0 auto;padding:0 24px;height:78px;display:flex;align-items:center;justify-content:space-between;}
.brand{display:flex;flex-direction:column;}
.brand b{font-family:'Libre Baskerville',serif;font-weight:400;font-size:26px;color:var(--green);line-height:1;}
.brand i{font-style:normal;font-size:10.5px;letter-spacing:.2em;color:var(--muted);margin-top:6px;font-weight:600;}
.links{display:flex;align-items:center;gap:30px;}
.links a{color:var(--green)!important;font-weight:500;font-size:15.5px;position:relative;padding:6px 0;}
.links a:after{content:"";position:absolute;left:0;bottom:0;height:2px;width:0;background:var(--gold);transition:width .25s;}
.links a:hover:after,.links a.on:after{width:100%;}
.links a.on{font-weight:700;}
.links a.cta{background:var(--green);color:var(--paper)!important;padding:11px 22px;border-radius:999px;font-weight:600;}
.links a.cta:after{display:none;}
.links a.cta:hover{background:var(--green2);}
#mtoggle,.burger{display:none;}
.spacer{height:78px;}

/* hero */
.hero{position:relative;overflow:hidden;background:linear-gradient(135deg,var(--sage) 0%,#EDEFDF 100%);padding:90px 24px 110px;}
.hero:before{content:"";position:absolute;right:-180px;top:-180px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(232,181,46,.22),transparent 70%);}
.hero h1{font-size:58px;line-height:1.12;margin:0 0 24px;font-weight:700;}
.hero h1 em{font-weight:400;color:var(--green2);}
.hero .lead{font-size:21px;}
.hero .imgbox{position:relative;}
.badge{position:absolute;left:-28px;bottom:34px;background:var(--paper);border-radius:16px;padding:18px 22px;box-shadow:0 20px 40px -18px rgba(40,50,30,.5);display:flex;gap:14px;align-items:center;}
.badge .n{font-family:'Libre Baskerville',serif;font-size:34px;font-weight:700;color:var(--gold2);}
.badge .t{font-size:13.5px;line-height:1.35;color:var(--green);font-weight:600;}
.fade{animation:fadeUp .8s ease both;} .fade2{animation:fadeUp .8s .15s ease both;} .fade3{animation:fadeUp .8s .3s ease both;}
@keyframes fadeUp{from{opacity:0;transform:translateY(18px);}to{opacity:1;transform:none;}}

/* franja de confiança */
.trust{background:var(--green);color:var(--paper);padding:26px 24px;}
.trust .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;}
.trust div div{display:flex;gap:12px;align-items:center;font-size:15px;font-weight:500;}
.trust .ic{width:38px;height:38px;flex:none;border-radius:50%;background:rgba(232,181,46,.18);color:var(--gold);display:flex;align-items:center;justify-content:center;font-size:18px;}

/* pregunta de cada dia */
.daily p{font-family:'Libre Baskerville',serif;font-size:27px;margin:0;padding:18px 0;color:var(--ink);}
.daily .mid{font-weight:700;border-top:1px solid var(--line);border-bottom:1px solid var(--line);}
.daily h2{font-family:'DM Sans',sans-serif!important;font-size:40px;margin:0 0 26px;}

/* targetes */
.card{background:var(--paper);border:1px solid #e7e1d2;border-radius:20px;padding:34px 30px;transition:all .25s ease;display:flex;flex-direction:column;height:100%;}
.card:hover{transform:translateY(-6px);box-shadow:0 26px 50px -28px rgba(40,50,30,.45);border-color:var(--gold);}
.mg a.card,.mg a.card p{color:var(--ink)!important;}
.card .num{margin-bottom:22px;}
.card h3{font-size:22px;margin:0 0 6px;font-weight:700;}
.card .sub{font-family:'Libre Baskerville',serif;font-style:italic;color:var(--muted);font-size:15px;margin:0 0 16px;}
.card p{font-size:16.5px;line-height:1.6;margin:0 0 12px;}
.card .more{margin-top:auto;padding-top:14px;font-weight:700;color:var(--green)!important;font-size:15px;}
.num{width:48px;height:48px;border-radius:50%;background:var(--gold);display:flex;align-items:center;justify-content:center;font-family:'Libre Baskerville',serif;font-weight:700;font-size:16px;color:var(--green);flex:none;}

/* serveis detallats */
.svc{display:grid;grid-template-columns:1fr 1.25fr;border-radius:24px;overflow:hidden;background:var(--paper);border:1px solid #e7e1d2;margin-bottom:34px;box-shadow:0 30px 60px -40px rgba(40,50,30,.4);}
.svc:nth-child(even){grid-template-columns:1.25fr 1fr;}
.svc:nth-child(even) .pic{order:2;}
.svc .pic{min-height:340px;background-size:cover;background-position:center;background-color:#e8e0cf;position:relative;}
.svc .pic.empty{background-image:repeating-linear-gradient(45deg,#e8e0cf,#e8e0cf 12px,#efe8d9 12px,#efe8d9 24px);}
.svc .pic .num{position:absolute;top:24px;left:24px;width:58px;height:58px;font-size:20px;box-shadow:0 8px 20px -6px rgba(0,0,0,.3);}
.svc .txt{padding:48px 52px;}
.svc h3{font-size:30px;margin:0 0 6px;font-weight:400;}
.svc .sub{font-family:'Libre Baskerville',serif;font-style:italic;color:var(--muted);font-size:17px;margin:0 0 24px;}
.svc ul{list-style:none;padding:0;margin:0 0 26px;}
.svc li{font-size:18px;line-height:1.55;padding:6px 0 6px 30px;position:relative;}
.svc li:before{content:"✓";position:absolute;left:0;color:var(--gold2);font-weight:700;}
.svc .ideal{background:var(--sage);border-radius:12px;padding:14px 18px;font-weight:600;color:var(--green);font-size:15.5px;margin:0;}

/* comptes */
.box{background:var(--paper);border-radius:22px;padding:44px 46px;box-shadow:0 30px 60px -40px rgba(40,50,30,.5);}
.box h3{font-size:28px;margin:0 0 8px;font-weight:700;}
.box em{display:block;font-size:17px;color:var(--muted);margin-bottom:24px;}
.box ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;column-gap:28px;}
.box li{font-size:16.5px;line-height:1.45;padding:14px 0 14px 28px;border-bottom:1px solid #ebe7da;position:relative;}
.box li:before{content:"";position:absolute;left:0;top:20px;width:12px;height:12px;border-radius:3px;border:2px solid var(--gold);}

/* línia temporal */
.tl{position:relative;max-width:860px;margin:0 auto;}
.tl:before{content:"";position:absolute;left:28px;top:10px;bottom:10px;width:2px;background:linear-gradient(var(--gold),var(--sage2));}
.tl .it{display:flex;gap:30px;padding:0 0 46px;position:relative;}
.tl .num{width:58px;height:58px;font-size:19px;box-shadow:0 0 0 8px var(--paper);}
.tl h3{font-size:26px;margin:8px 0 10px;font-weight:700;}
.tl p{font-size:18px;line-height:1.65;margin:0;color:var(--muted);}

/* banda primera experiència */
.band{background:var(--green);border-radius:28px;padding:64px;color:var(--paper);display:grid;grid-template-columns:1.2fr 1fr;gap:56px;align-items:center;position:relative;overflow:hidden;}
.band:after{content:"";position:absolute;right:-120px;bottom:-160px;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,rgba(232,181,46,.25),transparent 70%);}
.mg .band h2{color:var(--paper);font-size:40px;margin:0 0 18px;}
.band p{color:#dfe5d3;font-size:18px;line-height:1.65;margin:0 0 14px;}
.band .eyebrow{color:var(--gold);}
.band .note{border-left:3px solid var(--gold);padding-left:18px;font-style:italic;color:#f1efe4;}
.band .photo{position:relative;z-index:1;}

/* qui soc */
.mg p.quote{font-family:'Libre Baskerville',serif;font-size:30px;line-height:1.45;color:var(--green);font-style:italic;position:relative;padding-top:40px;}
.quote:before{content:"“";position:absolute;top:-30px;left:50%;transform:translateX(-50%);font-size:110px;color:var(--gold);font-style:normal;line-height:1;}
.about p{font-family:'Libre Baskerville',serif;font-size:19px;line-height:1.7;margin:0 0 20px;}
.values{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:20px;}
.values div{background:var(--paper);border-radius:18px;padding:30px;text-align:center;}
.values b{display:block;font-family:'Libre Baskerville',serif;font-size:22px;color:var(--green);margin:12px 0 8px;}
.values span{color:var(--muted);font-size:16px;line-height:1.55;}
.values .ic{font-size:30px;}

/* FAQ */
.faq details{background:var(--paper);border:1px solid #e7e1d2;border-radius:16px;margin-bottom:14px;transition:box-shadow .2s;}
.faq details[open]{box-shadow:0 20px 40px -30px rgba(40,50,30,.5);border-color:var(--gold);}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:20px;padding:24px 28px;font-family:'Libre Baskerville',serif;font-weight:700;font-size:19px;color:var(--green);}
.faq summary::-webkit-details-marker{display:none;}
.faq summary:after{content:"+";flex:none;width:34px;height:34px;border-radius:50%;background:var(--sage);display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-size:22px;transition:transform .25s;}
.faq details[open] summary:after{transform:rotate(45deg);background:var(--gold);}
.faq .a{font-size:17px;line-height:1.7;padding:0 28px 26px;color:var(--muted);}
.faq .a p{margin:0 0 14px;} .faq .a p:last-child{margin:0;}

/* capçalera de pàgina interior */
.phead{background:linear-gradient(135deg,var(--sage) 0%,#EDEFDF 100%);padding:80px 24px 70px;text-align:center;}
.phead h1{font-size:50px;margin:0 0 18px;font-weight:700;}
.phead p{font-size:20px;color:var(--muted);max-width:700px;margin:0 auto;line-height:1.6;}

/* contacte */
.cinfo{background:var(--green);color:var(--paper);border-radius:24px;padding:44px;height:100%;}
.mg .cinfo h3{color:var(--paper);font-size:26px;margin:0 0 20px;}
.cinfo .row{display:flex;gap:16px;padding:16px 0;border-bottom:1px solid rgba(255,255,255,.12);font-size:16px;line-height:1.5;color:#e5eadb;}
.cinfo .row b{color:var(--gold);display:block;font-size:13px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px;}
.cinfo ol{padding-left:20px;margin:10px 0 0;color:#e5eadb;font-size:15.5px;line-height:1.7;}
div[data-testid="stForm"]{background:var(--paper);border:1px solid #e7e1d2!important;border-radius:24px;padding:36px!important;box-shadow:0 30px 60px -40px rgba(40,50,30,.4);}
div[data-testid="stForm"] label p{font-weight:600;color:var(--green);}
div[data-testid="stFormSubmitButton"] button,a[data-testid="baseLinkButton-primary"]{background:var(--gold)!important;color:var(--ink)!important;border:none!important;border-radius:999px!important;padding:12px 28px!important;font-weight:700!important;}

/* CTA final i peu */
.final{text-align:center;}
.final h2{font-size:48px;line-height:1.2;margin:10px 0 18px;font-weight:700;}
.final em{display:block;font-size:22px;color:var(--muted);}
.foot{background:var(--green);color:#d9dfcd;padding:70px 24px 30px;}
.foot .cols{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:40px;}
.foot .brand b{color:var(--paper);font-size:30px;}
.foot .brand i{color:var(--gold);}
.foot h4{color:var(--paper)!important;font-family:'DM Sans',sans-serif!important;font-size:14px;letter-spacing:.15em;text-transform:uppercase;margin:0 0 18px;}
.foot a{display:block;color:#d9dfcd!important;padding:5px 0;font-size:15.5px;}
.foot a:hover{color:var(--gold)!important;}
.foot p{font-size:15px;line-height:1.6;margin:16px 0 0;max-width:340px;}
.foot .legal{border-top:1px solid rgba(255,255,255,.12);margin-top:50px;padding-top:24px;font-size:13px;color:#aeb7a3;display:flex;justify-content:space-between;}

/* mòbil */
@media (max-width:900px){
 .grid2,.grid3,.band,.values,.foot .cols{grid-template-columns:1fr;gap:36px;}
 .svc,.svc:nth-child(even){grid-template-columns:1fr;}
 .svc:nth-child(even) .pic{order:0;}
 .svc .pic{min-height:220px;} .svc .txt{padding:32px 26px;}
 .trust .wrap{grid-template-columns:1fr 1fr;}
 .box ul{grid-template-columns:1fr;}
 .hero h1{font-size:38px;} .mg h2.title,.final h2,.phead h1,.mg .band h2{font-size:32px;}
 .daily p{font-size:21px;} .band{padding:40px 26px;}
 .badge{left:12px;bottom:12px;}
 .sec{padding:64px 16px;}
 .burger{display:flex;flex-direction:column;gap:5px;cursor:pointer;padding:10px;}
 .burger span{width:24px;height:2px;background:var(--green);}
 .links{display:none;position:absolute;top:78px;left:0;right:0;background:var(--cream);flex-direction:column;align-items:flex-start;padding:16px 24px 26px;gap:12px;border-bottom:1px solid #e6dfcd;}
 #mtoggle:checked ~ .links{display:flex;}
}
</style>
"""

# ───────────────────────── contingut ─────────────────────────
STEPS = [
    ("Ens coneixem", "Parlem de quina part de la vostra alimentació vols resoldre, qui menja a casa, els horaris, els gustos, els aliments que no us agraden i les necessitats."),
    ("Revisem la teva cuina", "Comprovem l'espai, els fogons, el forn, els estris i la capacitat de conservació."),
    ("Dissenyo la teva proposta", "Acordem el menú, les quantitats, la compra, la data, el pressupost i les condicions."),
    ("Cuino a casa teva", "Compro els ingredients, cuino, divideixo en racions, envaso i etiqueto. En acabar, netejo i deixo la cuina i tot el que he utilitzat endreçats."),
    ("Gaudeixes dels teus plats", "Segueixes les indicacions de conservació i de preparació final per gaudir dels plats acordats."),
    ("Revisem el resultat", "M'expliques quins plats, quantitats i formats han funcionat millor. Amb aquesta informació preparo, si vols, una proposta periòdica."),
]

COSTS = [
    "Persones que mengen a casa: d'1 a 6 o més.", "Compra setmanal d'aliments.",
    "Plats preparats comprats cada setmana i el seu cost.", "Comandes a domicili o per emportar i el seu cost.",
    "Dinars i sopars fora de casa.", "Esmorzars i berenars comprats fora.",
    "Hores setmanals dedicades a l'alimentació.",
]

SERVICES = [
    ("Cuina quotidiana", "Escalfar i llestos",
     ["Plats casolans complets per arribar, escalfar i menjar.", "Planificació, compra i cuina resoltes."],
     "Ideal si vols delegar la planificació, la compra i la cuina."),
    ("Jornada de preparacions de base", "Avança allò que et pren més temps",
     ["Preparacions casolanes a punt per combinar i acabar en minuts.", "Sofregits, salses, brous, verdures, llegums i proteïnes preparats amb antelació."],
     "Ideal si vols cuinar més de pressa, sense començar de zero."),
    ("Cuina mixta", "Comoditat i flexibilitat",
     ["Plats a punt i preparacions de base per combinar amb flexibilitat.", "Opcions per als dies atrafegats i per aprofitar allò que ja tens."],
     "Ideal si vols tenir opcions sense haver de decidir-ho tot cada dia."),
    ("Celebracions i dies assenyalats", "Preparatius per a molts convidats",
     ["Preparatius per Nadal, aniversaris i àpats familiars.", "Elaboracions dividides en racions, identificades i a punt per escalfar."],
     "Ideal si vols rebre convidats sense passar tota la celebració a la cuina."),
    ("Experiències gastronòmiques privades", "Una taula per recordar",
     ["Una taula especial per a sopars i celebracions.", "Menú propi, servei al moment i temps per als teus convidats."],
     "Ideal si vols viure l'ocasió sense ocupar-te de la cuina."),
]

FAQ = [
    ("Cuines a casa meva?", ["Sí. Cuino a la teva cuina després de revisar l'espai, l'equipament disponible i la capacitat de conservació. Així puc dissenyar una proposta que funcioni de debò a casa teva."]),
    ("Puc triar el menú?", ["Abans de dissenyar-lo, conec els vostres gustos, costums, aliments que no consumiu i allò que necessiteu resoldre. Amb aquesta informació preparo una proposta equilibrada i adaptada al vostre dia a dia."]),
    ("Qui fa la compra?", ["M'ocupo de seleccionar i comprar els ingredients necessaris perquè puguis delegar tot el procés i no t'hagis de preocupar de res. Els aliments es cobren per separat i el seu cost es justifica de manera transparent amb els tiquets de compra."]),
    ("Quants àpats es poden preparar?", ["Dependrà del nombre de persones, les elaboracions triades, les quantitats, l'equipament i l'espai disponible a la nevera o al congelador. Abans de confirmar el servei acordarem quina part de la vostra alimentació voleu deixar resolta."]),
    ("Com es conserven els plats?", ["Cada elaboració es divideix en racions, s'identifica i es conserva de la manera més adequada. En acabar, tindràs indicacions clares sobre l'ordre de consum i la manera d'escalfar o acabar cada preparació per gaudir-ne en les millors condicions."]),
    ("Pots adaptar el menú a al·lèrgies, intoleràncies o pautes alimentàries?", [
        "Explica'm qualsevol al·lèrgia, intolerància o restricció alimentària des de la primera conversa. Abans d'acceptar el servei, estudiaré la teva situació i comprovaré si puc adaptar el menú i treballar amb les condicions de seguretat necessàries.",
        "Si segueixes una pauta indicada per un metge o un dietista-nutricionista, la pots compartir amb mi. Jo no dissenyo dietes ni pautes nutricionals, però puc estudiar com convertir aquestes indicacions en plats adaptats al teu dia a dia."]),
    ("Quant costa?", ["Cada proposta s'adapta al nombre de persones, els àpats que vols resoldre, la freqüència, l'espai disponible i el grau de personalització. Després d'una breu conversa rebràs una proposta clara amb l'abast, el pressupost i tot el que inclou."]),
    ("On treballes?", ["Actualment, el servei està disponible al Vendrell i als voltants. Si vius una mica més lluny, consulta-m'ho i comprovaré si m'hi puc desplaçar."]),
    ("Com comencem?", [
        "Escriu-me per missatge i explica'm quina part de la vostra alimentació vols resoldre.",
        "Després parlarem de casa vostra, la vostra rutina, els vostres gustos i les necessitats que he de tenir en compte.",
        "Quan m'hagis facilitat tota la informació, la revisaré i prepararé una proposta clara amb el servei recomanat, l'abast, la data disponible i el pressupost.",
        "Comprovarem la cuina, els estris i l'espai de conservació; et demanaré algunes fotografies o farem una breu videotrucada abans de confirmar la proposta definitiva.",
        "Si tot encaixa, fareu el pagament de la reserva, confirmarem la data i jo m'ocuparé d'organitzar la resta."]),
]

# ───────────────────────── blocs comuns ─────────────────────────
def nav(current: str) -> str:
    items = "".join(
        f'<a href="{link(k)}" target="_self" class="{"on" if k == current else ""}">{v}</a>'
        for k, v in PAGES.items() if k != "contacte"
    )
    return f"""
<div class="nav"><div class="in">
<a class="brand" href="{link('inici')}" target="_self"><b>Maria Giuseppina</b><i>CHEF PRIVADA</i></a>
<input type="checkbox" id="mtoggle"><label class="burger" for="mtoggle"><span></span><span></span><span></span></label>
<div class="links">{items}<a class="cta" href="{link('contacte')}" target="_self">Parlem de casa teva</a></div>
</div></div>
<div class="spacer"></div>"""


def page_head(eyebrow: str, title: str, text: str) -> str:
    return f"""
<section class="phead"><div class="fade">
<p class="eyebrow" style="justify-content:center">{eyebrow}</p>
<h1>{title}</h1><p>{text}</p></div></section>"""


def final_cta() -> str:
    return f"""
<section class="sec bg-sage final"><div class="narrow">
<p class="eyebrow" style="justify-content:center">Quan comencem?</p>
<h2>Menjar casolà sense haver de pensar cada dia què cuinar.</h2>
<em>Obrir la nevera i trobar-hi tranquil·litat.</em>
<div class="btns" style="justify-content:center">{btn("Parlem de casa teva →")}</div>
</div></section>"""


def footer() -> str:
    pages = "".join(f'<a href="{link(k)}" target="_self">{v}</a>' for k, v in PAGES.items())
    contact = f'<a href="{wa_url()}" target="_blank">WhatsApp</a>'
    if EMAIL:
        contact += f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    return f"""
<div class="foot"><div class="wrap">
<div class="cols">
<div><div class="brand"><b>Maria Giuseppina</b><i>CHEF PRIVADA · CUINA PENSADA PER A CASA TEVA</i></div>
<p>Cuina casolana a casa teva, al Vendrell i voltants. Menjar bé sense que sigui una altra preocupació.</p></div>
<div><h4>Navega</h4>{pages}</div>
<div><h4>Contacte</h4>{contact}<a href="{link('preguntes')}" target="_self">Preguntes freqüents</a></div>
</div>
<div class="legal"><span>© Maria Giuseppina</span><span>El Vendrell · Baix Penedès</span></div>
</div></div>"""


def primera_experiencia() -> str:
    return f"""
<section class="sec bg-paper"><div class="wrap"><div class="band">
<div style="position:relative;z-index:1">
<p class="eyebrow">Primera experiència</p>
<h2>Cinc dies amb els àpats resolts.</h2>
<p>Una manera senzilla de comprovar com funcionaria el servei en la teva vida quotidiana.</p>
<p>Conec els teus gustos i la teva rutina, dissenyo el menú, organitzo la compra i cuino a casa teva.</p>
<p class="note">La proposta inclou fins a 10 plats complets per a dues persones, pensats per a cinc dies de comides o sopars. La quantitat final s'ajusta a les necessitats de cada llar.</p>
<div class="btns">{btn("Vull la meva primera experiència")}</div>
</div>
<div>{photo("plats", 400)}</div>
</div></div></section>"""


# ───────────────────────── pàgines ─────────────────────────
def page_inici():
    trust = [("🏠", "Cuino a casa teva"), ("🥘", "Menú adaptat als vostres gustos"),
             ("🧺", "Compra, cuina i neteja incloses"), ("⭐", "+15 anys en gastronomia")]
    trust_html = "".join(f'<div><span class="ic">{i}</span>{t}</div>' for i, t in trust)
    cards = "".join(
        f'<a class="card" href="{link("serveis")}" target="_self"><div class="num">{i:02d}</div>'
        f'<h3>{t}</h3><p class="sub">{s}</p><p>{lines[0]}</p><span class="more">Més informació →</span></a>'
        for i, (t, s, lines, _) in enumerate(SERVICES[:3], 1)
    )
    render(f"""
<div class="mg">
<section class="hero"><div class="wrap grid2">
<div>
<p class="eyebrow fade">Chef privada · El Vendrell i voltants</p>
<h1 class="fade2">Menjar casolà <em>sense haver de pensar</em> cada dia què cuinar.</h1>
<p class="lead fade3">Cuino a casa teva plats casolans, variats i pensats per als vostres gustos. Tu obres la nevera i hi trobes tranquil·litat.</p>
<div class="btns fade3">{btn("Parlem de casa teva →")}{btn("Veure serveis", "serveis", "ghost")}</div>
</div>
<div class="imgbox fade2">{photo("tupper", 500)}
<div class="badge"><span class="n">10</span><span class="t">plats complets<br>en la primera experiència</span></div></div>
</div></section>

<div class="trust"><div class="wrap">{trust_html}</div></div>

<section class="sec bg-paper center daily"><div class="narrow">
<p class="eyebrow" style="justify-content:center;font-family:'DM Sans'">La pregunta de cada dia</p>
<h2>Què mengem avui?</h2>
<p>No pesa només cuinar…</p>
<p class="mid">Pesa haver de pensar-ho cada dia:<br>decidir, comprar, cuinar, recollir i netejar.</p>
<p>I saber que demà tot torna a començar…</p>
</div></section>

<section class="sec bg-cream"><div class="wrap grid2">
<div>{photo("davantal", 480)}</div>
<div>
<p class="eyebrow">Què puc fer per casa teva?</p>
<h2 class="title">Que menjar bé deixi de ser una altra preocupació.</h2>
<p class="lead">Menjar casolà i variat, sense haver de pensar cada dia què cuinar.</p>
<p class="lead">Preparo una proposta pensada per als vostres gustos i el vostre dia a dia.</p>
<div class="btns">{btn("Com treballo", "com-treballo", "ghost")}</div>
</div>
</div></section>

<section class="sec bg-paper"><div class="wrap">
<div class="center" style="margin-bottom:50px">
<p class="eyebrow" style="justify-content:center">Com ho podem resoldre?</p>
<h2 class="title">Tria quina part de la cuina vols delegar</h2>
<p class="lead narrow">Tenir plats a punt, avançar preparacions o gaudir d'una taula especial.</p>
</div>
<div class="grid3">{cards}</div>
<div class="btns" style="justify-content:center">{btn("Veure tots els serveis", "serveis", "ghost")}</div>
</div></section>
</div>""")
    render(f'<div class="mg">{primera_experiencia()}{final_cta()}</div>')


def page_serveis():
    svcs = "".join(
        f'<div class="svc"><div class="pic {"" if img_uri(f"card{i}") else "empty"}" style="{bg(f"card{i}")}">'
        f'<div class="num">{i:02d}</div></div><div class="txt"><h3>{t}</h3><p class="sub">{s}</p>'
        f'<ul>{"".join(f"<li>{x}</li>" for x in lines)}</ul><p class="ideal">{ideal}</p></div></div>'
        for i, (t, s, lines, ideal) in enumerate(SERVICES, 1)
    )
    costs = "".join(f"<li>{c}</li>" for c in COSTS)
    render(f"""
<div class="mg">
{page_head("Serveis", "Tria quina part de la cuina vols delegar", "Tenir plats a punt, avançar preparacions o gaudir d'una taula especial. Comencem per allò que avui et pren més temps, energia o tranquil·litat.")}
<section class="sec bg-cream"><div class="wrap">{svcs}</div></section>
<section class="sec bg-sage"><div class="wrap grid2">
<div>
<p class="eyebrow">El teu punt de partida</p>
<h2 class="title">Quant et costa resoldre els àpats cada setmana?</h2>
<p class="lead">El preu d'un àpat no és només el que hi ha al plat. També compten les comandes d'última hora i el temps que dediques a decidir, comprar, cuinar i recollir.</p>
<div class="btns">{btn("Comparar-ho amb una proposta per a casa meva")}</div>
</div>
<div class="box"><h3>Fes els teus comptes</h3><em>Revisa aquests punts amb les teves dades:</em><ul>{costs}</ul></div>
</div></section>
{final_cta()}
</div>""")


def page_com_treballo():
    steps = "".join(
        f'<div class="it"><div class="num">{i:02d}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i, (t, d) in enumerate(STEPS, 1)
    )
    render(f"""
<div class="mg">
{page_head("Com treballo", "De la primera conversa a la nevera organitzada", "Un procés clar, pas a pas, perquè només t'hagis de preocupar de gaudir dels plats.")}
<section class="sec bg-paper"><div class="tl">{steps}</div></section>
{primera_experiencia()}
{final_cta()}
</div>""")


def page_qui_soc():
    render(f"""
<div class="mg">
{page_head("Qui soc", "Maria José Arroyo", "Cuinera i creadora de Maria Giuseppina.")}
<section class="sec bg-paper"><div class="wrap grid2 about">
<div>{photo("retrat", 560)}</div>
<div>
<p class="eyebrow" style="font-family:'DM Sans'">La meva història</p>
<p>La cuina és la meva passió des dels vuit anys i fa més de quinze anys que treballo en el món de la gastronomia.</p>
<p>Maria Giuseppina neix d'una cuina propera, generosa i profundament vinculada a la llar.</p>
<p>Una cuina que recorda les mares i les àvies que cuinaven per cuidar els seus, però adaptada a la vida d'avui.</p>
<div class="btns">{btn("Parlem de casa teva →")}</div>
</div>
</div></section>
<section class="sec bg-sage center"><div class="narrow">
<p class="quote">Vull ajudar-te a viure l'alimentació quotidiana amb més tranquil·litat i a convertir les ocasions especials en experiències que perdurin en la memòria.</p>
</div>
<div class="wrap values">
<div><span class="ic">🤝</span><b>Propera</b><span>Conec els vostres gustos, la vostra rutina i la vostra cuina.</span></div>
<div><span class="ic">🍲</span><b>Generosa</b><span>Plats casolans i variats, com els de casa de sempre.</span></div>
<div><span class="ic">🏡</span><b>Vinculada a la llar</b><span>Cuino a casa teva i ho deixo tot endreçat.</span></div>
</div></section>
{final_cta()}
</div>""")


def page_preguntes():
    faq = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="a">'
        + "".join(f"<p>{p}</p>" for p in ps) + "</div></details>"
        for i, (q, ps) in enumerate(FAQ)
    )
    render(f"""
<div class="mg">
{page_head("Preguntes freqüents", "Tot el que necessites saber", "Si no trobes la resposta, escriu-me i t'ho explico.")}
<section class="sec bg-cream"><div class="narrow faq">{faq}</div></section>
{final_cta()}
</div>""")


def page_contacte():
    render(f"""
<div class="mg">
{page_head("Contacte", "Parlem de casa teva", "Explica'm quina part de la vostra alimentació vols resoldre i et preparo una proposta clara amb el servei recomanat, l'abast, la data i el pressupost.")}
</div>""")
    render('<div style="height:70px"></div>')
    _, c1, gap, c2, _ = st.columns([0.6, 5, 0.4, 4, 0.6])
    with c1:
        with st.form("contacte"):
            nom = st.text_input("Nom")
            poble = st.text_input("Població", placeholder="El Vendrell, Calafell, Cunit…")
            persones = st.select_slider("Persones que mengen a casa", ["1", "2", "3", "4", "5", "6 o més"], value="2")
            serveis = st.multiselect("Què t'interessa?", [s[0] for s in SERVICES] + ["Primera experiència (5 dies)"],
                                     placeholder="Tria una o més opcions")
            msg = st.text_area("Explica'm una mica la vostra rutina", height=120,
                               placeholder="Horaris, gustos, al·lèrgies o intoleràncies, què voldries resoldre…")
            ok = st.form_submit_button("Preparar missatge", use_container_width=True)
        if ok:
            if not nom.strip():
                st.warning("Escriu el teu nom, si us plau.")
            else:
                text = (f"Hola Maria José! Soc {nom.strip()}"
                        + (f", de {poble.strip()}" if poble.strip() else "") + ".\n"
                        + f"Som {persones} persones a casa.\n"
                        + (f"M'interessa: {', '.join(serveis)}.\n" if serveis else "")
                        + (f"\n{msg.strip()}" if msg.strip() else ""))
                st.success("Missatge a punt! Revisa'l i envia'l per WhatsApp.")
                st.code(text, language=None)
                st.link_button("Enviar per WhatsApp →", wa_url(text), type="primary", use_container_width=True)
                if EMAIL:
                    st.link_button("Enviar per correu", f"mailto:{EMAIL}?subject=Proposta%20Maria%20Giuseppina&body={urllib.parse.quote(text)}",
                                   use_container_width=True)
    with c2:
        render(f"""
<div class="mg"><div class="cinfo">
<h3>Com comencem?</h3>
<div class="row"><div><b>Zona</b>El Vendrell i voltants. Si vius una mica més lluny, consulta-m'ho.</div></div>
<div class="row"><div><b>Resposta</b>Després d'una breu conversa rebràs una proposta clara amb l'abast i el pressupost.</div></div>
<ol>
<li>M'expliques què vols resoldre.</li>
<li>Parlem de la vostra rutina i gustos.</li>
<li>Reps la proposta i el pressupost.</li>
<li>Revisem la cuina (fotos o videotrucada).</li>
<li>Confirmem la data i jo m'ocupo de la resta.</li>
</ol>
<div class="btns"><a class="btn btn-light" href="{wa_url()}" target="_blank">Escriu-me directament</a></div>
</div></div>""")
    render('<div style="height:90px"></div>')


ROUTES = {
    "inici": page_inici, "serveis": page_serveis, "com-treballo": page_com_treballo,
    "qui-soc": page_qui_soc, "preguntes": page_preguntes, "contacte": page_contacte,
}

# ───────────────────────── main ─────────────────────────
current = st.query_params.get("p", "inici")
if current not in ROUTES:
    current = "inici"

render(CSS)
render(f'<div class="mg">{nav(current)}</div>')
ROUTES[current]()
render(f'<div class="mg">{footer()}</div>')
