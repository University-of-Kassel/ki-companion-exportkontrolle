---
id: "KF-03h"
title: "US-(Re-)Exportkontrollrecht: Red Flags und Hochschulszenarien"
version: "1.1-public.2"
status: "draft"
last_reviewed: "2026-10-22"
review_cycle: null
profiles:
  - "researcher"
scope: "Hochschulen und Forschungseinrichtungen; Schwerpunkt Deutschland/EU"
document_type: "Kuratierte Knowledge File Exportkontrolle"
related: []
knowledge_area: null
purpose: "Typische Risikosignale im Hochschulkontext erkennen und angemessen eskalieren."
binding: "Orientierung; keine abschließende Rechtsprüfung."
---

<!-- SPDX-License-Identifier: Apache-2.0; Public adaptation 2026-10-22; source version 1.1; editorial adaptation, not a new legal review. -->
<!-- Editorial revision 2026-10-26: researcher-role, response-rule or source-register consistency; no new legal review; last_reviewed retained. -->

# KF-03h – US-(Re-)Exportkontrollrecht: Red Flags und Hochschulszenarien


---

## 1. Grundsatz

Red Flags sind Hinweise darauf, dass ein Vorgang nicht mit einer einfachen Standardantwort abgeschlossen werden sollte. Sie bedeuten nicht automatisch, dass ein Vorgang verboten oder genehmigungspflichtig ist. Sie bedeuten aber, dass weitere Informationen, fachliche Prüfung oder juristische Eskalation erforderlich sein können.

**Bot-Regel:** Bei Red Flags keine Entwarnung geben, keine Genehmigungsfreiheit behaupten und keine Güterlisten-/ECCN-Nummern erfinden. Die nachfolgenden Prüfpunkte und Szenariofragen sind ein Auswahlpool, kein automatisch auszugebender Fragenkatalog. Pro Antwort höchstens drei eigenständig beantwortbare Informationspunkte erfragen; fehlende Angaben allein sind kein Beleg für hohes Risiko.

---

## 2. Red Flags nach Themenfeld

### 2.1 US-origin oder US-markierte Items

**Signal:** Gerät, Bauteil, Software, Firmware oder technische Dokumentation stammt von einem US-Hersteller oder ist als EAR, ECCN, EAR99, ITAR oder US export controlled markiert.

**Warum relevant:** US-origin items können auch außerhalb der USA subject to the EAR bleiben. Bei Reexport aus Deutschland in ein Drittland kann US-Reexportrecht relevant werden.

**Bot-Reaktion:**

- ECCN/EAR99/ITAR-Angabe anfragen,
- Empfängerland, Endnutzer und Endverwendung klären,
- bei ITAR-Hinweis eskalieren,
- keine abschließende Bewertung.

### 2.2 ECCN vorhanden

**Signal:** Hersteller oder Vertrag nennt eine ECCN, z. B. 3A..., 5D..., 6A..., 9E...

**Warum relevant:** Eine ECCN zeigt, dass das Item auf der Commerce Control List beschrieben sein kann. Ob eine Lizenzpflicht besteht, hängt weiter von Land, Endnutzer, Endverwendung und weiteren Verboten ab.

**Bot-Reaktion:**

- ECCN dokumentieren,
- Land/Empfänger/Endverwendung prüfen,
- bei Drittlandtransfer oder Technologiezugang eskalieren,
- keine pauschale Entwarnung.

### 2.3 EAR99 als Scheinsicherheit

**Signal:** Forschende sagen: „Das ist EAR99, also frei.“

**Warum relevant:** EAR99 heißt nicht automatisch frei. Auch EAR99 kann bei Embargo, gelisteten Parteien, bestimmten Endverwendungen oder Sanktionsprogrammen relevant sein.

**Bot-Reaktion:**

- EAR99 korrekt einordnen,
- Endnutzer/Endverwendung/Land/Listenstatus weiter prüfen,
- bei Hochrisikoland oder Endverwendungsrisiko eskalieren.

### 2.4 ITAR / USML / Defense Article

**Signal:** Unterlagen, Vertrag oder Hersteller nennen ITAR, USML, defense article, defense service, technical data controlled under ITAR, DDTC.

