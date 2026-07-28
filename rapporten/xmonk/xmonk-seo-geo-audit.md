# SEO & GEO Audit — XMONK (xmonk.nl)

**Aanleiding:** inbound formulieraanvraag van Arjen van Leeuwen (XMONK), 27 juli 2026, 10:59 CEST
**Opgesteld:** 28 juli 2026
**Voor:** GoldLemon — voorbereiding op het eerste gesprek
**Status:** extern onderzoek (desk research). Geen toegang tot de website zelf, geen toegang tot Google Analytics of Search Console van de klant.

---

## 0. Onderzoeksverantwoording — lees dit eerst

Dit rapport is opgebouwd uit publieke bronnen en eigen DNS-metingen. Eén beperking is bepalend voor hoe je dit rapport moet lezen:

> **De website xmonk.nl kon niet direct worden opgevraagd.** Het uitgaande netwerkbeleid van deze werkomgeving blokkeerde alle directe HTTP(S)-verzoeken (403 vanaf de egress-proxy, voor élk domein — niet specifiek voor XMONK). Alle uitspraken over de inhoud en structuur van de site zijn daarom afgeleid uit zoekresultaten, titels en snippets — niet uit het lezen van de HTML.

Wat daardoor **niet** in dit rapport staat en wat je in een vervolgstap met directe toegang alsnog moet meten, staat in §12. Dat is geen bijzaak: een deel van de meest concrete verkoopargumenten (Core Web Vitals, schema-implementatie, robots.txt, sitemap, interne links, indexatiestatus) zit precies in dat gat.

### Betrouwbaarheidscodering

Elke bevinding in dit rapport heeft een label. Behandel ze niet als gelijkwaardig.

| Label | Betekenis |
|---|---|
| **[GEMETEN]** | Zelf gemeten in deze sessie, reproduceerbaar (DNS-queries, CRM-checks). Hard. |
| **[ZOEK]** | Consistent teruggevonden in meerdere onafhankelijke zoekopdrachten. Betrouwbaar, maar niet op de bron zelf gecontroleerd. |
| **[AFGELEID]** | Redenering op basis van patronen. Plausibel, expliciet niet bewezen. |
| **[ONBEVESTIGD]** | Kwam één keer voorbij, of bronnen spreken elkaar tegen. Niet in een klantpresentatie gebruiken zonder verificatie. |

Waar de markt zelf onenigheid heeft — en bij GEO is dat vaak — staat dat er expliciet bij. Dit rapport bevat bewust géén verzonnen zoekvolumes, geen verzonnen ranking-posities en geen KvK-nummer dat we niet konden verifiëren.

---

## 1. Samenvatting

XMONK is een klein online-marketingbureau in Cruquius dat SEO en SEA verkoopt, maar zijn eigen vindbaarheid nooit heeft ingericht. Dat is de kern van de zaak, en het is tegelijk het beste verkoopargument: het probleem is groot, concreet en goed uitlegbaar aan iemand met een commerciële achtergrond.

De vijf bevindingen, in volgorde van urgentie:

1. **XMONK is organisch onvindbaar voor elke commerciële term die het verkoopt.** In zestien verschillende zoekopdrachten op termen als "SEO bureau Haarlem", "online marketing bureau Haarlemmermeer" en "SEO bureau Hoofddorp" kwam xmonk.nl niet één keer naar voren. De site verschijnt alleen bij een zoekopdracht op de eigen merknaam. [ZOEK]

2. **XMONK staat op geen enkel vergelijkingsplatform — en dat is het grootste gat.** Niet op Sortlist, Clutch, DesignRush, Trustpilot of Trustoo. Juist die platforms bezetten het merendeel van de zoekresultaten bij "welk bureau moet ik kiezen"-vragen, en zijn precies het type bron waar AI-assistenten hun aanbevelingen op baseren. Een concurrent uit hetzelfde dorp (Fortune Agency, Cruquius) staat wél op twee van die platforms. [ZOEK]

3. **De merknaam werkt tegen XMONK in AI-zoekresultaten.** "XMONK" botst met een Indiaas leiderschapscoachingbedrijf (xMonks, xmonks.com) en met xmonk.net, een domein dat door ScamAdviser als laag-vertrouwen is gemarkeerd. Wie zoekt op "XMONK reviews" vindt eerder die twee dan XMONK zelf. Voor een taalmodel dat een entiteit moet herkennen is dit een reëel probleem, niet een cosmetisch. [ZOEK]

4. **Er is geen contentmotor.** Geen blog, geen kennisbank, geen cases, geen locatiepagina's. De vindbare site bestaat uit ongeveer zeven pagina's. Ondertussen heeft de directe concurrent uit Haarlem een blog, een wiki met tientallen definitiepagina's, gekwantificeerde cases én een reeks artikelen over GEO. [ZOEK]

5. **De e-mailinfrastructuur heeft een meetbaar en direct oplosbaar defect.** Het DMARC-record van xmonk.nl bevat geen `rua=`-adres, waardoor XMONK nul rapportages ontvangt over wie er namens hun domein mailt, en `sp=none` laat subdomeinen volledig onbeschermd. Voor een bureau dat zelf e-mailmarketing en outbound verkoopt, is dit een pijnlijk maar goedkoop te repareren detail. Dit is de enige bevinding die we volledig zelf hebben gemeten. [GEMETEN]

**Over de aanvraag zelf:** XMONK vraagt om te ranken op "marketing", "seo" en "nieuwe website". Alle drie zijn niet haalbaar of niet nuttig, en dat moet in het eerste gesprek eerlijk op tafel. Zie §9 voor de onderbouwing en een vervangende lijst van tien termen die wél te winnen zijn.

**Positionering voor het gesprek:** Arjen van Leeuwen komt uit media-sales (Hearst Magazines, Sanoma Media, Icemedia) en zit sinds 2020 bij XMONK. [ZOEK] Voer het gesprek dus commercieel, niet technisch: omzetkansen, concurrenten met naam, en wat het kost om het gat te dichten. Niet over crawl budget en canonical tags.

---

## 2. Lead- en bedrijfsprofiel

### De aanvraag

| Veld | Waarde |
|---|---|
| Naam | Arjen van Leeuwen |
| Telefoon | +31 6 45 21 01 47 |
| Website | www.xmonk.nl |
| Genoemde concurrenten | Ad your service, Blauwe Monsters (2 van de 3 gevraagde ingevuld) |
| Gevraagde keywords | marketing, seo, nieuwe website (3 van de 10 gevraagde ingevuld) |
| Tijdzone | Europe/Amsterdam (GMT+02:00) |
| Ingediend | 27 juli 2026, 10:59 |

Twee observaties over het formulier zelf. Ten eerste is het maar half ingevuld: twee van drie concurrenten, drie van tien keywords. Dat is geen desinteresse maar waarschijnlijk een teken dat er intern nog geen keywordstrategie ligt — wat de aanleiding voor de aanvraag zou kunnen zijn. Ten tweede staat er een IP-adres uit Brazilië (186.247.163.146) bij een Nederlandse tijdzone-instelling. Waarschijnlijk vakantie, VPN of mobiele roaming. Onschuldig, maar noem het niet in het gesprek zonder het te weten.

**CRM-status:** XMONK en Arjen van Leeuwen komen niet voor in HubSpot — niet als contact, niet als bedrijf, ook niet op achternaam. Dit is een volledig nieuwe lead zonder voorgeschiedenis. [GEMETEN]

### Het bedrijf

| Gegeven | Waarde | Label |
|---|---|---|
| Adres | Crommelinbaan 29A, **2142 EX** Cruquius (gemeente Haarlemmermeer) | [ZOEK] |
| Telefoon | 023 – 785 4169 | [ZOEK] |
| E-mail | info@xmonk.nl | [ZOEK] |
| Openingstijden | ma–vr 09:00–18:00, reactie binnen 24 uur | [ZOEK] |
| Actief sinds | ten laatste 2020 (via LinkedIn-profiel Arjen van Leeuwen) | [AFGELEID] |
| Diensten | SEO, SEA, display advertising, social media, digital signage, contentmarketing | [ZOEK] |
| Teamgrootte | onbekend | — |
| KvK-nummer | **niet geverifieerd — bewust weggelaten** | — |

Twee correcties op wat je elders zou kunnen vinden:

- De postcode is **2142 EX**, niet 2134 EX. Onafhankelijke kadaster- en postcodebronnen (postcode.nl, kadastralekaart.com, planviewer.nl) geven consistent 2142 EX voor Crommelinbaan 29 in Cruquius. [ZOEK]
- Er circuleert een KvK-nummer (80388957) in AI-gegenereerde samenvattingen van zoekresultaten, maar geen enkele bron toonde dat nummer daadwerkelijk gekoppeld aan XMONK in een register. **Het staat daarom niet in dit rapport als feit.** Verifieer het in het gesprek of via KVK.nl voordat je het ergens vastlegt.

### Vindbare paginastructuur

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

Wat hieraan opvalt:

- **Geen enkele title tag bevat een plaatsnaam.** Geen Haarlem, geen Haarlemmermeer, geen Hoofddorp. Voor een bureau dat lokale MKB-klanten wil, is dat het meest elementaire gemis dat er is. [ZOEK]
- **De SEO-pagina heeft het woord "SEO bureau" niet in de title** — die begint met "Voor Optimale Vindbaarheid", een merkzin. De pagina die op "SEO" moet ranken, geeft de zoekmachine als eerste signaal iets anders. [ZOEK]
- **De titelconventie is inconsistent**: meestal "[Onderwerp] | XMONK", maar bij `/seo/` staat het merk niet achteraan en het onderwerp niet vooraan. [ZOEK]
- **Geen blog, geen over-ons, geen cases, geen vacatures, geen prijzen** in ongeveer tien gerichte zoekopdrachten. Dat is geen bewijs dat ze niet bestaan, maar wel dat ze niet vindbaar zijn — en voor SEO is dat hetzelfde. [ZOEK]
- De URL-structuur (`/seo/`, `/testimonial/[slug]/`) past bij WordPress. Eén losse aanwijzing noemde de formulierplugin nex-forms. [ONBEVESTIGD]
- De enige gevonden testimonial-URL eindigt op `-4`, wat in WordPress meestal duidt op meerdere pagina's met dezelfde titel. In één zoekopdracht kwam de inhoud van die pagina terug als "Lorem ipsum" — mogelijk een niet-afgemaakte template. **Dit moet je zelf bekijken zodra je de site kunt openen**, want een gepubliceerde Lorem-ipsum-pagina op de site van een marketingbureau is een pijnlijk maar zeer makkelijk te fixen detail. [ONBEVESTIGD]

---

## 3. Bevinding 1 — organisch onvindbaar op eigen dienstverlening

Er zijn zestien commerciële zoekopdrachten uitgevoerd op de termen waar XMONK zijn brood mee verdient. **Bij geen enkele verscheen xmonk.nl.** [ZOEK]

| Zoekterm | Wie er wél verscheen | XMONK |
|---|---|---|
| SEO bureau Haarlem | Hulc, SAM Online Marketing, ROXTAR, Ranking Masters, **LYNX Media (Cruquius)**, Versgeplukt, httpmarketing, seo-haarlem.nl, mpowerDigital | afwezig |
| SEO bureau Hoofddorp | SAM Online Marketing, Online Ambition, Your Salespoint, Connect Your World, SEO Capital, mpowerDigital | afwezig |
| online marketing bureau Haarlem | Trustoo, Sortlist, One Media, MADE Marketing, The Success Agency | afwezig |
| online marketing bureau Haarlemmermeer | Trustoo, DigiSwift, The Success Agency, Reward, Fortune Agency, Scoob | afwezig |
| marketing bureau Cruquius | Trustoo, marketing-bureaus.nl, DesignRush, reclamebureausgids.nl, MADE Marketing | **afwezig in eigen dorp** |
| SEA bureau Haarlem | Onlinemeersucces, Shoptimalisatie, Digital Wizards, C-Corner, Vitenda, mpowerDigital | afwezig |
| digital signage leverancier Nederland | Samsung, eventplanner.nl, Dustin, Signtifix, Adaptable, Wikipedia, Viewie Media | afwezig |
| nieuwe website laten maken Haarlem | VrijdagOnline, Chuck's Webdesign, Webaware, Projectie, MADE Marketing, C-Corner | afwezig |

Twee dingen die je in het gesprek moet noemen:

**XMONK is niet vindbaar in zijn eigen dorp.** Bij "marketing bureau Cruquius" verschijnen Fortune Agency, OOSEOO en STOOP marketing — allemaal via directories. XMONK niet. Cruquius is een dorp; als je daar niet vindbaar bent, ben je nergens vindbaar.

**Er zit een concurrent in Cruquius die XMONK niet als concurrent genoemd heeft.** LYNX Media (lynx-media.nl), ook Cruquius, verschijnt wél bij "SEO bureau Haarlem" en heeft een pagina voor "website laten maken". Dat is de meest directe geografische concurrent die er bestaat, en die staat niet op het formulier. [ZOEK]

**Belangrijke nuance over methode.** Het gebruikte zoekhulpmiddel is een algemene web-search-API, geen letterlijke Google.nl-SERP-scraper. De genoemde volgorde is een indicatie van concurrentiedichtheid, geen geverifieerde ranking-positie. Dat XMONK in zestien onafhankelijke zoekopdrachten nul keer verschijnt is een sterk signaal, maar voor een harde uitspraak over ranking-posities heb je een rank tracker (Ahrefs, Semrush) nodig. Zeg dat er eerlijk bij; het maakt de rest van het rapport geloofwaardiger.

---

## 4. Bevinding 2 — nul aanwezigheid op de vergelijkingsplatforms

Dit is de belangrijkste bevinding van het hele onderzoek, en tegelijk de goedkoopste om op te lossen.

Bij zoekopdrachten met keuze-intentie — "beste online marketing bureau Haarlem", "welk marketing bureau moet ik kiezen", "top 10 marketing bureaus Noord-Holland" — worden de resultaten niet gedomineerd door bureaus, maar door **vergelijkingssites en lijstjes**. Over elf onderzochte zoekopdrachten bezetten directories en listicles ruwweg 55–70% van de zichtbare posities, en bij brede vergelijkingsvragen liep dat op naar bijna 100%. Bij "top 10 marketing bureaus Noord-Holland" bestond de volledige resultatenpagina uit Sortlist-categoriepagina's. [ZOEK]

De poortwachters, gerangschikt naar hoe vaak ze verschenen:

| Platform | Verschijnt bij | XMONK aanwezig? |
|---|---|---|
| **trustoo.nl** | 6+ zoekopdrachten, vaak positie 1; heeft per-plaats top-10-pagina's, inclusief Cruquius | **nee** |
| **sortlist.nl / .com** | 5 zoekopdrachten, soms de volledige pagina | **nee** |
| **agencies.semrush.com** | domineerde de Engelstalige variant met 6 van 9 posities | **nee** |
| **designrush.com** | Cruquius-zoekopdracht en concurrentprofielen | **nee** |
| **clutch.co** | agency-vergelijkingen | **nee** |
| **trustpilot.com** | reviews | **nee** |

En de vergelijking die het pijnlijk maakt: **Trustoo heeft een pagina met "10 online marketing bureaus in Cruquius", gemiddelde score 9,9. XMONK staat er niet tussen. Fortune Agency — óók uit Cruquius — staat er wél op, én heeft een DesignRush-profiel met geciteerde klantquotes.** Twee platforms voor de buurman, nul voor XMONK. [ZOEK]

**Waarom dit dubbel zo zwaar weegt.** Deze platforms zijn niet alleen goed voor organisch verkeer. Ze zijn precies het soort bron waar een taalmodel op terugvalt bij een "welk bureau moet ik kiezen"-vraag: derde-partij, reviewgedekte, al-gesynthetiseerde vergelijkingscontent die exact het antwoord geeft op de vraag die de gebruiker stelt. Een bureau dat op geen enkel vergelijkingsplatform staat, is structureel onzichtbaar op het moment dat de klant kiest — voor mensen én voor AI.

Bijkomend: er is geen Wikipedia-artikel, geen Wikidata-entiteit, geen persdekking en geen aantoonbare merkvermelding buiten de eigen site gevonden. [ZOEK] Een Google Bedrijfsprofiel met reviews kwam ook niet naar boven, maar dat is niet hetzelfde als bewijs dat het niet bestaat — Google Maps-content komt vaak niet terug in gewone webzoekresultaten. Dit moet direct in Maps gecontroleerd worden.

---

## 5. Bevinding 3 — het merk botst in de zoekresultaten

Zoek op "XMONK reviews", "XMONK ervaringen" of "XMONK marketing bureau" en je krijgt overwegend twee andere entiteiten: [ZOEK]

