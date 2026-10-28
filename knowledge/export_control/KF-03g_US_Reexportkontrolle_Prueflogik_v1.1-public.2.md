---
id: "KF-03g"
title: "US-(Re-)Exportkontrollrecht: Prüflogik für Exportkontrollvorgänge"
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
purpose: "Handhabbare Prüfsystematik, um US-Bezüge in Hochschulvorgängen zu erkennen, zu dokumentieren und bei\
  \ Bedarf zu eskalieren."
binding: "Orientierung; keine abschließende US-rechtliche Prüfung."
---

<!-- SPDX-License-Identifier: Apache-2.0; Public adaptation 2026-10-22; source version 1.1; editorial adaptation, not a new legal review. -->
<!-- Editorial revision 2026-10-26: researcher-role, response-rule or source-register consistency; no new legal review; last_reviewed retained. -->

# KF-03g – US-(Re-)Exportkontrollrecht: Prüflogik für Exportkontrollvorgänge


---

## 1. Grundsatz

US-(Re-)Exportkontrollrecht wird bei Hochschulvorgängen als **zusätzlicher Risikofilter** behandelt. Der Filter soll klären:

1. Gibt es einen US-Bezug?
2. Könnte ein Item subject to the EAR sein?
3. Ist eine ECCN/EAR99/ITAR-Angabe bekannt oder zu beschaffen?
4. Gibt es ein erhöhtes Risiko wegen Land, Endnutzer, Endverwendung, Listenstatus, Technologiezugang oder Vertragsklauseln?
5. Muss fachlich, juristisch oder extern eskaliert werden?

Der Filter ersetzt nicht die EU-/deutsche Prüfung. EU-Dual-Use-Verordnung, AWG/AWV, BAFA-Zuständigkeit, EU-Sanktionen, nationale Genehmigungspflichten, Forschungssicherheit, Datenschutz und ggf. EU Blocking Statute bleiben eigenständig zu prüfen.

---

## 2. Zeitpunkt im Prozess

Der US-Filter sollte früh eingesetzt werden:

- bei Erstkontakt / Anfrageaufnahme,
- bei Beschaffung oder Leihe von US-Geräten/US-Software,
- bei Export, Versand, Mitnahme, Transfer oder Reparatur,
- bei Vertragsprüfung,
- bei internationalen Kooperationen,
- bei Gastwissenschaftler:innen und Laborzugängen,
- bei Cloud-/IT-/Repository-Zugriffen,
- bei Hochrisikoländern und sensiblen Technologien.

**Empfehlung:** Der US-Filter sollte kein separater Spezialprozess sein, sondern ein Abschnitt in der allgemeinen Exportkontroll-Fallaufnahme.

---

## 3. Schnellfilter für Forschendenbot

Der Schnellfilter ist auf höchstens drei entscheidende Rückfragen pro Antwort begrenzt. Weitere Aspekte werden bei Bedarf in einem späteren Gesprächsschritt geklärt.


Der Forschendenbot soll bei erkennbarer Relevanz höchstens drei entscheidende Fragen stellen. Geeignet sind:

1. **Was genau soll geteilt, versendet, mitgenommen oder zugänglich gemacht werden, und worin besteht der konkrete US-Bezug?**  
   Zum Beispiel US-Hersteller, US-Komponente, US-Software, US-Cloud, ECCN/EAR99/ITAR-Hinweis oder einschlägige Vertragsklausel.

2. **An wen und wohin geht es?**  
   Land, Institution, Empfänger/Endnutzer, tatsächlicher Zugriffs- oder Nutzungsort und mögliche Weitergabe.

3. **Wofür soll es genutzt werden?**  
   Zweck, Endverwendung und gegebenenfalls technisch sensible Anwendung.

Wenn die Antworten unvollständig sind, soll der Bot keine Entwarnung geben, sondern fehlende Informationen benennen.

---

## 4. Prüfschritt 0: Mindestinformationen sammeln

Vor Bewertung sollten folgende Informationen erfasst werden:

| Feld | Benötigte Information |
|---|---|
| Gegenstand | Was genau ist betroffen? Gerät, Software, Technologie, Material, Daten, Zugang? |
| Handlung | Export, Reexport, Transfer, Upload, Download, Cloud-Zugriff, Schulung, Mitnahme, Reparatur, Leihe? |
| Ursprung | Hersteller, Lieferant, Herkunftsland, US-origin Hinweise? |
| US-Klassifikation | ECCN, EAR99, ITAR/USML, CCATS, unbekannt? |
| Technische Details | Modell, Seriennummer, Leistungsdaten, technische Parameter, Version, Bauteile, Software/Firmware? |
| Empfänger | Institution, Land, konkrete Personen, Endnutzer, Zwischenhändler, Partner? |
| Endverwendung | Zweck, Projekt, Methoden, Anwendung, militärische/zivile Nutzung, Weitergabe? |
| Zugang | Wer erhält welche Daten/Software/Technologie? Lokal, remote, Cloud, Git, Labor? |
| Vertrag | Export-control-, sanctions-, reexport-, no-foreign-person-, prohibited-country- oder publication-restriction-Klauseln? |
| Listen/Embargo | EU-Listen, ggf. BIS/OFAC/CSL, Hochrisikoland, Embargo? |
| Fristen | Geplanter Versand/Zugriff/Projektstart; Eilbedürftigkeit? |

---

## 5. Prüfschritt 1: US-Bezug erkennen

### 5.1 Typische US-Bezüge

Ein US-Bezug liegt nahe bei:

- US-Hersteller,
- US-Lieferant,
- US-origin Gerät, Bauteil, Sensor, Chip, Laser, Computer, Messinstrument,
- US-Software, US-Firmware, US-SaaS, US-Cloud,
- US-Datenbank oder Plattform,
- US-source code,
- US-technische Daten, Handbücher, Spezifikationen,
- US-Komponenten in einem deutschen/europäischen System,
- US-Funding,
- US-Projektpartner,
- US-Vertragsklauseln,
- US-person im Projektteam,
- ECCN-, EAR99-, ITAR-, USML-, DDTC-, OFAC-, BIS- oder reexport-Hinweis.

### 5.2 Dokumentationssatz

Wenn kein US-Bezug erkennbar ist:

> Nach den vorliegenden Angaben ist kein spezifischer US-Bezug erkennbar. US-(Re-)Exportkontrollrecht wird daher derzeit nicht vertieft geprüft. Dies ersetzt nicht die EU-/deutsche Exportkontroll-, Embargo- und Sanktionsprüfung.

Wenn ein US-Bezug offen ist:

> Ein möglicher US-Bezug ist nicht geklärt. Vor einer Einordnung sollten Hersteller-/Lieferantenangaben zu Ursprung, ECCN/EAR99 und ggf. ITAR/USML eingeholt werden.

Wenn ein US-Bezug erkennbar ist:

> Es liegt ein US-Bezug vor. Daher sollte geprüft werden, ob der betroffene Gegenstand, die Software oder Technologie subject to the EAR ist oder ob ITAR-/OFAC-/Sanktionsaspekte berührt sind.

---

## 6. Prüfschritt 2: „Subject to the EAR“ vorprüfen

### 6.1 Mögliche Gründe für EAR-Relevanz

Ein Item kann subject to the EAR sein, wenn:

- es sich in den USA befindet,
- es US-origin ist,
- es außerhalb der USA hergestellt wurde, aber kontrollierte US-origin Inhalte enthält,
- es unter De-minimis-Regeln fällt,
- es unter eine Foreign Direct Product Rule fällt,
- BIS individuell oder durch EAR-Änderung eine EAR-Relevanz festgelegt hat.

### 6.2 Hochschulnahe Beispiele

| Fall | Mögliche EAR-Relevanz |
|---|---|
| US-Laborgerät an der Einrichtung soll nach Indien verliehen werden | US-origin item; möglicher Reexport |
| Deutscher Prototyp enthält US-Sensor und US-Firmware | De-minimis-/Komponenten-/Software-Frage |
| US-Simulationssoftware soll Partnern in Drittstaat zugänglich gemacht werden | Software subject to EAR; Lizenzbedingungen; Reexport/Zugriff |
| US-Herstellerunterlagen werden in Cloud-Ordner gelegt | Technologiezugang; deemed reexport möglich |
| KI-Modelltraining mit US-GPUs/advanced computing ICs und PRC-Bezug | advanced computing controls, FDP, end-use/end-user prüfen |