**Warum relevant:** ITAR ist ein anderer, oft strengerer US-Regelungsbereich für defense articles, defense services und technical data. Hochschulübliche Fundamental-Research-Argumente reichen hier nicht für eine einfache Entwarnung.

**Bot-Reaktion:**

- hohe Eskalation,
- keine eigene Klassifikation,
- keine Weitergabe/Zugriffsöffnung empfehlen,
- juristische/fachliche Prüfung.

### 2.5 US-Komponenten in deutschem/europäischem System

**Signal:** Ein in Deutschland entwickelter Prototyp enthält US-Chips, US-Sensoren, US-Firmware, US-Software oder US-Technologie.

**Warum relevant:** De-minimis-Regeln oder FDP-Regeln können dazu führen, dass ein foreign-made item subject to the EAR ist.

**Bot-Reaktion:**

- US-Anteil/Komponenten/Software/Firmware dokumentieren,
- ECCN der US-Komponenten anfragen,
- Zielland/Endnutzer/Endverwendung prüfen,
- bei sensibler Technologie oder Hochrisikoland eskalieren.

### 2.6 Foreign Direct Product / Halbleiter / advanced computing

**Signal:** Halbleiter, GPUs, AI accelerators, advanced computing ICs, Chipdesign, Foundry, EDA-Software, Halbleiterfertigung, PRC/China/Macau-Bezug, Entity List, Cloud-/IaaS-Nutzung für KI-Training.

**Warum relevant:** BIS hat besondere und dynamische Controls und Guidance für advanced computing, Halbleiter, AI model training, China/PRC, Country Group D:5 und Macau veröffentlicht. FDP-Regeln können komplexe extraterritoriale Wirkungen haben.

**Bot-Reaktion:**

- als hoher US-Prüfpunkt kennzeichnen,
- keine Eigenprüfung der FDP-Regeln,
- Endnutzer/Endverwendung und Listenstatus klären,
- fachlich/juristisch eskalieren.

### 2.7 Technologiezugang / Source Code / Cloud / Git

**Signal:** Internationale Personen oder Partner sollen Zugriff auf technische Unterlagen, Source Code, Herstellerdaten, private Repositories, Cloud-Ordner, Laborbücher, Remote-Systeme oder Softwarelizenzen erhalten.

**Warum relevant:** Freigabe von Technologie oder Source Code subject to the EAR kann als deemed reexport relevant sein.

**Bot-Reaktion:**

- Zugriffskreis, Staatsangehörigkeiten/permanent residency und Inhalte klären,
- Fundamental Research vs. proprietäre/restricted technology unterscheiden,
- bei ECCN-/ITAR-/Export-Control-Markings eskalieren,
- Need-to-know und Zugriffsbeschränkung empfehlen.

### 2.8 Gastwissenschaftler:innen aus Hochrisikoländern

**Signal:** Gastwissenschaftler:in oder Projektmitglied aus Iran, Russland, Belarus, China/PRC, Nordkorea, Syrien oder anderem sensiblen Kontext erhält Zugang zu Labor, Software, Cloud, technischen Daten oder US-Geräten.

**Warum relevant:** Nicht die Person als solche ist das Problem, sondern der konkrete Zugang zu kontrollierter Technologie/Software, die Endverwendung und ggf. Listen-/Embargokontext.

**Bot-Reaktion:**

- keine pauschale Ablehnung,
- konkrete Zugriffstiefe klären,
- bei US-kontrollierter Technologie oder Hochrisiko-Endverwendung eskalieren,
- ggf. Forschungssicherheit zusätzlich berücksichtigen.

### 2.9 Vertragliche US-Exportkontrollklauseln

**Signal:** Vertrag verlangt compliance with U.S. export control laws, U.S. sanctions, EAR, ITAR, OFAC, no access by foreign persons, no Iran/Cuba/Russia/China, no reexport without authorization.

**Warum relevant:** Verträge können Pflichten schaffen, die operativ, rechtlich oder politisch mit EU-/deutschem Recht kollidieren können. Besonders bei Iran/Kuba kann das EU Blocking Statute relevant sein.

**Bot-Reaktion:**

- Klausel nicht selbst akzeptieren/auslegen,
- Justiziariat/Vertragsprüfung empfehlen,
- Exportkontrollstelle einbinden,
- bei Iran/Kuba EU Blocking Statute nennen.

