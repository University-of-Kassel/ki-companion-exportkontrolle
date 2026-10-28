# Einrichtung in der eigenen KI-Umgebung

Stand: 26.10.2026 | Dokumentversion 1.1 | Quellrelease 1.0.0

Diese Anleitung ist plattformunabhängig. Die Einrichtung wählt Plattform, Sprachmodell und Betriebsform selbst. Das Repository liefert Textbausteine, Konfigurationsvorlagen, Prüfskripte und Testfälle, **keinen fertigen Onlinedienst und keinen universellen Importadapter**. Das [Open-WebUI-Beispiel](openwebui.md) ist optional.

Welche Dateien und Angaben eine Einrichtung konkret bearbeiten muss und welche Betriebsbausteine nicht mitgeliefert werden, zeigt der [Einrichtungsleitfaden](einrichtungsleitfaden.md).

**Ausgangsstatus: Alle 39 KFs sind `draft`.** Die 36 fachlichen KFs sind für den Wissensabruf vorgesehen; zwei lokale Vorlagen und KF-15 als Evaluationsmaterial bleiben davon getrennt. Ein im Paket mitgeführtes Prüfdatum ist keine Freigabe für eine andere Einrichtung.

## 1. Verantwortung und Testumgebung festlegen

Fachliche Inhaltsprüfung, institutionelle Kontakte/Verfahren, technischen Betrieb und Freigabe zuordnen. Für die Erprobung eine getrennte, zugriffsbeschränkte Umgebung einrichten und zunächst synthetische statt realer Fallinformationen verwenden. Datenflüsse, Modellanbieter, Speicherung und Löschung nach den eigenen Vorgaben prüfen.

Die ausgewählte Umgebung muss folgende Funktionen ermöglichen oder die betreibende Einrichtung muss sie ergänzen:

| Funktion | Zu prüfen |
|---|---|
| Verbindliche Anweisungen | System-/Entwickleranweisungen oder gleichwertige, nicht durch Nutzereingaben ersetzbare Konfiguration |
| Kontrollierte Wissensbereitstellung | Ausgewählte Markdown-Texte oder eine inhaltlich gleichwertige Konvertierung; funktionsfähiger Abruf oder kontrollierte Kontextbereitstellung |
| Lokaler Kontext | Bestätigte Kontakte und Verfahren sind bei Bedarf tatsächlich verfügbar, nicht nur irgendwo gespeichert |
| Werkzeugsteuerung | Keine ungewollte Websuche, kein behauptetes Screening, keine fachfremden Werkzeuge |
| Testbarkeit | Antworten und verwendeten Wissenskontext nachvollziehbar prüfen; Versionen und Einstellungen dokumentieren |
| Zugriffsschutz | Interne Konfiguration, Testumgebung und öffentliche Quelldateien trennen |

Kann eine Umgebung diese Anforderungen nicht abbilden, ist zusätzliche technische Integration erforderlich. Ein erfolgreicher Dateiimport allein genügt nicht.

## 2. Quellstand und Wissensumfang prüfen

Einen bestimmten Release oder Commit als Arbeitsstand festhalten. Die Inhaltsauswahl steht in `config/knowledge-manifest.json`. Das gesamte Repository darf **nicht** pauschal als Wissen eingebunden werden: Tests, Anleitungen, lokale Vorlagen und Lizenztexte gehören nicht in die fachliche Wissenssammlung.

Jede Einrichtung prüft fachliche Richtigkeit, Aktualität, Rechtsraum, institutionelle Passung und Nutzungsbedingungen selbst. Die öffentliche Vorlage bleibt Draft. Anpassungen und spätere lokale Freigaben werden in einer eigenen Arbeitsfassung dokumentiert.

Wer den Standard-Validator nutzt, muss Manifest und Dateien unter `knowledge/` konsistent halten. Zentrale KFs sind als Mindestbestand hinterlegt. Eine reduzierte fachliche Ausrichtung erfordert daher auch eine bewusste Anpassung von Rollenbeschreibung, Abhängigkeiten und Tests; Dateien nicht stillschweigend weglassen. [Wissenspflege](knowledge-maintenance.md).

## 3. Institutionelle Angaben bestätigen

Neutrale Platzhalter durch eigene bestätigte Angaben ersetzen. Unbekannte Namen, Rollen, Kontakte und Abläufe bleiben unbekannt. Fakten und Verfahrensangaben getrennt freigeben. Herkunftshinweise im Repository sind keine lokalen Ansprechpartner.

Die mitgelieferte Konfiguration nutzt `.local/institution.json`; die [Konfigurationsanleitung](configuration.md) erläutert Felder und Kontrollen. Bei einer anderen technischen Umsetzung muss dieselbe Trennung zwischen bestätigten, unbestätigten und fehlenden Angaben gewahrt bleiben. Vertrauliche Konfiguration nicht in ein öffentliches Repository übernehmen.

## 4. Anweisungen und Wissen zusammenstellen

**Empfohlener Hilfsweg:** Der Offline-Paketbau übernimmt die explizite Auswahl, setzt lokale Angaben nur nach Bestätigung ein und kennzeichnet Draft-Inhalte.

```bash
python -m pip install -r requirements.txt
python scripts/validate_repository.py
python -m unittest discover -s tests -v
python scripts/build_bundle.py --mode review --out dist/review
# Mit institutionellen Angaben alternativ einen neuen Ausgabeordner verwenden:
python scripts/build_bundle.py --mode review --config .local/institution.json --out dist/review-local
```

Die Hilfsskripte benötigen Python 3.11+. Der Paketbau selbst sendet keine Dateien an eine Plattform oder ein Modell.

