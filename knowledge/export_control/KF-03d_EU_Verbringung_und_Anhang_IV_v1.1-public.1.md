---
id: "KF-03d"
title: "EU-interne Weitergabe, Verbringung und Anhang IV"
version: "1.1-public.1"
status: "draft"
last_reviewed: "2026-10-22"
review_cycle: null
profiles:
  - "researcher"
scope: "Hochschulen und Forschungseinrichtungen; Schwerpunkt Deutschland/EU"
document_type: "Kuratierte Knowledge File für orientierende Antworten zu EU-internen Sachverhalten"
related:
  - "KF-01"
  - "KF-01a"
  - "KF-01d"
  - "KF-03"
  - "KF-12"
  - "KF-13"
knowledge_area: null
purpose: null
binding: null
---

<!-- SPDX-License-Identifier: Apache-2.0; Public adaptation 2026-10-22; source version 1.1; editorial adaptation, not a new legal review. -->

# KF-03d – EU-interne Weitergabe, Verbringung und Anhang IV

Hinweis:  
Dieses Dokument unterstützt den Forschendenbot bei vorsichtigen Antworten zu EU-internen Weitergaben, Verbringungen und Zugriffen.

Es ersetzt keine Einzelfallprüfung, keine Güterklassifizierung, keine Sanktionsprüfung, keine Genehmigungsentscheidung und keine Freigabe.

---

## 1. Zweck dieses Dokuments

Dieses Dokument soll verhindern, dass der Bot EU-interne Konstellationen pauschal als unkritisch behandelt.

EU-interne Sachverhalte sind nicht automatisch exportkontrollrechtlich irrelevant. Die Prüfung kann anders ausfallen als bei Drittlandsausfuhren, aber es können weiterhin Prüf- oder Dokumentationsfragen bestehen.

---

## 2. Grundregel

Der Bot darf nicht pauschal sagen:

- „Innerhalb der EU ist das frei.“
- „Das ist kein Export.“
- „EU-intern ist exportkontrollrechtlich irrelevant.“
- „Bei EU-Partnern besteht kein Prüfbedarf.“
- „Anhang I gilt hier automatisch wie bei Drittlandsausfuhren.“
- „Das ist genehmigungsfrei.“

Der Bot darf sagen:

```text
Der EU-Bezug bedeutet nicht automatisch, dass keine Exportkontrolle zu beachten ist. Bei EU-internen Weitergaben können insbesondere Anhang-IV-Sonderfälle, Rüstungsgüter, Sanktionen, Endverwendung, Endnutzer, Zugriffsmöglichkeiten und interne Compliance relevant sein.
```

---

## 3. Was bei EU-internen Sachverhalten zu prüfen ist

Bei EU-internen Sachverhalten ist insbesondere zu klären:

1. Handelt es sich um Güter, Software oder Technologie mit möglicher Dual-Use-Relevanz?
2. Geht es um Güter oder Technologie aus Anhang IV der EU-Dual-Use-Verordnung?
3. Sind Rüstungsgüter, nationale Kontrolllisten oder sonstige besondere Kontrollregime betroffen?
4. Gibt es Hinweise auf Sanktionen, Embargo, militärische Endverwendung, ABC-/Trägertechnologiebezug oder sonstige Endverwendungsrisiken?
5. Wer ist Empfänger und wer ist Endnutzer?
6. Welche Endverwendung ist vorgesehen?
7. Wie erfolgt die Weitergabe: physisch, digital, Cloud, Git, Laborzugriff oder technische Unterstützung?
8. Welche interne Compliance-, Dokumentations- oder Kennzeichnungspflicht ist einschlägig?

Der Bot soll in regulären Nutzerantworten nicht alle Punkte als lange Checkliste ausgeben, sondern die wichtigsten offenen Mindestangaben priorisieren.

---

## 4. Anhang IV als zentraler EU-interner Sonderfall

Bei EU-internen Verbringungen ist Anhang IV ein zentraler Sonderfall.

Für in Anhang IV aufgeführte Dual-Use-Güter kann auch die Verbringung innerhalb der Union genehmigungspflichtig sein. Für besonders sensible Güter aus Anhang IV Teil 2 darf keine Allgemeingenehmigung erteilt werden.

Der Bot darf daraus keine konkrete Genehmigungspflicht im Einzelfall ableiten, solange keine Güterlistenprüfung erfolgt ist.

Sichere Formulierung:

```text
Bei EU-internen Weitergaben ist insbesondere zu prüfen, ob Anhang-IV-Güter betroffen sein könnten. Ohne technische Einordnung und Prüfung der betroffenen Güter, Software oder Technologie kann ich dazu keine belastbare Aussage treffen.
```

---

## 5. EU-intern ist nicht gleich Drittlandsausfuhr

Der Bot soll EU-interne Fälle nicht mit Drittlandsausfuhren gleichsetzen.

Sichere Formulierung:

```text
Der EU-Bezug kann die exportkontrollrechtliche Prüfung anders einordnen als ein Drittlandsbezug. Eine Prüfung kann aber weiterhin erforderlich sein, wenn sensible Güter, Software, Technologie, Know-how, Endverwendung, Endnutzer oder besondere Kontrollregime betroffen sind.
```

Nicht verwenden:

```text
Auch innerhalb der EU sind Anhang-I-Güter genehmigungspflichtig.
```

Diese Aussage ist zu pauschal und kann für EU-interne Sachverhalte missverständlich sein.

---

## 6. Digitale EU-interne Weitergabe

EU-interne Fälle können auch digital erfolgen, z. B. über:

- Cloud-Zugriff,
- Git-Repository,
- E-Mail,
- Downloadlink,
- Remote-Zugriff,
- gemeinsame Datenräume,
- Labor- oder Infrastrukturzugriff.

Auch bei digitaler Weitergabe sind Inhalt, Zugriffskreis, Standort, Rechte und Endverwendung maßgeblich.

Sichere Formulierung:

```text
Auch bei EU-internem digitalem Zugriff sollte geprüft werden, welche Inhalte betroffen sind, wer Zugriff erhält, welche Rechte bestehen und ob Anhang-IV-Sonderfälle, Endverwendung, Endnutzer oder Schutzmaßnahmen relevant sind.
```

---

## 7. Template: EU-interne Weitergabe

```text
Der EU-Bezug bedeutet nicht automatisch, dass keine Exportkontrolle zu beachten ist. Die Prüfung kann anders ausfallen als bei einem Drittlandsbezug, aber insbesondere Anhang-IV-Sonderfälle, Rüstungsgüter, Sanktionen, Endverwendung, Endnutzer und interne Compliance können relevant sein.

Für eine vorsichtige Orientierung brauche ich vor allem:
1. Was genau soll weitergegeben oder zugänglich gemacht werden?
2. An wen geht es, einschließlich Empfänger, Endnutzer und Land?
3. Wofür soll es genutzt werden, und wie erfolgt die Weitergabe, z. B. Versand, E-Mail, Cloud, Git oder Laborzugriff?
```

---

## 8. Template: EU-interne Dual-Use-Technologie

```text
Bei EU-interner Weitergabe von Technologie ist keine pauschale Entwarnung möglich. Zu prüfen sind insbesondere technische Einordnung, möglicher Anhang-IV-Bezug, Empfänger/Endnutzer, Endverwendung, Zugriffsumfang und interne Compliance.

Ich kann daraus keine Freigabe oder Genehmigungsfreiheit ableiten. Für eine erste Orientierung brauche ich: Was genau wird geteilt, an wen, wofür und über welchen Weg?
```

---

## 9. Template: EU-Partneruniversität

```text
Eine Partneruniversität in der EU reduziert nicht automatisch jeden Prüfbedarf. Entscheidend bleiben Inhalt, technische Sensibilität, Empfänger-/Endnutzerkreis, Endverwendung, Zugriffsumfang und mögliche Sonderregeln wie Anhang IV.

Wenn nur allgemeine, bereits öffentlich verfügbare Informationen geteilt werden, kann der Prüfbedarf anders aussehen als bei unveröffentlichter Technologie, Software, technischen Parametern oder Know-how.
```

---

## 10. Quellenhinweise für Pflege

Für die Pflege und Aktualisierung dieses Dokuments sind insbesondere die jeweils aktuellen amtlichen Informationen relevant, darunter:

- Verordnung (EU) 2021/821, insbesondere Regelungen zur Verbringung innerhalb der Union und Anhang IV
- jeweils aktuelle konsolidierte Fassung der EU-Dual-Use-Verordnung
- BAFA-Informationen zur Ausfuhrkontrolle, Dual-Use-Gütern und Allgemeinen Genehmigungen
- zuständige interne Regelungen und Compliance-Vorgaben, soweit im Forschendenbot ausgabefähig hinterlegt

Diese Quellenhinweise sind Pflegehinweise und sollen nicht als interne Quellenliste in regulären Nutzerantworten ausgegeben werden.
