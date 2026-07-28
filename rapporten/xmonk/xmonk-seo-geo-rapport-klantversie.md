# SEO- en GEO-analyse — xmonk.nl

**Voor:** XMONK, Cruquius
**Opgesteld door:** Gold Lemon
**Datum:** 28 juli 2026
**Naar aanleiding van:** jullie aanvraag van 27 juli 2026

---

## 0. Verantwoording — lees dit eerst

Deze analyse is opgebouwd uit publieke bronnen en eigen DNS-metingen. Eén beperking bepaalt hoe je dit rapport moet lezen:

> **De website xmonk.nl kon niet direct worden opgevraagd.** Het netwerkbeleid van onze onderzoeksomgeving blokkeerde alle uitgaande HTTP-verzoeken — voor élk domein, niet specifiek voor die van jullie. Alle uitspraken over de inhoud en structuur van de site komen daarom uit zoekresultaten, titels en snippets, en niet uit het lezen van de pagina's zelf.

Wat daardoor **niet** gemeten is, staat in §11. Dat is geen bijzaak: laadsnelheid, schema-implementatie, robots.txt en interne linkstructuur zitten precies in dat gat. Die meten we in een vervolgstap zodra we toegang hebben.

Er staan in dit rapport bewust **geen zoekvolumes en geen ranking-posities**. Daarvoor is een betaalde datatool nodig (Ahrefs, Semrush of DataForSEO) die tijdens dit onderzoek niet beschikbaar was. We hebben ze niet geschat en niet ingevuld — een getal dat er zelfverzekerd uitziet maar nergens op steunt, maakt een rapport onbruikbaar.

### Betrouwbaarheidscodering

Elke bevinding heeft een label. Ze zijn niet gelijkwaardig.

| Label | Betekenis |
|---|---|
| **[GEMETEN]** | Zelf gemeten, reproduceerbaar. Hard. |
| **[ZOEK]** | Consistent teruggevonden in meerdere onafhankelijke zoekopdrachten. Betrouwbaar, niet op de bron zelf gecontroleerd. |
| **[AFGELEID]** | Redenering op basis van patronen. Plausibel, niet bewezen. |
| **[ONBEVESTIGD]** | Kwam één keer voorbij, of bronnen spreken elkaar tegen. Verifieer voordat je erop handelt. |

---

## 1. Samenvatting

De kern in één zin: **XMONK verkoopt SEO, maar de eigen vindbaarheid is nooit ingericht.** Dat is een veelvoorkomend patroon bij bureaus — betalende klanten gaan voor — maar de omvang van het gat is in dit geval groot en goed te dichten.

Vijf bevindingen, op volgorde van urgentie:

1. **Geen zichtbaarheid op de eigen dienstverlening.** In zestien zoekopdrachten op commerciële termen als "SEO bureau Haarlem", "online marketing bureau Haarlemmermeer" en "SEO bureau Hoofddorp" kwam xmonk.nl niet één keer naar voren. De site verschijnt alleen bij een zoekopdracht op de merknaam zelf. Ook bij "marketing bureau Cruquius" — het eigen dorp — is XMONK afwezig, terwijl andere bureaus uit Cruquius daar wél staan. [ZOEK]

2. **Geen aanwezigheid op vergelijkingsplatforms.** Niet op Sortlist, Clutch, DesignRush, Trustpilot of Trustoo. Juist die platforms bezetten het merendeel van de zoekresultaten bij "welk bureau moet ik kiezen"-vragen, en zijn precies het type bron waarop AI-assistenten hun aanbevelingen baseren. Dit is het grootste gat én het goedkoopst te dichten. [ZOEK]

3. **De merknaam botst in de zoekresultaten.** "XMONK" concurreert met een Indiaas leiderschapscoachingbedrijf (xMonks) en met xmonk.net, een domein met een lage vertrouwensscore bij ScamAdviser. Wie zoekt op "XMONK reviews" vindt eerder die twee dan jullie. Voor taalmodellen die entiteiten moeten herkennen is dat een reëel probleem. [ZOEK]

4. **Geen contentmotor.** Geen blog, geen kennisbank, geen cases, geen locatiepagina's. Ongeveer zeven vindbare pagina's in totaal. [ZOEK]

5. **Een defect in de e-mailauthenticatie.** Het DMARC-record van xmonk.nl bevat geen rapportageadres, waardoor er nul rapportages binnenkomen over wie er namens het domein mailt. Subdomeinen zijn onbeschermd. Dit is de enige bevinding die volledig zelf gemeten is, en het is met één DNS-wijziging te repareren. [GEMETEN]

**Over de opgegeven keywords:** "marketing", "seo" en "nieuwe website" zijn geen van drieën haalbaar of nuttig. §8 legt uit waarom en geeft een onderbouwde vervangende lijst van tien termen.

---

## 2. Wat er nu online staat

### Vindbare pagina's

Zeven pagina's kwamen consistent naar boven, met hun letterlijke title tags:

| URL | Title tag |
|---|---|
| `/` | SEO, SEA, Social Media En De Beste User Experience \| XMONK |
| `/seo/` | Voor Optimale Vindbaarheid En Beste User Experience \| SEO |
| `/sea/` | Online Advertising \| XMONK |
| `/display-advertising/` | Display Advertising \| XMONK |
| `/digital-signage/` | Digital Signage High End Videoschermen \| XMONK |
| `/social-media/` | Social Media \| XMONK |
| `/contact/` | Contact \| XMONK |
| `/testimonial/leendert-van-pommeren-4/` | Leendert Van Pommeren \| XMONK |

Wat daaraan opvalt:

- **Geen enkele title tag bevat een plaatsnaam.** Geen Haarlem, geen Haarlemmermeer, geen Hoofddorp. Voor een bureau dat lokale MKB-klanten bedient is dit het meest elementaire gemis dat er is. [ZOEK]
- **De SEO-pagina heeft "SEO bureau" niet in de titel.** Die begint met "Voor Optimale Vindbaarheid" — een merkzin. De pagina die op SEO-termen moet ranken geeft de zoekmachine als eerste signaal iets anders. [ZOEK]
- **De titelconventie is inconsistent.** Meestal "[Onderwerp] | XMONK", maar bij `/seo/` staat het merk niet achteraan. [ZOEK]
- **Geen blog, over-ons, cases, vacatures of prijzen** in ongeveer tien gerichte zoekopdrachten. Dat bewijst niet dat ze niet bestaan, maar wel dat ze niet vindbaar zijn — en voor zoekmachines is dat hetzelfde. [ZOEK]
- Dezelfde merkzinnen ("met onstuitbare energie", "passie en ambitie") komen terug op meerdere dienstpagina's, wat wijst op een gedeelde template-intro in plaats van per pagina geschreven copy. [AFGELEID]