| Ausgabedatei | Zweck und Übernahme |
|---|---|
| `System.compiled.md` | Zusammengeführter Systemprompt und Forschendenprofil, einschließlich geprüftem lokalem Kontext. Als verbindliche Anweisungen der Anwendung bereitstellen. |
| `knowledge/*.md` | Nur diese 36 ausgewählten fachlichen Texte für den Wissensabruf beziehungsweise kontrollierten Kontext verwenden. |
| `Description.md`, `Starter-Prompts.md` | Optionale Oberflächentexte; an die eigene Anwendung anpassen. |
| `model-settings.reference.json` | Menschlich lesbare Konfigurationsreferenz. Kein getestetes Importformat und kein API-Aufruf. |
| `build-manifest.json` | Versionen, Status und Prüfsummen für die lokale Nachvollziehbarkeit. |
| `READ_ME_FIRST.txt` | Kurzhinweise zur privaten Nutzung des Vorbereitungspakets. |

**Eigene Umsetzung ohne diese Skripte:** `bot/prompts/System.md` und `bot/prompts/Guardrails.md` bilden gemeinsam die verbindlichen Anweisungen. Bestätigte lokale Angaben separat hinzufügen, unbekannte Angaben ausdrücklich unbekannt lassen und nur die manifestierten Wissensdateien einbinden. Draft-Kennzeichnung, Review-Modus, Ausschlüsse und Freigabesperre müssen dann selbst umgesetzt werden. Ein manuelles Kopieren umgeht diese automatischen Kontrollen; es ist keine Freigabe.

## 5. In die gewählte Plattform integrieren

Anweisungen nicht lediglich als gewöhnliche Nutzerfrage oder als zufällig abrufbare Wissensdatei hinterlegen. Die entsprechende Konfiguration der Plattform verwenden und widersprechende globale Vorgaben prüfen. Kann die Plattform die vollständigen Anweisungen nicht aufnehmen, nicht unbemerkt abschneiden; stattdessen die Integration überarbeiten und erneut testen.

Für Wissen sind etwa ein Dokumentenabruf (Retrieval/RAG) oder eine kontrollierte Zusammenstellung relevanter Inhalte als Modellkontext denkbar. Verfahren, Dateigrenzen, Verarbeitung, Kontextlänge und Werkzeugpfade hängen von der eigenen Umgebung ab. Der Bestand muss dem Bot tatsächlich verfügbar sein; eine hochgeladene Datei allein beweist keinen erfolgreichen Abruf. Lokale Fakten sollen nicht allein von einem zufälligen Suchtreffer abhängen.

Unnötige Werkzeuge und externe Abrufe deaktivieren. Die Edition enthält keine Websuche und kein Live-Screening. Sichtbare Quellenkarten, Zugriffsrechte und Protokollierung sind gesonderte Plattformfunktionen; ein Prompt allein steuert sie nicht zuverlässig.

Das Vorbereitungspaket behauptet keine Kompatibilität mit einer konkreten Plattform. Benötigte Konvertierungen, Schnittstellen und Deploy-Schritte liegen bei der betreibenden Einrichtung. Das gilt auch für das optionale Open-WebUI-Beispiel.

## 6. Antwortverhalten und Wissensabruf testen

Die [45 Golden Questions](../evaluation/README.md) mit dem tatsächlichen Modell und den tatsächlichen Einstellungen ausführen. Mindestens Themenbegrenzung, ungewöhnliche Szenarien, Sprachwechsel, höchstens drei Rückfragen, fehlende und vorhandene lokale Fakten sowie belegten Wissensabruf abdecken. Synthetische Kontakte nur in einem isolierten Testprofil verwenden.

Technische Hilfsskript-Tests, Quellenprüfung und Modellantworten getrennt bewerten. Oberfläche und API-Runner können unterschiedliche Kontexte verwenden; Unterschiede anhand tatsächlicher Aufrufe untersuchen. [Plattformneutrales Testprotokoll](../evaluation/TEST_PROTOCOL.md).

## 7. Über eine lokale Inbetriebnahme entscheiden

Erst nach dokumentierter fachlicher Prüfung und bestandenen Laufzeittests über einen produktiven Betrieb entscheiden. In der eigenen Arbeitsfassung können die zuständigen Personen die wirklich geprüften KFs auf `approved` setzen und ihren tatsächlichen Prüfstand dokumentieren. Nicht pauschal Statuswerte umstellen, um eine technische Sperre zu umgehen.

```bash
# Erst nach lokaler Pruefung aller ausgewaehlten KFs:
python scripts/build_bundle.py --mode production --config .local/institution.json --out dist/production
```

Mit dem unveränderten öffentlichen Draft-Bestand schlägt dieser Befehl absichtlich fehl. Die Prüfung der Metadaten kann weder die Qualität einer fachlichen Prüfung beurteilen noch eine Plattform gegen manuelle Umgehung absichern. Auch nach einer Freigabe bleiben Antworten unverbindliche Orientierung.

## 8. Pflege und Aktualisierungen organisieren

Zuständigkeiten, Prüffristen, Fehlerkanal, Speicher-/Löschregeln und Rückkehr zu einem vorherigen Stand festlegen. Bei Änderungen an Modell, Prompt, Wissen oder lokalem Kontext relevante Tests wiederholen. Alte Wissensfassungen nicht parallel unkontrolliert eingebunden lassen. Bestätigte lokale Daten liegen im erzeugten Systemkontext; bei Änderungen muss auch dieser erneuert werden.

Die Skripte und Anleitungen unterstützen diese Arbeit. Sie ersetzen keine institutionelle Verantwortung und enthalten keine Garantie für richtige Antworten oder einen bestimmten Rechtsstand.
