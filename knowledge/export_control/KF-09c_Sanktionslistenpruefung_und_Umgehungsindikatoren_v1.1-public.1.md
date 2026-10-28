---
id: "KF-09c"
title: "Sanktionslistenprüfung und Umgehungsindikatoren"
version: "1.1-public.1"
status: "draft"
last_reviewed: "2026-10-22"
review_cycle: "quarterly"
profiles:
  - "researcher"
scope: "Hochschulen und Forschungseinrichtungen; Schwerpunkt Deutschland/EU"
document_type: "Kuratierte Knowledge File Exportkontrolle"
related: []
knowledge_area: null
purpose: null
binding: null
---

<!-- SPDX-License-Identifier: Apache-2.0; Public adaptation 2026-10-22; source version 1.1; editorial adaptation, not a new legal review. -->

# Sanktionslistenprüfung und Umgehungsindikatoren

## Zweck

Diese Datei beschreibt eine nachvollziehbare Mindestmethode für personenbezogene und einrichtungsbezogene Prüfungen sowie für die Erkennung möglicher Sanktionsumgehung. Sie ersetzt weder eine aktuelle amtliche Quellenprüfung noch die rechtliche Bewertung eines möglichen Treffers.

## Wichtige Systemgrenze

KI-Companion Exportkontrolle führt **keine aktuelle Sanktionslistenprüfung** durch, sofern kein angebundenes Screening-Werkzeug im konkreten Chat tatsächlich aufgerufen und erfolgreich ausgeführt wurde. Das bloße Vorhandensein dieser Knowledge File oder einer Linkliste ist kein Screening.

## Grundsatz

Ein Screening ist mehr als eine einfache Namenssuche. Es muss:

- aktuelle und einschlägige Quellen verwenden;
- Schreibvarianten, Aliasse und Transliteration berücksichtigen;
- Identität anhand zusätzlicher Merkmale verifizieren;
- bei Einrichtungen Eigentum, Kontrolle und Untereinheiten einbeziehen;
- Ergebnis, Datum, Quelle und Bearbeitung dokumentieren;
- zwischen Suchergebnis und rechtlicher Trefferbewertung unterscheiden.

## Datensparsame Erhebung

### Erste Suche

Für eine erste Suche reichen regelmäßig:

- vollständiger Name beziehungsweise offizieller Einrichtungsname;
- bekannte Schreibvarianten;
- Land;
- institutionelle Zugehörigkeit oder Rolle;
- bei Einrichtungen Sitz und konkrete Untereinheit.

### Klärung eines möglichen Treffers

Nur wenn ein möglicher Treffer vorliegt, können weitere Identifikatoren erforderlich sein, etwa:

- Geburtsdatum und Geburtsort;
- Anschrift;
- Staatsangehörigkeit;
- frühere Namen;
- Register- oder Identifikationsnummer;
- Mutter-, Tochter- oder kontrollierende Organisationen.

Ausweis- oder Passdaten dürfen nur verwendet werden, wenn dies für die Identitätsklärung erforderlich und datenschutzrechtlich zulässig ist. Es sind nur die erforderlichen Daten zu dokumentieren.

## Quellenhierarchie

Für EU-Sanktionen gilt:

1. **Amtlicher EU-Rechtsakt und Amtsblatt** – rechtlich maßgeblich;
2. **offizielle EU-Datensätze und EU-Ressourcen** – für konsolidierte Suche und Orientierung;
3. **zuständige deutsche Behörden** – insbesondere Bundesbank und BAFA;
4. **OpenSanctions** – ergänzendes Such-, Aggregations- und Matchingwerkzeug;
5. weitere Sekundärquellen nur zur Recherche, nicht als alleinige Entscheidungsgrundlage.

OpenSanctions kann die Suche nach Schreibvarianten und verknüpften Datensätzen unterstützen. Ein möglicher Treffer ist anhand des verlinkten Rechtsakts beziehungsweise des amtlichen Listeneintrags zu verifizieren. OpenSanctions ist keine amtliche Rechtsquelle.

## Prüfablauf

### 1. Suchraum festlegen

- einschlägiges Sanktionsregime und Vorgangsart bestimmen;
- betroffene Person, Einrichtung und Untereinheit identifizieren;
- bei Drittstaatenbezug gegebenenfalls weitere Rechtsordnungen getrennt prüfen.

### 2. Suchvarianten bilden

- Vorname und Nachname in unterschiedlicher Reihenfolge;
- Namensbestandteile einzeln und kombiniert;
- lateinische und nicht lateinische Schreibweisen;
- Bindestriche, Leerzeichen, Titel und Rechtsformvarianten;
- bekannte Aliasse und Abkürzungen.

