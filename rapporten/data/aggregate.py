import json, glob, os, re, sys, collections
BASE = os.path.dirname(os.path.abspath(__file__))
ENGINES = ["chatgpt", "perplexity", "gemini", "google_ai_mode"]
LABEL = {"chatgpt":"ChatGPT","perplexity":"Perplexity","gemini":"Gemini","google_ai_mode":"Google AI Mode"}

# Aliases: canonical name -> list of lowercase variants
ALIASES = {
 "Gold Lemon": ["gold lemon","goldlemon"],
 "Answermark": ["answermark"],
 "Robin van Schaik": ["robin van schaik"],
 "GHO Agency": ["gho agency","gho","ghostwriting agency"],
 "WADM": ["wadm","wadm | b2b agency","wadm b2b agency"],
 "Novicom": ["novicom","novicom marketing group"],
 "Next Business Academy": ["next business academy","next business agency","nextbusinessacademy"],
 "Jan-Willem Alphenaar": ["jan-willem alphenaar","jan willem alphenaar"],
 "Sortlist": ["sortlist","sortlist.nl"],
 "Alsona": ["alsona"],
 "MarketingXperts": ["marketingxperts"],
 "Marketingburos": ["marketingburos","marketingburos.nl"],
 "Socialmediabeheerbureau.nl": ["socialmediabeheerbureau","socialmediabeheerbureau.nl"],
 "Social Media Bureau Utrecht": ["social media bureau utrecht","socialmedia-bureau-utrecht"],
 "Frank Husmann": ["frank husmann","frankhusmann"],
 "Wahine Marketing": ["wahine marketing","wahine"],
 "Lead Today": ["lead today","leadtoday"],
 "Make Marketing Magic": ["make marketing magic"],
 "Merkelijkheid": ["merkelijkheid"],
 "iReclam": ["ireclam"],
 "Endeavour": ["endeavour"],
 "Webnexus": ["webnexus"],
 "Afdeling Online": ["afdeling online","afdelingonline"],
 "Whello": ["whello"],
 "Searchlab": ["searchlab"],
 "Digital Inside": ["digital inside","digitalinside"],
 "Wildbos": ["wildbos"],
 "Fingerspitz": ["fingerspitz","fingerspritz"],
 "DISTRIKT": ["distrikt"],
 "Knackpunkt": ["knackpunkt"],
 "PMA Solutions": ["pma solutions","pma-solutions"],
 "Made2Reach": ["made2reach"],
 "Rene Schipper": ["rene schipper","rené schipper"],
 "Victor Huiting": ["victor huiting"],
 "Linkleads": ["linkleads"],
 "Sandra Stassar": ["sandra stassar","stassar branding & coaching","stassar"],
 "Anneke van der Voort": ["anneke van der voort"],
 "PRminded": ["prminded","pr-minded","pr minded"],
 "Roel Willemse": ["roel willemse"],
 "Virtuele Helden": ["virtuele helden","virtuelehelden"],
 "Dapper": ["dapper","dapper – the demand agency","dapper - the demand agency"],
 "Tasmanic": ["tasmanic"],
 "Unmuted": ["unmuted"],
 "Red Panda Works": ["red panda works"],
 "PostAds": ["postads"],
 "Key Agency": ["key agency"],
}
EXCLUDE = {"linkedin","google","chatgpt","perplexity","gemini","microsoft","meta","openai","sales navigator","linkedin sales navigator"}

EXTRA = {
 "doelgroepbereikt":"Doelgroep Bereikt","linqed":"Linqed","liekecrouwers":"Lieke Crouwel","postivai":"Postiv",
 "lagrowthmachine":"La Growth Machine","socialmediabeheerbureau":"Socialmediabeheerbureau.nl","youlynq":"YouLynq.me",
 "managementboek":"Managementboek","webprofit":"Webprofit","socialmediaburo":"Socialmediaburo.nl","gho":"GHO Agency",
 "ghostwritingagency":"GHO Agency","afassoftware":"AFAS","nextbusinessagency":"Next Business Academy",
}
import unicodedata
def _key(n):
    n = unicodedata.normalize("NFKD", n).encode("ascii","ignore").decode()
    n = n.lower()
    n = re.sub(r"\.(nl|com|io|me|agency|ai)$", "", n.strip())
    return re.sub(r"[^a-z0-9]", "", n)
DISPLAY = collections.defaultdict(collections.Counter)
def canon(name):
    n = name.strip().strip("*").strip()
    low = re.sub(r"\s+"," ", n.lower()); low = re.sub(r"[®™]","", low).strip()
    if low in EXCLUDE or _key(n) in {_key(x) for x in EXCLUDE}: return None
    for c, vs in ALIASES.items():
        if low == c.lower() or low in vs: return c
    k = _key(n)
    if k in EXTRA: return EXTRA[k]
    for c in ALIASES:
        if _key(c) == k: return c
    DISPLAY[k][n] += 1
    return "KEY:" + k

def display(c):
    if c.startswith("KEY:"):
        return DISPLAY[c[4:]].most_common(1)[0][0]
    return c

def load():
    rows = []
    for e in ENGINES:
        for f in sorted(glob.glob(os.path.join(BASE, e, "P*.json"))):
            try: d = json.load(open(f))
            except Exception as ex:
                print("BAD", f, ex, file=sys.stderr); continue
            d["engine"] = e
            rows.append(d)
    return rows