**Twee punten om zelf te controleren:**

- De testimonial-URL eindigt op `-4`, wat in WordPress meestal duidt op meerdere pagina's met dezelfde titel. In één zoekresultaat kwam de inhoud van die pagina terug als "Lorem ipsum". Als dat live staat, is het in vijf minuten opgelost — maar het is het controleren waard. [ONBEVESTIGD]
- Wij vinden **geen LinkedIn-bedrijfspagina** voor XMONK, alleen persoonlijke profielen. Voor een B2B-bureau is dat een gat dat in een middag te dichten is. [ZOEK]

### Bedrijfsgegevens

Twee correcties op wat online circuleert:

- **De postcode.** Onafhankelijke kadaster- en postcodebronnen (postcode.nl, kadastralekaart.com, planviewer.nl) geven consistent **2142 EX** voor Crommelinbaan 29 in Cruquius. Als er ergens 2134 EX staat in vermeldingen of profielen, klopt dat niet — en consistente adresgegevens over alle platforms zijn juist voor lokale SEO belangrijk. [ZOEK]
- **Het KvK-nummer.** Er circuleert een nummer in AI-gegenereerde zoeksamenvattingen dat wij in geen enkel register aan XMONK gekoppeld konden vinden. Het staat daarom niet in dit rapport. Controleer welk nummer er in jullie vermeldingen staat.

---

## 3. Zichtbaarheid op commerciële zoektermen

Zestien commerciële zoekopdrachten uitgevoerd op de diensten die XMONK verkoopt. **Bij geen enkele verscheen xmonk.nl.** [ZOEK]

| Zoekterm | Wie er wél verscheen | XMONK |
|---|---|---|
| SEO bureau Haarlem | Hulc, SAM Online Marketing, ROXTAR, Ranking Masters, LYNX Media (Cruquius), Versgeplukt, httpmarketing, mpowerDigital | afwezig |
| SEO bureau Hoofddorp | SAM Online Marketing, Online Ambition, Your Salespoint, Connect Your World, SEO Capital, mpowerDigital | afwezig |
| online marketing bureau Haarlem | Trustoo, Sortlist, One Media, MADE Marketing, The Success Agency | afwezig |
| online marketing bureau Haarlemmermeer | Trustoo, DigiSwift, The Success Agency, Reward, Fortune Agency, Scoob | afwezig |
| marketing bureau Cruquius | Trustoo, marketing-bureaus.nl, DesignRush, reclamebureausgids.nl, MADE Marketing | afwezig |
| SEA bureau Haarlem | Onlinemeersucces, Shoptimalisatie, Digital Wizards, C-Corner, Vitenda, mpowerDigital | afwezig |
| digital signage leverancier Nederland | Samsung, eventplanner.nl, Dustin, Signtifix, Adaptable, Viewie Media | afwezig |
| nieuwe website laten maken Haarlem | VrijdagOnline, Chuck's Webdesign, Webaware, Projectie, MADE Marketing, C-Corner | afwezig |

Twee zaken die opvallen:

**Geen zichtbaarheid in het eigen dorp.** Bij "marketing bureau Cruquius" verschijnen Fortune Agency, OOSEOO en STOOP marketing — grotendeels via directories. Cruquius is klein; als je daar niet vindbaar bent, ben je nergens vindbaar.

**Er zit een concurrent in Cruquius die niet op jullie lijst stond.** LYNX Media (lynx-media.nl), eveneens Cruquius, verschijnt wél bij "SEO bureau Haarlem" en heeft een pagina voor "website laten maken". Dat is geografisch de meest directe concurrent die er bestaat. [ZOEK]

**Nuance over de methode.** Het gebruikte zoekhulpmiddel is een algemene web-search-API, geen letterlijke Google.nl-SERP-scraper. De genoemde volgorde geeft concurrentiedichtheid aan, geen geverifieerde ranking-positie. Dat xmonk.nl in zestien onafhankelijke zoekopdrachten nul keer verschijnt is een sterk signaal, maar voor harde posities per keyword is een rank tracker nodig. Dat is de eerste vervolgmeting die we adviseren.

---

## 4. Vergelijkingsplatforms — het grootste gat

Bij zoekopdrachten met keuze-intentie — "beste online marketing bureau Haarlem", "welk marketing bureau moet ik kiezen", "top 10 marketing bureaus Noord-Holland" — worden de resultaten niet gedomineerd door bureaus, maar door **vergelijkingssites en lijstjes**. Over elf onderzochte zoekopdrachten bezetten directories en listicles ruwweg 55–70% van de zichtbare posities. Bij brede vergelijkingsvragen liep dat op naar bijna 100%: bij "top 10 marketing bureaus Noord-Holland" bestond de volledige resultatenpagina uit Sortlist-categoriepagina's. [ZOEK]

| Platform | Verschijnt bij | XMONK aanwezig? |
|---|---|---|
| **trustoo.nl** | 6+ zoekopdrachten, vaak positie 1; heeft per-plaats top-10-pagina's, inclusief Cruquius | **nee** |
| **sortlist.nl / .com** | 5 zoekopdrachten, soms de volledige pagina | **nee** |
| **agencies.semrush.com** | domineerde de Engelstalige variant met 6 van 9 posities | **nee** |
| **designrush.com** | Cruquius-zoekopdracht en concurrentprofielen | **nee** |
| **clutch.co** | agency-vergelijkingen | **nee** |
| **trustpilot.com** | reviews | **nee** |

Ter illustratie van de omvang: Trustoo heeft een pagina met "10 online marketing bureaus in Cruquius", gemiddelde score 9,9. XMONK staat daar niet tussen. Fortune Agency — eveneens uit Cruquius — staat er wél op én heeft een DesignRush-profiel met geciteerde klantquotes. [ZOEK]