### 6.3 Bot-Grenze

Der Bot soll nicht endgültig feststellen, ob ein Item subject to the EAR ist. Er soll die dafür notwendigen Informationen benennen und ggf. Eskalation empfehlen.

---

## 7. Prüfschritt 3: ECCN, EAR99, ITAR/USML klären

### 7.1 Informationsquellen

Priorisierte Quellen:

1. Hersteller-/Lieferantenangabe im Angebot, Datenblatt, Export Control Statement, Manual oder Vertrag.
2. ECCN/EAR99-Angabe auf Rechnung, Lieferschein, Lizenzunterlagen oder Produktseite.
3. CCATS-/BIS-Klassifizierungsangabe, falls vorhanden.
4. Fachliche interne Prüfung anhand technischer Parameter.
5. Externe Rechts-/Exportkontrollberatung bei komplexen Fällen.

### 7.2 Was beim Hersteller angefragt werden sollte

Empfohlene Rückfrage:

```text
Bitte teilen Sie uns für das Produkt / die Software / die technische Dokumentation folgende exportkontrollrechtliche Angaben mit:
- US-Ursprung ja/nein?
- ECCN oder EAR99 nach den U.S. Export Administration Regulations?
- Falls ECCN: vollständige ECCN und ggf. Kontrollgründe?
- ITAR-/USML-Relevanz ja/nein?
- CCATS oder sonstige Klassifizierungsgrundlage, falls vorhanden?
- Gelten Reexport-, Länder-, Endnutzer- oder Endverwendungsbeschränkungen?
```

### 7.3 Umgang mit unbekannter ECCN

Wenn ECCN/EAR99 unbekannt ist:

- keine Entwarnung,
- Herstellerangaben einholen,
- technische Parameter sammeln,
- bei sensiblen Gütern eskalieren,
- Vorgang bis zur Klärung nicht als abgeschlossen bewerten.

### 7.4 ITAR-Hinweis

Wenn ITAR/USML erwähnt wird:

- hohe Eskalation,
- keine Eigenklassifizierung durch Bot,
- keine Weitergabe an ausländische Personen/Partner ohne Prüfung,
- Vertrags-/Rechtsprüfung einbinden.

---

## 8. Prüfschritt 4: Land, Empfänger, Endnutzer, Endverwendung

### 8.1 Grundsatz

Die US-Prüfung endet nicht bei ECCN/EAR99. Zusätzlich sind zu prüfen:

- Bestimmungsland,
- Endnutzer,
- Endverwendung,
- beteiligte Zwischenparteien,
- Listenstatus,
- mögliche Umleitung,
- Kenntnis/Red Flags,
- Embargo-/Sanktionsprogramme.

### 8.2 Endverwendungsfragen

Niedrigschwellige Fragen:

- Handelt es sich um offene, zivile Forschung?
- Gibt es militärische, nachrichtendienstliche oder sicherheitsbehördliche Beteiligung?
- Gibt es Nuklear-, Raketen-, UAV-, chemische oder biologische Endverwendungsbezüge?
- Geht es um advanced computing, KI-Modelltraining, Halbleiter, Quanten-/Sensorik, Luft-/Raumfahrt, Kryptografie oder Telekommunikation?
- Ist eine Weitergabe an Dritte geplant oder möglich?
- Sind Endnutzer und Zweck plausibel und transparent?

### 8.3 Listenprüfung

Bei US-Bezug und Risikosignalen sollten ggf. geprüft werden:

- BIS Entity List,
- BIS Denied Persons List,
- BIS Unverified List,
- BIS Military End-User List,
- OFAC SDN List,
- OFAC Non-SDN Consolidated Sanctions List,
- Consolidated Screening List.

**Bot-Regel:** KI-Companion Exportkontrolle darf nicht behaupten, aktuelle Listen geprüft zu haben, wenn keine Live-Prüfung erfolgt ist. Formulierung: „Eine aktuelle Listenprüfung sollte durchgeführt werden.“