### 3. Ergebnis einordnen

Für die technische oder orientierende Ausgabe sind folgende neutrale Zustände geeignet:

- **no_match_found / kein Treffer gefunden:** In den tatsächlich geprüften Quellen wurde keine Übereinstimmung gefunden. Dies ist keine Gesamtfreigabe.
- **possible_match / möglicher Treffer:** Namensähnlichkeit oder Teilübereinstimmung; Identität muss fachlich geklärt werden.
- **insufficient_data / unzureichende Angaben:** Die vorhandenen Daten reichen für eine belastbare Suche oder Abgrenzung nicht aus.
- **screening_unavailable / Screening nicht verfügbar:** Werkzeug oder Quelle war nicht erreichbar beziehungsweise wurde nicht ausgeführt.

Ein **bestätigter Treffer** darf erst nach belastbarem Identitätsabgleich und Prüfung des maßgeblichen Rechtsakts angenommen werden.

### 4. Eigentum und Kontrolle prüfen

Auch eine nicht namentlich gelistete Einrichtung kann sanktionsrechtlich erfasst sein, wenn sie im Eigentum oder unter Kontrolle eines gelisteten Akteurs steht. Bei unklaren Strukturen sind Beteiligungen, Kontrolle, tatsächliche Leitung und wirtschaftliche Bereitstellung vertieft zu prüfen.

### 5. Dokumentieren

```text
Prüfdatum:
Prüfende Stelle oder Werkzeug:
Geprüfte Person/Einrichtung:
Schreibweisen/Aliasse:
Quellen und Datenstand:
Suchergebnis:
Identitätsabgleich:
Eigentum/Kontrolle:
Offene Punkte:
Folgeschritt:
```

## Umgehungsindikatoren

Eine vertiefte Prüfung ist insbesondere erforderlich bei:

- ungewöhnlicher Einbindung von Zwischenhändlern oder Drittstaaten;
- abweichendem Rechnungsempfänger, Endnutzer oder Lieferort;
- Privatadressen oder privaten Accounts bei institutionellen Vorgängen;
- kurzfristigem Austausch von Beteiligten nach Rückfragen;
- unklarer Eigentümer- oder Kontrollstruktur;
- widersprüchlichen Angaben zu Zweck oder Endverwendung;
- Wunsch nach unzutreffender, verkürzter oder neutraler Warenbeschreibung;
- Aufteilung von Lieferungen oder Zahlungen ohne sachliche Begründung;
- ungewöhnlicher Barzahlung, Kryptowährung oder komplexer Zahlungsroute;
- Nutzung von VPN, Proxy, Remotezugriff oder Account-Sharing zur Umgehung von Länder-, Sanktions- oder Lizenzbeschränkungen;
- Forschungspartnern ohne nachvollziehbare fachliche Rolle;
- Weiterleitung sensibler Daten an nicht genannte Einrichtungen.

## Bot-Regeln

- Kein „kein Treffer = freigegeben“.
- Keinen Treffer allein aufgrund eines ähnlichen Namens bestätigen.
- Keine personenbezogene Verdachtsbehauptung formulieren.
- Klar benennen, ob ein Werkzeug tatsächlich ausgeführt wurde.
- Sachlich zwischen Listentreffer, Kontextindikator und ungeklärtem Sachverhalt unterscheiden.
- Nur die für den nächsten Prüfschritt erforderlichen personenbezogenen Daten erfragen.
- Bei möglichem Treffer an die zuständige fachliche Stelle verweisen.

## Quellen

- Europäische Kommission, konsolidierte Finanzsanktionsliste und Ressourcen: https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en
- EU Sanctions Map: https://www.sanctionsmap.eu/
- Deutsche Bundesbank, Finanzsanktionen: https://www.bundesbank.de/de/service/finanzsanktionen/finanzsanktionen-609138
- OpenSanctions, EU Council Official Journal Sanctioned Entities: https://www.opensanctions.org/datasets/eu_journal_sanctions/
- OpenSanctions, EU Financial Sanctions Files: https://www.opensanctions.org/datasets/eu_fsf/
- Europäische Kommission, Sanktionsumgehung und Due Diligence: https://finance.ec.europa.eu/publications/circumvention-and-due-diligence_en
- BAFA, Verhinderung von Sanktionsumgehung: https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Embargos/Russland/Regelungen_Verhinderung_Sanktionsumgehung/regelungen_verhinderung_sanktionumgehung_node.html
- Weitere Quellen: siehe KF-98.