1. **xMonks** (xmonks.com, xmonks.club) — een Indiaas coaching- en leiderschapsontwikkelingsbedrijf met een aanzienlijke voetafdruk: eigen site, Instagram, LinkedIn, ZoomInfo, podcast op Apple Podcasts.
2. **xmonk.net** — een ongerelateerd domein dat door ScamAdviser, ScamDoc en WOT is gemarkeerd met een matige vertrouwensscore en verborgen Whois-eigenaar.

De echte xmonk.nl verschijnt slechts één keer, laag, en er is geen enkele review-, testimonial- of profielpagina van derden die naar boven komt.

**Waarom dit meer is dan een ongelukje.** Taalmodellen werken met entiteiten. Als de naam "XMONK" in de trainingsdata en in de live zoekindex vooral gekoppeld is aan een Indiaas coachingbedrijf en aan een domein met een vertrouwenswaarschuwing, dan kan een AI-assistent XMONK niet betrouwbaar herkennen als "online marketingbureau in de regio Haarlem" — en in het slechtste geval koppelt hij het aan de verkeerde. De oplossing hiervoor is niet de naam veranderen, maar het merk stevig **verankeren aan onderscheidende attributen**: consistente naam-adres-telefoongegevens over alle platforms, `Organization`- en `LocalBusiness`-schema met `sameAs`-verwijzingen naar de eigen sociale profielen, en vermeldingen op Nederlandse platforms die de combinatie XMONK + Cruquius/Haarlemmermeer + online marketing steeds opnieuw bevestigen.

Kleine maar relevante bijkomstigheid: er is geen LinkedIn-bedrijfspagina van XMONK gevonden, alleen het persoonlijke profiel van Arjen van Leeuwen (`linkedin.com/in/arjenleeuwen`). Een Instagram-account `@ig.xmonk` bestaat, maar de beschreven inhoud (gaming en mobiele apparaten) past niet bij een marketingbureau, dus dat is vermoedelijk iemand anders. [ONBEVESTIGD] Dit moet in het gesprek uitgevraagd worden — een ontbrekende LinkedIn-bedrijfspagina is voor een B2B-bureau een gat dat in een middag te dichten is.

---

## 6. Bevinding 4 — geen contentmotor

In tien uiteenlopende zoekopdrachten (inclusief expliciete blog-, artikel- en jaartalfilters op 2023, 2024 en 2025) kwam steeds dezelfde set van zeven statische pagina's terug. Geen blog, geen kennisbank, geen gedateerde content, geen cases. [ZOEK]

Bijkomend signaal: dezelfde merkzinnen ("met onstuitbare energie", "passie en ambitie") komen terug op meerdere verschillende dienstpagina's. Dat duidt op een gedeelde template-intro in plaats van per pagina geschreven copy — het klassieke patroon van een brochuresite. [AFGELEID]

Eén testimonial (Leendert van Pommeren) is de enige vorm van sociaal bewijs die vindbaar is. Geen klantenlijst, geen logo's, geen gekwantificeerde resultaten. [ZOEK]

Waarom dit uitmaakt is niet abstract: contentpagina's zijn het enige mechanisme waarmee je informationele zoekvragen ("wat kost SEO per maand", "hoe werkt Google Ads") kunt bezetten, en dat zijn precies de zoekvragen waar AI-antwoorden uit worden opgebouwd. Zonder content is er niets om geciteerd te worden.

---

## 7. Bevinding 5 — technische infrastructuur

Dit is het enige deel van het onderzoek dat volledig zelf gemeten is, met directe DNS-queries. Deze cijfers zijn hard en reproduceerbaar. [GEMETEN]

### Hosting

| Item | Waarde | Beoordeling |
|---|---|---|
| A-record xmonk.nl / www | 45.152.250.14 (beide, geen split) | in orde |
| Reverse DNS | s1146.hostingsecure.com | **shared hosting** |
| Nameservers | ns1.hoasted.nl, ns2.hoasted.eu, ns3.hoasted.com | Nederlandse hoster, in orde |
| CDN | geen | verbeterpunt |
| IPv6 (AAAA) | ontbreekt | klein verbeterpunt |
| CAA-record | ontbreekt | klein verbeterpunt |
| `mail.xmonk.nl` | wijst naar de webserver (45.152.250.14) terwijl de MX naar Microsoft 365 gaat | verouderd record, opruimen |

De reverse DNS (`s1146...`) verraadt een genummerde shared-hostingserver. Dat betekent gedeelde resources en geen controle over de buren, wat direct raakt aan Core Web Vitals. Zonder CDN wordt elke bezoeker vanaf één Nederlandse server bediend. Voor een lokaal bureau met Nederlandse klanten is dat verdedigbaar, maar in combinatie met shared hosting is dit de eerste plek om naar te kijken als de laadtijden slecht blijken.

### E-mailauthenticatie — hier zit een echt defect

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

1. **Het DMARC-record heeft geen `rua=`.** Er is geen rapportageadres geconfigureerd, dus XMONK ontvangt **nul** aggregatierapporten. Ze hebben letterlijk geen zicht op wie er namens hun domein mailt, of hun eigen mail authenticeert, of dat iemand hun domein misbruikt. Dit is een one-line fix met onmiddellijk effect.
2. **`sp=none`.** Het hoofddomein staat op `quarantine`, maar subdomeinen hebben géén beleid. Dat is precies het gat dat bij domeinspoofing wordt gebruikt: `mail.xmonk.nl` of `facturen.xmonk.nl` is volledig onbeschermd.
3. **SPF eindigt op `~all` (softfail) met vier `include`-verwijzingen.** Vier includes plus een los IP-adres brengt het record in de buurt van de DNS-lookuplimiet van tien, en `~all` in plaats van `-all` betekent dat niet-geautoriseerde afzenders alleen worden gemarkeerd, niet geweigerd. De aanwezigheid van `_spf.mijnwefact.nl` (facturatiesoftware) en twee verschillende hostingpartijen suggereert historisch gegroeide configuratie die nooit is opgeruimd.

**Waarom dit in een SEO-rapport staat.** Niet omdat het rankings beïnvloedt — dat doet het niet. Maar omdat het een bureau is dat e-mailmarketing en outbound verkoopt, en de eigen e-mailauthenticatie niet op orde heeft. In het gesprek is dit het meest overtuigende bewijs dat er écht gekeken is, en het is binnen een uur te repareren. Gebruik het als opener, niet als hoofdgerecht.

---

## 8. Concurrentieanalyse

XMONK noemde twee van de drie gevraagde concurrenten. Beide zijn geïdentificeerd en onderzocht, plus twee die XMONK zelf niet noemde maar die relevanter zijn dan één van de genoemde.

### Ad Your Service B.V. — adyourservice.nl

| Gegeven | Waarde |
|---|---|
| Entiteit | Ad Your Service B.V., KVK 77793811 |
| Locatie | Amsterdam-West (adres inconsistent tussen bronnen) |
| Opgericht | 2017, begonnen als soloproject van Nils Kuipers |
| Team | 8–10 personen (bronnen spreken elkaar tegen) |
| Positionering | "voor een sterke online marketingstrategie" — full-service verlengstuk van de marketingafdeling |
| Klanten | Prinses Máxima Centrum, OppoSuits, Derec, Levi9, Little Label |

Let op: er bestaat een **ongerelateerde Belgische** entiteit "AD Your Service SRL" in Antwerpen. Niet verwarren. [ZOEK]

**Sterker dan XMONK op:** breder dienstenpakket (e-mailmarketing, marketplaces, cursussen en workshops, huisstijl, online recruitment — allemaal diensten die XMONK niet heeft); een actieve, technisch georiënteerde blog (SEO-tools, Ahrefs/Semrush/Moz-gidsen, GA4, PageSpeed, Google Ads-extensies, met minstens één 2026-post); en een sterk reputatiebewijs — vermelding in de **FONK150** met een klanttevredenheidsscore van **9,22**, beschreven als top-5 in hun categorie. Dat is precies het type onafhankelijke, gekwantificeerde proof point dat XMONK volledig mist. Klantnamen als Prinses Máxima Centrum en Levi9 doen de rest.

**Zwakker dan XMONK op:** geen zichtbaar programma van lokale landingspagina's. En hun title tags bevatten de merknaam dubbel ("… | ad your service adyourservice") — een klein maar reëel on-page-defect.