def main():
    rows = load()
    prompts = json.load(open(os.path.join(BASE,"prompts.json")))
    n_prompts = len(prompts)
    ok = [r for r in rows if r.get("status") == "ok" and r.get("answer_text")]
    per_engine_ok = collections.Counter(r["engine"] for r in ok)
    total_answers = len(ok)

    # entity stats
    stats = collections.defaultdict(lambda: {"mentions":0,"engines":set(),"positions":[],"citations":0,
                                             "types":collections.Counter(),"domains":collections.Counter(),
                                             "per_engine":collections.Counter(),"prompts":set(),"cats":collections.Counter()})
    domain_cites = collections.Counter()      # domain -> answers citing it
    domain_cites_engine = collections.defaultdict(collections.Counter)
    for r in ok:
        seen = set()
        # ranked list of canonical entities in this answer
        ents = []
        for ent in r.get("entities", []) or []:
            c = canon(ent.get("name",""))
            if not c or c in seen: continue
            seen.add(c); ents.append((c, ent))
        for pos, (c, ent) in enumerate(ents, start=1):
            s = stats[c]
            s["mentions"] += 1
            s["engines"].add(r["engine"]); s["per_engine"][r["engine"]] += 1
            s["positions"].append(pos)
            s["types"][ent.get("type") or "overig"] += 1
            if ent.get("domain"): s["domains"][ent["domain"].lower().replace("www.","")] += 1
            s["prompts"].add(r["id"]); s["cats"][r.get("cat","?")] += 1
        cited = set()
        for src in r.get("sources", []) or []:
            dom = (src.get("domain") or re.sub(r"^https?://(www\.)?","", src.get("url","")).split("/")[0]).lower().replace("www.","")
            if dom: cited.add(dom)
        for dom in cited:
            domain_cites[dom] += 1; domain_cites_engine[dom][r["engine"]] += 1
        r["_cited"] = cited

    # citations per entity = answers where the entity's own domain is cited
    ent_domain = {}
    for c, s in stats.items():
        dom = s["domains"].most_common(1)[0][0] if s["domains"] else None
        ent_domain[c] = dom
    for c, s in stats.items():
        dom = ent_domain[c]
        if not dom: continue
        s["citations"] = sum(1 for r in ok if any(d == dom or d.endswith("."+dom) for d in r["_cited"]))

    # score
    table = []
    for c, s in stats.items():
        share = s["mentions"] / total_answers
        cite_share = s["citations"] / total_answers
        avg_pos = sum(s["positions"]) / len(s["positions"])
        # positiegewogen aandeel: elke vermelding telt 1/positie, gedeeld door alle antwoorden
        pos_share = sum(1/p for p in s["positions"]) / total_answers
        cover = len(s["engines"])
        score = 100 * (0.60*share + 0.25*cite_share + 0.15*pos_share)
        table.append({
            "naam": display(c), "type": s["types"].most_common(1)[0][0], "domein": ent_domain[c],
            "vermeldingen": s["mentions"], "vermeldingsgraad": round(100*share,1),
            "citaties": s["citations"], "citatiegraad": round(100*cite_share,1),
            "gem_positie": round(avg_pos,1), "engines": cover,
            "per_engine": {LABEL[e]: s["per_engine"][e] for e in ENGINES},
            "categorieen": dict(s["cats"]),
            "score": round(score,1),
        })
    table.sort(key=lambda x: (-x["score"], -x["vermeldingen"], x["gem_positie"]))
    out = {
        "total_answers": total_answers, "per_engine_ok": dict(per_engine_ok), "n_prompts": n_prompts,
        "ranking": table,
        "top_cited_domains": [{"domein": d, "antwoorden": n, "per_engine": {LABEL[e]: domain_cites_engine[d][e] for e in ENGINES}} for d, n in domain_cites.most_common(40)],
    }
    json.dump(out, open(os.path.join(BASE,"result.json"),"w"), indent=1, ensure_ascii=False)
    print(f"answers ok: {total_answers} / {len(rows)}  per engine: {dict(per_engine_ok)}")
    print(f"{'#':>2} {'naam':32} {'type':9} {'verm':>4} {'%':>5} {'cit':>4} {'pos':>4} {'eng':>3} {'score':>5}  C/P/G/A")
    for i, t in enumerate(table[:30], 1):
        pe = t["per_engine"]
        print(f"{i:>2} {t['naam'][:32]:32} {t['type'][:9]:9} {t['vermeldingen']:>4} {t['vermeldingsgraad']:>5} {t['citaties']:>4} {t['gem_positie']:>4} {t['engines']:>3} {t['score']:>5}  {pe['ChatGPT']}/{pe['Perplexity']}/{pe['Gemini']}/{pe['Google AI Mode']}")
    print("\nTop cited domains:")
    for d in out["top_cited_domains"][:25]:
        print(f"  {d['domein']:35} {d['antwoorden']:>3}  {d['per_engine']}")
    for name in ["Gold Lemon","Answermark","Robin van Schaik"]:
        pos = next((i for i,t in enumerate(table,1) if t["naam"]==name), None)
        print(f"\n{name}: rank {pos}", next((t for t in table if t['naam']==name), "niet genoemd"))

if __name__ == "__main__":
    main()