### 8.4 Hochrisikoländer / sensible Konstellationen

Besonders erhöhte Aufmerksamkeit bei:

- Iran,
- Kuba,
- Syrien,
- Nordkorea,
- Russland,
- Belarus,
- besetzte Gebiete der Ukraine,
- China/PRC, Hongkong, Macau bei bestimmten Technologien und Endverwendungen,
- Länder-/Personenkonstellationen mit Umgehungs- oder Beschaffungsrisiko.

**[AKTUALISIEREN]** Länderrisiken und Programme ändern sich häufig. Keine statische Liste als abschließende Grundlage verwenden.

---

## 9. Prüfschritt 5: Technologiezugang und deemed reexport

### 9.1 Relevante Zugriffsformen

Technologiezugang kann entstehen durch:

- Laborzugang,
- Schulung,
- technische Einweisung,
- Remote-Zugriff,
- Cloud-Ordner,
- Git-Repository,
- Ticket-/Issue-System,
- elektronische Laborbücher,
- geteilte Datenräume,
- Herstellerportale,
- Software-Lizenzen,
- Source-Code-Repositories,
- technische Meetings,
- Präsentationen mit nicht veröffentlichten technischen Details.

### 9.2 Bewertung

Nicht jeder Labor- oder Cloud-Zugang ist exportkontrollrechtlich relevant. Relevanz steigt, wenn:

- technische Daten subject to the EAR betroffen sind,
- Source Code betroffen ist,
- proprietäre oder zugangsbeschränkte Herstellerinformationen betroffen sind,
- ECCN-/ITAR-/USML-Hinweise existieren,
- Personen aus Hochrisikoländern beteiligt sind,
- militärische oder WMD-Endverwendungsrisiken bestehen,
- Inhalte nicht veröffentlicht werden dürfen.

### 9.3 Dokumentationsfragen

- Welche Personen erhalten Zugriff?
- Welche Staatsangehörigkeit/permanent residency ist relevant?
- Welche Dateien, Daten, Software oder technischen Unterlagen sind betroffen?
- Sind die Informationen veröffentlicht, publishable, fundamental research oder proprietär/restricted?
- Gibt es Zugriffsbeschränkungen, Need-to-know, Rollenrechte?
- Gibt es Export-control markings oder Vertragspflichten?

---

## 10. Prüfschritt 6: Konflikte mit EU-Recht / Blocking Statute

### 10.1 Wann prüfen?

Bei folgenden Hinweisen:

- US-Sanktionsklausel verlangt Ausschluss bestimmter Länder/Personen,
- US-Partner verlangt Einhaltung sämtlicher US-Sanktionen,
- Iran- oder Kuba-Bezug,
- Projekt soll wegen US-Sanktionsvorgaben abgelehnt/abgebrochen werden,
- Vertrag enthält „no dealings with sanctioned countries“ ohne EU-/deutschen Rechtsbezug,
- Cloud-/Softwareanbieter verweigert Zugriff wegen US-Sanktionen.

### 10.2 Bot-Regel

Der Bot soll nicht sagen: „Das ist wegen US-Recht verboten“, wenn eine EU-Blocking-Statute-Problematik möglich ist.

Sichere Formulierung:

> Hier kann ein Spannungsverhältnis zwischen US-Sanktionsvorgaben und EU-/deutschem Recht einschließlich EU Blocking Statute entstehen. Das sollte juristisch geprüft werden; eine operative Ablehnung allein mit Verweis auf US-Sanktionsrecht wäre nicht belastbar.

---

## 11. Orientierung für Forschende

Informationsstand und sachlicher Prüfbedarf werden getrennt beschrieben. Fehlende Angaben begründen zunächst Klärungsbedarf, keine Risikoklasse. Die folgenden Abschnitte sind keine Freigabestufen oder Verwaltungsentscheidungen.

### Kein konkreter zusätzlicher US-Prüfhinweis aus den bisherigen Angaben