**Waarom dit dubbel weegt.** Deze platforms leveren niet alleen organisch verkeer. Ze zijn precies het soort bron waarop een taalmodel terugvalt bij een "welk bureau moet ik kiezen"-vraag: content van derden, gedekt door reviews, en al gesynthetiseerd tot exact het antwoord dat de gebruiker zoekt. Een bureau dat op geen enkel vergelijkingsplatform staat, is structureel onzichtbaar op het moment dat de klant kiest — voor mensen én voor AI.

Aanvullend: er is geen Wikipedia-artikel, geen Wikidata-entiteit, geen persdekking en geen aantoonbare merkvermelding buiten de eigen site gevonden. [ZOEK] Een Google Bedrijfsprofiel met reviews kwam evenmin naar boven, maar dat is geen bewijs van afwezigheid — Google Maps-content verschijnt vaak niet in gewone webzoekresultaten. Dit moet direct in Maps gecontroleerd worden.

---

## 5. Het merknaamconflict

Zoek op "XMONK reviews", "XMONK ervaringen" of "XMONK marketing bureau" en er verschijnen overwegend twee andere entiteiten: [ZOEK]

1. **xMonks** (xmonks.com, xmonks.club) — een Indiaas coaching- en leiderschapsontwikkelingsbedrijf met een aanzienlijke voetafdruk: eigen site, Instagram, LinkedIn, ZoomInfo, podcast.
2. **xmonk.net** — een ongerelateerd domein dat door ScamAdviser, ScamDoc en WOT is gemarkeerd met een matige vertrouwensscore en verborgen Whois-eigenaar.

xmonk.nl verschijnt slechts één keer, laag in de resultaten. Er is geen enkele review- of profielpagina van derden die naar boven komt.

**Waarom dit meer is dan een ongelukje.** Taalmodellen werken met entiteiten. Als de naam "XMONK" in zowel trainingsdata als live zoekindexen vooral gekoppeld is aan een Indiaas coachingbedrijf en aan een domein met een vertrouwenswaarschuwing, kan een AI-assistent XMONK niet betrouwbaar herkennen als online marketingbureau in de regio Haarlem — en in het slechtste geval koppelt hij de verkeerde informatie aan de naam.

De oplossing is niet de naam veranderen, maar het merk stevig **verankeren aan onderscheidende attributen**: consistente naam-, adres- en telefoongegevens over alle platforms, `Organization`- en `LocalBusiness`-schema met `sameAs`-verwijzingen naar de eigen profielen, en vermeldingen op Nederlandse platforms die de combinatie XMONK + Cruquius/Haarlemmermeer + online marketing steeds opnieuw bevestigen.

---

## 6. Technische infrastructuur

Dit is het enige deel van het onderzoek dat volledig zelf gemeten is, met directe DNS-queries op 28 juli 2026. Deze gegevens zijn hard en reproduceerbaar. [GEMETEN]

### Hosting

| Item | Waarde | Beoordeling |
|---|---|---|
| A-record xmonk.nl / www | 45.152.250.14 (beide) | in orde |
| Reverse DNS | s1146.hostingsecure.com | **shared hosting** |
| Nameservers | ns1.hoasted.nl, ns2.hoasted.eu, ns3.hoasted.com | in orde |
| CDN | geen | verbeterpunt |
| IPv6 (AAAA) | ontbreekt | klein verbeterpunt |
| CAA-record | ontbreekt | klein verbeterpunt |
| `mail.xmonk.nl` | wijst naar de webserver terwijl de MX naar Microsoft 365 gaat | verouderd record, opruimen |

De reverse DNS verraadt een genummerde shared-hostingserver: gedeelde resources, geen controle over de buren, direct van invloed op laadtijden. Zonder CDN wordt elke bezoeker vanaf één Nederlandse server bediend. Voor een lokaal bureau met Nederlandse klanten is dat verdedigbaar, maar in combinatie met shared hosting is dit de eerste plek om te kijken als de Core Web Vitals tegenvallen.

### E-mailauthenticatie

```
MX     0 xmonk-nl.mail.protection.outlook.com          → Microsoft 365
SPF    v=spf1 include:spf.protection.outlook.com
              include:_spf.hostnet.nl
              include:_spf.mijnwefact.nl
              include:spf.myfasthosting.com
              ip4:145.239.216.145 ~all
DMARC  v=DMARC1; p=quarantine; sp=none; adkim=r; aspf=r;
       pct=100; fo=0; rf=afrf; ri=86400
DKIM   default-selector aanwezig, 2048-bit RSA
```

Drie concrete problemen:

1. **Het DMARC-record heeft geen `rua=`.** Er is geen rapportageadres geconfigureerd, dus jullie ontvangen **nul** aggregatierapporten. Er is geen zicht op wie er namens xmonk.nl mailt, of de eigen mail correct authenticeert, of dat iemand het domein misbruikt. Eén regel om toe te voegen, direct effect.
2. **`sp=none`.** Het hoofddomein staat op `quarantine`, maar subdomeinen hebben géén beleid. Dat is precies het gat dat bij domeinspoofing wordt gebruikt: `mail.xmonk.nl` of `facturen.xmonk.nl` is volledig onbeschermd.
3. **SPF eindigt op `~all` (softfail) met vier includes.** Vier includes plus een los IP brengt het record in de buurt van de DNS-lookuplimiet van tien, en `~all` betekent dat niet-geautoriseerde afzenders alleen worden gemarkeerd, niet geweigerd. De aanwezigheid van facturatiesoftware en twee verschillende hostingpartijen in het record wijst op historisch gegroeide configuratie die nooit is opgeruimd.

Dit beïnvloedt geen rankings. Het staat in dit rapport omdat het de bezorgbaarheid van jullie eigen e-mail raakt, en omdat het binnen een uur te repareren is.

---

## 7. Concurrentieanalyse

Jullie noemden twee concurrenten. Beide zijn onderzocht, plus twee die niet genoemd werden maar geografisch dichterbij zitten.

### Ad Your Service B.V. — adyourservice.nl

Amsterdam-West, opgericht 2017, 8–10 personen. Full-service positionering, klanten als Prinses Máxima Centrum, OppoSuits, Levi9 en Little Label. [ZOEK]

