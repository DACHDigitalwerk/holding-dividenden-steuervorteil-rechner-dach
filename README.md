# ??? DACH Holding-Steuervorteil-, ? 8b KStG Schachtelprivileg-, ? 10 KStG (AT) & CH-Beteiligungsabzug-Rechner 2026

[![Live Web-App](https://img.shields.io/badge/Live_Web--App-Holding_&_?_8b_KStG_Rechner_2026-4f46e5?style=for-the-badge)](https://dachdigitalwerk.github.io/holding-dividenden-steuer-rechner/)
[![DACH CFO Hub](https://img.shields.io/badge/DACH_CFO_&_Tax_Hub-38_Kostenlose_Rechner-10b981?style=for-the-badge)](https://dachdigitalwerk.github.io/)

Open-Source Python-Engine & interaktiver Online-Rechner zur Berechnung des **Holding-Steuervorteils (Operative GmbH/AG + Mutter-Holding vs. Privatentnahme)** f?r **Deutschland (`? 8b Abs. 1, 2 & 5 KStG` / `? 9 Nr. 2a GewStG`)**, **?sterreich (`? 10 Abs. 1 KStG`)** und die **Schweiz (`Art. 69 & 70 DBG Beteiligungsabzug`)**.

?? **Direkt zum kostenlosen Online-Rechner (100 % Browser-basiert & DIN-A4 PDF-Dossier):**
- **[DACH Holding-Steuervorteil- & ? 8b KStG Schachtelprivileg-Rechner 2026](https://dachdigitalwerk.github.io/holding-dividenden-steuer-rechner/)**
- **[Fachratgeber: Holding gr?nden & ? 8b KStG (95 % steuerfrei / 10 % vs. 15 % Quote)](https://dachdigitalwerk.github.io/holding-dividenden-steuer-rechner/holding-gruenden-steuervorteil-8b-kstg-95-prozent-rechner-2026.html)**
- **[Fachratgeber: GmbH-Verkauf & Exit ?ber Holding (~1,54 % Steuer & 7-Jahres-Sperrfrist)](https://dachdigitalwerk.github.io/holding-dividenden-steuer-rechner/veraeusserungsgewinn-gmbh-verkauf-holding-exit-steuer-1-5-prozent.html)**
- **[Fachratgeber: Holding ?sterreich (? 10 KStG 0 %) vs. Schweiz (Art. 69 DBG)](https://dachdigitalwerk.github.io/holding-dividenden-steuer-rechner/holding-oesterreich-10-kstg-schweiz-beteiligungsabzug-vergleich-2026.html)**

---

## ? Features (Rechtsstand 2026)

1. **???? Deutschland (`? 8b Abs. 1, 2 & 5 KStG`):**
   - Automatische Schwellenpr?fung f?r Streubesitz (`< 10 %`), KSt-Schachtelprivileg ohne Gewerbesteuerk?rzung (`10 % bis < 15 %`) und volles KSt-/GewSt-Schachtelprivileg (`>= 15 %`, effektive Holding-Steuerlast nur **~1,54 %**).
   - Unternehmensverkauf (Share Deal nach `? 8b Abs. 2 KStG`): **95 % steuerfrei** auch unter 10 % Beteiligungsquote!
2. **???? ?sterreich (`? 10 Abs. 1 Z 1 KStG`):**
   - **100 % steuerfreie Beteiligungsertr?ge (`0,00 %` Holding-Steuer)** ohne 5-%-Betriebsausgabenfiktion.
3. **???? Schweiz (`Art. 69 & 70 DBG`):**
   - Beteiligungsabzug f?r qualifizierte Beteiligungen ab 10 % Quote.
4. **?? Mehrj?hriger Zinseszins- & Reinvestitions-Simulator (5?30 Jahre):**
   - Ber?cksichtigt laufende Holding-Verwaltungskosten (steuerlich abzugsf?hig) sowie Brutto-Endverm?gen in der Holding und Netto-Endverm?gen nach finaler Privataussch?ttung.

---

## ?? Schnellstart & Tests

```bash
pip install -e .
pytest -v
dach-holding --country DE --ebt 200000 --share 100 --years 15 --exit-gain 1000000
```

---

## ?? Rechtlicher Hinweis (? 2 RDG / ? 5 StBerG / BGH I ZR 226/20 ? Smartlaw)

Dieses Software-Paket und die zugeh?rige Web-Applikation dienen ausschlie?lich der regelbasierten mathematisch-schematischen Kalkulation und stellen keine individuelle Rechts- oder Steuerberatung dar.
