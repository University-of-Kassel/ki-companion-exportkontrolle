---
id: "KF-03f"
title: "US-(Re-)Exportkontrollrecht: Grundlagen"
version: "1.0-public.1"
status: "draft"
last_reviewed: "2026-07-02"
review_cycle: null
profiles:
  - "researcher"
scope: "Hochschulen und Forschungseinrichtungen; Schwerpunkt Deutschland/EU"
document_type: "Kuratierte Knowledge File Exportkontrolle"
related: []
knowledge_area: null
purpose: "Grundbegriffe und Einordnung des US-(Re-)Exportkontrollrechts für Exportkontrollvorgänge im Hochschulkontext."
binding: "Orientierung und Fallstrukturierung; keine Rechtsberatung, keine abschließende US-rechtliche Prüfung,\
  \ keine Freigabeentscheidung."
---

<!-- SPDX-License-Identifier: Apache-2.0; Public adaptation 2026-10-22; source version 1.0; editorial adaptation, not a new legal review. -->

# KF-03f – US-(Re-)Exportkontrollrecht: Grundlagen


---

## 1. Warum US-(Re-)Exportkontrollrecht für eine deutsche Universität relevant sein kann

US-Exportkontrollrecht kann auch bei Vorgängen außerhalb der USA relevant werden. Für deutsche Hochschulen ist das vor allem dann wichtig, wenn ein Forschungsvorhaben, ein Gerät, eine Software, technische Daten, ein Cloud-/IT-Dienst, ein Vertrag oder eine Person einen US-Bezug hat.

Typische Beispiele:

- ein Messgerät, Sensor, Chip, Laser, Rechner, Bauteil oder Prototyp hat US-Ursprung,
- ein in Deutschland gebautes System enthält kontrollierte US-Komponenten,
- eine Software, Firmware, Datenbank, Cloud-Leistung oder Lizenz stammt von einem US-Anbieter,
- technische Unterlagen, Quellcode, Handbücher, Trainingsdaten, Spezifikationen oder Designinformationen stammen von einem US-Hersteller,
- ein Projektvertrag enthält US-export-control-, sanctions-, reexport- oder prohibited-country-Klauseln,
- eine US-Person ist im Projekt tätig,
- eine internationale Kooperation betrifft sanktionierte, gelistete oder militärnahe Einrichtungen,
- Technologiezugänge werden für internationale Forschende, Gastwissenschaftler:innen oder Projektpartner geöffnet,
- ein Vorgang betrifft Hochrisikoländer oder sensible Endverwendungen.

**Grundsatz für KI-Companion Exportkontrolle:** US-Recht wird nicht in jedem Vorgang vollständig geprüft. Es wird als zusätzlicher Prüf- und Eskalationsstrang berücksichtigt, wenn ein US-Bezug erkennbar ist.

---

## 2. Zentrale US-Regelungsstränge

### 2.1 EAR / BIS

Die **Export Administration Regulations (EAR)** werden vom **Bureau of Industry and Security (BIS)** des U.S. Department of Commerce administriert. Sie betreffen Exporte, Reexporte und Transfers in-country von „items subject to the EAR“.

„Items“ meint im EAR-Kontext nicht nur physische Waren, sondern auch:

- commodities / Waren,
- software,
- technology.

Wichtige EAR-Bereiche:

- **Part 734** – Scope of the EAR: Was ist subject to the EAR?
- **Part 732** – Steps for using the EAR: Prüfsystematik.
- **Part 736** – General Prohibitions.
- **Part 738** – Commerce Country Chart.
- **Part 740** – License Exceptions.
- **Part 742** – Control Policy.
- **Part 744** – End-use and End-user Controls.
- **Part 746** – Embargoes and other special controls.
- **Part 748** – Applications and classifications.
- **Part 762** – Recordkeeping.
- **Part 774, Supplement No. 1** – Commerce Control List (CCL).

**Quelle:** BIS EAR Table of Contents: https://media.bis.gov/regulations/ear/table-of-contents

### 2.2 OFAC-Sanktionen

Das **Office of Foreign Assets Control (OFAC)** des U.S. Department of the Treasury administriert US-Sanktionsprogramme und Sanktionslisten. OFAC ist nicht dasselbe wie BIS/EAR.

OFAC-relevante Elemente:

- SDN List,
- Non-SDN Consolidated Sanctions List,
- länder- und themenbezogene Sanktionsprogramme,
- Eigentums-/Kontrollfragen,
- Verbote für U.S. persons,
- ggf. extraterritorial wirkende Sanktionsrisiken.

**Wichtig:** Bei EU-Akteuren können extraterritoriale US-Sanktionen in ein Spannungsverhältnis zum EU Blocking Statute geraten. Dies darf nicht rein operativ im Bot entschieden werden.

**Quellen:**

- OFAC Sanctions List Service: https://ofac.treasury.gov/sanctions-list-service
- OFAC Sanctions Programs and Country Information: https://ofac.treasury.gov/sanctions-programs-and-country-information

### 2.3 ITAR / DDTC

Die **International Traffic in Arms Regulations (ITAR)** werden durch die **Directorate of Defense Trade Controls (DDTC)** des U.S. Department of State administriert. ITAR betrifft insbesondere defense articles, defense services und technical data auf bzw. im Zusammenhang mit der U.S. Munitions List (USML).

Für eine deutsche Universität ist ITAR typischerweise kein Standardprüfbereich, aber ein deutlicher Eskalationshinweis, wenn Unterlagen, Geräte, Software, technische Daten oder Verträge Begriffe enthalten wie:

- ITAR,
- USML,
- defense article,
- defense service,
- technical data controlled under ITAR,
- DDTC authorization,
- no foreign persons,
- export controlled under 22 CFR parts 120-130.

**Bot-Regel:** KI-Companion Exportkontrolle soll ITAR nicht vertieft prüfen und keine ITAR-Klassifikation vornehmen. Bei ITAR-Hinweisen: hohe Eskalation und juristische/fachliche Prüfung.

**Quelle:** DDTC ITAR Overview: https://deccs.pmddtc.state.gov/deccs?id=ddtc_public_portal_itar_landing

### 2.4 Antiboycott-Regeln

Die US-Antiboycott-Regeln sind in EAR Part 760 geregelt und werden durch BIS/OAC administriert. Sie können relevant werden, wenn Verträge, Ausschreibungen, Lieferbedingungen oder Erklärungen Formulierungen enthalten, die eine Teilnahme an nicht von den USA sanktionierten Boykotten verlangen oder unterstützen.

Für Hochschulen ist das meist ein Randthema, kann aber bei internationalen Verträgen, Beschaffungen, Lieferungen, Konsortialverträgen oder Drittmittelprojekten auftauchen.

**Bot-Regel:** Bei Boycott-/Antiboycott-Klauseln nicht selbst bewerten, sondern Vertrag/juristische Prüfung empfehlen.

**Quellen:**

- BIS Office of Antiboycott Compliance: https://www.bis.gov/OAC
- eCFR Part 760: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-760

### 2.5 EU Blocking Statute

Das EU Blocking Statute schützt EU-Akteure vor der extraterritorialen Anwendung bestimmter Drittstaatengesetze. Die EU-Kommission beschreibt den Zweck der Blocking Regulation so, dass EU-Operatoren gegen extraterritoriale Anwendung von Drittstaatengesetzen geschützt werden sollen; die EU erkennt solche extraterritorialen Wirkungen grundsätzlich nicht an.

Für Hochschulen ist das wichtig, wenn US-Sanktionsrecht, US-Vertragsklauseln oder US-Restriktionen faktisch verlangen, bestimmte Kooperationen allein wegen US-Sanktionen zu unterlassen, obwohl EU-/deutsches Recht dies nicht in derselben Weise verlangt.

Besonders sensibel:

- Iran,
- Kuba,
- bestimmte US-Sanktionsklauseln,
- Vertragsvorgaben eines US-Partners oder US-Funders,
- Finanzierungs-, Zahlungs- oder Cloud-/Software-Nutzungsbedingungen.

**Bot-Regel:** Bei möglicher Kollision zwischen US-Sanktionsvorgaben und EU Blocking Statute: nicht entscheiden, sondern juristisch eskalieren.

**Quelle:** EU-Kommission, Blocking Statute: https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en

---

## 3. Zentrale Begriffe

### 3.1 „Subject to the EAR“

Der wichtigste Vorbegriff ist **subject to the EAR**. Wenn ein Item subject to the EAR ist, fällt es grundsätzlich in den Anwendungsbereich der EAR. Das bedeutet noch nicht automatisch, dass eine Genehmigung erforderlich ist.

Nach EAR Part 734 können insbesondere folgende Items subject to the EAR sein:

- alle Items in den USA,
- US-origin items, auch außerhalb der USA,
- bestimmte ausländische Items mit kontrolliertem US-Anteil nach De-minimis-Regeln,
- bestimmte foreign-produced direct products nach FDP-Regeln,
- bestimmte Items, für die BIS ausdrücklich informiert oder die EAR entsprechend geändert hat.

**Merksatz:** Subject to the EAR = Anwendungsbereich. Genehmigungspflicht = weitere Prüfung nach Klassifikation, Land, Endnutzer, Endverwendung, Listenstatus und Verboten.

**Quellen:**

- BIS – Determine what is subject to the EAR: https://media.bis.gov/licensing/determine-what-is-subject-to-the-EAR
- EAR Part 734: https://media.bis.gov/regulations/ear/734

### 3.2 Commodity, Software, Technology

Die EAR erfassen nicht nur physische Güter. Für Hochschulen besonders wichtig ist die Unterscheidung:

- **Commodity:** physischer Gegenstand, Gerät, Bauteil, Material, Sensor, Chip, Laborgerät.
- **Software:** Programme, Quellcode, Objektcode, Firmware, ggf. Algorithmen in softwareförmiger Umsetzung.
- **Technology:** spezifisches technisches Wissen, technische Daten, Entwicklungs-, Herstellungs- oder Nutzungsinformationen.

Technologie kann in sehr unterschiedlichen Formen vorliegen:

- technische Zeichnungen,
- Spezifikationen,
- Parameter,
- Herstellungsanleitungen,
- Prüfanweisungen,
- Source Code,
- Schulungsunterlagen,
- proprietäre Handbücher,
- Modellierungs- oder Prozesswissen,
- kontrollierte Herstellerdaten.

### 3.3 Export, Reexport, Transfer in-country

Für deutsche Hochschulen ist vor allem **Reexport** relevant.

- **Export:** Ausfuhr/Übertragung aus den USA.
- **Reexport:** Versand oder Übertragung eines Items subject to the EAR von einem Nicht-US-Land in ein anderes Nicht-US-Land.
- **Transfer in-country:** Weitergabe innerhalb desselben Landes an eine andere Person oder Verwendung, wenn EAR-relevant.

Bei Technologie und Source Code kann eine **Freigabe** bzw. ein Zugriff relevant sein, nicht nur ein Paketversand.

**Quelle:** BIS – What is a reexport?: https://media.bis.gov/learn-support/what-reexport

### 3.4 Deemed Export und Deemed Reexport

Ein **deemed export** liegt im US-Kontext vor, wenn in den USA Technologie oder Source Code subject to the EAR an eine foreign person freigegeben wird.

Ein **deemed reexport** ist im Hochschulkontext außerhalb der USA besonders relevant: Eine Freigabe außerhalb der USA von Technologie oder Source Code subject to the EAR an eine foreign person eines anderen Landes kann als Reexport in das Land der Staatsangehörigkeit oder permanent residency dieser Person gelten.

Beispiele:

- Gastwissenschaftler:in erhält Zugriff auf US-kontrollierte Technologieunterlagen.
- Internationale Projektpartner erhalten Zugang zu US-origin Source Code.
- Ein Cloud-Ordner enthält technische Daten subject to the EAR und wird für Personen aus mehreren Ländern freigeschaltet.
- Laborpersonal wird an einem US-kontrollierten System mit kontrollierten technischen Daten geschult.

**Quelle:** eCFR 15 CFR § 734.14: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.14

### 3.5 ECCN

Die **Export Control Classification Number (ECCN)** ist die Klassifikationsnummer eines Items auf der Commerce Control List (CCL). Sie ist ein zentraler Baustein zur Bestimmung möglicher US-Lizenzpflichten.

Die ECCN gibt Hinweise auf:

- Kategorie der Technologie,
- Art des Items,
- technische Kontrollparameter,
- Kontrollgründe,
- weitere Prüfpfade im EAR-System.

Beispiele für CCL-Kategorien:

- 0 – Nuclear Materials, Facilities and Equipment,
- 1 – Materials, Chemicals, Microorganisms and Toxins,
- 2 – Materials Processing,
- 3 – Electronics,
- 4 – Computers,
- 5 – Telecommunications and Information Security,
- 6 – Sensors and Lasers,
- 7 – Navigation and Avionics,
- 8 – Marine,
- 9 – Aerospace and Propulsion.