*(Let op: er bestaat een ongerelateerde Belgische entiteit "AD Your Service SRL" in Antwerpen — niet dezelfde partij.)*

**Sterker dan XMONK op:** een breder dienstenpakket (e-mailmarketing, marketplaces, cursussen en workshops, huisstijl, online recruitment); een actieve, technisch georiënteerde blog (SEO-tools, GA4, PageSpeed, Google Ads-extensies, met minstens één post uit 2026); en een sterk onafhankelijk reputatiebewijs — vermelding in de **FONK150** met een klanttevredenheidsscore van **9,22**, beschreven als top-5 in hun categorie.

**Zwakker:** geen zichtbaar programma van lokale landingspagina's, en hun title tags bevatten de merknaam dubbel ("… | ad your service adyourservice").

**Relevante opening:** Ad Your Service heeft **niets** gepubliceerd over GEO of AI-zoekvindbaarheid. Hun AI-content is algemeen van aard. Op dat vlak staan jullie gelijk — daar valt een positie te pakken. [ZOEK]

### Blauwe Monsters — blauwemonsters.nl

Dit is de zwaarste concurrent van de twee, en op twee punten waarschijnlijk zwaarder dan jullie denken.

| Gegeven | Waarde |
|---|---|
| Opgericht | 2012, gegroeid uit de eigen webshop HemdVoorHem.nl |
| **Locatie** | **Jan van Krimpenweg 7, 2031 CE Haarlem** — verhuisd van Hoofddorp naar Haarlem in juli 2022 |
| Eigendom | overgenomen door **4NG** (onderdeel van **Conclusion**) in juli/augustus 2023 |
| Team | 44 bij overname, "50+" in latere eigen content |
| Klanten | 300+, B2C en B2B |
| Specialisatie | e-commerce en performance marketing; SEO, SEA, CRO, content, e-mail, social ads, marketplaces, server-side tagging |

De twee punten: **ze zitten sinds juli 2022 in Haarlem zelf**, niet meer in Hoofddorp, en **sinds 2023 zitten ze in 4NG/Conclusion** — een groep die na de overname doorgroeide naar elf labels en circa 460 medewerkers. De concurrentie komt dus niet van een bureau van vijftig mensen, maar van een bureau van vijftig mensen met concernbudget erachter. [ZOEK]

**Hun contentpositie:**

- **Locatiepagina's op schaal**: `/seo-bureau/[stad]/` en `/seo/[stad]/` voor meerdere steden.
- **Een wiki/glossarium**: `/wiki/[categorie]/[term]/` met tientallen definitiepagina's (featured snippet, orphan page, paginering, geotargeting, call-to-action). Precies het formaat dat AI-antwoordmachines graag citeren.
- **Cases met harde cijfers**: "+300 non-branded keywords in top-3", "48% meer top-3-rankings", "148% meer e-mailtransacties".
- **Een actieve blog** met recente, gedateerde posts.
- **Een lopend GEO-programma**: minstens vijf artikelen, waaronder "Van SEO naar GEO: Zo speel je in op AI Overviews en AI mode" en "Bing introduceert AI Performance: data voor GEO". [ZOEK]

Dat laatste betekent: op het thema "klaar voor AI-zoeken" hebben zij een voorsprong. Post-voor-post nadoen volstaat niet; er is inhoudelijk iets beters nodig. §10 beschrijft wat dat zou kunnen zijn.

**Zwakke plekken:** de twee parallelle URL-structuren voor locatiepagina's wijzen op technische schuld uit een migratie, en hun Sortlist-profiel lijkt uit het Hoofddorp-tijdperk te stammen en sinds de overname niet bijgewerkt. [ONBEVESTIGD]

### Twee concurrenten uit het eigen dorp

**LYNX Media (lynx-media.nl), Cruquius.** Verschijnt bij "SEO bureau Haarlem" en heeft een pagina voor "website laten maken". Geografisch de meest directe concurrent die bestaat. [ZOEK]

**Fortune Agency (fortuneagency.nl), Cruquius.** Staat op Trustoo (score 9,9, top-10 webdesigners Cruquius) én op DesignRush met geciteerde klantquotes. Het bewijs dat een bureau van vergelijkbare omvang uit hetzelfde dorp die platformaanwezigheid wél voor elkaar krijgt. [ZOEK]

### Vergelijking

| Dimensie | XMONK | Ad Your Service | Blauwe Monsters |
|---|---|---|---|
| Team | klein | 8–10 | 50+ (concern: ~460) |
| Vindbare pagina's | ~7 | tientallen | honderden |
| Blog | **geen** | actief | actief |
| Kennisbank/wiki | **geen** | geen | **ja** |
| Locatiepagina's | **geen** | geen | **ja** |
| Cases met cijfers | **geen** | klantnamen | **ja** |
| Onafhankelijk reputatiebewijs | **geen** | **FONK150, 9,22** | Feedback Company |
| Directoryprofielen | **geen** | Sortlist | Sortlist |
| GEO/AI-content | **geen** | **geen** | **5+ artikelen** |
| Nabijheid tot Haarlem | Cruquius | Amsterdam | **Haarlem zelf** |

---

## 8. Keywordanalyse

### De drie opgegeven termen

Jullie gaven "marketing", "seo" en "nieuwe website" op. Alle drie adviseren wij te laten vallen. De onderbouwing:

**"marketing" — niet haalbaar, en zou niet converteren.** De resultaten worden bezet door Wikipedia, Coursera, Salesforce en de American Marketing Association. Puur informationeel: studenten en nieuwsgierigen, geen kopers. Zelfs in het onwaarschijnlijke geval dat XMONK er zou ranken, wil die bezoeker een definitie, geen offerte. [ZOEK]

**"seo" — hetzelfde probleem, scherper.** Concurrentie: Google's eigen Search Central-documentatie, Search Engine Land, universiteiten. In de Nederlandse resultaten zijn dit soort posities eigendom van Frankwatching, Marketingfacts en de grote landelijke toolmerken. Een meerjarig autoriteitsspel voor partijen met een aanzienlijk groter budget. [ZOEK]

