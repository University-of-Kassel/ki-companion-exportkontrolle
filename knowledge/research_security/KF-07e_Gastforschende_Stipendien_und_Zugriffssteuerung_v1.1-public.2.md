---
id: "KF-07e"
title: "Gastforschende, Stipendien und Zugriffssteuerung"
version: "1.1-public.2"
status: "draft"
last_reviewed: "2026-10-22"
review_cycle: "annual"
profiles:
  - "researcher"
scope: "Hochschulen und Forschungseinrichtungen; Schwerpunkt Deutschland/EU"
document_type: "Kuratierte Knowledge File Forschungssicherheit"
related: []
knowledge_area: null
purpose: null
binding: null
---

<!-- SPDX-License-Identifier: Apache-2.0; Public adaptation 2026-10-22; source version 1.1; editorial adaptation, not a new legal review. -->
<!-- Editorial revision 2026-10-26: researcher-role, response-rule or source-register consistency; no new legal review; last_reviewed retained. -->

# Gastforschende, Stipendien und Zugriffssteuerung

## Zweck

Diese Datei strukturiert die Prüfung von Gastaufenthalten, Promotionsvorhaben, Stipendien und vergleichbaren Aufenthalten. Sie verbindet Exportkontrolle, Forschungssicherheit, Datenschutz, IT-Sicherheit und eine praktikable, projektbezogene Zugriffssteuerung.

## Grundsätze

- Nationalität oder Herkunft allein darf keine Risikoeinstufung bestimmen.
- Ein Stipendium oder staatlicher Fördergeber ist kein automatischer Ausschlussgrund.
- Entscheidend sind Thema, Person, Heimatinstitution, Förderbedingungen, konkrete Tätigkeiten, benötigte Güter, Daten, Software, Zugriffe, Endverwendung und Weitergabe.
- Schutzmaßnahmen müssen sachlich begründet, verhältnismäßig, projektbezogen und dokumentiert sein.
- Der Zugriff wird nach Erforderlichkeit vergeben und nicht nach pauschalen Länder- oder Personenkategorien.

## Mindestangaben

### Person und institutioneller Kontext

- Name, Funktion, Fachgebiet und Projektrolle;
- aktuelle Heimatinstitution und konkrete Untereinheit;
- Gastgeberin oder Gastgeber an der betreibenden Einrichtung;
- relevante Beschäftigungs-, Förder- und Mehrfachaffiliationen;
- Aufenthaltszeitraum und tatsächlicher Arbeits-/Zugriffsstandort.

Zusätzliche personenbezogene Identifikatoren sind nur bei konkretem Klärungsbedarf und unter Beachtung der Datenschutzanforderungen zu erheben.

### Projekt und Tätigkeiten

- konkrete Forschungsfrage und Arbeitspakete;
- vorgesehene Labor-, Geräte-, Software- und Datennutzung;
- Veröffentlichungsstatus der Informationen;
- Schulungen, technische Beratung oder gemeinsame Entwicklung;
- Endnutzer, Ergebnisverwendung und geplante Weitergabe.

### Finanzierung und Verträge

- Förderorganisation und konkrete Förderlinie;
- Vertragsparteien;
- Berichts-, Rückkehr-, Geheimhaltungs-, Daten-, Publikations- und IP-Pflichten;
- weitere Sponsoren, Auftraggeber oder Endnutzer.

## Zugriffsmatrix

Die konkrete Bezeichnung der Stufen ist lokal abzustimmen. Folgende funktionale Unterscheidung kann als Entwurf dienen:

### Stufe A – allgemeiner, projektbezogener Standardzugang

- persönliche Basis-IT;
- veröffentlichte oder allgemein zugängliche Informationen;
- für das Projekt erforderliche Standardräume und -dienste;
- keine administrativen Rechte und keine nicht erforderlichen internen Datensätze.

### Stufe B – begrenzter Fachzugang

- ausgewählte interne Datensätze, Software, Geräte oder Laborbereiche;
- personalisierte, befristete Rechte;
- dokumentierte Freigabe durch fachlich verantwortliche Person und System-/Datenverantwortliche;
- Least-Privilege und regelmäßige Überprüfung.

### Stufe C – besonders schutzbedürftiger Zugang

- nicht öffentlicher Quellcode, technische Zeichnungen, sensible Forschungsdaten, Spezialsoftware oder administrative Funktionen;
- zusätzliche Prüfung von Exportkontrolle, Forschungssicherheit, Datenschutz, IT-Sicherheit und Anbieterbedingungen;
- ausdrücklich dokumentierte Freigabe, technische Schutzmaßnahmen und engmaschige Überprüfung.

### Stufe D – bis zur fachlichen oder rechtlichen Klärung nicht freischalten