Produktgruppen innerhalb der ECCN-Systematik:

- A – Systems, Equipment and Components,
- B – Test, Inspection and Production Equipment,
- C – Materials,
- D – Software,
- E – Technology.

**Quelle:** BIS Interactive Commerce Control List: https://media.bis.gov/regulations/ear/interactive-commerce-control-list

### 3.6 EAR99

**EAR99** bedeutet: Ein Item ist subject to the EAR, aber nicht durch eine spezifische ECCN auf der CCL beschrieben.

Wichtig:

- EAR99 bedeutet nicht automatisch „frei“.
- Bei bestimmten Ländern, Endnutzern, Endverwendungen oder Sanktionslisten kann auch EAR99 relevant oder genehmigungspflichtig sein.
- EAR99 ist keine Entwarnung bei Embargo, gelisteten Parteien, WMD-/militärischer Endverwendung oder Umgehungsrisiken.

**Bot-Regel:** Wenn Nutzende sagen „ist EAR99, also unproblematisch“, soll der Bot korrigieren: EAR99 ist ein niedrigschwelligerer Klassifikationsstatus, ersetzt aber keine Länder-, Endnutzer-, Endverwendungs- und Listenprüfung.

**Quelle:** BIS – Classify your item: https://media.bis.gov/licensing/classify-your-item

### 3.7 CCL und Order of Review

Die **Commerce Control List (CCL)** ist Supplement No. 1 to Part 774 der EAR. Sie enthält die ECCN-Einträge.

Für KI-Companion Exportkontrolle gilt:

- Der Bot soll keine abschließende CCL-Klassifikation vornehmen.
- Der Bot darf erklären, dass die ECCN beim Hersteller/Lieferanten oder ggf. über fachliche Prüfung zu klären ist.
- Der Bot darf bei offensichtlichen Kategorien grob sensibilisieren, z. B. Sensoren/Laser, Elektronik, Computer, Telekommunikation/Informationssicherheit, Luft-/Raumfahrt.
- Der Bot soll keine Güterlistennummer erfinden.

**Quellen:**

- BIS Interactive CCL: https://media.bis.gov/regulations/ear/interactive-commerce-control-list
- BIS – Classify your item: https://media.bis.gov/licensing/classify-your-item

### 3.8 CCATS / Classification Request

Für bestimmte Fälle kann eine offizielle Klassifizierung bei BIS eingeholt werden. Das erfolgt über SNAP-R und wird als Commodity Classification Automated Tracking System (CCATS) bzw. classification request behandelt.

Für eine deutsche Hochschule ist das nicht automatisch der Standardweg. Häufig ist zuerst der Hersteller/Lieferant die wichtigste Quelle für ECCN/EAR99/ITAR-Angaben.

**Bot-Regel:** Der Bot soll nicht vorschlagen, dass Forschende eigenständig US-Anträge stellen. Er kann erklären, dass eine Herstellerangabe, CCATS-Angabe oder juristische/fachliche Prüfung benötigt wird.

**Quelle:** BIS – Classify your item: https://media.bis.gov/licensing/classify-your-item

### 3.9 De-minimis-Regel

Ausländische Produkte können subject to the EAR sein, wenn sie kontrollierte US-origin Inhalte enthalten und bestimmte Schwellen überschreiten oder wenn Sonderregeln greifen.

Typischer Hochschulfall:

- Ein in Deutschland gebautes Gerät enthält US-Komponenten.
- Ein Prototyp enthält US-Software oder US-Firmware.
- Eine foreign-made technology ist mit kontrollierter US-origin technology vermischt.

Die De-minimis-Prüfung ist komplex, technisch und wertbezogen. Sie ist für den Bot nicht abschließend leistbar.

**Bot-Regel:** Wenn ein selbstgebautes oder europäisches System US-Komponenten/US-Software enthält und in ein Drittland gehen soll, soll KI-Companion Exportkontrolle „US-De-minimis-Prüfung ggf. erforderlich“ als Eskalationspunkt nennen.

**Quelle:** eCFR 15 CFR § 734.4: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.4

### 3.10 Foreign Direct Product Rule (FDP)

Die **Foreign Direct Product Rules** können dazu führen, dass außerhalb der USA hergestellte Items subject to the EAR sind, wenn sie direkte Produkte bestimmter US-Technologie oder US-Software sind oder mit bestimmten Anlagen hergestellt wurden, die selbst auf US-Technologie/Software beruhen.

