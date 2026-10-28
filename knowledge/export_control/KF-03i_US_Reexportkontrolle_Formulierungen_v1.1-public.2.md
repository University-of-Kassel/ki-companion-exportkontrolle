---
id: "KF-03i"
title: "US-(Re-)Exportkontrollrecht: Formulierungen für KI-Companion Exportkontrolle"
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
purpose: "Sichere, vorsichtige Formulierungsbausteine für Bot-Antworten zu US-(Re-)Exportkontrollrecht."
binding: "Textbausteine für Orientierung; keine Rechtsberatung, keine Freigabe."
---

<!-- SPDX-License-Identifier: Apache-2.0; Public adaptation 2026-10-22; source version 1.1; editorial adaptation, not a new legal review. -->
<!-- Editorial revision 2026-10-26: researcher-role, response-rule or source-register consistency; no new legal review; last_reviewed retained. -->

# KF-03i – US-(Re-)Exportkontrollrecht: Formulierungen für KI-Companion Exportkontrolle


---

## 1. Grundregel für Bot-Antworten

US-(Re-)Exportkontrollrecht soll in KI-Companion Exportkontrolle so formuliert werden:

- vorsichtig,
- nicht rechtsverbindlich,
- als zusätzlicher Prüfpunkt,
- mit klarer Trennung von EU/deutscher Exportkontrolle,
- ohne erfundene ECCN/Güterlistennummern,
- ohne Behauptung einer aktuellen US-Listenprüfung,
- mit konkreten nächsten Schritten.

### Standard-Hinweis am Ende substantieller Antworten

> Dies ist eine erste orientierende Einschätzung und keine rechtsverbindliche Bewertung.

Bei US-Recht besonders:

> Der US-Bezug sollte als zusätzlicher Prüfpunkt dokumentiert und bei unklarer ECCN/EAR99, ITAR-Hinweisen, Sanktions-/Listenbezug oder sensibler Endverwendung fachlich geprüft werden.

---

## 2. Kurzbausteine für den Forschendenbot

### 2.1 Allgemeiner US-Bezug

> Hier gibt es einen möglichen US-Bezug. Deshalb sollte zusätzlich zur EU-/deutschen Exportkontrollprüfung geklärt werden, ob der Gegenstand, die Software oder die Technologie „subject to the EAR“ ist. Dafür sind vor allem Herstellerangaben zu US-Ursprung, ECCN/EAR99 und ggf. ITAR/USML relevant.

### 2.2 Kein erkennbarer US-Bezug

> Nach Ihren Angaben ist derzeit kein spezifischer US-Bezug erkennbar. Damit steht zunächst die EU-/deutsche Exportkontroll-, Embargo- und Sanktionsprüfung im Vordergrund. Falls doch US-Software, US-Komponenten, US-Herstellerunterlagen, US-Cloud-Dienste oder US-Vertragsklauseln beteiligt sind, sollte der US-Prüfpunkt erneut aufgenommen werden.

### 2.3 US-Bezug offen

> Der US-Bezug ist noch offen. Bitte prüfen Sie insbesondere Hersteller, Lieferant, Software/Firmware, technische Unterlagen, Cloud-/SaaS-Anbieter und Vertragsklauseln auf Hinweise wie ECCN, EAR99, EAR, ITAR, USML, OFAC oder „U.S. export controlled“.

### 2.4 ECCN/EAR99 fehlt

> Für eine belastbare Einordnung fehlt die US-Klassifikation. Bitte fragen Sie beim Hersteller oder Lieferanten nach ECCN oder EAR99 sowie nach möglichen Reexport-, Länder-, Endnutzer- oder Endverwendungsbeschränkungen. Ohne diese Information sollte keine Entwarnung formuliert werden.

### 2.5 EAR99 korrekt einordnen

> EAR99 bedeutet nicht automatisch „frei“. Es heißt zunächst nur, dass das Item zwar subject to the EAR sein kann, aber nicht unter einer spezifischen ECCN der Commerce Control List geführt wird. Land, Endnutzer, Endverwendung, Embargos und Listenstatus bleiben trotzdem zu prüfen.

### 2.6 ECCN vorhanden

> Da eine ECCN genannt ist, sollte der Vorgang nicht nur nach EU-/deutschem Recht, sondern auch mit Blick auf US-Reexportkontrolle betrachtet werden. Entscheidend sind nun Zielland, Empfänger, Endverwendung, mögliche Weitergabe und aktuelle Listen-/Sanktionsbezüge.

### 2.7 ITAR/USML-Hinweis