**Belangrijkste opening:** Ad Your Service heeft **niets** gepubliceerd over GEO of AI-zoekvindbaarheid. Hun AI-content is algemeen ("1 jaar met ChatGPT", afbeeldingen genereren met ChatGPT-4, voice search) en positioneert hen niet als AI-visibility-specialist. Op dat vlak staan XMONK en Ad Your Service gelijk — en daar valt een positie te pakken. [ZOEK]

### Blauwe Monsters — blauwemonsters.nl

Dit is de serieuze concurrent, en XMONK onderschat vermoedelijk hoe serieus.

| Gegeven | Waarde |
|---|---|
| Opgericht | 2012, gegroeid uit de eigen webshop HemdVoorHem.nl (Michiel Snoek, Dennis Stokman) |
| **Locatie** | **Jan van Krimpenweg 7, 2031 CE Haarlem** — verhuisd van Hoofddorp naar Haarlem in juli 2022 |
| Eigendom | overgenomen door **4NG** (onderdeel van **Conclusion**) in juli/augustus 2023 |
| Team | 44 bij overname, "50+" in latere eigen content |
| Klanten | 300+, B2C en B2B |
| Positionering | "Resultaatgericht Online Marketing Bureau", recenter: "waar AI en expertise samenkomen" |
| Specialisatie | e-commerce en performance marketing; SEO, SEA, CRO, content, e-mail, social ads, marketplaces, server-side tagging, call tracking |

**Twee dingen die je in het gesprek moet noemen omdat XMONK ze misschien niet weet:**

1. **Blauwe Monsters zit sinds juli 2022 in Haarlem zelf**, in de Waarderpolder. Niet meer in Hoofddorp. Dat maakt hen een directere geografische concurrent dan XMONK denkt. [ZOEK]
2. **Ze zijn onderdeel van 4NG/Conclusion sinds 2023** — een groep die na de overname doorgroeide naar elf labels en circa 460 medewerkers. XMONK concurreert niet met een bureau van vijftig mensen, maar met een bureau van vijftig mensen mét concernbudget erachter. [ZOEK]

**Hun contentmoat, waar XMONK niets tegenover heeft:**

- **Locatiepagina's op schaal**: `/seo-bureau/[stad]/` én `/seo/[stad]/` (Amsterdam, Haarlem, Groningen en meer). Precies de strategie die XMONK niet uitvoert. Kanttekening: die twee parallelle URL-structuren duiden op technische schuld uit een migratie — een zwak punt om te controleren.
- **Een wiki/glossarium**: `/wiki/[categorie]/[term]/` met tientallen definitiepagina's (featured snippet, orphan page, paginering, htaccess, geotargeting, call-to-action). Dit is een aanzienlijk topical-authority-bezit, en precies het formaat dat AI-antwoordmachines graag citeren.
- **Cases met harde cijfers**: "+300 non-branded keywords in top-3", "48% meer top-3-rankings", "148% meer e-mailtransacties".
- **Een actieve blog** met recente, gedateerde posts.

**En het punt dat het meest urgent is:** Blauwe Monsters publiceert al een samenhangend GEO-programma. Minstens vijf artikelen, met titels als "Van SEO naar GEO: Zo speel je in op AI Overviews en AI mode", "AI geeft de antwoorden, maar SEO bepaalt wie ze levert", "Websites optimaliseren voor AI (GEO)", "Bing introduceert AI Performance: data voor GEO" en een lokale-SEO-stuk dat expliciet de link legt naar AI Overviews. [ZOEK]

Dat betekent: als XMONK zich wil onderscheiden op "klaar voor AI-zoeken", loopt het op dat punt al achter op de dichtstbijzijnde grote concurrent. Post-voor-post nadoen is niet genoeg; er is iets inhoudelijk beters nodig — bijvoorbeeld eigen meetdata over AI-zichtbaarheid van Nederlandse MKB-sites, iets wat niemand in deze markt publiceert.

**Zwakker dan XMONK op:** nauwelijks iets gevonden. De twee plekken om te controleren zijn de inconsistente URL-structuur en een mogelijk verouderd Sortlist-profiel met 14 reviews uit het Hoofddorp-tijdperk, dat sinds de overname en verhuizing niet lijkt te zijn bijgewerkt. [ONBEVESTIGD]

### Twee concurrenten die XMONK niet noemde

**LYNX Media (lynx-media.nl), Cruquius.** Zit in hetzelfde dorp, verschijnt bij "SEO bureau Haarlem" en heeft een pagina voor "website laten maken". De meest directe geografische concurrent die bestaat, en niet genoemd op het formulier. [ZOEK]

**Fortune Agency (fortuneagency.nl), Cruquius.** Ook hetzelfde dorp. Staat op Trustoo (score 9,9, top-10 webdesigners Cruquius) én op DesignRush met geciteerde klantquotes. Het levende bewijs dat een bureau van vergelijkbare omvang uit hetzelfde dorp die platformaanwezigheid wél voor elkaar krijgt. [ZOEK]

### Samenvattende vergelijking

| Dimensie | XMONK | Ad Your Service | Blauwe Monsters |
|---|---|---|---|
| Team | onbekend, klein | 8–10 | 50+ (concern: ~460) |
| Vindbare pagina's | ~7 | tientallen | honderden |
| Blog | **geen** | actief | actief |
| Kennisbank/wiki | **geen** | geen | **ja, tientallen pagina's** |
| Locatiepagina's | **geen** | geen | **ja, meerdere steden** |
| Cases met cijfers | **geen** | klantnamen | **ja, gekwantificeerd** |
| Onafhankelijk reputatiebewijs | **geen** | **FONK150, 9,22** | Feedback Company |
| Directoryprofielen | **geen** | Sortlist | Sortlist (mogelijk verouderd) |
| GEO/AI-content | **geen** | **geen** | **5+ artikelen** |
| Geografische nabijheid tot Haarlem | Cruquius | Amsterdam | **Haarlem zelf** |

De kolom die het verhaal vertelt: XMONK staat op zes van de tien rijen op "geen".

---

## 9. Keywordanalyse

### De drie gevraagde termen — eerlijke beoordeling

XMONK vroeg om "marketing", "seo" en "nieuwe website". Alle drie moeten van de lijst af. Dit is het belangrijkste eerlijke gesprek dat in de eerste call gevoerd moet worden, en het is te brengen als deskundigheid in plaats van als afwijzing.

**"marketing" — niet haalbaar, en zou niet werken.** De resultaten worden bezet door Wikipedia, Coursera, Salesforce en de American Marketing Association. Puur informationeel: studenten en nieuwsgierigen, geen kopers. Geen enkel Nederlands bureau in de buurt. Zelfs in het onwaarschijnlijke geval dat XMONK er zou ranken, wil die bezoeker een definitie, geen offerte. Dit is de bakker die op het woord "brood" wil ranken. [ZOEK]

**"seo" — hetzelfde probleem, nog scherper.** Concurrentie: Google's eigen Search Central-documentatie, Search Engine Land, digital.gov, universiteiten. In de Nederlandse resultaten zijn dit soort posities eigendom van Frankwatching, Marketingfacts en de grote landelijke toolmerken. Dit is een meerjarig autoriteitsspel voor partijen met een veel groter budget dan XMONK's klanten ooit goedkeuren. [ZOEK]

**"nieuwe website" — zwak, en niet wat kopers typen.** Twee exact-match generieke domeinen (nieuwewebsite.nl, nieuwe-website.com) bezetten deze term landelijk. Belangrijker: Nederlanders die klaar zijn om een website te laten bouwen typen **"website laten maken"**, niet "nieuwe website". De term heeft dus zwakkere koopintentie én een moeilijker veld. Vervangen. [ZOEK]

**Hoe je dit brengt:** "Alle drie de termen die jullie hebben opgegeven zijn óf woordenboektermen waar Wikipedia en Google's eigen documentatie op staan, óf niet de woorden die kopers daadwerkelijk intypen. De tien termen hieronder zijn gekozen omdat er al échte lokale concurrenten om vechten — en dat is precies het bewijs dat er kopers achter zitten."

### De aanbevolen tien

Geselecteerd uit een onderzochte lijst van 34 termen. **Geen enkel zoekvolume in dit rapport is een meting** — er was geen keyword-tool beschikbaar, en er zijn bewust geen getallen verzonnen. De concurrentiebeoordeling komt uit wie er daadwerkelijk in de zoekresultaten verscheen.