Besonders relevant sind FDP-Regeln bei:

- Halbleitern,
- advanced computing,
- KI-Beschleunigern,
- bestimmten China-/PRC-Konstellationen,
- gelisteten Entities,
- Russland/Belarus-Konstellationen,
- sensiblen Herstellungsanlagen.

Die FDP-Regeln sind hochkomplex und ändern sich dynamisch.

**Bot-Regel:** Nicht selbst anwenden. Bei Hinweisen auf advanced computing, Halbleiter, GPUs/AI-Chips, PRC/China, Entity List, Russland/Belarus oder komplexe Lieferketten: FDP als Prüfpunkt nennen und eskalieren.

**Quellen:**

- eCFR 15 CFR § 734.9: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.9
- BIS – Reexports and exports from abroad: https://media.bis.gov/learn-support/reexports-and-exports-from-abroad

### 3.11 End-use, End-user, U.S. person controls

Auch wenn ein Item aufgrund Klassifikation und Land zunächst nicht eindeutig genehmigungspflichtig wirkt, können Endnutzer- und Endverwendungskontrollen greifen. BIS weist darauf hin, dass Lizenzanforderungen auf Basis von Endnutzer/Endverwendung oder bestimmten Aktivitäten von U.S. persons relevant sein können.

Hochrelevante Endverwendungen:

- militärische Endverwendung,
- military-intelligence end use/end user,
- nukleare Endverwendung,
- Raketen-/UAV-Bezug,
- chemische oder biologische Waffen,
- advanced computing für WMD- oder military-intelligence-Zwecke,
- Umgehung, diversion oder procurement für gelistete Parteien.

**Bot-Regel:** End-use/End-user ist immer mitzudenken, auch bei EAR99 oder scheinbar zivilem Forschungskontext.

**Quelle:** BIS – Guidance on end-user and end-use controls and U.S. person controls: https://media.bis.gov/licensing/guidance-on-end-user-and-end-use-controls-and-us-person-controls

### 3.12 U.S. person

Der Begriff **U.S. person** kann je nach Regelung unterschiedliche Wirkungen haben. Im EAR-Kontext können bestimmte Aktivitäten von U.S. persons auch dann kontrolliert sein, wenn nicht unmittelbar ein Item subject to the EAR übertragen wird.

Für Hochschulen kann das relevant werden, wenn:

- US-Staatsangehörige,
- Personen mit U.S. permanent residency,
- US-Unternehmen,
- US-Niederlassungen,
- US-Projektpartner,
- U.S.-person-Personal in Drittmittelprojekten

an sensiblen technischen Tätigkeiten beteiligt sind.

**Bot-Regel:** Die Anwesenheit einer U.S. person im Projekt ist kein automatisches Problem, aber bei WMD-, military-intelligence-, Raketen-, UAV-, Nuklear-, Iran-/China-/Russland-/Nordkorea-Kontext ein Eskalationssignal.

### 3.13 Knowledge / Wissen im EAR-Sinne

Mehrere EAR-Pflichten knüpfen daran an, ob eine Person Kenntnis oder Grund zur Kenntnis bestimmter Umstände hat. Für den Hochschulprozess ist wichtig:

- Red Flags dürfen nicht ignoriert werden.
- Unklare Endverwendung oder ungewöhnliche Umstände müssen nachgefragt werden.
- „Wir wussten es nicht“ trägt nicht, wenn offensichtliche Hinweise vorlagen.

**Bot-Regel:** Bei Red Flags soll KI-Companion Exportkontrolle aktiv auf Klärungsbedarf hinweisen.

### 3.14 Restricted Party Lists

Bei US-Bezug können neben EU-Sanktionslisten auch US-Listen relevant sein.

Wichtige US-Listen/Instrumente:

- OFAC SDN List,
- OFAC Non-SDN Consolidated Sanctions List,
- BIS Entity List,
- BIS Denied Persons List,
- BIS Unverified List,
- BIS Military End-User List,
- Consolidated Screening List (CSL) als gebündeltes Such-/Download-Instrument.

**Bot-Regel:** Der Bot darf auf die Existenz dieser Listen hinweisen, aber keine aktuelle Listenprüfung behaupten, wenn keine angebundene, aktuelle Listenprüfung erfolgt.

**Quellen:**

- BIS Consolidated Screening List: https://www.bis.gov/node/18530
- OFAC Sanctions List Service: https://ofac.treasury.gov/sanctions-list-service
- BIS Entity List FAQs: https://www.bis.gov/media/documents/entity-list-faqs.pdf

