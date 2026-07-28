# Rapporten

Onderzoeks- en auditrapporten voor inbound leads en klanten.

## XMONK (xmonk.nl) — juli 2026

Inbound formulieraanvraag van Arjen van Leeuwen (XMONK, Cruquius) voor SEO en GEO, ingediend 27 juli 2026.

| Bestand | Voor wie | Inhoud |
|---|---|---|
| [rapporten/xmonk/xmonk-seo-geo-rapport-klantversie.md](rapporten/xmonk/xmonk-seo-geo-rapport-klantversie.md) | **de klant** | Deelbare versie: bevindingen, concurrentieanalyse, keywordadvies, GEO-hoofdstuk, roadmap |
| [rapporten/xmonk/xmonk-seo-geo-audit.md](rapporten/xmonk/xmonk-seo-geo-audit.md) | intern | Volledige audit inclusief verkoophoek, leadprofiel en CRM-status |
| [rapporten/xmonk/gespreksnotitie.md](rapporten/xmonk/gespreksnotitie.md) | **intern** — niet delen | Eén pagina: opener, de drie kernpunten, wat uitvragen, wat níet beweren |

PDF's in de Gold Lemon-huisstijl staan in [rapporten/xmonk/pdf/](rapporten/xmonk/pdf/) en worden gegenereerd met [tools/build_pdf.py](tools/build_pdf.py):

```
python3 tools/build_pdf.py <input.md> <output.pdf> --ondertitel "..."
```

Vereist `pip install weasyprint markdown` en `apt-get install fonts-montserrat`.

**Kern:** XMONK verkoopt SEO maar is onvindbaar voor elke commerciële term die het aanbiedt — inclusief in het eigen dorp. Staat op geen enkel vergelijkingsplatform, heeft geen contentmotor, en de merknaam botst in de zoekresultaten met een ongerelateerd buitenlands bedrijf. De drie keywords die ze zelf opgaven zijn niet haalbaar; er ligt een vervangende lijst van tien.

**Belangrijke leesinstructie:** xmonk.nl kon niet direct worden opgevraagd (netwerkbeleid van de werkomgeving blokkeerde alle uitgaande HTTP-verzoeken). Uitspraken over de website komen uit zoekresultaten, niet uit inspectie van de pagina's. Alleen de DNS- en e-mailbevindingen zijn zelf gemeten. Elke bevinding in het rapport heeft een betrouwbaarheidslabel — zie §0.
