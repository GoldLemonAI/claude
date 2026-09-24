# AI-scan: wie is het antwoord bij "LinkedIn-autoriteit voor B2B-MKB in Nederland"?

Scan uitgevoerd: 24 september 2026
Methode: Answermark-scan (zie hoofdstuk 2)
Voor: Robin van Schaik, Gold Lemon en Answermark
Databestanden: `rapporten/data/` (prompts, alle 120 antwoorden, ranglijst, script)

## 1. Samenvatting

We stelden 30 vragen over LinkedIn-autoriteit, personal branding en LinkedIn-bureaus voor B2B-MKB aan vier AI-zoekmachines: ChatGPT, Perplexity, Gemini en Google AI Mode. Dat leverde 120 antwoorden op. In die antwoorden werden 506 verschillende partijen bij naam genoemd. De top 20 hieronder is de lijst van partijen die AI het vaakst noemt en het vaakst als bron gebruikt.

Het antwoord op de vraag "wie is het antwoord" is GHO Agency. Zij worden in 23 van de 120 antwoorden genoemd en hun eigen site wordt 26 keer als bron aangehaald. Geen enkele andere partij komt daar in de buurt.

Gold Lemon staat op plaats 6. Dat is de hoogste positie van een breed B2B-bureau dat niet uitsluitend LinkedIn doet. De keerzijde: alle 10 vermeldingen komen van ChatGPT en Perplexity. Gemini en Google AI Mode noemen Gold Lemon geen enkele keer, en halen goldlemon.nl ook nergens als bron aan.

Answermark en Robin van Schaik komen in geen van de 120 antwoorden voor. De vragen over AI-zichtbaarheid en GEO (P18, P26) leveren een versnipperd beeld op zonder dominante partij. Die categorie is nog van niemand.

## 2. Meetmethode

### Promptset

30 prompts in het Nederlands, verdeeld over drie categorieën. Elke prompt is aan alle vier engines gesteld, letterlijk hetzelfde.

| Categorie | Aantal | Waar het over gaat |
|---|---|---|
| Bureau | 12 (P01-P12) | Een bedrijf zoekt een bureau, ghostwriter, trainer of specialist voor LinkedIn |
| Expert | 8 (P13-P20) | Wie zijn de experts, wie moet je volgen, wie is een voorbeeld |
| Hoe | 10 (P21-P30) | Hoe bouw je autoriteit op, hoe vaak posten, wat kost het, met vraag naar bronnen |

De volledige lijst staat in `rapporten/data/prompts.json`. Geen enkele prompt noemt Gold Lemon, Answermark of een concurrent bij naam.

### Engines en instellingen

| Engine | Via | Model en instellingen |
|---|---|---|
| ChatGPT | DataForSEO LLM Responses | gpt-4o, webzoeken geforceerd aan, land NL, temperatuur 0,3 |
| Perplexity | DataForSEO LLM Responses | sonar, land NL, temperatuur 0,3 |
| Gemini | DataForSEO LLM Responses | gemini-3.5-flash, webzoeken aan (landinstelling niet beschikbaar) |
| Google AI Mode | DataForSEO SERP API | Nederland, taal Nederlands, desktop |

Elke prompt is één keer per engine gesteld, op 24 september 2026 tussen 17:50 en 18:30. Kosten van de 120 calls plus vijf testcalls: 5,07 dollar aan DataForSEO-tegoed.

### Wat we tellen

Per antwoord leggen we twee dingen vast.

1. Welke partijen bij naam genoemd worden in de antwoordtekst, in volgorde van eerste vermelding. Bureaus, personen, platforms (zoals Sortlist of Frankwatching) en tools tellen mee. LinkedIn, Google, ChatGPT en soortgelijke platforms die het onderwerp zelf zijn tellen niet mee.
2. Welke domeinen als bron worden aangehaald (de bronvermeldingen of citaties die de engine meegeeft).

Namen zijn genormaliseerd zodat "WADM | B2B Agency" en "WADM" dezelfde partij zijn. De extractie is per antwoord door een taalmodel gedaan en daarna met een script gecontroleerd op dubbelingen.

### De vier meetcriteria