Wenn die vorhandenen Informationen keinen konkreten US-Ursprungs-, Klassifikations-, Sanktions-, Personen- oder Vertragsbezug erkennen lassen, darf dies nur auf diese Informationen bezogen werden. Nicht bekannte Komponenten oder Vertragsbedingungen gelten nicht als nachweislich unkritisch. Die EU-/deutsche Betrachtung bleibt davon getrennt.

Mögliche Formulierung:

> Aus den bisherigen Angaben ergibt sich kein konkreter zusätzlicher US-Prüfhinweis. Das ersetzt keine abschließende Prüfung; neue Angaben zu Ursprung, Inhalt, Beteiligten oder Vertragsbedingungen können die Einordnung verändern.

### Entscheidende Informationen fehlen

Bei einem bereits erkennbaren möglichen US-Bezug können insbesondere Herstellerangaben, ECCN/EAR99, betroffene Inhalte, Empfänger oder Endverwendung fehlen. Diese Lücken werden gezielt geklärt. Eine unbekannte ECCN oder Endverwendung allein begründet keine hohe Risikoeinstufung.

Pro Antwort höchstens drei eigenständig beantwortbare Rückfragen auswählen. Bei Produktangaben kann es sinnvoll sein, eine vorhandene Klassifikation oder Export-Control-Angabe des Herstellers anzufragen. Nicht behaupten, dass eine US-Genehmigung bereits erforderlich oder entbehrlich sei.

### Konkreter zusätzlicher Prüfhinweis

Ein tatsächlicher Hinweis auf US-kontrollierte Inhalte, einschlägige Lieferbeschränkungen, sensible Endverwendung, einen möglichen Listentreffer oder eine relevante Vertragsklausel kann fachliche Klärung erfordern. Den konkreten Auslöser benennen und erklären, welche Information für den nächsten Schritt fehlt. Nationale Zugehörigkeit, internationale Zusammenarbeit oder eine Informationslücke allein ersetzen diesen Auslöser nicht.

### Betroffene Tätigkeit vor Weitergabe oder Zugriff klären

Bei konkreten Hinweisen etwa auf ITAR/USML, einschlägige Verbote oder Listenmaßnahmen, sensible U.S.-person-Aktivitäten oder einen möglichen Konflikt mit dem EU Blocking Statute ist eine fachliche und gegebenenfalls juristische Prüfung vor der betroffenen Tätigkeit angezeigt.

Keine Bot-Freigabe oder pauschale Verbotsaussage formulieren. Unterschiedliche Tätigkeiten getrennt betrachten; ein offener Prüfpunkt sperrt nicht automatisch das gesamte Forschungsvorhaben. Der konkrete Länder- und Rechtsbezug sowie der aktuelle Quellenstand müssen nachvollziehbar sein.

---

## 12. Anfragevorbereitung für Forschende

Auf ausdrücklichen Wunsch kann der Bot eine kurze, datensparsame Sachverhaltsdarstellung oder Anfrage an die zuständige Stelle vorbereiten. Sie kann bekannte Angaben zum Gegenstand, möglichen US-Bezug, geplanten Vorgang und offenen Prüfpunkt enthalten. Fehlende Angaben werden als offen gekennzeichnet.

Die Anfrage ist kein interner Prüfvermerk. Sie darf keine durchgeführte Listenprüfung, administrative Einstufung, Freigabe, Auflage oder einen abgeschlossenen Vorgang dokumentieren, sofern lediglich eine Bot-Orientierung vorliegt. Tatsächlich von Nutzenden mitgeteilte Entscheidungen können als solche zugeordnet werden; sie werden nicht zur eigenen Entscheidung des Bots.

Konkrete lokale Zuständigkeiten und Verfahren stammen ausschließlich aus dem dafür bestätigten lokalen Kontext. Aus allgemeinen Empfehlungen dieses Dokuments werden keine institutionellen Prozessregeln abgeleitet.

---

## 13. Rückfragenbausteine für Forschende

Die folgenden Fragen sind ein Auswahlpool. Pro Antwort höchstens drei eigenständig beantwortbare Informationspunkte wählen; bereits bekannte Angaben nicht wiederholen. Mehrere eigenständig beantwortbare Teilfragen in einem Bulletpoint zählen einzeln und werden gegebenenfalls auf spätere Gesprächsschritte verteilt.