> Der ITAR-/USML-Hinweis ist ein starkes Eskalationssignal. KI-Companion Exportkontrolle kann diesen Bereich nicht abschließend prüfen. Bitte geben Sie die Unterlagen nicht weiter und öffnen Sie keine Zugriffe, bevor der Fall fachlich und ggf. juristisch geprüft wurde.

### 2.8 Fundamental Research

> Offene Forschungsergebnisse können im US-Recht unter die Fundamental-Research-Entlastung fallen. Das gilt aber nicht automatisch für bereits vorhandene US-kontrollierte Software, technischen Source Code, Herstellerunterlagen, proprietäre Daten oder zugangsbeschränkte Technologie, die in das Projekt eingebracht oder geteilt werden.

### 2.9 US-Software

> Bei US-Software sind nicht nur Installation und Nutzung relevant, sondern auch Lizenzbedingungen, ECCN/EAR99, Source-Code-Zugriff, Cloud-/SaaS-Zugriffe und mögliche Länder- oder Nutzerbeschränkungen. Bitte prüfen Sie die Export-Control-Angaben des Anbieters und klären Sie, wer in welchem Land Zugriff erhalten soll.

### 2.10 US-Gerät / US-Komponente

> Bei einem US-origin Gerät oder einer US-Komponente kann eine Reexportprüfung relevant werden, wenn das Gerät aus Deutschland in ein anderes Land weitergegeben, verliehen, repariert oder zugänglich gemacht wird. Bitte klären Sie Herstellerangaben, ECCN/EAR99, Zielland, Empfänger und Endverwendung.

### 2.11 De-minimis / Eigenbau

> Auch ein in Deutschland gebautes System kann US-relevant sein, wenn kontrollierte US-Komponenten, US-Software, US-Firmware oder US-Technologie enthalten sind. Ob De-minimis-Regeln greifen, ist komplex und sollte nicht durch den Bot abschließend bewertet werden.

### 2.12 Foreign Direct Product / advanced computing

> Bei advanced computing, Halbleitern, KI-Beschleunigern, GPUs, Chipdesign, EDA-Software, Foundry-Bezug oder PRC/China-/Macau-Konstellationen können US-Regeln besonders dynamisch und komplex sein. Eine Foreign-Direct-Product- oder End-use-/End-user-Prüfung kann erforderlich sein. Bitte fachlich eskalieren.

### 2.13 Technologiezugang / deemed reexport

> Nicht nur physischer Versand kann relevant sein. Wenn Personen außerhalb der USA Zugriff auf Technologie oder Source Code subject to the EAR erhalten, kann ein deemed reexport zu prüfen sein. Wichtig sind Inhalt, Zugriffskreis, Staatsangehörigkeit/permanent residency, Veröffentlichungsstatus und etwaige Export-Control-Markings.

### 2.14 Gastwissenschaftler:innen

> Entscheidend ist nicht allein die Person oder Staatsangehörigkeit, sondern der konkrete Zugriff. Bitte klären Sie, ob die Person Zugang zu US-kontrollierter Technologie, Source Code, proprietären Herstellerdaten, export-control-markierten Unterlagen oder sensiblen Endverwendungen erhalten soll.

### 2.15 US-Sanktions-/OFAC-Bezug

> OFAC-Sanktionsrecht ist ein eigener US-Regelungsstrang neben den EAR. Bei US-Bezug und Sanktionshinweisen sollte eine aktuelle Listen- und Sanktionsprüfung erfolgen. KI-Companion Exportkontrolle kann keine aktuelle OFAC-/BIS-Listenprüfung bestätigen, wenn keine Live-Prüfung angebunden ist.

### 2.16 EU Blocking Statute

> Bei Iran-/Kuba-Bezug oder US-Sanktionsklauseln kann ein Spannungsverhältnis zwischen US-Sanktionsvorgaben und EU-/deutschem Recht einschließlich EU Blocking Statute entstehen. Das sollte juristisch geprüft werden; eine operative Entscheidung allein mit Verweis auf US-Sanktionsrecht wäre nicht belastbar.

### 2.17 U.S. person im Projekt

> Die Beteiligung einer U.S. person ist nicht automatisch problematisch. Sie kann aber relevant werden, wenn die Person bestimmte technische Unterstützung in sensiblen Bereichen leistet, insbesondere bei military-intelligence-, WMD-, Raketen-, UAV-, Nuklear-, chemischen oder biologischen Endverwendungsbezügen.

### 2.18 Vertragsklausel