| Criterium | Wat het meet | Gewicht in score |
|---|---|---|
| Vermeldingsgraad | Aandeel van de 120 antwoorden waarin de partij bij naam wordt genoemd | 60% |
| Citatiegraad | Aandeel van de 120 antwoorden waarin het eigen domein van de partij als bron wordt aangehaald | 25% |
| Positie | Elke vermelding telt 1 gedeeld door de positie in het antwoord (als eerste genoemd is 1, als vijfde 0,2), opgeteld en gedeeld door 120 | 15% |
| Enginedekking | In hoeveel van de vier engines de partij minstens één keer voorkomt | apart gerapporteerd, geen gewicht |

Score = 100 × (0,60 × vermeldingsgraad + 0,25 × citatiegraad + 0,15 × positie). Een partij die in alle 120 antwoorden als eerste genoemd zou worden en overal geciteerd, scoort 100.

Waarom deze gewichten: genoemd worden is waar het om gaat, dus dat weegt het zwaarst. Geciteerd worden zegt of de engine jouw eigen site leest of dat hij je kent via een lijst van een ander. Positie corrigeert voor het verschil tussen "als eerste aanbevolen" en "ergens onderaan in een lijst van veertien".

### Beperkingen

- Eén run per prompt. AI-antwoorden verschillen per keer. In een testrun vóór de scan noemde Google AI Mode bij P01 wel Gold Lemon, in de scanrun niet. Kleine verschillen in de ranglijst zijn ruis; de grote lijnen zijn stabiel.
- De ChatGPT-antwoorden komen van gpt-4o via de API met webzoeken, niet uit de consumentenapp. De consumentenapp gebruikt een nieuwer model en eigen zoekinstellingen.
- Gemini kon niet op Nederland worden ingesteld. De prompts zijn Nederlands, dus de antwoorden zijn overwegend Nederlands, maar Gemini haalt vaker internationale bronnen aan.
- 30 prompts, geen 50. De standaardscan van Answermark gebruikt er 50 of meer. Voor een eerste beeld van de markt is 30 voldoende; voor een klantrapport doen we 50.
- Bij een aantal antwoorden van ChatGPT en Gemini is de tekst afgekapt door de tokenlimiet. Partijen die daarna genoemd zouden zijn, ontbreken.

## 3. De top 20

Vermeld in = aantal antwoorden (van 120) met de naam. Eigen site geciteerd = aantal antwoorden met het eigen domein als bron. Gem. positie = gemiddelde plek in de volgorde van genoemde partijen. De vier enginekolommen geven het aantal antwoorden per engine (van 30).

| # | Partij | Type | Vermeld in | Vermeldingsgraad | Eigen site geciteerd | Gem. positie | Engines | ChatGPT | Perplexity | Gemini | Google AI Mode | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GHO Agency | bureau | 23 | 19.2% | 26 | 2.8 | 3/4 | 0 | 8 | 10 | 5 | 18.4 |
| 2 | Corinne Keijzer | persoon | 18 | 15.0% | 6 | 4.7 | 4/4 | 3 | 3 | 7 | 5 | 11.0 |
| 3 | Frankwatching | platform | 11 | 9.2% | 20 | 5.9 | 4/4 | 1 | 3 | 5 | 2 | 10.2 |
| 4 | Searchlab | bureau | 9 | 7.5% | 20 | 3.2 | 3/4 | 0 | 5 | 2 | 2 | 9.2 |
| 5 | Solvex | bureau | 11 | 9.2% | 11 | 1.7 | 3/4 | 5 | 5 | 0 | 1 | 8.8 |
| 6 | Gold Lemon | bureau | 10 | 8.3% | 13 | 3.6 | 2/4 | 5 | 5 | 0 | 0 | 8.5 |
| 7 | iReclam | bureau | 11 | 9.2% | 11 | 3.7 | 2/4 | 10 | 1 | 0 | 0 | 8.4 |
| 8 | YouLynq.me | bureau | 11 | 9.2% | 12 | 5.4 | 4/4 | 2 | 1 | 7 | 1 | 8.4 |
| 9 | Richard van der Blom | persoon | 13 | 10.8% | 3 | 4.2 | 4/4 | 3 | 3 | 4 | 3 | 8.3 |
| 10 | Sortlist | platform | 8 | 6.7% | 17 | 4.9 | 3/4 | 1 | 4 | 0 | 3 | 7.9 |
| 11 | Personally | bureau | 10 | 8.3% | 7 | 2.8 | 3/4 | 0 | 2 | 6 | 2 | 7.3 |
| 12 | Sandra Stassar | persoon | 10 | 8.3% | 9 | 7.1 | 4/4 | 2 | 1 | 5 | 2 | 7.1 |
| 13 | Social Selling Coach | bureau | 9 | 7.5% | 10 | 4.8 | 3/4 | 2 | 0 | 6 | 1 | 7.0 |
| 14 | Sculpt Studios | bureau | 7 | 5.8% | 14 | 3.7 | 4/4 | 2 | 3 | 1 | 1 | 7.0 |
| 15 | Victor Huiting | persoon | 10 | 8.3% | 6 | 6.1 | 4/4 | 1 | 1 | 6 | 2 | 6.5 |
| 16 | Digital Moves | bureau | 9 | 7.5% | 7 | 3.8 | 4/4 | 3 | 1 | 4 | 1 | 6.5 |
| 17 | Dapper | bureau | 10 | 8.3% | 3 | 5.6 | 4/4 | 3 | 2 | 3 | 2 | 6.1 |
| 18 | MagicPost | platform | 4 | 3.3% | 19 | 12.0 | 3/4 | 1 | 1 | 2 | 0 | 6.1 |
| 19 | Whello | bureau | 8 | 6.7% | 8 | 5.6 | 4/4 | 1 | 2 | 4 | 1 | 6.0 |
| 20 | Marketingfacts | platform | 6 | 5.0% | 12 | 7.7 | 3/4 | 1 | 3 | 2 | 0 | 5.6 |