---

## 4. Fundamental Research und Hochschulen

### 4.1 Grundidee

Nach EAR § 734.8 ist Technologie oder Software, die während oder infolge von fundamental research entsteht und zur Veröffentlichung bestimmt ist, nicht subject to the EAR.

Das ist für Hochschulen wichtig, weil offene Grundlagenforschung häufig nicht durch die EAR beschränkt werden soll.

### 4.2 Grenzen

Die Fundamental-Research-Entlastung hat Grenzen:

- Sie gilt für Technologie/Software, die aus der Forschung entsteht und zur Veröffentlichung bestimmt ist.
- Sie gilt nicht automatisch für bereits vorhandene Technologie oder Software subject to the EAR, die in das Projekt eingebracht wird.
- Sie ist gefährdet, wenn Forschende Veröffentlichungsbeschränkungen aus proprietären oder national-security-Gründen akzeptieren.
- Prepublication review kann unschädlich sein, wenn sie nur Patentrechte schützt oder versehentliche Offenlegung proprietärer Sponsorinformationen verhindert und keine inhaltliche Publikationsbeschränkung darstellt.
- Proprietäre technische Daten, NDA-Informationen, vertrauliche Herstellerunterlagen, kontrollierter Source Code oder zugangsbeschränkte technische Spezifikationen bleiben gesondert zu prüfen.

### 4.3 KI-Companion Exportkontrolle-Merksatz

> Offene Forschungsergebnisse können unter die Fundamental-Research-Entlastung fallen. Das entlastet aber nicht automatisch US-origin Geräte, Software, Quellcode, technische Daten oder proprietäre Informationen, die in das Projekt eingebracht oder geteilt werden.

**Quelle:** eCFR 15 CFR § 734.8: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.8

---

## 5. Typische Hochschulkonstellationen

### 5.1 US-origin Laborgerät

Relevanz:

- Gerät kann subject to the EAR sein.
- ECCN/EAR99 beim Hersteller klären.
- Bei Reexport aus Deutschland in Drittland kann US-Reexportrecht relevant werden.
- Bei Hochrisikoland, gelistetem Empfänger oder sensibler Endverwendung eskalieren.

### 5.2 US-Software oder Cloud-Service

Relevanz:

- Software kann subject to the EAR sein.
- Nutzungslizenz kann Reexport-/Country-/User-Beschränkungen enthalten.
- Cloud-/SaaS-Zugriffe können länder- oder personenbezogen eingeschränkt sein.
- Source Code und technische Dokumentation sind gesondert sensibel.

### 5.3 Technische Herstellerunterlagen

Relevanz:

- Handbücher sind nicht immer kontrollierte Technologie, können es aber sein, wenn sie spezifisches Entwicklungs-, Produktions- oder Nutzungswissen enthalten.
- Proprietäre oder export-controlled Unterlagen dürfen nicht ungeprüft an internationale Partner weitergegeben werden.

### 5.4 Gastwissenschaftler:innen und Laborzugang

Relevanz:

- Deemed reexport kann bei Zugriff auf Technologie/Source Code subject to the EAR relevant sein.
- Staatsangehörigkeit/permanent residency, konkrete Technologie und Zugriffstiefe sind wichtig.
- Laborzugang ist weniger problematisch, wenn nur allgemein veröffentlichte Informationen oder frei zugängliche Forschungsergebnisse genutzt werden.

### 5.5 US-Komponenten in Eigenbau/Systemintegration

Relevanz:

- Ein deutsches System kann wegen kontrollierter US-Komponenten, US-Software, De-minimis oder FDP-Regeln US-relevant sein.
- Besonders relevant bei Sensorik, Lasern, Elektronik, Halbleitern, Luft-/Raumfahrt, Informationssicherheit, advanced computing.

### 5.6 China-/PRC-Kontexte

Relevanz:

- Nicht jeder China-Bezug ist ein Exportkontrollfall.
- Erhöhte Sensibilität bei advanced computing, KI-Chips, Halbleitern, Quanten-/Sensorik, Luft-/Raumfahrt, Kryptografie, Telekommunikation, Militärnähe, gelisteten Einrichtungen, unklaren Endverwendungen.
- BIS hat in den letzten Jahren dynamische Guidance und Controls zu advanced computing, AI model training und PRC-Kontexten veröffentlicht.