**"nieuwe website" — zwak, en niet wat kopers typen.** Twee exact-match generieke domeinen (nieuwewebsite.nl, nieuwe-website.com) bezetten deze term landelijk. Belangrijker: wie klaar is om een website te laten bouwen typt **"website laten maken"**, niet "nieuwe website". Zwakkere koopintentie én een moeilijker veld. [ZOEK]

### De tien aanbevolen termen

Geselecteerd uit een onderzochte lijst van 34. De concurrentiebeoordeling komt uit wie er daadwerkelijk in de zoekresultaten verscheen. Nogmaals: **geen enkel zoekvolume in dit rapport is een meting.**

| # | Zoekterm | Intentie | Wat er nodig is | Concurrentie |
|---|---|---|---|---|
| 1 | online marketing bureau Haarlem | commercieel, lokaal | eigen landingspagina, niet de homepage | matig: Digital Wizards, One Media, Reward, MADE Marketing |
| 2 | SEO bureau Haarlemmermeer | commercieel, thuisbasis | locatiepagina met transparante prijzen | matig: Ralf van Veen, C-Corner, HTTP Marketing, Bureau Bijma |
| 3 | SEO specialist Haarlem | commercieel, zoekt een persoon | bio-pagina met naam en credentials | **dun** — veel ruis van vacatures |
| 4 | Google Ads bureau Hoofddorp | commercieel, hoge koopintentie | aparte SEA-pagina voor Hoofddorp | matig: Online Meer Succes, Stijgt, Connect Your World, Smoop |
| 5 | social media bureau Haarlem | commercieel, dienstspecifiek | dienstpagina met lokale cases | **dun**: Social Sparrow, Blitskikker, Endeavour Heroes |
| 6 | website laten maken Haarlemmermeer | commercieel, lokaal + dienst | portfolio-gedreven landingspagina | matig, en LYNX Media uit Cruquius zit hier |
| 7 | marketingbureau Amstelveen | commercieel, koopkrachtige regio | locatiepagina, lagere prioriteit | **zwaar** — één directory noemt 65 bureaus |
| 8 | digital signage bureau | commercieel, B2B, landelijk | dienstpagina met de creatieve invalshoek | zie hieronder |
| 9 | digitale reclameborden winkel | commercieel, retail-niche | landingspagina + leadmagneet | hardware-resellers: VEBO, Display4all, Q-lite |
| 10 | wat kost SEO per maand | informationeel, top of funnel | blogartikel met prijstabel en FAQ | matig: Whello, Opklopper, Go Online |

**Nummers 8 en 9 zijn de strategische kans.** Bij "digital signage" verschijnen vooral hardwareleveranciers en softwareplatformen (Samsung, First Impression, ZetaDisplay, Viewie Media). Er zijn twee échte regionale concurrenten die full-service narrowcasting verkopen: **DooH Solutions & Services** (Haarlemmermeer) en **UW-S** (Haarlem). Maar **geen enkele partij in dit veld positioneert zich als marketingbureau dat óók de contentstrategie voor het scherm doet.** Campagnedenken plus het scherm is een verdedigbare positie, en die dienst is al in huis. [ZOEK]

**Nummer 10 is de GEO-instap.** "Wat kost SEO per maand" heeft geen Wikipedia-probleem, wordt bezet door middelgrote bureaublogs, en het antwoordformaat — korte directe prijsindicatie, prijstabel, FAQ — is precies wat AI Overviews en chatassistenten oplichten.

**Marktcontext voor prijstransparantie:** Nederlandse bronnen noemen voor MKB-SEO ruwweg €500–€1.500 per maand, met een bredere range van €250 tot €3.500, uurtarieven van €50–€150 en tien tot twintig uur per maand. Meerdere directe concurrenten in de regio publiceren hun prijzen openlijk (Ralf van Veen vanaf €1.000/maand, Marketingbureau Hoofddorp vanaf €250/maand). Prijzen verzwijgen is in deze markt dus eerder een nadeel dan bescherming. [ZOEK]

### Advies

Laat "marketing" en "seo" volledig vallen. Vervang "nieuwe website" door "website laten maken Haarlemmermeer". Val de kale landelijke term "website laten maken" niet frontaal aan — die wordt bezet door grote pure-play webbouwers met jaren SEO-investering.

---

## 9. GEO — wat werkt, en wat niet

Dit hoofdstuk is bewust sceptisch geschreven. Een groot deel van wat er over AI-zichtbaarheid wordt gepubliceerd komt van bureaus en toolleveranciers met commercieel belang bij urgentie, en dezelfde precies klinkende percentages duiken op tientallen bijna identieke blogs op zonder methodologie of steekproefgrootte. Wat hieronder staat is gesorteerd op bewijskracht.

### Wat GEO wel en niet is

Google's eigen standpunt is dat optimaliseren voor AI-functies **nog steeds SEO is**: dezelfde crawlbaarheid, contentkwaliteit en E-E-A-T. De praktijk is genuanceerder: klassieke ranking-signalen correleren zwakker met AI-citaties dan off-site merksignalen. Goede SEO is dus een **vloer, niet het hele spel**.

De hardste cijfers die er zijn, uit een Ahrefs-analyse van **75.000 merken**: merkvermeldingen op het web correleren met zichtbaarheid in AI Overviews op **r = 0,664**, tegenover **r = 0,218 voor backlinks** — ongeveer drie keer zo sterk. Een leveranciersstudie, geen peer-reviewed onderzoek, maar mét openbaar gemaakte steekproefgrootte, en daarmee beter onderbouwd dan bijna al het andere in dit veld.

Wat je **niet** moet geloven: de veelgeciteerde bewering dat de overlap tussen Google's top 10 en AI-geciteerde bronnen "van 70% naar onder 20%" is gedaald. Geen enkele bron levert daar een dataset bij.

### Hoe de antwoordmachines werken