Plaats 21 tot 30:

21. Michiel Verstraten (persoon, 5x, score 5.1)
22. Carolina Posma (persoon, 2x, score 5.0)
23. Marjolein Bongers (persoon, 9x, score 4.9)
24. Rene Schipper (persoon, 6x, score 4.9)
25. Frank Husmann (persoon, 5x, score 4.9)
26. Jorrit Drieënhuizen (persoon, 5x, score 4.8)
27. Doelgroep Bereikt (bureau, 5x, score 4.5)
28. Jan van Musscher (persoon, 1x, score 4.5)
29. Just Connecting (bureau, 8x, score 4.4)
30. Red Panda Works (bureau, 8x, score 4.4)

Nog 476 partijen werden één tot vier keer genoemd. Daar zit de lange staart: eenmanszaken, regionale bureaus en internationale namen die door één engine één keer worden genoemd.

## 4. Wat opvalt

### GHO Agency wint op eigen kracht

GHO Agency wordt geciteerd via hun eigen pagina's: de dienstenpagina over LinkedIn-marketing (9 keer), en blogs over ghostwriting, personal branding en waarom CEO's kiezen voor ghostwriting (samen 17 keer). Perplexity, Gemini en Google AI Mode lezen die pagina's en nemen ze over. Het is het schoolvoorbeeld van wat Answermark bouwt: eigen content die precies de vraag beantwoordt die een koper aan AI stelt. Opvallend is dat ChatGPT ze nul keer noemt. ChatGPT leunt op iReclam en op de lijsten van Sortlist.

### Personen winnen de expertvragen, bureaus de bureauvragen

Corinne Keijzer en Richard van der Blom staan hoog omdat ze de acht expertprompts domineren (13 en 10 vermeldingen). Bij de bureauprompts komen ze nauwelijks voor. Andersom geldt hetzelfde: GHO Agency, Searchlab, iReclam, Gold Lemon en Whello halen hun vermeldingen bij de bureauprompts. Alleen Solvex en YouLynq.me scoren in alle drie categorieën.

| Partij | bureau-prompts (12) | expert-prompts (8) | hoe-prompts (10) |
|---|---|---|---|
| GHO Agency | 15 | 2 | 6 |
| Corinne Keijzer | 1 | 13 | 4 |
| Frankwatching | 0 | 3 | 8 |
| Searchlab | 8 | 0 | 1 |
| Solvex | 4 | 2 | 5 |
| Gold Lemon | 7 | 0 | 3 |
| iReclam | 8 | 1 | 2 |
| YouLynq.me | 6 | 3 | 2 |
| Richard van der Blom | 1 | 10 | 2 |
| Sortlist | 7 | 1 | 0 |
| Personally | 6 | 4 | 0 |
| Sandra Stassar | 6 | 4 | 0 |
| Social Selling Coach | 2 | 5 | 2 |
| Sculpt Studios | 3 | 0 | 4 |
| Victor Huiting | 2 | 6 | 2 |
| Digital Moves | 1 | 8 | 0 |
| Dapper | 7 | 2 | 1 |
| MagicPost | 0 | 1 | 3 |
| Whello | 7 | 1 | 0 |
| Marketingfacts | 0 | 1 | 5 |