| # | Zoekterm | Intentie | Wat er nodig is | Concurrentie |
|---|---|---|---|---|
| 1 | online marketing bureau Haarlem | commercieel, lokaal | eigen landingspagina, niet de homepage | matig: Digital Wizards, One Media, Reward, MADE Marketing, The Success Agency |
| 2 | SEO bureau Haarlemmermeer | commercieel, eigen thuisbasis | locatiepagina met transparante prijzen | matig: Ralf van Veen, C-Corner, HTTP Marketing, Bureau Bijma |
| 3 | SEO specialist Haarlem | commercieel, zoekt een persoon | bio-pagina met naam en credentials van de SEO-lead | **dun** — veel ruis van vacatures, weinig echte pagina's |
| 4 | Google Ads bureau Hoofddorp | commercieel, hoge koopintentie | aparte SEA-pagina voor Hoofddorp | matig: Online Meer Succes, Stijgt, Connect Your World, Smoop |
| 5 | social media bureau Haarlem | commercieel, dienstspecifiek | dienstpagina met lokale cases | **dun**: Social Sparrow, Blitskikker, Endeavour Heroes |
| 6 | website laten maken Haarlemmermeer | commercieel, lokaal + dienst | portfolio-gedreven landingspagina | matig, en **LYNX Media uit Cruquius zit hier** |
| 7 | marketingbureau Amstelveen | commercieel, lokaal, koopkrachtig | locatiepagina, lagere prioriteit | **zwaar** — één directory noemt 65 bureaus voor Amstelveen |
| 8 | digital signage bureau | commercieel, B2B, landelijk | dienstpagina met de creatieve invalshoek | zie hieronder |
| 9 | digitale reclameborden winkel | commercieel, retail-niche | landingspagina + leadmagneet | hardware-resellers: VEBO, Display4all, Q-lite |
| 10 | wat kost SEO per maand | informationeel, top of funnel | blogartikel met prijstabel en FAQ | matig: Whello, Opklopper, Go Online |

**Nummers 8 en 9 zijn de echte kans, maar niet leeg.** Bij "digital signage" verschijnen vooral hardwareleveranciers en softwareplatformen (Samsung, First Impression, ZetaDisplay, Viewie Media, IP Digital). Er zijn twee échte regionale concurrenten die full-service narrowcasting verkopen: **DooH Solutions & Services** (Haarlemmermeer) en **UW-S** (Haarlem). Maar — en dit is het punt — **geen enkele partij in dit veld positioneert zich als marketingbureau dat óók de contentstrategie voor het scherm doet.** Campagnedenken plus het scherm is een echte, verdedigbare positie, en XMONK heeft die dienst al in huis. [ZOEK]

**Nummer 10 is de GEO-instap.** "Wat kost SEO per maand" heeft geen Wikipedia-probleem, wordt bezet door middelgrote bureaublogs, en het antwoordformaat (korte directe prijsindicatie, prijstabel, FAQ) is precies wat AI Overviews en chatassistenten oplichten. Dit is het beste enkele artikel om mee te beginnen.

**Marktcontext voor de prijsstelling van dat artikel** (bruikbaar in het gesprek): Nederlandse bronnen noemen voor MKB grofweg €500–€1.500 per maand voor een serieus SEO-traject, met een bredere range van €250 tot €3.500, uurtarieven tussen €50 en €150, en een inspanning van tien tot twintig uur per maand. Meerdere directe concurrenten in de regio publiceren hun prijzen openlijk (Ralf van Veen vanaf €1.000/maand, Marketingbureau Hoofddorp vanaf €250/maand) — prijzen verzwijgen is in deze markt dus een nadeel, geen bescherming. [ZOEK]

### Wat te schrappen

- **"marketing"** en **"seo"** — volledig laten vallen.
- **"nieuwe website"** — vervangen door #6, "website laten maken Haarlemmermeer".
- De kale landelijke term **"website laten maken"** niet frontaal aanvallen: die wordt bezet door grote pure-play webbouwers (Webstijn, Flerque, Yourhosting, Stuurlui) met jaren SEO-investering.

---

## 10. GEO-playbook

Dit deel is het meest bewust sceptisch geschreven, want GEO is het onderwerp waar de meeste onzin over wordt gepubliceerd. Een groot deel van de "2026-statistieken" die je online vindt over AI-zichtbaarheid komt van bureaus en toolleveranciers met een commercieel belang bij urgentie, en dezelfde precies klinkende percentages ("41% meer citaties", "3,4x zoveel kans") duiken op tientallen bijna identieke blogs op zonder methodologie of steekproefgrootte. Wat hieronder staat is gesorteerd op bewijskracht, niet op hoe goed het klinkt.

### Wat GEO wel en niet is

Google's eigen standpunt is dat optimaliseren voor AI-functies **nog steeds SEO is**: dezelfde crawlbaarheid, contentkwaliteit en E-E-A-T, geen aparte discipline. De praktijk is genuanceerder. Het best onderbouwde onderzoek laat zien dat klassieke ranking-signalen zwakker correleren met AI-citaties dan off-site merksignalen — dus goede SEO is een **vloer, niet het hele spel**.

De hardste cijfers die er zijn, uit een Ahrefs-analyse van **75.000 merken**: merkvermeldingen op het web correleren met zichtbaarheid in AI Overviews op **r = 0,664**, tegenover **r = 0,218 voor backlinks**. Ongeveer drie keer zo sterk. Merken in het hoogste kwartiel qua vermeldingen haalden gemiddeld 169 AI-Overview-verschijningen tegen 14 voor het kwartiel eronder. Dit is een leveranciersstudie, geen peer-reviewed onderzoek, maar mét openbaar gemaakte steekproefgrootte — en daarmee beter onderbouwd dan bijna al het andere in dit veld.

Wat je **niet** moet geloven: de veelgeciteerde bewering dat de overlap tussen Google's top 10 en AI-geciteerde bronnen "van 70% naar onder 20%" is gedaald. Geen enkele bron geeft daar een dataset of methodologie bij. Richting plausibel, cijfer onbruikbaar.

### Hoe de antwoordmachines eigenlijk werken