### 2.10 Publikations- und Geheimhaltungsbeschränkungen

**Signal:** Sponsor oder Vertrag beschränkt Veröffentlichung, verlangt Freigabe aus Sicherheitsgründen, untersagt Veröffentlichung technischer Ergebnisse oder setzt nationality restrictions.

**Warum relevant:** Fundamental Research kann gefährdet sein, wenn Forschende Beschränkungen aus proprietären oder national-security-Gründen akzeptieren. Proprietäre oder restricted technology bleibt gesondert relevant.

**Bot-Reaktion:**

- Publikationsfreiheit klären,
- Vertrag prüfen,
- Fundamental-Research-Entlastung nicht vorschnell annehmen.

### 2.11 Militärische oder nachrichtendienstliche Nähe

**Signal:** Endnutzer ist Verteidigungsministerium, Militärakademie, militärnahes Unternehmen, Sicherheitsbehörde, Nachrichtendienst, police/security service, military-civil fusion entity oder Dual-Use-Zulieferer.

**Warum relevant:** End-use/end-user controls können unabhängig von der normalen Klassifikation greifen. MEU-/Entity-List-Fragen können relevant sein.

**Bot-Reaktion:**

- Endnutzer/Endverwendung genau klären,
- Listenprüfung empfehlen,
- Forschungssicherheit berücksichtigen,
- hohe Eskalation bei US-Bezug.

### 2.12 WMD / Nuklear / Raketen / UAV / Chemie / Biologie

**Signal:** Nukleartechnik, Uran/Thorium, Isotopenproduktion, Raketen, Flugkörper, UAV/Drohnen, Aerosoltechnik, Toxine, Pathogene, chemische Synthese mit Waffenbezug, Trägersysteme.

**Warum relevant:** WMD-/CBW-/Raketen-/UAV-Endverwendungen sind klassische Hochrisikofelder für Exportkontrolle und US-End-use controls.

**Bot-Reaktion:**

- sehr hohe Eskalation,
- keine Entwarnung,
- BAFA-/EU-/deutsche Prüfung plus US-Bezug gesondert prüfen.

### 2.13 Unklare oder unplausible Endverwendung

**Signal:** Empfänger kann Zweck nicht erklären, technische Anforderungen passen nicht zum Forschungszweck, private E-Mail-Adressen, Zwischenhändler, ungewöhnliche Lieferwege, Weitergabe an Dritte, Druck auf schnelle Lieferung, Umgehung offizieller Kanäle.

**Warum relevant:** Red Flags können auf diversion/procurement/Umgehung hinweisen. BIS betont Due-Diligence- und Endverwendungsprüfungen.

**Bot-Reaktion:**

- Rückfragen stellen,
- keine Freigabe oder Entwarnung suggerieren,
- fachliche Prüfung empfehlen.

### 2.14 Reparatur, Rücksendung, Leihe, Konferenzmitnahme

**Signal:** US-Gerät soll zur Reparatur in Drittland, an Hersteller, an Partner oder zu Konferenz/Demo mitgenommen werden.

**Warum relevant:** Auch temporäre Ausfuhren, Rücksendungen, Reexporte oder Technologieübertragungen können relevant sein.

**Bot-Reaktion:**

- Eigentümer, Hersteller, Zielland, Dauer, Zweck, technische Daten und ECCN klären,
- nicht auf „nur temporär“ als Entwarnung vertrauen.

### 2.15 Verschlüsselung / Informationssicherheit

**Signal:** Kryptografie, Informationssicherheit, Telekommunikation, verschlüsselte Software, secure communications, penetration testing, exploit research, cyber tools.

**Warum relevant:** EAR-Kategorie 5 kann betroffen sein; encryption controls sind komplex. Zusätzlich können Cyber-/Dual-Use- und Forschungssicherheitsfragen relevant sein.

**Bot-Reaktion:**

- ECCN/EAR99 anfragen,
- Veröffentlichung/offene Forschung vs. kontrollierter Source Code unterscheiden,
- bei Export/Cloud/Zugriffen eskalieren.

---

## 3. Länder- und Kontext-Red-Flags

### 3.1 Iran

Risikoindikatoren:

- US-origin Gerät/Software/Technologie,
- OFAC-/US-Sanktionsbezug,
- EU-/deutsche Embargo- und Sanktionsprüfung,
- Technologiezugang für Personen/Institutionen mit Iran-Bezug,
- US-Vertragsklausel verbietet Iran-Bezug,
- mögliche EU Blocking Statute Kollision.

Bot-Reaktion:

- keine pauschale Ablehnung allein wegen Iran-Bezug,
- EU/deutsche Embargoprüfung nennen,
- US-Bezug als gesonderten Prüfpunkt nennen,
- bei US-Sanktionsklausel: juristisch eskalieren.

### 3.2 Kuba

Risikoindikatoren:

- US-Sanktions-/OFAC-Bezug,
- US-Vertragsklausel,
- US-Software/Cloud,
- EU Blocking Statute möglich.

Bot-Reaktion:

- keine operative Entscheidung allein auf US-Sanktionen stützen,
- juristische Prüfung empfehlen.

### 3.3 Russland/Belarus

Risikoindikatoren:

- EU-Sanktionen,
- US/EAR Russia/Belarus controls,
- Umgehung über Drittstaaten,
- military end users,
- high-priority items,
- dual-use/advanced technology,
- Reparatur/Weiterleitung/Transit.

Bot-Reaktion:

- sehr hohe Sensibilität,
- EU-/deutsche Prüfung vorrangig,
- bei US-Bezug EAR/OFAC/BIS-Listen prüfen lassen,
- keine Entwarnung.

### 3.4 China/PRC, Hongkong, Macau

Risikoindikatoren:

- advanced computing ICs, GPUs, AI accelerators,
- KI-Modelltraining,
- Halbleiterfertigung, EDA, Foundry,
- Quanten, Sensorik, Laser, Luft-/Raumfahrt,
- Militärnähe, military-civil fusion,
- Entity List/MEU/UVL-Bezug,
- US-origin Technologie/Software/Equipment,
- Cloud-/IaaS-Nutzung.

Bot-Reaktion:

- differenziert: nicht jeder China-Bezug ist ein Fall,
- bei genannten Technologien aber erhöhte Sensibilität,
- Endnutzer/Endverwendung/Listung/FDP/EAR prüfen lassen,
- Forschungssicherheit mitdenken.

### 3.5 Nordkorea, Syrien, besetzte Gebiete

Risikoindikatoren:

- umfassende Embargo-/Sanktionsrelevanz,
- US-origin oder EAR/OFAC-Bezug,
- WMD-/militärische Nähe,
- Umgehung über Drittstaaten.

Bot-Reaktion:

- hohe Eskalation,
- keine Freigabeaussage,
- aktuelle EU-/deutsche und ggf. US-Prüfung.

---

## 4. Hochschulszenarien

### Szenario 1: US-Laborgerät an Partnerhochschule

**Fall:** Ein US-origin Spektrometer soll für drei Monate an eine Partnerhochschule außerhalb der EU verliehen werden.

**Prüfpunkte:**

- Hersteller/Lieferant?
- ECCN/EAR99?
- Zielland?
- Empfängerinstitution und Endverwendung?
- Bleibt das Gerät unter Kontrolle der Uni?
- Rücktransport?
- Software/Firmware/technische Unterlagen enthalten?
- Reexport restrictions?

**Bewertung:** US-Reexportprüfung ggf. erforderlich. Temporäre Leihe ist keine automatische Entwarnung.

### Szenario 2: US-Software in internationalem Projekt

**Fall:** Eine Forschungsgruppe nutzt US-Simulationssoftware und möchte Projektpartnern in Drittstaaten Zugriff geben.

**Prüfpunkte:**

- ECCN/EAR99 der Software?
- Lizenzbedingungen zu Ländern/Nutzern/Reexport?
- Zugriff auf Source Code oder nur Nutzung?
- Cloud/SaaS oder lokale Installation?
- Partnerland/Endnutzer/Endverwendung?

**Bewertung:** Software und Lizenzbedingungen prüfen; bei Hochrisikoland oder sensibler Endverwendung eskalieren.

### Szenario 3: Gastwissenschaftler:in erhält Herstellerunterlagen

**Fall:** Eine Gastwissenschaftlerin soll technische US-Herstellerunterlagen für ein Messgerät erhalten.

**Prüfpunkte:**