**Quelle:** BIS Advanced Computing guidance overview: https://www.bis.gov/node/18210

### 5.7 Iran, Kuba, Russland/Belarus, Nordkorea, Syrien

Relevanz:

- Hohe Embargo-/Sanktionssensibilität.
- US-Regeln können strenger oder anders gelagert sein als EU-/deutsches Recht.
- Bei Iran/Kuba ist zusätzlich EU Blocking Statute zu beachten.
- Kein Bot sollte allein aus US-Sanktionsrecht eine Ablehnung formulieren.

---

## 6. Was KI-Companion Exportkontrolle sicher sagen darf

KI-Companion Exportkontrolle darf:

- US-Bezüge als Prüfpunkt benennen,
- erklären, warum EAR/OFAC/ITAR unterschiedliche Stränge sind,
- nach ECCN/EAR99/ITAR-Hinweisen fragen,
- auf De-minimis/FDP als mögliche komplexe Eskalationspunkte hinweisen,
- erklären, dass EAR99 keine automatische Entwarnung ist,
- erklären, dass Fundamental Research nicht alle US-origin Inputs entlastet,
- auf Listenprüfung als aktuellen, separaten Prozess hinweisen,
- Eskalation an Exportkontrollstelle/Rechtsprüfung empfehlen,
- eine strukturierte Anfrage an die Exportkontrollstelle vorbereiten.

KI-Companion Exportkontrolle darf nicht:

- eine verbindliche US-Rechtsprüfung durchführen,
- ECCN oder EAR99 erfinden,
- behaupten, eine aktuelle OFAC-/BIS-Listenprüfung durchgeführt zu haben, wenn das nicht technisch angebunden ist,
- ITAR-Fälle selbst klassifizieren,
- Genehmigungspflichten nach US-Recht abschließend bejahen oder verneinen,
- eine Ablehnung allein auf US-Sanktionsrecht stützen,
- EU Blocking Statute Konflikte operativ entscheiden.

---

## 7. Lokale Festlegungen und Unsicherheiten

Die folgenden Punkte sind einrichtungsspezifisch. Sie sind nur bekannt, wenn sie im bestätigten lokalen Kontext stehen; andernfalls als unbekannt behandeln und nicht vermuten:

- interne Zuständigkeit für vertiefte US-Reexportkontrollfragen,
- ob bei US-Bezug standardmäßig eine BIS/OFAC/CSL-Prüfung erfolgt oder nur bei Risikosignalen,
- genutzte Tools und Quellen für aktuelle US-Listenprüfungen sowie deren Dokumentation,
- Zeitpunkt, zu dem externe US-Rechtsberatung eingeholt wird,
- interne Übergabe von US-Exportkontrollklauseln an Justiziariat oder Vertragsprüfung,
- Dokumentation von IT-/Cloud-Zugängen auf EAR-kontrollierte Technologie.

**Rechtlich offen:** Der Umgang mit US-Sanktionsvorgaben in Iran-/Kuba-Konstellationen im Verhältnis zur EU Blocking Statute wird nicht selbst entschieden, sondern fachlich und juristisch prüfen lassen.

---

## 8. Quellen

- BIS EAR: https://media.bis.gov/regulations/ear
- BIS Determine what is subject to the EAR: https://media.bis.gov/licensing/determine-what-is-subject-to-the-EAR
- BIS Classify your item: https://media.bis.gov/licensing/classify-your-item
- BIS Reexports and exports from abroad: https://media.bis.gov/learn-support/reexports-and-exports-from-abroad
- BIS End-user, end-use and U.S. person controls: https://media.bis.gov/licensing/guidance-on-end-user-and-end-use-controls-and-us-person-controls
- BIS Interactive CCL: https://media.bis.gov/regulations/ear/interactive-commerce-control-list
- eCFR Part 734: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734
- eCFR § 734.4 De minimis: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.4
- eCFR § 734.8 Fundamental Research: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.8
- eCFR § 734.9 FDP Rules: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.9
- eCFR § 734.14 Reexport: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.14
- OFAC Sanctions List Service: https://ofac.treasury.gov/sanctions-list-service
- OFAC Sanctions Programs: https://ofac.treasury.gov/sanctions-programs-and-country-information
- EU Blocking Statute: https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en
- DDTC ITAR Overview: https://deccs.pmddtc.state.gov/deccs?id=ddtc_public_portal_itar_landing
