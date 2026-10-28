---
id: "KF-07f"
title: "Daten, Software, Cloud und IT-Zugänge"
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

# Daten, Software, Cloud und IT-Zugänge

## Zweck

Digitale Bereitstellungen können exportkontrollrechtlich, sanktionsrechtlich, datenschutzrechtlich, lizenzrechtlich und forschungssicherheitsbezogen relevant sein. Diese Datei strukturiert die Prüfung von Software, Quellcode, technischen Daten, Cloud-, VPN-, HPC- und Fernzugriffen.

Ein digitaler Zugriff ist **nicht allein wegen seiner technischen Form automatisch ein kontrollierter Export**. Entscheidend sind Inhalt, Klassifizierung, Nutzer, tatsächlicher Standort, Rechteumfang, öffentliche Verfügbarkeit, Endverwendung, Weitergabe sowie Anbieter- und Vertragsbedingungen.

## Fünf getrennte Prüfdimensionen

### 1. Exportkontrolle

- Handelt es sich um kontrollierte Software oder Technologie?
- Liegt ein grenzüberschreitender Export, eine Übermittlung oder ein sonstiger relevanter Technologietransfer vor?
- Welche Person hat von welchem Staat oder Gebiet aus Zugriff?
- Sind Endverwendungs- oder Catch-all-Regeln relevant?

### 2. Sanktionen und Anbieterbeschränkungen

- Sind Person, Einrichtung, Eigentümer oder Endnutzer gelistet?
- Bestehen Länder-, Gebiets-, Dienstleistungs- oder Bereitstellungsverbote?
- Beschränkt der Anbieter Nutzer, Staat, Einrichtung oder Endverwendung?
- Würde eine technische Lösung eine Geosperre oder Vertragsbedingung umgehen?

### 3. Forschungssicherheit

- Welche nicht öffentlichen Daten, Methoden oder technischen Fähigkeiten werden zugänglich?
- Ist der Rechteumfang für das Arbeitspaket erforderlich?
- Bestehen institutionelle, finanzielle oder vertragliche Weitergabepflichten?
- Welche Abhängigkeiten und Möglichkeiten des Massendownloads oder der Weiterverwendung entstehen?

### 4. Datenschutz

- Sind personenbezogene oder besonders sensible Daten betroffen?
- Auf welcher Rechtsgrundlage werden Daten verarbeitet oder übermittelt?
- Wo werden Daten gespeichert, verarbeitet und tatsächlich abgerufen?
- Welche Unterauftragnehmer, Behördenzugriffe, Lösch- und Rückgaberegeln bestehen?
- Sind Datenminimierung, Pseudonymisierung oder ein reduzierter Datensatz möglich?

### 5. IT-Sicherheit und Lizenzbedingungen

- Sind personalisierte Accounts, MFA und befristete Rechte vorgesehen?
- Sind Logging, Monitoring und Offboarding angemessen?
- Welche Lizenz-, Nutzungs-, Export- oder Geobeschränkungen gelten?
- Bestehen sichere Alternativen zu privaten Accounts, privater Cloud oder lokalen Datenträgern?

## Relevante Bereitstellungsformen

- Download oder E-Mail-Versand;
- Freigabe eines Cloudordners;
- Zugriff auf Git-Repositories oder Quellcode;
- VPN, Remote Desktop oder SSH;
- Nutzung eines Lizenzservers;
- Zugang zu HPC, Rechenclustern oder Spezialdatenbanken;
- Bildschirmfreigabe, Onlineschulung oder technische Beratung;
- Upload von Daten in Dienste eines Drittanbieters;
- gemeinsame oder private Accounts;
- lokale Kopie oder Synchronisation auf Endgeräten.

## Mindestprüfung

### Inhalt

- Datentyp, Software, Quellcode, Modell, technische Unterlage oder Funktion;
- öffentlich verfügbar oder nicht öffentlich;
- mögliche Güterlisten- oder sonstige Kontrollrelevanz;
- Schutzbedarf, Personenbezug und vertragliche Beschränkungen;
- technische Parameter und vorgesehene Nutzung.

### Person und Einrichtung

- Identität, Rolle und institutionelle Zugehörigkeit;
- konkrete Untereinheit;
- tatsächlicher Nutzungs- und Zugriffsstandort;
- weitere Personen mit Zugriff;
- Sponsor, Endnutzer und mögliche Weitergabe.

### Dienst und Anbieter

- Anbieter, Vertrag und eingesetzte Produktversion;
- Speicher-, Verarbeitungs- und Supportstandorte;
- Unterauftragnehmer;
- Länder-, Sanktions-, Export- und Lizenzbedingungen;
- Möglichkeiten von Download, Export, API-Zugriff und Account-Sharing.

### Erforderlichkeit

- Welche Funktionen, Systeme und Daten werden für das Arbeitspaket tatsächlich benötigt?
- Genügt ein reduzierter, veröffentlichter oder synthetischer Datensatz?
- Genügt Lesezugriff?
- Muss ein Download oder lokales Speichern möglich sein?
- Ist der Zugriff zeitlich begrenzt?

### Endverwendung und Weitergabe

- konkrete wissenschaftliche Arbeitsschritte;
- spätere Nutzung durch Heimatinstitution, Sponsor oder Dritte;
- Export, Kopie, lokales Speichern und Einbindung in andere Systeme;
- vorgesehene Publikation, Archivierung, Löschung und Rückgabe.

## Warnhinweise