- Sind die Unterlagen öffentlich oder proprietär?
- Enthalten sie kontrollierte Technologie?
- Gibt es Export-Control-Markings?
- Staatsangehörigkeit/permanent residency?
- Zweck und Zugriffstiefe?

**Bewertung:** Deemed reexport möglich, wenn Technologie/Source Code subject to the EAR betroffen ist.

### Szenario 4: Deutscher Prototyp mit US-Komponenten

**Fall:** Ein an der Uni entwickeltes Messsystem enthält US-Sensoren und soll in ein Drittland exportiert werden.

**Prüfpunkte:**

- ECCN der US-Komponenten?
- kontrollierter US-Anteil?
- US-Software/Firmware enthalten?
- De-minimis-Prüfung erforderlich?
- Zielland/Endverwendung?

**Bewertung:** Nicht allein deutsches Produkt; US-Komponenten können US-Prüfung auslösen.

### Szenario 5: AI/advanced computing mit PRC-Bezug

**Fall:** Ein Projekt nutzt US-GPUs oder Cloud-Ressourcen für KI-Modelltraining mit einem chinesischen Partner.

**Prüfpunkte:**

- Welche Chips/Cloud/Provider?
- Subject to EAR?
- ECCN 3A090/4A090 oder verwandte Klassifikationen möglich?
- Partner/ultimate parent in Country Group D:5/Macau?
- Military-intelligence/WMD-Endverwendung ausgeschlossen?
- Listenstatus?

**Bewertung:** Hohe US-Exportkontrollsensibilität; nicht durch Bot abschließend prüfbar.

### Szenario 6: US-Vertrag mit prohibited-country-Klausel

**Fall:** Ein US-Partner verlangt, dass keine Personen aus bestimmten Ländern Zugang zu Projektinformationen erhalten.

**Prüfpunkte:**

- Ist die Klausel exportkontrollrechtlich begründet?
- Bezieht sie sich auf EAR, ITAR, OFAC, sanctions?
- Betrifft sie US-origin controlled technology?
- Kollidiert sie mit EU-/deutschem Recht, Diskriminierungsrecht, Forschungsfreiheit oder EU Blocking Statute?

**Bewertung:** Vertrags-/Rechtsprüfung erforderlich; Bot darf keine Akzeptanz empfehlen.

### Szenario 7: Fundamental Research wird als Pauschalargument genutzt

**Fall:** Forschende argumentieren, das Projekt sei offene Grundlagenforschung, daher seien US-Regeln irrelevant.

**Prüfpunkte:**

- Entstehen die Informationen im Projekt und sollen veröffentlicht werden?
- Werden vorhandene US-controlled technology/software/Source Code eingebracht?
- Gibt es NDA, Publikationsbeschränkung oder proprietary information?
- Werden technische Herstellerdaten geteilt?

**Bewertung:** Fundamental Research kann entlasten, aber nicht automatisch alle Inputs und Zugriffe.

### Szenario 8: Reparatur eines US-Geräts

**Fall:** Ein US-origin Gerät soll zur Reparatur an einen Standort außerhalb der USA geschickt werden.

**Prüfpunkte:**

- Ist es derselbe Hersteller oder ein Drittanbieter?
- Zielland?
- ECCN/EAR99?
- Technische Daten/Software/Firmware werden mitgesendet?
- Ersatzgerät/Komponenten?
- Rücksendung?

**Bewertung:** Reparatur kann Export/Reexport sein; nicht automatisch unproblematisch.

### Szenario 9: Publication Review und NDA

**Fall:** Sponsor erlaubt Publikation nur nach Freigabe und behält sich Ausschluss bestimmter technischer Details vor.

**Prüfpunkte:**

- Dient Review nur Patentschutz/proprietärer Informationsschutz oder national-security-/Exportkontrollbeschränkung?
- Werden Ergebnisse tatsächlich frei veröffentlicht?
- Werden vertrauliche technische Daten eingebracht?

**Bewertung:** Fundamental-Research-Status prüfen; Vertrag eskalieren.

### Szenario 10: US-Person im Projekt

**Fall:** Eine US-Staatsbürgerin arbeitet an der Einrichtung an einem Projekt mit möglicher UAV- oder Raketen-Endverwendung.

**Prüfpunkte:**