| Platform | Ophaalmechanisme | Wat dat betekent |
|---|---|---|
| **Google AI Overviews / AI Mode** | Google's eigen index. "Query fan-out": splitst één vraag in 8–12 subvragen en haalt op passage-niveau op | Gewone Google-indexatie is de toegangspoort. Optimaliseer op passage-niveau |
| **ChatGPT Search** | Bing-index, niet Google | Bing Webmaster Tools met sitemap en IndexNow is een randvoorwaarde — wordt vrijwel altijd vergeten |
| **Perplexity** | Eigen crawler plus live RAG. **Voert JavaScript niet betrouwbaar uit** | Kritieke content server-side renderen |
| **Claude** | Routeert websearch via de Brave Search API, sinds mei 2026 aangevuld met een vector-database | Zichtbaarheid in een niet-Google-index doet mee. [ONBEVESTIGD] |
| **Microsoft Copilot** | Bing-index. Sinds februari 2026 blokkeert `NOARCHIVE` citatie volledig | Controleer of er ergens `NOARCHIVE` staat. [ONBEVESTIGD] |
| **Gemini** | "Grounding with Google Search" | Zelfde poort als Google Search |

### Crawler-toegang — hier gaat het het vaakst mis

Elke aanbieder heeft nu **gescheiden bots** voor training, indexering en live ophalen. De verkeerde blokkeren vernietigt je AI-zichtbaarheid zonder dat je klassieke rankings iets laten zien.

| Aanbieder | Training (blokkeren kost geen zichtbaarheid) | Indexering (**nooit blokkeren**) | Live ophalen (**nooit blokkeren**) |
|---|---|---|---|
| OpenAI | `GPTBot` | `OAI-SearchBot` | `ChatGPT-User` |
| Anthropic | `ClaudeBot` | `Claude-SearchBot` | `Claude-User` |
| Perplexity | — | `PerplexityBot` | `Perplexity-User` |
| Google | `Google-Extended` (beleidstoken, géén crawler) | `Googlebot` | — |
| Microsoft | — | `Bingbot` | — |
| Apple | `Applebot-Extended` | `Applebot` | — |

Twee valkuilen:

1. **`Googlebot` blokkeren in de veronderstelling dat het "de AI-bot" is.** Dat sloopt de gewone SEO onmiddellijk. AI Overviews draaien op dezelfde Googlebot-index als organisch; er is momenteel geen manier om wél in Google Search te staan maar niet in AI Overviews.
2. **Een brede `Disallow` die ook `OAI-SearchBot`, `Claude-SearchBot` of `PerplexityBot` raakt.** Dat verwijdert een merk uit een hele categorie AI-vindbaarheid **zonder dat de klassieke rankings veranderen** — de schade is dus onzichtbaar in normale SEO-monitoring.

Advies: alle index- en ophaalbots toestaan. Of je trainingsbots blokkeert is een bewuste bedrijfs- en IP-afweging, geen ongeluk in een robots.txt.

### llms.txt — geen werkende hefboom

Kort: **llms.txt is geen hefboom en zou niet als AI-optimalisatiewerk verkocht moeten worden.**

- Google heeft het expliciet afgewezen. Gary Illyes zei dat Google het niet ondersteunt en dat niet van plan is; John Mueller vergeleek het met de achterhaalde keywords-metatag.
- Geen enkele grote aanbieder heeft publiek toegezegd het in productie te lezen.
- Een SE Ranking-onderzoek onder 300.000 domeinen vond ~10,1% adoptie; een analyse van meer dan 500 miljoen AI-botbezoeken vond **408** hits die specifiek op een llms.txt-bestand gericht waren.

Het kost bijna niets om toe te voegen, en er is een echte use case — documentatiesites waarvan de doelgroep AI-codeeragents zijn. Voor een marketingbureausite is dat niet de situatie.

### Schema.org — hygiëne, geen truc

Google's officiële standpunt: er is **geen speciale structured data nodig** voor AI Overviews of AI Mode. Geen enkele bron heeft een causaal effect van schema op LLM-citaties geïsoleerd — taalmodellen verwerken getokeniseerde tekst, er zit geen schema-parser in het model. Waar schema wél helpt is bij crawlen en indexeren: correcte entiteitsherkenning in de indexen waar de AI-pijplijnen bovenop zitten. Voor XMONK is dat gezien §5 juist relevant.

**Een harde deadline:** Google is per **7 mei 2026** gestopt met FAQ-rich-results. Het FAQ-filter, het Search Console-rapport en de Rich Results Test-ondersteuning verdwijnen in juni 2026, de API-data in augustus 2026. `FAQPage` blijft een geldig schema.org-type en mag blijven staan — het levert alleen geen zichtbaar SERP-resultaat meer op.

Wel implementeren, als hygiëne: `Organization` en `LocalBusiness` (met `address`, `geo`, `openingHoursSpecification` en `sameAs`), `Person` voor auteursbio's, en `Article` en `BreadcrumbList` als standaard.

### Contentpatronen — het enige met echt onderzoek erachter

Het fundament is één paper: **GEO: Generative Engine Optimization**, KDD 2024, van Princeton, Georgia Tech, het Allen Institute en IIT Delhi.

| Ingreep | Effect op zichtbaarheid |
|---|---|
| **Statistieken toevoegen** | **+41%** |
| **Citaten toevoegen** | **+28%** |
| **Externe bronnen aanhalen** | **+115%**, geconcentreerd bij zwakker presterende content |

Dit zijn de enige methodologisch onderbouwde cijfers in het vakgebied. Er is **geen onafhankelijke replicatie uit 2025 of 2026 gevonden**, ondanks expliciet zoeken. Alles wat zich voordoet als "nieuw GEO-onderzoek uit 2026" bleek hetzelfde paper te herhalen.

De structurele adviezen — antwoord in de eerste 40–60 woorden, vraagvormige tussenkoppen, blokken van 100–300 woorden, opeenvolgende koppenhiërarchie — zijn plausibel en kosten niets, maar élk specifiek getal dat erbij wordt geleverd komt uit blogs zonder onderliggend onderzoek. Doe het wel, verwacht geen gegarandeerde percentages.

### Off-site: waar de winst zit

Prioriteitsvolgorde op basis van bewijskracht — en gunstig, want de goedkoopste actie is ook de meest effectieve:

1. **Reviews en profielen op vergelijkingsplatforms**: Sortlist, Clutch, Trustoo, Trustpilot, Google Bedrijfsprofiel. Een G2-analyse van meer dan 10.000 zoekopdrachten vond dat merken die actief zijn op reviewplatforms ongeveer drie keer hogere ChatGPT-citatiepercentages halen.
2. **Opgenomen worden in "beste bureaus"-lijstjes.** Een taalmodel behandelt een lijstje van derden als een **al gesynthetiseerd antwoord** op precies de vraag die de gebruiker stelt. Eén zelfgepubliceerde pagina kan dat niet nabootsen.
3. **Merkvermeldingen boven links** — zie de Ahrefs-correlatie hierboven.
4. **Wikipedia en Wikidata**, mits de notabiliteit dat toelaat. Op dit moment vermoedelijk nog niet aan de orde.
5. **UGC-platforms.** Reddit en YouTube presteren in AI-citaties ver boven hun klassieke autoriteit.

### Meten

- **GA4 heeft sinds 13 mei 2026 een native "AI Assistant"-kanaal** (medium `ai-assistant`), breed beschikbaar rond 7 juni 2026. Herkent ChatGPT, Gemini, Claude, Deepseek, Copilot en Grok. **Twee vangnetten:** Perplexity zit er níet in en valt door naar Referral, en de wijziging is **niet retroactief**. Bouw dus alsnog een eigen Channel Group met een regex op `chatgpt\.com|chat\.openai\.com|gemini\.google\.com|claude\.ai|perplexity\.ai|copilot\.microsoft\.com`, bóven de standaard Referral-regel.
- **Search Console heeft sinds 3 juni 2026 een generative-AI-rapport**, met impressies, pagina's, landen, apparaten en datums — **maar geen clicks, geen CTR en geen zoektermen.** [ONBEVESTIGD op de exacte uitrol per land]
- **Handmatig meten** is het startpunt. De werkbare eenheid is de **prompt-run**: één antwoord, van één engine, op één prompt, op één moment, in één taal. Begin met 15–30 prompts verdeeld over merk-, categorie-, vergelijkings- en probleemvragen, met **minimaal 3 runs per prompt** — LLM-antwoorden variëren tussen runs, anders dan een Google-ranking.

### Marktcontext

- Pew Research: gebruikers klikken door bij **8%** van de zoekopdrachten met een AI Overview, tegen **15%** zonder.
- De zero-click-ratio in de VS lag in de eerste vier maanden van 2026 op **68,01%**, tegen 60,45% in 2024.
- AI Overviews verschijnen bij meer dan 20% van alle zoekopdrachten.
- **De conversiecijfers voor AI-verkeer zijn onbruikbaar.** Bronnen noemen 4,4x, 23x, "15,9% conversie" — onderling onverenigbaar en zonder controleerbare dataset. Wat wél consistent is: AI-referralverkeer is nog **minder dan 1% van het totale webverkeer**. Het eerlijke verhaal is "klein volume, waarschijnlijk hogere kwaliteit" — zonder multiplier.

### Wat de markt zelf niet weet

1. **Of GEO een echt vak is of herverpakte SEO** is een levend debat. Digiday en CXL publiceerden expliciete "is dit hype"-stukken.
2. **Of schema causaal effect heeft op LLM-citaties** — niemand heeft dat geïsoleerd van het feit dat betere teams ook betere content schrijven.
3. **Nederlandstalig AI-zoeken is nagenoeg onbestudeerd.** Het KDD-paper en alle retrieval-onderzoeken zijn op Engelstalige corpora gedaan. Of die +41% en +28% ook in het Nederlands gelden is **niet getest**.

---

## 10. Roadmap

### Fase 0 — quick wins, eerste twee weken

1. **DMARC repareren:** `rua=`-rapportageadres toevoegen, `sp=quarantine` instellen.
2. **SPF opruimen:** includes terugbrengen tot wat werkelijk gebruikt wordt, richting `-all`, verouderd `mail.xmonk.nl`-record verwijderen.
3. **robots.txt controleren** op de crawler-val uit §9, en op `NOARCHIVE`.
4. **Profielen aanmaken** op Trustoo, Sortlist, Clutch en Google Bedrijfsprofiel, met identieke naam-, adres- en telefoongegevens. De laagst hangende vrucht in dit hele rapport: dicht het gat uit §4 én levert het entiteitssignaal uit §5.
5. **LinkedIn-bedrijfspagina** aanmaken of claimen.
6. **Testimonial-pagina controleren** op placeholder-inhoud.
7. **Title tags herschrijven** met plaatsnamen, te beginnen bij `/seo/` en de homepage.
8. **Bing Webmaster Tools** inrichten met sitemap en IndexNow — de toegangspoort voor ChatGPT en Copilot.

### Fase 1 — fundament, maand 1 tot 3

- Volledige technische audit met directe sitetoegang (zie §11).
- `Organization`- en `LocalBusiness`-schema met `sameAs`, gericht op het entiteitsconflict.
- Vier locatiepagina's voor de termen 1, 2, 4 en 6 uit §8. Aparte URL's met eigen content — geen gekopieerde tekst met een andere plaatsnaam, dat is de klassieke fout bij locatiepagina's.
- De bio-pagina voor "SEO specialist Haarlem", het dunste concurrentieveld in de lijst.
- Nulmeting AI-zichtbaarheid: 20 prompts, 3 runs per prompt, over ChatGPT, Perplexity, Google AI Mode en Claude.
- GA4-kanaalgroep inrichten inclusief de Perplexity-regex.

### Fase 2 — content en autoriteit, maand 3 tot 6

- Het artikel "wat kost SEO per maand" volgens het antwoord-eerst-formaat, met prijstabel, eigen cijfers en externe bronvermeldingen — de drie ingrepen uit het KDD-paper.
- De digital-signage-positionering uitwerken: campagnedenken plus scherm, expliciet tegenover de hardwareleveranciers.
- Cases met harde cijfers publiceren.
- Actieve outreach naar "beste bureaus"-lijstjes.
- Een kennisbank starten: korte definitiepagina's, hoge dichtheid, makkelijk te citeren.

### Fase 3 — differentiatie, maand 6 tot 12

Uit §9 blijkt dat Nederlandstalig AI-zoeken vrijwel onbestudeerd is: alle bekende effectgroottes komen uit Engelstalig onderzoek, zonder replicatie in het Nederlands.

Daar ligt een positie. Meet met de eigen prompt-methodologie de AI-zichtbaarheid van een gedefinieerde set Nederlandse MKB-sites, en publiceer die data. Dat levert drie dingen tegelijk: de originele statistieken die volgens het KDD-paper het sterkste citatie-effect hebben, een reden voor vakmedia om XMONK te vermelden, en een positionering die geen enkele concurrent in deze markt heeft.

