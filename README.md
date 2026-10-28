# KI-Companion Exportkontrolle

**Orientierung zu Exportkontrolle und Forschungssicherheit für Forschende.**

Dieses Repository enthält Systemprompt, Forschendenprofil, kuratierte Wissensdateien, lokale Konfigurationsvorlagen, Tests und Anleitungen für einen institutionell anpassbaren KI-Assistenten. Es enthält **keinen eigenen Modellserver und keine Modellgewichte**. Die betreibende Einrichtung wählt ihre Plattform und ihr Sprachmodell selbst. Eine bestimmte Chatoberfläche oder ein bestimmter Anbieter wird nicht vorausgesetzt.

**Dieses Repository ist eine Ausgangsbasis zur Anpassung durch Einrichtungen, kein betriebsfertiges System.** Die Angaben sind bewusst allgemein und neutral gehalten. Lokale Angaben, fachliche Prüfung, Plattform, Modell und Tests ergänzt die jeweilige Einrichtung selbst.

Projekt: [University-of-Kassel/ki-companion-exportkontrolle](https://github.com/University-of-Kassel/ki-companion-exportkontrolle)  
Vorbereitete Version: **1.0.0**, Bearbeitungsstand: **26.10.2026**.  
Rechte: **Universität Kassel**; Entwicklung: **Nina Felgen**. Diese Herkunft bestimmt nicht die lokale Zuständigkeit bei nachnutzenden Einrichtungen.

Die Projektpflege erfolgt im führenden GitLab-Repository; GitHub dient als öffentlicher Spiegel. Der [Veröffentlichungsablauf](docs/publishing.md) beschreibt diese Richtung und den Umgang mit Beiträgen auf GitHub. Dieser Quellenstand belegt noch keine erfolgte Veröffentlichung oder Inbetriebnahme.

## Zweck und Grenzen

Der Assistent erläutert Begriffe, strukturiert geplante Kooperationen, Transfers und Zugriffe, erkennt fehlende Angaben und hilft bei einer datensparsamen Anfrage an eine zuständige Stelle. Er antwortet in der Sprache der letzten Nachricht und stellt höchstens drei entscheidende Rückfragen. Fachfremde Anfragen werden abgegrenzt; ungewöhnliche oder hypothetische Szenarien werden nicht ungeprüft als verifizierte Tatsachen behandelt.

**Keine Rechtsberatung, keine Genehmigung oder Freigabe, keine abschließende Güterklassifikation und keine aktuelle Personen- oder Sanktionslistenprüfung.** Es gibt keine integrierte Websuche oder Screening-API. Eine Promptregel ist keine technisch garantierte Sicherheitsgrenze.

Fachlicher Schwerpunkt: **Deutschland/EU**. Institutionelle Neutralität bedeutet nicht, dass das Wissen ohne fachliche Anpassung auf jede Rechtsordnung übertragbar ist.

## Alle veröffentlichten Wissensdateien sind Drafts

**Alle 39 KF-Dateien tragen `status: draft`: 36 fachliche Wissensbausteine, zwei lokale Vorlagen und eine Datei mit Evaluationsfällen.** Keine frühere interne Freigabe wird als Freigabe für eine nachnutzende Einrichtung übernommen. Jede Einrichtung prüft selbst, ob, in welcher Fassung und unter welchen Bedingungen sie die Inhalte verwenden kann. Auch Prompts, Konfiguration und Betriebskonzept sind vor Ort zu prüfen und zu testen.

Der Draft-Status ist eine Publikationsentscheidung, keine erneute fachliche Prüfung. Redaktionelle Änderungen und Dateiversionen sind im [Changelog](CHANGELOG.md) dokumentiert; vorhandene `last_reviewed`-Angaben dürfen nicht als neue Rechtsstandsprüfung dieser Veröffentlichung verstanden werden.

**Quellveröffentlichung und institutionelle Inbetriebnahme sind getrennte Schritte.** Ein `review`-Paket stellt die ausgewählten Entwürfe zum Test bereit. Ein `production`-Paket wird blockiert, solange ausgewählte KFs noch Draft sind. Nur nach eigener dokumentierter Prüfung dürfen Einrichtungen den Status ihrer lokalen Arbeitsfassung anpassen; die öffentliche Vorlage bleibt Draft. Ein erfolgreicher Paketbau oder CI-Lauf ist keine fachliche Freigabe und kein Test der Modellantworten.

## Einstieg: plattformunabhängige Einrichtung

Die [allgemeine Einrichtungsanleitung](docs/setup.md) beschreibt Voraussetzungen, lokale Anpassung, Wissensbereitstellung, Tests und Freigabe unabhängig von einem bestimmten Produkt. Der [Einrichtungsleitfaden](docs/einrichtungsleitfaden.md) ergänzt sie um eine Dateiübersicht, die Pflege der lokalen Angaben und die noch offenen Betriebsaufgaben.

Benötigt wird eine von der Einrichtung freigegebene Umgebung, in der verbindliche Systemanweisungen und die ausgewählte Wissensbasis kontrolliert bereitgestellt werden können. Das kann eine vorhandene Assistenzplattform oder eine eigene Anwendung sein. Schnittstellen, Formate, Kontextgrenzen und Abrufverfahren müssen jeweils geprüft werden. Ein universeller Importadapter und eine garantierte Plattformkompatibilität werden nicht mitgeliefert.

### Optionaler lokaler Paketbau

Die mitgelieferten Offline-Skripte erleichtern Validierung und Zusammenstellung der Textdateien. Dafür sind Python **3.11 oder neuer** und die Abhängigkeit aus `requirements.txt` erforderlich. Python ist keine pauschale Voraussetzung für die gewählte Laufzeitplattform.

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell alternativ:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/validate_repository.py --public-release
python -m unittest discover -s tests -v
python scripts/build_bundle.py --mode review
```

Das Ergebnis liegt in `dist/review/`. Es ist ein **lokales, plattformneutrales Vorbereitungspaket**, kein öffentlicher Quellrelease und kein installationsfertiges Importformat. Bestehende Ausgabeverzeichnisse werden nicht überschrieben; für weitere Läufe beispielsweise `--out dist/review-2` verwenden.

`System.compiled.md` enthält die zusammengeführten Anweisungen. **Nur `knowledge/*.md`** ist als fachliches Laufzeitwissen vorgesehen. Wie beides an das Modell angebunden wird, richtet sich nach der eigenen Plattform. `model-settings.reference.json` ist eine lesbare Konfigurationshilfe, kein API-Payload oder Importstandard. Alternativ ist eine eigene Zusammenstellung möglich; die in der Anleitung beschriebenen Auswahl-, Review- und Datenschutzregeln sind dabei ebenfalls einzuhalten.

## Institutionelle Angaben hinterlegen

`config/institution.example.json` nach `.local/institution.json` kopieren, Platzhalter durch bestätigte Angaben ersetzen und unbekannte optionale Werte leer lassen. Fakten und Verfahren **getrennt** prüfen, die jeweiligen Review-Flags und Datumsfelder setzen. Reale Kontakte nicht in Beispieldateien committen.

```bash
python scripts/build_bundle.py --mode review --config .local/institution.json --out dist/review-local
```

Ohne bestätigte Konfiguration bleibt der Bot institutionell unkonfiguriert. Unbefüllte Vorlagen werden nicht als echte Kontakte in den Systemkontext übernommen. JSON und Paketbau sind Hilfsmittel dieses Repositories, keine Vorgabe für das interne Konfigurationsformat einer Plattform. [Felder und Prüflogik](docs/configuration.md).

## Aufbau

| Bereich | Inhalt |
|---|---|
| `bot/` | Systemprompt, Forschendenanweisungen, Beschreibung und Starter. |
| `knowledge/` | 36 fachliche KFs, alle Drafts; keine lokalen Kontakte oder Testfälle. |
| `local_templates/` | Zwei neutrale lokale Vorlagen, beide Drafts. |
| `config/` | Getrennte Listen für Laufzeitwissen und öffentliche Dateien; Beispielkonfiguration. |
| `evaluation/` | Golden Questions, Testdaten, KF-15 als Draft und Testprotokoll. |
| `templates/` | Anfragevorbereitung für Forschende. |
| `scripts/` | Offline-Prüfung, Paketbau, Testplan und Quellarchiv. |
| `tests/` | Technische Tests der Hilfsskripte. |
| `docs/` | Einrichtung, Anpassung, Pflege und optionale Beispiele. |
| `.gitlab-ci.yml` | Technische Prüfung im führenden GitLab-Repository. |
| `.github/` | Zusätzlicher Prüfworkflow für den GitHub-Spiegel. |

Es gibt **genau einen Bot**, kein Knowledge-Submodul und keine institutionelle Deploy-Abhängigkeit. `System.md` und `Guardrails.md` bilden gemeinsam die Anweisungen desselben Bots.

`config/knowledge-manifest.json` bestimmt das fachliche Laufzeitwissen. `config/public-files.json` nennt dagegen jede veröffentlichbare Datei einzeln. Eine neue Datei wird erst nach Prüfung und Aufnahme in die passende Liste berücksichtigt. Lokale Daten und Build-Ausgaben bleiben unter `.local/` beziehungsweise `dist/`.

## Anleitungen

[Allgemeine Einrichtung](docs/setup.md) | [Einrichtungsleitfaden](docs/einrichtungsleitfaden.md) | [Architektur](docs/architecture.md) | [Lokale Konfiguration](docs/configuration.md) | [Wissenspflege](docs/knowledge-maintenance.md) | [Evaluation](evaluation/README.md) | [Veröffentlichung](docs/publishing.md).

Für Forschende steht außerdem eine [Vorlage zur Anfragevorbereitung](templates/anfragevorbereitung_forschende.md) bereit.

[Open WebUI](docs/openwebui.md) ist ausschließlich ein **optionales Einrichtungsbeispiel**. Es ist weder Voraussetzung noch die einzige zulässige Laufzeitumgebung; das Beispiel ersetzt keinen Test der eingesetzten Version.

## Lizenz und externe Komponenten

Die eigenen Projektdateien stehen unter **Apache License 2.0**. Vollständiger Text: [LICENSE](LICENSE); Herkunft: [NOTICE](NOTICE) und [CREDITS.md](CREDITS.md). Verlinkte Rechtsakte, Leitfäden, Webseiten und Fremdwerke werden dadurch nicht um-lizenziert. Original-PDFs werden nicht mitgeliefert.

Plattform, Modell und externe Dienste werden nicht mitveröffentlicht; es gelten deren eigene Bedingungen. Das betrifft auch Open WebUI, sofern eine Einrichtung diese optionale Plattform verwendet. [Abhängigkeiten und Primärquellen](DEPENDENCIES.md).