Diese Stufe ist zu verwenden, wenn wesentliche Angaben fehlen, ein möglicher Listentreffer vorliegt, eine rechtliche Beschränkung nicht ausgeschlossen ist oder Schutzmaßnahmen noch nicht festgelegt sind.

Nur wenn ein rechtliches Verbot tatsächlich festgestellt wurde, darf der Zugang als unzulässig bezeichnet werden. Fehlende Informationen allein sind kein personenbezogener Risikonachweis.

## Prozess

### 1. Bedarf bestimmen

- Welche konkreten Aufgaben soll die Person erledigen?
- Welche Daten, Systeme, Räume, Geräte und Funktionen sind dafür erforderlich?
- Kann mit veröffentlichten, reduzierten oder synthetischen Daten gearbeitet werden?
- Genügt Lesezugriff?
- Ist Download oder lokales Speichern erforderlich?

### 2. Prüfdimensionen zuordnen

- Exportkontrolle und Sanktionen;
- Forschungssicherheit;
- Datenschutz;
- IT-Sicherheit;
- Lizenz- und Anbieterbedingungen;
- arbeits-, gast- oder vertragsrechtliche Vorgaben.

### 3. Rechte festlegen

- personalisiert und befristet;
- Least-Privilege und Need-to-know;
- keine gemeinsamen Accounts;
- getrennte Ablage unterschiedlicher Schutzbedarfe;
- dokumentierte Freigabe und Ablaufdatum.

### 4. Änderungen und Auffälligkeiten behandeln

Erneute Prüfung bei:

- Themen- oder Aufgabenänderung;
- neuer Institution, Förderung oder Affiliation;
- erweitertem Daten-, Software-, Labor- oder HPC-Zugriff;
- zusätzlicher Weitergabe oder neuem Nutzungsort;
- ungewöhnlichen Download-, Login- oder Zugriffsereignissen.

### 5. Offboarding

- Accounts, Schlüssel und Berechtigungen zum Enddatum entziehen;
- lokale Kopien, Datenträger und Rückgaben nach den geltenden Regeln behandeln;
- Weiterverwendung, Löschung und Archivierung dokumentieren;
- verbleibende Publikations-, Geheimhaltungs- oder Rückgabepflichten klären.

## Lokale Festlegungen

Folgende Punkte sind einrichtungsspezifisch:

- wer die Zugriffsstufen fachlich festlegt;
- wer B- und C-Zugriffe technisch und organisatorisch genehmigt;
- was als Standardzugang der Stufe A gilt;
- welche Stelle Exportkontrolle/Forschungssicherheit, Datenschutz und IT-Sicherheit einbindet;
- wer Logging, Laufzeiten und Offboarding technisch umsetzt;
- wie lange Zugriffsprotokolle gespeichert werden;
- wie Konflikt- und Eskalationsfälle entschieden und dokumentiert werden.

Diese Angaben nur nennen, wenn sie im bestätigten lokalen Kontext stehen; nicht erfinden oder vermuten.

## Antwortmuster

**Einordnung:** Der Gast- oder Förderbezug ist kein automatischer Ausschlussgrund. Entscheidend sind konkrete Tätigkeit, Vertragspflichten und die für das Projekt tatsächlich benötigten Zugriffe.

**Zu klären:** Heimatinstitution und Förderbedingungen, Arbeitspakete, Daten/Software/Geräte, Zugriffsstandort, Endverwendung und Weitergabe.

**Nächster Schritt:** Zunächst personalisierten, befristeten Mindestzugriff vorsehen und weitergehende Rechte erst nach dokumentierter fachlicher und technischer Prüfung vergeben.

## Quellen

- DFG, Risiken internationaler Kooperationen: https://www.dfg.de/de/grundlagen-themen/grundlagen-und-prinzipien-der-foerderung/sicherheitsrelevante-forschung/risiken-int-kooperationen
- DAAD/KIWi, Checkliste Wissenssicherheit: https://www.daad.de/de/infos-services-fuer-hochschulen/kompetenzzentrum/kiwi-publikationen/kiwi-kompass-checkliste/
- BAFA, Exportkontrolle und Wissenschaft: https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Academia/academia_node.html
- DFG, Resilienz von Forschungsdateninfrastrukturen: https://www.dfg.de/de/aktuelles/neuigkeiten-themen/pressemitteilungen/2026/pressemitteilung-nr-09
- Bundesamt für Verfassungsschutz, Wirtschaft und Wissenschaft: https://www.verfassungsschutz.de/DE/service/praevention_wirtschafts-und-wissenschaftsschutz/wirtschaft-und-wissenschaft_node.html
- Weitere Quellen: siehe KF-98.