> Die Exportkontrollklausel sollte nicht nur fachlich, sondern auch vertraglich/juristisch geprüft werden. Besonders aufmerksam sollte man bei Verweisen auf EAR, ITAR, OFAC, U.S. sanctions, prohibited countries, reexport restrictions, no foreign persons oder nationality restrictions sein.

---

## 3. Antwortformate

Diese Formate sind nur für eine konkrete Einzelfallorientierung bestimmt. Bekannte Angaben nicht erneut abfragen. Pro Chat-Antwort höchstens drei eigenständig beantwortbare Rückfragen auswählen; ein wichtigerer fehlender Informationspunkt ersetzt einen weniger wichtigen, statt als Unterfrage hinzuzukommen.

### 3.1 Kurzes Forschendenformat

```markdown
### Erste Einordnung
Hier gibt es einen möglichen US-Bezug, weil [US-Hersteller/Software/Komponente/Vertragsklausel/Zugriff]. Das heißt noch nicht automatisch, dass eine US-Genehmigung erforderlich ist, aber der US-Prüfpunkt sollte dokumentiert werden.

### Was noch fehlt
Für die nächste Orientierung sind insbesondere folgende offene Punkte relevant:
1. Welche Export-Control-Angabe des Herstellers liegt vor?
2. Wer soll den Gegenstand oder Inhalt tatsächlich nutzen?
3. Wofür ist die Nutzung vorgesehen?

### Nächster Schritt
Bitte holen Sie beim Hersteller/Lieferanten die Export-Control-Angaben ein und geben Sie den Vorgang mit diesen Informationen an die Exportkontrollprüfung weiter.

Dies ist eine erste orientierende Einschätzung und keine rechtsverbindliche Bewertung.
```

### 3.2 Vollformat mit EU/US-Trennung

```markdown
## Exportkontrolle – EU/deutsches Recht
[Einordnung nach EU-Dual-Use, AWG/AWV, Embargo/Sanktionen, BAFA-Prüfbedarf.]

## Zusätzlicher US-Prüfpunkt
[US-Bezug: ja/nein/offen. EAR/OFAC/ITAR/ECCN/EAR99/De-minimis/FDP/Zugriff/Vertragsklausel benennen.]

## Was fehlt
[Konkrete fehlende Informationen.]

## Empfehlung
[Informationen einholen, keine Freigabe, Eskalation, Vertrags-/Rechtsprüfung, Listenprüfung.]

Dies ist eine erste orientierende Einschätzung und keine rechtsverbindliche Bewertung.
```


## 4. Mailvorlagen

Diese Vorlagen dienen ausschließlich einem ausdrücklich angeforderten Textentwurf aus Sicht der Forschenden. Sie werden nicht automatisch an eine Erstorientierung angehängt und sind keine Rückfragenkataloge, die der Bot den Nutzenden stellen soll. Nur fallrelevante Bausteine verwenden; unbekannte Angaben als offen kennzeichnen. Ein Entwurf ist keine tatsächlich versandte Nachricht oder erfolgte Prüfung. Reine Textentwürfe erhalten keinen zusätzlichen Standardhinweis zur Einzelfallorientierung.

### 4.1 Anfrage an Hersteller/Lieferant

Die Fragen im folgenden Muster sind optionale Bausteine für den gewünschten Anfrageentwurf. Nur die zum Produkt und Prüfpunkt passenden Fragen auswählen; vorhandene Herstellerangaben nicht erneut erfragen. Die Drei-Rückfragen-Grenze betrifft die Klärungsfragen des Bots an Nutzende und wird nicht durch einen ungefragten umfangreichen Mailentwurf umgangen.

```text
Sehr geehrte Damen und Herren,

für unsere interne Exportkontrollprüfung benötigen wir zu folgendem Produkt / folgender Software / folgender technischer Dokumentation exportkontrollrechtliche Angaben:

[Produkt/Software/Dokumentation, Modell/Version, Angebot/Rechnung/Bestellnummer]

Bitte teilen Sie uns mit:

1. Handelt es sich um ein Produkt, Software, Technologie oder technische Dokumentation mit US-Ursprung oder US-exportkontrollrechtlicher Relevanz?
2. Welche ECCN oder EAR99-Einstufung nach den U.S. Export Administration Regulations gilt?
3. Falls eine ECCN gilt: Bitte nennen Sie die vollständige ECCN und ggf. vorhandene CCATS-/Klassifizierungsgrundlage.
4. Besteht eine ITAR-/USML-Relevanz?
5. Gelten Reexport-, Länder-, Endnutzer- oder Endverwendungsbeschränkungen?
6. Gibt es besondere Beschränkungen für Zugriff, Weitergabe, Cloud-Nutzung, Source Code oder technische Dokumentation?

Vielen Dank und freundliche Grüße
```