- Account-Sharing oder Gruppenaccount;
- private E-Mail-Adresse oder privater Cloudspeicher;
- VPN oder Proxy zur Umgehung von Geoblocking;
- Installation unbekannter Fernzugriffssoftware;
- Vollzugriff, obwohl nur ein Teilprojekt bearbeitet wird;
- Massendownloads oder ungewöhnliche Zugriffsereignisse;
- Sponsor verlangt Rohdaten, Quellcode oder administrative Rechte ohne klare Projektbegründung;
- Nutzerstandort oder Identität weicht von den Angaben ab;
- Anbieter untersagt die Nutzung im betroffenen Staat, durch die Einrichtung oder für die Endverwendung;
- unklare Löschung, Rückgabe oder Weitergabe nach Projektende.

## Schutzmaßnahmen

- personalisierte und befristete Accounts;
- Multi-Faktor-Authentifizierung;
- Least-Privilege und Lesezugriff als Ausgangspunkt;
- Download- und Exportbeschränkungen, soweit technisch, rechtlich und projektbezogen angemessen;
- Protokollierung besonders schutzbedürftiger Zugriffe;
- getrennte Entwicklungs-, Test- und Produktivumgebungen;
- keine administrativen Rechte ohne dokumentierte Erforderlichkeit;
- Freigabe von Quellcode, technischen Daten und Spezialsoftware auf Dateisatz- oder Systemebene;
- sofortiges Offboarding bei Projektende oder Rollenwechsel;
- regelmäßige Sicherung und resiliente Ablage kritischer Forschungsdaten.

## US-Bezug

Bei US-Software, US-Cloud, US-Hardware oder US-Technologie sind getrennt zu prüfen:

- Anbieter- und Sanktionsbedingungen;
- mögliche EAR-Relevanz aufgrund von US-Ursprung, kontrolliertem Inhalt oder bestimmten Foreign-Direct-Product-Regeln;
- Klassifizierung und bekannte Nutzungsbeschränkungen;
- Nutzer, Staat, Einrichtung und Endverwendung;
- OFAC- oder sonstige US-Sanktionsbezüge.

Die bloße Nutzung des Internets, eine US-Dollar-Zahlung oder eine allgemein verfügbare Standardsoftware begründet für sich allein keine EAR-Einstufung.

## China-bezogene Datentransfers

Bei Datentransfers, Cloud- oder Plattformnutzung mit China-Bezug zusätzlich prüfen:

- Speicher-, Verarbeitungs- und Zugriffsorte;
- vertragliche Zugriffs- und Weitergaberechte;
- einschlägige chinesische Datenschutz- und Datensicherheitsanforderungen;
- mögliche Behörden- oder Drittzugriffe;
- Löschung, Rückgabe und Weiterverwendung;
- Vereinbarkeit mit deutschen und europäischen Datenschutzanforderungen.

Der KIWi-Kompass „Datenschutz in China“ bietet hierfür Checklisten und Hinweise zur Vertragsgestaltung.

## Lokale Festlegungen

Folgende Punkte sind einrichtungsspezifisch:

- zulässige Cloud- und Kollaborationsdienste;
- Verfahren für externe Accounts, VPN, HPC und Lizenzserver;
- Zuständigkeiten von IT-Sicherheit, Datenschutz, System-/Datenverantwortlichen und Exportkontroll-/Forschungssicherheitsstelle;
- Freigabeprozess für besonders schutzbedürftige Daten und Spezialsoftware;
- Loggingumfang und Aufbewahrungsdauer;
- Offboarding, Löschung und Rückgabe.

Diese Angaben nur nennen, wenn sie im bestätigten lokalen Kontext stehen; nicht ergänzen oder vermuten.

## Antwortmuster

**Einordnung:** Ein digitaler Zugriff kann eine relevante Bereitstellung von Software, Technologie, Daten oder technischem Wissen sein. Die technische Zugriffsform allein entscheidet jedoch nicht über Exportkontrolle oder Zulässigkeit.

**Zu klären:** konkreter Inhalt, Nutzer und Einrichtung, tatsächlicher Standort, Anbieter und Vertrag, Rechteumfang, Endverwendung, Weitergabe sowie Datenschutz- und IT-Sicherheitsanforderungen.

**Nächster Schritt:** Zunächst personalisierten, befristeten Mindestzugriff ohne administrative Rechte oder nicht erforderlichen Download vorsehen und die fünf Prüfdimensionen dokumentieren.

## Quellen

- BAFA, Exportkontrolle und Wissenschaft: https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Academia/academia_node.html
- BAFA, Handbuch Exportkontrolle und Academia: https://www.bafa.de/SharedDocs/Downloads/DE/Aussenwirtschaft/afk_aca_broschuere_handbuch.html
- DFG, Sicherheitsrelevante Forschung: https://www.dfg.de/de/grundlagen-themen/grundlagen-und-prinzipien-der-foerderung/sicherheitsrelevante-forschung
- DFG, Empfehlungen zur Resilienz von Forschungsdateninfrastrukturen: https://www.dfg.de/de/aktuelles/neuigkeiten-themen/pressemitteilungen/2026/pressemitteilung-nr-09
- DAAD/KIWi, rechtliche Rahmenbedingungen und „Datenschutz in China“: https://www.daad.de/de/infos-services-fuer-hochschulen/kompetenzzentrum/kiwi-themen/rechtliche-rahmenbedingungen/
- BIS, Determine What Is Subject to the EAR: https://media.bis.gov/licensing/determine-what-is-subject-to-the-EAR
- Weitere Quellen: siehe KF-98.