| Platform | Ophaalmechanisme | Wat dat betekent |
|---|---|---|
| **Google AI Overviews / AI Mode** | Google's eigen index (Googlebot). Gebruikt "query fan-out": splitst één vraag in 8–12 subvragen (bij Deep Search honderden) en haalt op passage-niveau op. | Gewone Google-indexatie is de toegangspoort. Optimaliseer op **passage-niveau**, niet alleen paginaniveau. |
| **ChatGPT Search** | Bing-index en -crawlinfrastructuur, niet Google. | Bing Webmaster Tools met sitemap en IndexNow is een randvoorwaarde. Wordt vaak vergeten. |
| **Perplexity** | Eigen crawler (PerplexityBot) plus live RAG met hybride BM25 en vectorretrieval. **Voert JavaScript niet betrouwbaar uit.** | Kritieke content server-side renderen. Client-side JS-content is voor Perplexity mogelijk onzichtbaar. |
| **Claude** | Routeert websearch via de Brave Search API (bewijs: ~86,7% citatie-overlap met Brave's organische top), sinds mei 2026 aangevuld met TurboPuffer als vector-database. | Zichtbaarheid in een niet-Google-index (Brave) doet mee. [ONBEVESTIGD — deels op geleakte parameters gebaseerd] |
| **Microsoft Copilot** | Bing-index met "sequential grounding". Sinds februari 2026: `NOARCHIVE` blokkeert citatie volledig, `NOCACHE` beperkt tot titel en meta. | Controleer of er ergens `NOARCHIVE` staat — dat sluit je volledig uit van Copilot-citaties. [ONBEVESTIGD] |
| **Gemini** | "Grounding with Google Search": een classifier beslist per vraag of live Google-resultaten in de context worden geïnjecteerd. | Zelfde poort als Google Search. |

### Crawler-toegang — hier gaat het vaakst mis

Elke aanbieder heeft nu **gescheiden bots** voor training, indexering en live ophalen. Het blokkeren van de verkeerde vernietigt je AI-zichtbaarheid zonder dat je klassieke rankings iets laten zien. Dit is de meest waardevolle technische controle die je bij een nieuwe klant kunt doen, en de meest onderschatte.

| Aanbieder | Training (blokkeren kost geen zichtbaarheid) | Indexering (**nooit blokkeren**) | Live ophalen (**nooit blokkeren**) |
|---|---|---|---|
| OpenAI | `GPTBot` | `OAI-SearchBot` | `ChatGPT-User` |
| Anthropic | `ClaudeBot` | `Claude-SearchBot` | `Claude-User` |
| Perplexity | — | `PerplexityBot` | `Perplexity-User` |
| Google | `Google-Extended` (een beleidstoken, géén aparte crawler) | `Googlebot` | — |
| Microsoft | — | `Bingbot` | — |
| Apple | `Applebot-Extended` | `Applebot` | — |

Twee valkuilen, expliciet:

1. **`Googlebot` blokkeren in de veronderstelling dat het "de AI-bot" is.** Dat sloopt je gewone SEO onmiddellijk. AI Overviews draaien op dezelfde Googlebot-index als organisch — er is op dit moment geen manier om wél in Google Search te staan maar niet in AI Overviews.
2. **Een brede `Disallow` waarmee ook `OAI-SearchBot`, `Claude-SearchBot` of `PerplexityBot` worden geraakt.** Dit verwijdert het merk uit een hele categorie AI-vindbaarheid **zonder dat de klassieke rankings veranderen** — de schade is dus onzichtbaar in normale SEO-monitoring. Precies daarom moet dit een vast onderdeel van elke audit zijn.

Aanbeveling: alle index- en ophaalbots toestaan. De keuze om trainingsbots te blokkeren (`GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`) is een bewuste bedrijfs- en IP-afweging — geen ongeluk in een robots.txt.

### llms.txt — verkoop dit niet

Kort en duidelijk: **llms.txt is geen werkende hefboom en moet niet als "AI-SEO-werk" gefactureerd worden.**

- Google heeft het expliciet afgewezen. Gary Illyes zei dat Google het niet ondersteunt en dat niet van plan is; John Mueller vergeleek het met de achterhaalde keywords-metatag.
- Geen enkele grote aanbieder heeft publiek toegezegd het in productie te lezen.
- Adoptie is laag en crawler-interesse verwaarloosbaar: een SE Ranking-onderzoek onder 300.000 domeinen vond ~10,1% adoptie, en een analyse van meer dan 500 miljoen AI-botbezoeken vond **408** hits die specifiek op een llms.txt-bestand gericht waren.

Het kost bijna niets om toe te voegen, en er is een echte use case — documentatie- en developersites waarvan de doelgroep AI-codeeragents zijn. Voor een marketingbureausite is dat niet de situatie. Zet het niet op de factuur.

### Schema.org — hygiëne, geen truc

Google's officiële standpunt: er is **geen speciale structured data nodig** voor AI Overviews of AI Mode. En er is geen enkele bron die een causaal effect van schema op LLM-citaties heeft geïsoleerd — taalmodellen verwerken getokeniseerde tekst, er zit geen schema-parser in het model. Waar schema wél helpt, is bij crawlen en indexeren: correcte entiteitsherkenning en attributie in de indexen waar de AI-pijplijnen bovenop zitten.

De veelgeciteerde bewering dat "structured data de nauwkeurigheid van GPT-5 van 16% naar 54% tilt" is onverifieerbaar en wordt door bronnen zelf betwist. Niet gebruiken. Hetzelfde geldt voor de "28–40% meer citaties door FAQ-schema"-cijfers: de artikelen die ze publiceren zeggen er zelf bij dat het waarschijnlijk verwarring is met het feit dat teams die FAQ-schema toevoegen óók betere Q&A-copy schrijven.

**Belangrijke deadline die wél hard is:** Google is per **7 mei 2026** gestopt met FAQ-rich-results in de zoekresultaten. Het FAQ-filter, het Search Console-rapport en de Rich Results Test-ondersteuning verdwijnen in juni 2026; de API-data in augustus 2026. `FAQPage` blijft een geldig schema.org-type en mag op pagina's blijven staan — het levert alleen geen zichtbaar SERP-resultaat meer op. Als een bureau FAQ-schema nog verkoopt als "rich snippet"-winst, verkoopt het iets wat niet meer bestaat.

Wat wel te implementeren, als hygiëne: `Organization` en `LocalBusiness` (met `address`, `geo`, `openingHoursSpecification`, en `sameAs` naar de sociale profielen — voor XMONK extra belangrijk vanwege het naamconflict in §5), `Person` voor auteursbio's gekoppeld aan de organisatie, en `Article` en `BreadcrumbList` als standaard.

### Contentpatronen — het enige met echt onderzoek erachter

Het fundament is één paper: **GEO: Generative Engine Optimization**, KDD 2024, van Princeton, Georgia Tech, het Allen Institute en IIT Delhi ([arXiv:2311.09735](https://arxiv.org/pdf/2311.09735)). Effectgroottes:

| Ingreep | Effect op zichtbaarheid |
|---|---|
| **Statistieken toevoegen** | **+41%** |
| **Citaten toevoegen** | **+28%** |
| **Externe bronnen aanhalen** | **+115%**, maar geconcentreerd bij zwakker presterende content — afnemend rendement voor content die al sterk staat |

Dit zijn de enige methodologisch onderbouwde cijfers in het hele vakgebied. Er is **geen onafhankelijke replicatie uit 2025 of 2026 gevonden**, ondanks expliciet zoeken. Alles wat zich voordoet als "nieuw GEO-onderzoek uit 2026" bleek bij navraag hetzelfde paper te herhalen. Behandel elk nieuw percentage met wantrouwen tot er een controleerbare dataset bij staat.

De structurele adviezen (antwoord in de eerste 40–60 woorden, vraag-vormige H2's, blokken van 100–300 woorden, opeenvolgende koppenhiërarchie) zijn mechanistisch plausibel en kosten niets, maar élk specifiek getal dat erbij wordt geleverd — 2,8x, 3,4x, 44,2% — komt uit blogs zonder onderliggend onderzoek. Doe het wel, beloof geen percentages.

Praktisch dus: begin elke pagina met het directe antwoord, gebruik vraagvormige tussenkoppen waar dat natuurlijk is, houd antwoordblokken kort voordat je uitwerkt, en — dit is het enige advies met een echte studie erachter — **zet er eigen statistieken, citaten en verwijzingen naar externe bronnen in.**

### Off-site: waar de winst echt zit

Op basis van het bewijs is dit de prioriteitsvolgorde, en die is voor XMONK gunstig omdat de goedkoopste actie ook de meest effectieve is:

1. **Reviews en profielen op vergelijkingsplatforms.** Voor de Nederlandse markt: Sortlist, Clutch, Trustoo, Trustpilot, en het Google Bedrijfsprofiel. Een G2-analyse van meer dan 10.000 zoekopdrachten vond dat merken die actief zijn op reviewplatforms ongeveer drie keer hogere ChatGPT-citatiepercentages halen; G2 zelf had 22,4% invloed op software-gerelateerde vragen. Clutch en Sortlist zijn de directe Europese equivalenten met hetzelfde mechanisme. [voor de NL-platforms specifiek is geen studie gevonden — het mechanisme is hetzelfde, het cijfer niet overdraagbaar]
2. **Opgenomen worden in "beste [dienst] bureaus Nederland"-lijstjes.** Dit is waarom listicles zo zwaar wegen: een LLM behandelt een lijstje van derden als een **al-gesynthetiseerd antwoord** op precies de vraag die de gebruiker stelt ("welk bureau is het beste voor X"). Eén zelfgepubliceerde pagina kan dat structureel niet nabootsen.
3. **Merkvermeldingen boven links.** Zie de Ahrefs-correlatie hierboven: vermeldingen wegen ongeveer drie keer zo zwaar als backlinks. Cases, gastbijdragen, vakmedia, ongelinkte vermeldingen.
4. **Wikipedia en Wikidata**, mits de notabiliteit het toelaat — voor XMONK op dit moment vermoedelijk niet. Wikipedia wordt consistent genoemd als de meest geciteerde bron in AI-antwoorden, maar de precieze percentages die circuleren (27% versus 7,8%) spreken elkaar tegen, dus gebruik de richting en niet het getal.
5. **UGC-platforms.** Reddit en YouTube presteren in AI-citaties ver boven hun klassieke autoriteit. Welke van de twee nu op nummer één staat, verschilt per bron — het patroon is betrouwbaarder dan de rangorde.

### Meten

- **GA4 heeft sinds 13 mei 2026 een native "AI Assistant"-kanaal** in de Default Channel Group (medium `ai-assistant`), breed beschikbaar rond 7 juni 2026. Herkent ChatGPT, Gemini, Claude, Deepseek, Copilot en Grok. **Twee vangnetten die je moet inbouwen:** Perplexity zit er níet in en valt door naar Referral, en de wijziging is **niet retroactief** — historisch AI-verkeer blijft in de oude classificatie zitten. Bouw dus alsnog een eigen Channel Group met een regex op `chatgpt\.com|chat\.openai\.com|gemini\.google\.com|claude\.ai|perplexity\.ai|copilot\.microsoft\.com`, bóven de standaard Referral-regel.
- **Search Console heeft sinds 3 juni 2026 een generative-AI-rapport**, eerst in het VK uitgerold, met data vanaf 18 mei 2026. Het geeft impressies, pagina's, landen, apparaten en datums — **maar geen clicks, geen CTR en geen zoektermen.** Verwacht er dus geen keyword-inzicht van. [ONBEVESTIGD op de exacte uitrol per land]
- **Google Preferred Sources** (27 mei 2026) laat publishers domeinen nomineren voor AI Overviews, AI Mode en Top Stories. Nieuw en concreet genoeg om als actiepunt op te nemen. [ONBEVESTIGD]
- **Tools:** Profound (enterprise, vanaf circa $499/maand), Peec AI (midmarket, circa €89–199/maand), Otterly (instap, circa $29/maand), plus de AI-modules van Semrush en Ahrefs Brand Radar als je die suites al afneemt. Prijzen komen uit secundaire bronnen — controleer ze bij de leverancier voordat je ze doorbelast.
- **Handmatig meten** is voor een bureau van deze omvang het startpunt. De werkbare eenheid is de **prompt-run**: één antwoord, van één engine, op één prompt, op één moment, in één markt en taal. Begin met 15–30 prompts verdeeld over merk-, categorie-, vergelijkings- en probleemvragen, met **minimaal 3 runs per prompt** — LLM-antwoorden variëren tussen runs, anders dan een Google-ranking. Registreer per run: verschijnt het merk, wordt het aanbevolen of alleen genoemd, is er een link, wie verschijnt er nog, en is de beschrijving correct.

### Marktcontext

- Pew Research: gebruikers klikken door bij **8%** van de zoekopdrachten met een AI Overview, tegen **15%** zonder.
- De zero-click-ratio in de VS lag in de eerste vier maanden van 2026 op **68,01%**, tegen 60,45% in 2024.
- AI Overviews verschijnen bij meer dan 20% van alle zoekopdrachten en dat aandeel groeit.
- **De conversiecijfers voor AI-verkeer zijn onbruikbaar.** Bronnen noemen 4,4x, 23x, "15,9% conversie", "42–56% beter" — allemaal onderling onverenigbaar en zonder controleerbare dataset. Wat wél consistent is: AI-referralverkeer is nog **minder dan 1% van het totale webverkeer**. Het eerlijke verhaal is dus "klein volume, waarschijnlijk hogere kwaliteit" — zonder multiplier.

### Wat de markt zelf niet weet

Noem dit in het gesprek; het onderscheidt je van bureaus die GEO als zekerheid verkopen.

1. **Of GEO een echt vak is of herverpakte SEO** is een levend debat. Digiday en CXL publiceerden er expliciete "is dit hype"-stukken over, met citaten als: veel "GEO-experts" zijn simpelweg black-hat SEO's die zich hebben herpositioneerd op de AI-hype.
2. **Of schema causaal effect heeft op LLM-citaties** — niemand heeft dat geïsoleerd van het feit dat betere teams ook betere content schrijven.
3. **Of AI Overviews en Google Search ooit los te koppelen zijn** — nu niet, maar dat is een productbeslissing die Google kan wijzigen.
4. **Nederlandstalig AI-zoeken is nagenoeg onbestudeerd.** Het KDD-paper en alle retrieval-onderzoeken zijn op Engelstalige corpora gedaan. Of die +41% en +28% ook in het Nederlands gelden, is **niet getest**. Dat is een echt hiaat — en tegelijk de kans die in §11 staat: wie hier als eerste eigen meetdata publiceert, heeft iets wat niemand in deze markt heeft.

---

## 11. Voorstel en roadmap

### Fase 0 — quick wins, eerste twee weken

Bewust gekozen op zichtbaar resultaat tegen minimale inspanning, zodat er iets te laten zien is voordat de eerste factuur komt.

1. **DMARC repareren.** `rua=`-adres toevoegen voor rapportage, `sp=quarantine` instellen. Eén DNS-wijziging, direct effect. [GEMETEN probleem]
2. **SPF opruimen.** Vier includes terugbrengen naar wat echt gebruikt wordt, richting `-all` bewegen, het verouderde `mail.xmonk.nl`-A-record verwijderen.
3. **robots.txt controleren op de crawler-val** uit §10. Zorg dat `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `ChatGPT-User`, `Claude-User`, `Perplexity-User` en `Bingbot` toegang hebben, en controleer op `NOARCHIVE`.
4. **Profielen aanmaken op Trustoo, Sortlist, Clutch en het Google Bedrijfsprofiel**, met identieke naam-adres-telefoongegevens. Dit is de laagst hangende vrucht in het hele rapport: het dicht het gat uit §4 én levert het entiteitssignaal uit §5.
5. **LinkedIn-bedrijfspagina** aanmaken of claimen.
6. **De testimonial-pagina controleren** op Lorem-ipsum-inhoud en dat direct oplossen.
7. **Title tags herschrijven** met plaatsnamen erin, beginnend bij `/seo/` en de homepage.
8. **Bing Webmaster Tools** inrichten met sitemap en IndexNow — dit is de toegangspoort voor ChatGPT en Copilot en wordt vrijwel altijd vergeten.

### Fase 1 — fundament, maand 1 tot 3

- Volledige technische audit met directe sitetoegang (zie §12 voor de openstaande punten).
- `Organization`- en `LocalBusiness`-schema met `sameAs`-verwijzingen, gericht op het oplossen van het entiteitsconflict.
- Vier locatiepagina's voor de termen 1, 2, 4 en 6 uit §9. Aparte URL's, eigen content, geen gekopieerde tekst met een andere plaatsnaam — dat laatste is de klassieke fout bij locatiepagina's.
- De bio-pagina voor "SEO specialist Haarlem" (term 3), het dunste concurrentieveld in de lijst.
- Nulmeting AI-zichtbaarheid: 20 prompts, 3 runs per prompt, over ChatGPT, Perplexity, Google AI Mode en Claude. Dit is tegelijk het meetinstrument en het verkoopinstrument.
- GA4-kanaalgroep inrichten inclusief de Perplexity-regex.

### Fase 2 — content en autoriteit, maand 3 tot 6

- Het artikel "wat kost SEO per maand" volgens het antwoord-eerst-formaat, met prijstabel, eigen cijfers en externe bronvermeldingen — de drie ingrepen uit het KDD-paper.
- De digital-signage-positionering uitwerken: campagnedenken plus scherm, expliciet tegen de hardwareleveranciers gepositioneerd. Dit is het enige veld waar XMONK een structureel voordeel kan opbouwen.
- Cases met harde cijfers publiceren. Blauwe Monsters doet dit, XMONK niet, en het is het type content dat AI-antwoorden citeren.
- Actief outreach naar de "beste bureaus"-lijstjes.
- Een kennisbank starten in het formaat dat Blauwe Monsters al heeft — korte definitiepagina's, hoge dichtheid, makkelijk te citeren.

### Fase 3 — differentiatie, maand 6 tot 12

Hier zit het strategische antwoord op het feit dat Blauwe Monsters al vijf GEO-artikelen heeft: **niet inhalen op volume, maar iets publiceren wat zij niet hebben.**

Uit §10 blijkt dat Nederlandstalig AI-zoeken vrijwel onbestudeerd is. Alle bekende effectgroottes komen uit Engelstalig onderzoek en er is geen replicatie in het Nederlands. Dat is een gat waar XMONK in kan stappen: meet met de eigen prompt-methodologie de AI-zichtbaarheid van een gedefinieerde set Nederlandse MKB-sites, en publiceer die data. Dat levert drie dingen tegelijk op — de originele statistieken die volgens het KDD-paper het sterkste citatie-effect hebben, een reden voor vakmedia om XMONK te vermelden, en een positionering die geen enkele concurrent in deze markt heeft.

### Budgetkader

Voor context, niet als aanbod: Nederlandse bronnen noemen voor MKB-SEO ruwweg €500–€1.500 per maand, met een bredere marktrange van €250 tot €3.500, bij uurtarieven van €50–€150 en tien tot twintig uur per maand. Meerdere directe concurrenten publiceren hun prijzen openlijk, dus prijsvorming is in deze markt transparant. [ZOEK]

**Eén ding om in de gaten te houden bij de positionering:** XMONK is zelf een marketingbureau dat SEO verkoopt. Dit wordt geen gesprek over "wij weten hoe SEO werkt en u niet" — dat weet Arjen. Het wordt een gesprek over uitvoeringscapaciteit: het bureau heeft de eigen vindbaarheid nooit ingericht, waarschijnlijk omdat betaalde klanten altijd voorgingen. Dat is een respectabel en zeer gebruikelijk probleem, en het is een veel makkelijker gesprek dan een competentiediscussie.

---

## 12. Wat niet gemeten kon worden

Dit hoort in het rapport omdat het bepaalt wat je in het eerste gesprek kunt beweren en wat niet.

**Door de geblokkeerde sitetoegang niet gemeten — alsnog uitvoeren zodra de site opvraagbaar is:**

| Onderwerp | Waarom het uitmaakt |
|---|---|
| Core Web Vitals (LCP, INP, CLS) | Direct relevant gezien shared hosting zonder CDN |
| robots.txt en sitemap.xml | Bevat mogelijk de crawler-val uit §10 |
| Bestaande schema-implementatie | Bepaalt of §10's aanbevelingen nieuw of correctief zijn |
| Meta descriptions, koppenstructuur, interne links | Basis on-page-audit |
| Werkelijk aantal geïndexeerde pagina's | Bestaat er wél een blog die niet vindbaar is? |
| CMS, thema, pagebuilder, pluginlast | Bepaalt de haalbaarheid van technische ingrepen |
| Mobiele weergave en HTTPS-configuratie | Basishygiëne |
| De Lorem-ipsum-verdenking op de testimonial-pagina | Direct pijnlijk als het waar is |

**Alleen te meten met toegang van de klant:** Google Analytics en Search Console (werkelijk verkeer, huidige zoektermen, indexatiedekking), het Google Bedrijfsprofiel, historische ranking-data, huidige conversies en leadvolume.

**Alleen te meten met betaalde tools:** werkelijke zoekvolumes per keyword, echte ranking-posities, backlinkprofiel en domeinautoriteit van XMONK en de concurrenten, en hun daadwerkelijke publicatiefrequentie.

**Bewust niet in dit rapport opgenomen:** het KvK-nummer (niet te verifiëren), zoekvolumes (geen tool beschikbaar, niet verzonnen), ranking-posities (het zoekhulpmiddel is geen SERP-scraper), en de teamgrootte van XMONK (onbekend).

---

## 13. Bronnen

**Onderzoek en primaire bronnen**
- [GEO: Generative Engine Optimization (KDD 2024) — arXiv:2311.09735](https://arxiv.org/pdf/2311.09735)
- [Ahrefs — AI Overview brand correlation study, 75.000 merken](https://ahrefs.com/blog/ai-overview-brand-correlation/)
- [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google Developers — Grounding with Google Search](https://developers.googleblog.com/en/gemini-api-and-ai-studio-now-offer-grounding-with-google-search/)
- [Apple Support — About Applebot](https://support.apple.com/en-us/119829)
- Nog te lezen (niet opvraagbaar in deze sessie, mogelijk de eerste echte opvolgers van het KDD-paper): [arXiv:2606.20065](https://arxiv.org/pdf/2606.20065), [arXiv:2605.28565](https://arxiv.org/pdf/2605.28565), [arXiv:2606.07130](https://arxiv.org/pdf/2606.07130)

**Platformwijzigingen 2026**
- [Search Engine Journal — Google drops FAQ rich results](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/) · [Search Engine Land](https://searchengineland.com/google-to-no-longer-support-faq-rich-results-476957)
- [Search Engine Journal — GA4 adds AI Assistant channel](https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/) · [Semrush](https://www.semrush.com/blog/ga4-adds-ai-assistant-channel/)
- [PPC Land — Search Console generative AI reports](https://ppc.land/google-finally-gives-search-console-its-own-generative-ai-visibility-reports/)
- [9to5Google — Preferred Sources](https://9to5google.com/2026/05/27/google-ai-mode-preferred-sources/)
- [Search Engine Land — Query fan-out](https://searchengineland.com/guide/query-fan-out)
- [Search Engine Land — Zero-click searches 2026](https://searchengineland.com/google-zero-click-searches-2026-study-479717)

**Crawlers en llms.txt**
- [Search Engine Land — Anthropic Claude bots](https://searchengineland.com/anthropic-claude-bots-470171)
- [Am I Cited — GPTBot vs OAI-SearchBot](https://www.amicited.com/blog/gptbot-vs-oai-searchbot/)
- [Baseline Labs — Google over llms.txt](https://baselinelabs.ai/blog/llms-txt-google-search) · [presenc.ai — State of llms.txt 2026](https://presenc.ai/research/state-of-llms-txt-2026)
- [ZipTie — Hoe Perplexity werkt](https://ziptie.dev/blog/how-perplexity-ai-answers-work/)
- [Profound — Claude web search en Brave](https://www.tryprofound.com/blog/what-is-claude-web-search-explained)

**Kritische tegengeluiden (bewust opgenomen)**
- [Digiday — GEO hype busted](https://digiday.com/media/geo-hype-busted-experts-call-it-more-seo-than-new-discipline/)
- [CXL — Is AEO/GEO just SEO hype](https://cxl.com/blog/aeo-geo-seo-reality-check/)
- [Daniel K Cheung — Schema en AI-citaties, bewijsreview](https://www.danielkcheung.com/musings/schema-ai-citations-evidence-review)

**Meetmethodologie**
- [Search Engine Land — Prompt-level visibility meten](https://searchengineland.com/measure-prompt-level-visibility-ai-search-481577)
- [Aleyda Solis — AI search prompt library opbouwen](https://www.aleydasolis.com/en/ai-search/ai-search-prompt-library/)

**XMONK en concurrenten**
- [xmonk.nl](https://xmonk.nl/) · [/seo/](https://xmonk.nl/seo/) · [/digital-signage/](https://xmonk.nl/digital-signage/) · [/contact/](https://xmonk.nl/contact/)
- [LinkedIn — Arjen van Leeuwen](https://www.linkedin.com/in/arjenleeuwen/)
- [Ad Your Service — diensten](https://www.adyourservice.nl/onze-diensten/) · [OpenKVK 77793811](https://openkvk.nl/openkvk/hoofdvestiging-77793811-0000-ad-your-service-bv) · [FONK150-vermelding](https://www.adyourservice.nl/blog/online-marketing/fonk150-2023-een-klantonderzoek/)
- [Blauwe Monsters — het verhaal](https://blauwemonsters.nl/over-ons/het-verhaal) · [diensten](https://blauwemonsters.nl/diensten) · [Van SEO naar GEO](https://blauwemonsters.nl/blog/van-seo-naar-geo) · [AI geeft de antwoorden](https://blauwemonsters.nl/blog/ai-geeft-de-antwoorden-maar-seo-bepaalt-wie-ze-levert)
- [Consultancy.nl — 4NG neemt Blauwe Monsters over](https://www.consultancy.nl/nieuws/48577/4ng-versterkt-performance-marketing-capaciteiten-met-overname-blauwe-monsters) · [Wagenhof — verhuizing naar Haarlem](https://wagenhof.nl/nieuws/blauwe-monsters-verhuist-naar-haarlem/)
- [LYNX Media, Cruquius](https://lynx-media.nl/website-laten-maken)

**Nederlandse markt- en prijscontext**
- [Stramark — SEO-kosten 2026](https://www.stramark.nl/blog/seo-kosten/) · [Searchlab](https://searchlab.nl/kosten/wat-kost-seo-uitbesteden) · [Opklopper](https://opklopper.nl/blog/seo-kosten) · [Whello](https://whello.nl/marketing-tips/seo/wat-kost-seo)
- [Ralf van Veen — SEO Haarlemmermeer](https://ralfvanveen.com/seo-specialist-haarlemmermeer/) · [Marketingbureau Hoofddorp](https://marketingbureauhoofddorp.nl/)

---

*Onderzoek uitgevoerd 28 juli 2026. Alle DNS-metingen zijn op die datum verricht en kunnen wijzigen. Alle uitspraken over websitecontent zijn gebaseerd op zoekresultaten, niet op directe inspectie — zie §0 en §12.*