### Elke engine heeft eigen favorieten

- ChatGPT noemt iReclam in 10 van 30 antwoorden. Geen andere engine noemt ze meer dan één keer.
- Perplexity leunt op Sortlist, Searchlab, GHO Agency en Gold Lemon.
- Gemini leunt op GHO Agency, YouLynq.me, Personally en op YouTube: 10 van 30 Gemini-antwoorden citeren een YouTube-video.
- Google AI Mode citeert in 27 van 30 antwoorden een LinkedIn-pagina. Het noemt gemiddeld maar 4,7 partijen per antwoord, tegen 8 tot 10 bij de andere engines. Wie hier genoemd wil worden, moet op LinkedIn zelf vindbaar zijn met de juiste woorden.

Van de top 20 komen 12 partijen in alle vier engines voor. Gold Lemon en iReclam zijn de enige twee in de top 10 die in maar twee engines voorkomen.

### LinkedIn zelf is de grootste bron

| Domein | Antwoorden | ChatGPT | Perplexity | Gemini | Google AI Mode |
|---|---|---|---|---|---|
| nl.linkedin.com | 52 | 18 | 14 | 0 | 20 |
| linkedin.com | 36 | 9 | 20 | 0 | 7 |
| gho.agency | 26 | 0 | 9 | 11 | 6 |
| frankwatching.com | 20 | 1 | 7 | 9 | 3 |
| searchlab.nl | 20 | 0 | 12 | 4 | 4 |
| magicpost.in | 19 | 2 | 8 | 6 | 3 |
| sortlist.nl | 17 | 2 | 10 | 0 | 5 |
| sculptstudios.nl | 14 | 4 | 8 | 1 | 1 |
| goldlemon.nl | 13 | 4 | 9 | 0 | 0 |
| favikon.com | 13 | 2 | 3 | 6 | 2 |
| youlynq.me | 12 | 1 | 1 | 9 | 1 |
| marketingfacts.nl | 12 | 2 | 7 | 3 | 0 |
| ireclam.nl | 11 | 10 | 1 | 0 | 0 |
| solvex.nl | 11 | 5 | 5 | 0 | 1 |
| frankhusmann.nl | 11 | 0 | 3 | 7 | 1 |
| managementboek.nl | 10 | 2 | 3 | 5 | 0 |
| socialsellingcoach.nl | 10 | 2 | 0 | 6 | 2 |
| youtube.com | 10 | 0 | 0 | 10 | 0 |
| doelgroepbereikt.nl | 9 | 1 | 3 | 3 | 2 |
| thesuccessagency.nl | 9 | 2 | 3 | 2 | 2 |

De pagina's op nl.linkedin.com en linkedin.com worden in 88 van de 120 antwoorden aangehaald: profielen, bedrijfspagina's en Pulse-artikelen. Daarna komen de eigen sites van bureaus (gho.agency, searchlab.nl, goldlemon.nl) en de lijsten en vakmedia (Frankwatching, Sortlist, MagicPost, Favikon, Marketingfacts). Frankwatching wordt geciteerd via een handvol artikelen over thought leadership op LinkedIn uit 2025, plus één artikel uit mei 2026 over hoe je in AI-antwoorden terechtkomt.

## 5. Gold Lemon: waar het staat en waar het ontbreekt

| Prompt | Engine | Positie Gold Lemon | Aantal partijen genoemd | goldlemon.nl als bron |
|---|---|---|---|---|
| P01 | chatgpt | 5 | 14 | ja |
| P01 | perplexity | 1 | 11 | ja |
| P04 | perplexity | - | 6 | ja |
| P09 | chatgpt | 1 | 9 | ja |
| P09 | perplexity | 1 | 8 | ja |
| P10 | chatgpt | 1 | 8 | ja |
| P10 | perplexity | 1 | 7 | ja |
| P12 | perplexity | 8 | 8 | ja |
| P15 | perplexity | - | 1 | ja |
| P21 | perplexity | - | 6 | ja |
| P22 | perplexity | - | 0 | ja |
| P26 | chatgpt | 11 | 11 | nee |
| P26 | perplexity | 4 | 5 | ja |
| P27 | chatgpt | 3 | 3 | ja |