### 4.2 Erste Anfrage an die zuständige Stelle

```text
Sehr geehrte Damen und Herren,

ich plane [konkreter Vorgang]. Dabei ist [Gegenstand, Software oder Inhalt] betroffen. Einen möglichen US-Bezug erkenne ich an [vorliegende Herstellerangabe, Markierung oder Vertragsklausel; andernfalls offen].

Ich bitte um Unterstützung bei der fachlichen Klärung dieses Prüfpunkts. Bisher bekannt ist [knappe, belegte Sachverhaltsbeschreibung]. Offen ist insbesondere [entscheidende Informationslücke].

Bitte teilen Sie mir mit, welche weiteren Angaben für die Einzelfallprüfung benötigt werden.

Vielen Dank und freundliche Grüße
```

### 4.3 Sachverhaltsdarstellung an die zuständige Stelle

Nur soweit eine ausführlichere Zusammenstellung ausdrücklich gewünscht und für die Anfrage erforderlich ist:

```text
Sehr geehrte Damen und Herren,

ich bitte um fachliche Einordnung eines möglichen US-(Re-)Exportkontrollbezugs bei folgendem Vorhaben:

- Geplanter Vorgang: [bekannte Angaben]
- Betroffener Gegenstand oder Inhalt: [bekannte Angaben]
- Belegter US-Hinweis: [Herstellerangabe oder sonstige Quelle; andernfalls offen]
- Relevante Beteiligte und Standorte: [bekannte, erforderliche Angaben]
- Beabsichtigte Nutzung: [bekannte Angaben]
- Konkreter offener Prüfpunkt: [Frage]

Diese Zusammenstellung beschreibt mein Vorhaben und die mir bisher vorliegenden Angaben. Sie enthält keine Bestätigung einer bereits durchgeführten Listenprüfung oder Freigabe.

Vielen Dank und freundliche Grüße
```

### 4.4 Vertragsprüfung / Justiziariat

```text
Im Vertrag finden sich exportkontroll- bzw. sanktionsbezogene Klauseln mit US-Bezug.

Zu prüfen wäre insbesondere:
- Verweis auf EAR, ITAR, OFAC, U.S. sanctions oder prohibited countries,
- Reexport restrictions,
- no foreign person / nationality restrictions,
- Publikations- oder Zugangsbeschränkungen,
- mögliche Kollision mit EU-/deutschem Recht oder EU Blocking Statute,
- Auswirkungen auf Projektumsetzung, Datenaustausch, Personalzugriff und Veröffentlichung.

Eine fachliche Exportkontrollprüfung sollte parallel erfolgen, soweit Gegenstände, Software, Technologie oder technische Daten betroffen sind.
```

---

## 5. Sichere Reaktionen auf häufige Aussagen

### Aussage: „Das ist doch nur Forschung.“

> Das ist ein wichtiger Punkt, aber keine vollständige Entwarnung. Offene Forschungsergebnisse können unter die Fundamental-Research-Entlastung fallen. Wenn jedoch US-kontrollierte Software, Source Code, technische Herstellerdaten oder proprietäre Unterlagen eingebracht oder geteilt werden, muss dieser Input gesondert geprüft werden.

### Aussage: „Wir schicken nichts, es ist nur ein Zugriff.“

> Auch Zugriffe können relevant sein, wenn Technologie oder Source Code subject to the EAR betroffen sind. Bitte klären Sie, welche Inhalte zugänglich gemacht werden, wer Zugriff erhält und ob die Informationen veröffentlicht, proprietär oder export-control-markiert sind.

### Aussage: „Der Hersteller sagt, es ist EAR99.“

> EAR99 ist hilfreich, aber keine vollständige Entwarnung. Bitte dokumentieren Sie die Herstellerangabe mit Datum und Quelle. Zusätzlich bleiben Land, Endnutzer, Endverwendung, Weitergabe und Sanktions-/Listenbezug zu prüfen.

### Aussage: „Das Gerät bleibt bei uns.“

> Wenn keine Weitergabe, kein Versand, keine Mitnahme, kein Remote-Zugriff und keine technische Datenfreigabe erfolgt, kann der US-Reexportaspekt geringer sein. Falls aber internationale Personen Zugriff auf kontrollierte Technologie, Software, Source Code oder Herstellerdaten erhalten, sollte dies trotzdem geprüft werden.

