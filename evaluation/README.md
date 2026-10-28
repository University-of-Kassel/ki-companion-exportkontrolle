# Evaluation des Forschendenbots

Stand: 26.10.2026 | Version 1.2 | Quellstand 1.0.0

Die 45 Golden Questions sind **Testdefinitionen, keine bestandenen Tests**. 27 aktuelle Ausgangsfälle wurden erhalten oder gezielt neutralisiert; zwei negative Lokalfaktenfälle und 16 Scope-/Plausibilitätsfälle ergänzt. Unit-Tests unter `tests/` bewerten nur Hilfsskripte und Repository-Eigenschaften.

Die Fälle sind plattformneutral. Die eigene Oberfläche, Anwendung oder API kann zur Ausführung genutzt werden, sofern die tatsächlichen Anweisungen, Wissenskontexte und Gesprächsfolgen kontrolliert werden. Es wird keine bestimmte Plattform vorausgesetzt.

## Plan erstellen

```bash
python scripts/prepare_evaluation.py --out dist/evaluation-plan.json
```

Alle Einträge bleiben `not_run`. Kein Modell und kein Judge wird aufgerufen. Ein vorhandener Runner muss `questions` mit `id`, `question`, `expected_behavior`, optional `must_not`, `follows` und `fixture` verarbeiten. Kompatibilität mit einem institutionellen Evaluationsprojekt wurde nicht getestet.

`follows` verlangt eine echte Fortsetzung mit den tatsächlichen Botantworten der Vorgänger. Keine erfundenen Idealantworten verwenden. Für eigenständige Fälle neue Chats nutzen. Der exportierte Plan nennt die erforderlichen Vorgänger.

## Kontrollierte lokale Kontexte

`fixture: institution.test`: isoliertes Testprofil aus `evaluation/fixtures/institution.test.json` bauen. Namen, Rollen und `.invalid`-Adressen sind ausschließlich synthetische Sollwerte. Der ausdrückliche Schalter `--allow-test-fixture` erlaubt deren Wiedergabe nur in einem als synthetisch markierten Review-Paket. Er richtet keine technische Isolation auf der Chatplattform ein: dafür ein eigenes Testprofil verwenden. Production plus Fixture-Schalter ist unzulässig; reguläre institutionelle Konfigurationen verwenden den Schalter nicht.

```bash
python scripts/build_bundle.py --mode review --config evaluation/fixtures/institution.test.json --allow-test-fixture --out dist/fixture-review
```

`fixture: unconfigured`: separates Profil ohne institutionelle Konfiguration und ohne vorherigen lokalen Gesprächskontext. Vorlagen und Testfixture nicht als RAG anbinden. Andere Fälle können mit dem allgemeinen Review-Profil laufen.

Die Fixture wird nicht in das reguläre Wissensverzeichnis des Vorbereitungspakets kopiert. KF-15 ist nur Fallmaterial für Auswertung und Schulung, kein produktives Wissen.

## Bewertung

`expected_behavior` bewertet erwünschte Merkmale. Verstoß gegen `must_not` gesondert als harten Fehler festhalten; nicht durch gute Durchschnittswerte verdecken. Besonders relevant: falsche Kontakte, implizite Freigaben und behauptete Live-Prüfungen. Die Drei-Rückfragen-Grenze gilt über alle passenden Fälle.

Ein Fall mit "PDF sagt X" prüft nur die erklärte Konfliktbehandlung, sofern keine kontrollierten Dokumente eingespielt wurden. Eine korrekte Kontaktantwort beweist allein keinen bestimmten Retrieval-Weg. Browserchat und API-Runner mit Abrufprotokollen abgleichen.

Im [Testprotokoll](TEST_PROTOCOL.md) Plattformversion, Modellkennung, Einstellungen, Quellenhashes, Antwortqualität, Quellenabruf und Grenzen getrennt festhalten. Nach Modell- oder Wissenswechsel neu testen.

## Wissensabruf gesondert nachweisen

Die vorhandenen Golden Questions bewerten sichtbares Antwortverhalten. Für einen Abrufnachweis in einem eigenen Testprofil zusätzlich eine harmlose, eindeutige Testinformation ausschließlich in einem Test-Wissensdokument hinterlegen. Sie darf nicht zugleich im Systemprompt, im Fragetext oder in früheren Antworten stehen.

Die tatsächliche Dokument-/Abschnittsauswahl, den an das Modell übertragenen Inhalt und die Antwort gemeinsam protokollieren. Den Test mit vorhandenem und entferntem Testdokument durchführen; nach Entfernung gegebenenfalls Index und Chatkontext erneuern. Oberfläche und API sowie Administrator- und normale Nutzerrechte getrennt prüfen, sofern diese Zugangswege eingesetzt werden. Testdokumente gehören nicht in das reguläre Wissensmanifest.

Für Quellenkonflikte nur dann eine tatsächliche Konfliktauflösung bewerten, wenn die verglichenen Passagen kontrolliert bereitgestellt und deren Abruf belegt wurden. Ein grünes Ergebnis in einem abstrakten Policy-Test ersetzt diesen Nachweis nicht.