Wat goed gaat:

- Bij drie bureauprompts staat Gold Lemon op positie 1 bij zowel ChatGPT als Perplexity: de Haarlem-vraag (P09), de combinatie LinkedIn met SEO en AI-zichtbaarheid (P10) en de openingsvraag over autoriteit opbouwen (P01, alleen bij Perplexity op 1).
- Gold Lemon wordt vijf keer als eerste genoemd. Alleen Richard van der Blom, GHO Agency en Solvex scoren daar hoger.
- Bij P27 (wat kost het) noemt ChatGPT de pakketprijs van 2.495 euro per maand. De prijzen op de site worden dus gelezen en overgenomen.
- De geciteerde pagina's zijn de B2B-marketingbureaupagina (6 keer), de autoriteitspagina (4 keer) en de contentmarketingpagina (3 keer).

Wat ontbreekt:

- Nul vermeldingen bij Gemini en Google AI Mode. Gemini leest YouTube, Favikon, MagicPost en de eigen sites van bureaus. Google AI Mode leest LinkedIn. Gold Lemon is op geen van die plekken aanwezig met de woorden die deze prompts gebruiken.
- Nul vermeldingen bij de acht expertprompts. Robin van Schaik komt nergens voor. De bureaunaam wordt gelezen, de persoon niet.
- Geen Sortlist-profiel in de geciteerde lijsten. Sortlist wordt 17 keer aangehaald en is de belangrijkste externe bron voor Perplexity en Google AI Mode bij bureauvragen.

## 6. Answermark: een lege categorie

Prompt P18 (welke Nederlandse marketeers zijn autoriteit op AI-zichtbaarheid en GEO) en P26 (hoe combineer je LinkedIn-autoriteit met vindbaarheid in ChatGPT en Google AI) leveren per engine een andere lijst op, zonder overlap. Er is geen partij die deze vragen in meer dan één engine wint. Gold Lemon wordt bij P26 genoemd door ChatGPT (positie 11) en Perplexity (positie 4). Answermark komt nergens voor.

Dat is geen slecht nieuws. Het betekent dat de categorie waarin Answermark actief is nog geen antwoord heeft. De partij die er als eerste consequent over publiceert met eigen data, wordt dat antwoord.

## 7. Wat dit betekent voor het LinkedIn-plan

De scan bevestigt de kern van het plan van 18 september: LinkedIn is de grootste bron voor AI-antwoorden over dit onderwerp, en personen winnen de expertvragen. Vijf aanvullingen op basis van de cijfers:

1. Maak het LinkedIn-profiel van Robin en de bedrijfspagina vindbaar op de exacte termen uit deze prompts: autoriteit op LinkedIn, B2B-MKB, thought leadership, founder-led content. Google AI Mode leest die pagina's letterlijk.
2. Zet een Sortlist-profiel op met reviews. Dat is de kortste weg naar Perplexity en Google AI Mode bij bureauvragen.
3. Schrijf één gastartikel voor Frankwatching over autoriteit en AI-zichtbaarheid. Frankwatching wordt 20 keer geciteerd en is de belangrijkste bron bij de hoe-vragen.
4. Publiceer deze scan als eerste Answermark-onderzoek, en herhaal hem maandelijks. Wie de data levert over wie het antwoord is, wordt zelf het antwoord bij P18 en P26.
5. Overweeg YouTube-schermopnames van de Marktradar-posts. Gemini citeert YouTube in een derde van zijn antwoorden.

## 8. Bijlagen

- `rapporten/data/prompts.json`: de 30 prompts.
- `rapporten/data/antwoorden/<engine>/P01.json` t/m `P30.json`: per antwoord de volledige tekst, de genoemde partijen in volgorde en de aangehaalde bronnen.
- `rapporten/data/result.json`: de volledige ranglijst van 506 partijen en de brondomeinen.
- `rapporten/data/aggregate.py`: het script dat de ranglijst berekent.