### Aussage: „Der Partner ist nicht auf einer EU-Sanktionsliste.“

> Das ist wichtig, reicht bei US-Bezug aber nicht immer aus. Zusätzlich können BIS- oder OFAC-Listen relevant sein. Eine aktuelle US-Listenprüfung sollte nur behauptet werden, wenn sie tatsächlich durchgeführt und dokumentiert wurde.

### Aussage: „Der Vertrag verlangt nur allgemein die Einhaltung von US-Recht.“

> Allgemeine US-Exportkontroll- oder Sanktionsklauseln sollten nicht ungeprüft übernommen werden. Bitte lassen Sie die Klausel vertraglich/juristisch prüfen, insbesondere wenn sie Länder, Personen, Publikationen oder Zugriffe beschränkt.

### Aussage: „Der Partner sitzt in China, aber es ist Grundlagenforschung.“

> Ein China-Bezug ist nicht automatisch ein Exportkontrollproblem. Bei advanced computing, KI-Chips, Halbleitern, Quanten-/Sensorik, Luft-/Raumfahrt, Kryptografie, Militärnähe oder gelisteten Einrichtungen sollte der US-Prüfpunkt aber vertieft betrachtet werden.

### Aussage: „Die Person kommt aus Iran, darf sie ins Labor?“

> Entscheidend ist nicht allein die Herkunft der Person, sondern welcher konkrete Zugang gewährt wird. Allgemeiner Laborzugang und offene Forschung sind anders zu bewerten als Zugriff auf US-kontrollierte Technologie, Source Code, proprietäre Herstellerunterlagen oder sensible Endverwendungen. Bitte den Zugriff konkret beschreiben und prüfen lassen.

---

## 6. Do / Don’t für KI-Companion Exportkontrolle

### Do

- US-Bezug als Prüfpunkt benennen.
- Nach ECCN/EAR99/ITAR/USML fragen.
- EAR, OFAC, ITAR und EU Blocking Statute unterscheiden.
- Fehlende Informationen konkret benennen.
- Bei Red Flags eskalieren.
- Fundamental Research differenziert erklären.
- EAR99 richtig einordnen.
- Bei ITAR/USML sehr vorsichtig formulieren.
- Auf ausdrücklichen Wunsch eine datensparsame Anfrage aus Sicht der Forschenden vorbereiten.

### Don’t

- Keine ECCN erfinden.
- Keine „US-rechtlich frei“-Aussage treffen.
- Keine aktuelle OFAC-/BIS-Listenprüfung behaupten.
- Keine ITAR-Bewertung durchführen.
- Keine Ablehnung allein wegen US-Sanktionen formulieren, wenn EU Blocking Statute relevant sein kann.
- Nicht sagen: „kein Problem“, wenn ECCN, Endnutzer oder Endverwendung fehlen.
- Nicht die Staatsangehörigkeit einer Person allein als Ausschlussgrund behandeln.
- Nicht „Fundamental Research“ als pauschale Freistellung verwenden.

---

## 7. Quellenhinweise für Bot-Antworten

Wenn der Bot Quellen nennen soll, bevorzugt kurz:

- BIS / EAR für „subject to the EAR“, ECCN/EAR99, Reexport, De-minimis, FDP, End-use/end-user.
- OFAC für US-Sanktionslisten und US-Sanktionsprogramme.
- EU-Kommission für EU Blocking Statute.
- DDTC nur bei ITAR-/USML-Hinweisen.

Beispielformulierung:

> Hintergrund: Die EAR werden vom Bureau of Industry and Security administriert; OFAC-Sanktionen sind ein separater Sanktionsstrang; ITAR/DDTC betrifft defense articles/services/technical data und sollte bei Hinweisen immer gesondert geprüft werden.

---

## 8. Quellen

- BIS Determine what is subject to the EAR: https://media.bis.gov/licensing/determine-what-is-subject-to-the-EAR
- BIS Classify your item: https://media.bis.gov/licensing/classify-your-item
- BIS Reexports and exports from abroad: https://media.bis.gov/learn-support/reexports-and-exports-from-abroad
- BIS End-user/end-use and U.S. person controls: https://media.bis.gov/licensing/guidance-on-end-user-and-end-use-controls-and-us-person-controls
- OFAC Sanctions List Service: https://ofac.treasury.gov/sanctions-list-service
- EU Blocking Statute: https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en
- DDTC ITAR Overview: https://deccs.pmddtc.state.gov/deccs?id=ddtc_public_portal_itar_landing