---

## 11. Wat niet gemeten kon worden

Dit hoort in het rapport omdat het bepaalt welke conclusies wel en niet getrokken kunnen worden.

**Door de geblokkeerde sitetoegang niet gemeten — alsnog uit te voeren:**

| Onderwerp | Waarom het uitmaakt |
|---|---|
| Core Web Vitals (LCP, INP, CLS) | Relevant gezien shared hosting zonder CDN |
| robots.txt en sitemap.xml | Bevat mogelijk de crawler-val uit §9 |
| Bestaande schema-implementatie | Bepaalt of §9's aanbevelingen nieuw of correctief zijn |
| Meta descriptions, koppenstructuur, interne links | Basis on-page-audit |
| Werkelijk aantal geïndexeerde pagina's | Bestaat er wél content die niet vindbaar is? |
| CMS, thema, pagebuilder, pluginlast | Bepaalt de haalbaarheid van technische ingrepen |
| Mobiele weergave en HTTPS-configuratie | Basishygiëne |

**Alleen te meten met jullie toegang:** Google Analytics en Search Console (werkelijk verkeer, huidige zoektermen, indexatiedekking), het Google Bedrijfsprofiel, historische ranking-data, huidige conversies en leadvolume.

**Alleen te meten met betaalde tools:** werkelijke zoekvolumes per keyword, echte ranking-posities, backlinkprofiel en domeinautoriteit van XMONK en de concurrenten, en hun daadwerkelijke publicatiefrequentie.

**Bewust niet opgenomen:** het KvK-nummer (niet te verifiëren), zoekvolumes (geen tool beschikbaar), ranking-posities (het zoekhulpmiddel is geen SERP-scraper).

---

## 12. Bronnen

**Onderzoek en primaire bronnen**
- [GEO: Generative Engine Optimization (KDD 2024) — arXiv:2311.09735](https://arxiv.org/pdf/2311.09735)
- [Ahrefs — AI Overview brand correlation study, 75.000 merken](https://ahrefs.com/blog/ai-overview-brand-correlation/)
- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google Developers — Grounding with Google Search](https://developers.googleblog.com/en/gemini-api-and-ai-studio-now-offer-grounding-with-google-search/)
- [Apple Support — About Applebot](https://support.apple.com/en-us/119829)

**Platformwijzigingen 2026**
- [Search Engine Journal — Google drops FAQ rich results](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/) · [Search Engine Land](https://searchengineland.com/google-to-no-longer-support-faq-rich-results-476957)
- [Search Engine Journal — GA4 adds AI Assistant channel](https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/) · [Semrush](https://www.semrush.com/blog/ga4-adds-ai-assistant-channel/)
- [PPC Land — Search Console generative AI reports](https://ppc.land/google-finally-gives-search-console-its-own-generative-ai-visibility-reports/)
- [Search Engine Land — Query fan-out](https://searchengineland.com/guide/query-fan-out)
- [Search Engine Land — Zero-click searches 2026](https://searchengineland.com/google-zero-click-searches-2026-study-479717)

**Crawlers en llms.txt**
- [Search Engine Land — Anthropic Claude bots](https://searchengineland.com/anthropic-claude-bots-470171)
- [Am I Cited — GPTBot vs OAI-SearchBot](https://www.amicited.com/blog/gptbot-vs-oai-searchbot/)
- [Baseline Labs — Google over llms.txt](https://baselinelabs.ai/blog/llms-txt-google-search) · [presenc.ai — State of llms.txt 2026](https://presenc.ai/research/state-of-llms-txt-2026)
- [ZipTie — Hoe Perplexity werkt](https://ziptie.dev/blog/how-perplexity-ai-answers-work/)

**Kritische tegengeluiden**
- [Digiday — GEO hype busted](https://digiday.com/media/geo-hype-busted-experts-call-it-more-seo-than-new-discipline/)
- [CXL — Is AEO/GEO just SEO hype](https://cxl.com/blog/aeo-geo-seo-reality-check/)
- [Daniel K Cheung — Schema en AI-citaties, bewijsreview](https://www.danielkcheung.com/musings/schema-ai-citations-evidence-review)

**Meetmethodologie**
- [Search Engine Land — Prompt-level visibility meten](https://searchengineland.com/measure-prompt-level-visibility-ai-search-481577)
- [Aleyda Solis — AI search prompt library opbouwen](https://www.aleydasolis.com/en/ai-search/ai-search-prompt-library/)

**Concurrenten**
- [Ad Your Service — diensten](https://www.adyourservice.nl/onze-diensten/) · [FONK150-vermelding](https://www.adyourservice.nl/blog/online-marketing/fonk150-2023-een-klantonderzoek/)
- [Blauwe Monsters — het verhaal](https://blauwemonsters.nl/over-ons/het-verhaal) · [Van SEO naar GEO](https://blauwemonsters.nl/blog/van-seo-naar-geo)
- [Consultancy.nl — 4NG neemt Blauwe Monsters over](https://www.consultancy.nl/nieuws/48577/4ng-versterkt-performance-marketing-capaciteiten-met-overname-blauwe-monsters) · [Wagenhof — verhuizing naar Haarlem](https://wagenhof.nl/nieuws/blauwe-monsters-verhuist-naar-haarlem/)
- [LYNX Media, Cruquius](https://lynx-media.nl/website-laten-maken)

**Nederlandse markt- en prijscontext**
- [Stramark — SEO-kosten 2026](https://www.stramark.nl/blog/seo-kosten/) · [Searchlab](https://searchlab.nl/kosten/wat-kost-seo-uitbesteden) · [Whello](https://whello.nl/marketing-tips/seo/wat-kost-seo)
- [Ralf van Veen — SEO Haarlemmermeer](https://ralfvanveen.com/seo-specialist-haarlemmermeer/) · [Marketingbureau Hoofddorp](https://marketingbureauhoofddorp.nl/)

---

*Onderzoek uitgevoerd op 28 juli 2026. Alle DNS-metingen zijn op die datum verricht en kunnen wijzigen. Uitspraken over websitecontent zijn gebaseerd op zoekresultaten, niet op directe inspectie — zie §0 en §11.*