- Welche Tätigkeit genau?
- Item subject to EAR oder U.S.-person-control unabhängig davon?
- WMD-/military-intelligence-/Raketen-/UAV-Endverwendung?
- Partner/Endnutzer/Land?

**Bewertung:** U.S.-person-Aspekt ist nicht per se problematisch, aber bei sensibler Endverwendung eskalationsrelevant.

---

## 5. False Comfort Signals

Diese Aussagen sind **keine ausreichende Entwarnung**:

| Aussage | Warum nicht ausreichend? |
|---|---|
| „Es ist nur Forschung.“ | Fundamental Research entlastet nicht automatisch eingebrachte US-Technologie/Software. |
| „Es ist nur Software.“ | Software/Source Code kann selbst controlled sein. |
| „Es ist nur ein Cloud-Zugang.“ | Zugriff kann Technologie/Software freigeben. |
| „Das Gerät bleibt Eigentum der Uni.“ | Eigentum verhindert nicht Export/Reexport/Transfer. |
| „Es ist nur temporär.“ | Temporäre Ausfuhr/Leihe/Reparatur kann relevant sein. |
| „Der Partner ist nicht auf einer EU-Liste.“ | Bei US-Bezug können zusätzlich BIS/OFAC-Listen relevant sein. |
| „EAR99 heißt frei.“ | EAR99 kann bei Endnutzer/Endverwendung/Land/Listen relevant bleiben. |
| „Der Hersteller sagt no license required.“ | Aussage kann nur für bestimmte Länder/Endverwendungen gelten. |
| „Die Daten stehen in einem Projektordner.“ | Zugriffskreis und Inhalt sind entscheidend. |
| „Wir exportieren nichts physisch.“ | Technologie-/Source-Code-Freigaben können relevant sein. |
| „Das ist doch Deutschland, nicht USA.“ | US-origin items/US-controlled technology können außerhalb der USA subject to the EAR sein. |

---

## 6. Sachliche Prüfhinweise und nächste Schritte

Diese Übersicht ist keine Risikoskala. Sie trennt Informationslücken von konkreten fachlichen Anhaltspunkten. Die jeweils betroffene Tätigkeit, der belegte US-Bezug und die verfügbaren Quellen sind entscheidend; es gibt keine automatische hohe Einstufung wegen fehlender Angaben.

| Konstellation | Einordnung für die Erstorientierung | Möglicher nächster Schritt |
|---|---|---|
| US-Ursprung bekannt; Klassifikation und Vorgang beschrieben | US-Prüfpunkt anhand der konkreten Angaben betrachten, ohne Freigabe abzuleiten | Einschlägige Länder-, Endnutzer- und Endverwendungsaspekte fachlich klären; EU-/deutsche Prüfung getrennt halten |
| US-Ursprung erkennbar, ECCN/EAR99 unbekannt | Informationslücke zur Klassifikation | Vorhandene Herstellerangabe einholen |
| EAR99 mit konkretem Länder-, Listen- oder Endverwendungshinweis | EAR99 beseitigt diesen Prüfhinweis nicht | Einschlägige aktuelle Regel und konkrete Beteiligte fachlich prüfen lassen |
| ITAR-/USML-Hinweis | Konkreter Anlass für fachliche und gegebenenfalls juristische Prüfung | Betroffene Weitergabe oder Zugriffsöffnung vorher klären |
| Zugriff auf Technologie oder Source Code subject to the EAR | Vorgang und tatsächlicher Zugriff können relevant sein | Möglichen deemed reexport anhand der konkreten Konstellation prüfen lassen |
| Konkreter China-/PRC-Bezug bei advanced computing, Halbleitern oder KI-Chips | Zusätzlicher technologie- und vorgangsbezogener Prüfhinweis | Einschlägige EAR-, FDP-, End-use- und Listenfragen fachlich klären |
| Iran-/Kuba-Bezug mit US-Sanktionsklausel | Möglicher Konflikt unterschiedlicher Rechtsanforderungen | EU Blocking Statute und Vertragsklausel juristisch klären |
| Russland-/Belarus-Bezug mit US-Ursprung oder EAR-Hinweis | Zusätzlicher Länder- und Sanktionsprüfpunkt | Aktuelle EU- und einschlägige US-Regeln sowie mögliche Umgehung getrennt prüfen lassen |
| Konkreter Militär-, WMD-, Raketen-, UAV-, Nuklear- oder CBW-Endverwendungshinweis | Sensibler sachlicher Prüfhinweis | Betroffene Tätigkeit vor Umsetzung fachlich klären |
| Endverwendung oder Weitergabe noch nicht beschrieben | Zunächst Klärungsbedarf; keine hohe Risikoeinstufung allein wegen der Lücke | Die entscheidende fehlende Angabe erfragen; keine Freigabe aus der Lücke ableiten |
| Konkrete U.S.-person-Aktivität mit sensibler Endverwendung | Tätigkeitsbezogener zusätzlicher Prüfhinweis | Mögliche U.S.-person controls fachlich klären |
| Boycott-/Antiboycott-Klausel | Vertragsbezogener Prüfhinweis | Einschlägige Klausel zur rechtlichen Prüfung vorlegen |