### Allgemein

- Was genau soll ausgeführt, geteilt, übertragen, hochgeladen oder zugänglich gemacht werden?
- Handelt es sich um ein physisches Gerät, Software, Source Code, technische Daten, Material, Proben oder Know-how?
- Wer ist der Hersteller oder Lieferant?
- Welcher konkrete Hinweis auf US-Ursprung liegt vor?
- Liegen ECCN, EAR99, ITAR/USML oder Export-Control-Markings vor?
- Wer ist der tatsächliche Empfänger?
- In welchem Land erfolgt die Nutzung?
- Wofür soll der Gegenstand/die Information verwendet werden?
- Ist eine Weitergabe an Dritte vorgesehen oder möglich?
- Gibt es Vertrags-, Geheimhaltungs- oder Publikationsbeschränkungen?

### Bei Software/Cloud/Git

- Wo wird die Software gehostet?
- Wer erhält Zugriff?
- Enthält das Repository Source Code, technische Parameter oder Herstellerdaten?
- Gibt es Länder-/Nutzerbeschränkungen in der Lizenz?
- Sind die Inhalte bereits öffentlich verfügbar?
- Ist eine Veröffentlichung geplant?

### Bei Gastwissenschaftler:innen

- Auf welche Geräte, Unterlagen, Software oder Daten soll Zugriff gewährt werden?
- Sind darunter US-origin, ECCN-/EAR99-/ITAR-markierte oder proprietäre Informationen?
- Welche Staatsangehörigkeit/permanent residency ist relevant?
- Geht es um Einweisung in allgemeine Laborabläufe oder um nicht veröffentlichte technische Details?

### Bei Verträgen

- Enthält der Vertrag Export-control-, sanctions-, reexport-, ITAR-, EAR-, OFAC- oder prohibited-country-Klauseln?
- Werden Publikationen beschränkt?
- Gibt es no-foreign-person- oder nationality restrictions?
- Werden bestimmte Länder/Personen unabhängig von EU-/deutschem Recht ausgeschlossen?

---

## 14. Vorbereitung nach Art des Vorgangs

Je nach Fragestellung können Forschende bereits vorhandene Herstellerangaben, einschlägige Vertragsklauseln oder eine abstrakte Beschreibung des geplanten Zugriffs für die Beratung zusammenstellen. Dabei nur die für den konkreten Prüfpunkt erforderlichen Informationen verwenden.

Bei Beschaffung oder Geräteweitergabe können Export-Control-Angaben des Herstellers hilfreich sein. Bei Verträgen können einschlägige Export-, Sanktions-, Publikations- oder Zugangsklauseln zur fachlichen Prüfung vorgelegt werden. Bei Cloud-, Git- oder Laborzugriffen ist eine Beschreibung der tatsächlich betroffenen Inhalte und Rechte relevant.

Diese Hinweise legen weder einen lokalen Freigabeprozess noch eine bestimmte Zuständigkeit, Aufbewahrungsregel oder vorgeschriebene Listenprüfung fest. Solche Verfahrensangaben werden getrennt durch die betreibende Einrichtung bestätigt.

---

## 15. Quellen

- BIS EAR: https://media.bis.gov/regulations/ear
- BIS Determine what is subject to the EAR: https://media.bis.gov/licensing/determine-what-is-subject-to-the-EAR
- BIS Classify your item: https://media.bis.gov/licensing/classify-your-item
- BIS Reexports and exports from abroad: https://media.bis.gov/learn-support/reexports-and-exports-from-abroad
- BIS End-user and end-use controls: https://media.bis.gov/licensing/guidance-on-end-user-and-end-use-controls-and-us-person-controls
- BIS Consolidated Screening List: https://www.bis.gov/node/18530
- OFAC Sanctions List Service: https://ofac.treasury.gov/sanctions-list-service
- EU Blocking Statute: https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en
- eCFR § 734.4: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.4
- eCFR § 734.8: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.8
- eCFR § 734.9: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.9
- eCFR § 734.14: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.14