---

## 7. Antwortregeln bei Prüfhinweisen

### Wenn Informationen fehlen

Die Lücke benennen und die für den nächsten Schritt entscheidenden Angaben erfragen. Höchstens drei eigenständig beantwortbare Rückfragen stellen. Keine Risikoklasse oder Stop-Regel allein aus unvollständigen Angaben ableiten; fehlende Angaben sind ebenso wenig eine Freigabe.

### Wenn ein konkreter sachlicher Prüfhinweis vorliegt

Den Auslöser und die betroffene Tätigkeit knapp erklären, bereits mögliche Orientierung geben und einen verhältnismäßigen nächsten Schritt nennen. Eine datensparsame Anfrage kann auf Wunsch vorbereitet werden. Keine tatsächliche Prüfung oder Entscheidung der zuständigen Stelle behaupten.

### Wenn eine betroffene Tätigkeit vor Umsetzung geklärt werden muss

Bei einem konkreten ITAR-/USML-, Verbots-, Listen- oder sensiblen Endverwendungshinweis keine operative Freigabe suggerieren. Erklären, weshalb eine aktuelle fachliche oder gegebenenfalls juristische Prüfung angezeigt ist. Keine allgemeine Sperre für andere, getrennt zu betrachtende Projektteile erfinden.

Beispiel:

> Der geschilderte ITAR-/USML-Hinweis sollte vor der betroffenen Weitergabe oder Zugriffsöffnung fachlich und gegebenenfalls juristisch geklärt werden. Daraus folgt noch keine abschließende Bewertung des gesamten Vorhabens.

---

## 8. Lokale Zuständigkeiten und Verfahren

Ob eine Einrichtung bestimmte Prüfwerkzeuge, Dokumentationsabläufe, Vertragsbausteine oder Stop-Regeln verwendet, ergibt sich ausschließlich aus ihrem bestätigten lokalen Kontext. Ein allgemeiner fachlicher Prüfhinweis in dieser Datei begründet keine solche institutionelle Regel.

Fehlt der lokale Verfahrensstand, bleibt er offen. Der Bot kann die Anfrage fachlich vorbereiten, darf aber keine Zuständigkeit, verbindliche lokale Prüfreihenfolge oder bereits erfolgte Prüfung ergänzen.

---

## 9. Quellen

- BIS EAR: https://media.bis.gov/regulations/ear
- BIS End-user/end-use and U.S. person controls: https://media.bis.gov/licensing/guidance-on-end-user-and-end-use-controls-and-us-person-controls
- BIS Reexports and exports from abroad: https://media.bis.gov/learn-support/reexports-and-exports-from-abroad
- BIS Advanced Computing guidance overview: https://www.bis.gov/node/18210
- BIS Entity List FAQs: https://www.bis.gov/media/documents/entity-list-faqs.pdf
- BIS Consolidated Screening List: https://www.bis.gov/node/18530
- OFAC Sanctions List Service: https://ofac.treasury.gov/sanctions-list-service
- OFAC Programs: https://ofac.treasury.gov/sanctions-programs-and-country-information
- EU Blocking Statute: https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en
- DDTC ITAR Overview: https://deccs.pmddtc.state.gov/deccs?id=ddtc_public_portal_itar_landing
- eCFR § 734.8 Fundamental Research: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.8
- eCFR § 734.14 Reexport: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.14
