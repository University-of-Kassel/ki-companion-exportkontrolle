# Optionales Einrichtungsbeispiel: Open WebUI

Stand: 22.10.2026 | Dokumentversion 1.1

**Open WebUI ist keine Voraussetzung für dieses Repository.** Die [allgemeine Einrichtungsanleitung](setup.md) ist der plattformneutrale Einstieg. Dieser Anhang beschreibt nur eine mögliche **manuelle Einrichtung**, sofern sich die nachnutzende Einrichtung für Open WebUI entschieden hat. Ein automatischer API-Deploy-Adapter ist nicht Bestandteil des Releases. Die neutrale Edition wurde hier nicht in einer laufenden Instanz getestet. Bezeichnungen und Optionen hängen von der Open-WebUI-Version ab.

## 1. Voraussetzungen

Eine separat betriebene, gepflegte Open-WebUI-Instanz, ein freigegebener Modellzugang und funktionierende Dokumentverarbeitung/Embeddings sind erforderlich. Zugriffsrechte für Modell und Wissenssammlung klären. Kein Modellanbieter wird vorausgesetzt. Im Testprotokoll die genaue Modellkennung dokumentieren; bewegliche `latest`-Bezeichnungen allein sind kein reproduzierbarer Modellstand.

## 2. Paket erstellen

```bash
python scripts/validate_repository.py
python scripts/build_bundle.py --mode review --out dist/review
```

Mit bestätigten lokalen Daten zusätzlich `--config .local/institution.json` verwenden. 36 explizit ausgewählte KFs werden gebaut. Alle 36 fachlichen KFs sind Drafts und werden im Review entsprechend gekennzeichnet. Das Quellrelease enthält keine übernommene fachliche Freigabe für die Einrichtung.

## 3. Wissenssammlung

Unter **Workspace / Knowledge** eine neue Sammlung für diese Version anlegen. Ausschließlich `dist/review/knowledge/*.md` hochladen und die Verarbeitung abwarten. Nicht das ganze Repository, keine Testfälle, lokalen Vorlagen, README oder Original-PDFs importieren.

Bei Updates eine neue Sammlung erstellen und nach dem Test umstellen. Alte Dateien nicht zusätzlich stehen lassen: Sonst können widersprüchliche Versionen gleichzeitig gefunden werden.

## 4. Modellprofil

Unter **Workspace / Models** ein Profil anlegen. Name beispielsweise `KI-Companion Exportkontrolle - Review`, ID beispielsweise `ki-companion-exportkontrolle-review`. Ein verfügbares Basismodell auswählen. Beschreibung aus `Description.md`, den **vollständigen** Inhalt von `System.compiled.md` als Systemprompt und passende Starter aus `Starter-Prompts.md` übernehmen. Die neue Wissenssammlung zuweisen.

`model-settings.reference.json` ist eine lesbare Einstellungsreferenz, **kein Open-WebUI-Importformat**. Globale Anweisungen und Modell-Overrides auf Widersprüche prüfen.

## 5. Wissensabruf und Funktionen

Open WebUI unterscheidet Retrieval- und Werkzeugpfade. Im nativen Function-Calling-Modus kann Wissen über Knowledge-Tools abgerufen werden, statt automatisch als Kontext vorzuliegen. Daher nicht notwendige Knowledge-Tools abschalten und trotzdem einen Abruf erwarten.

Entweder einen funktionierenden automatischen Retrieval-Pfad konfigurieren **oder** den passenden nativen Knowledge-Tool-Pfad aktivieren und testen. Nicht unterstellen, dass eine beliebige API-Anfrage denselben Kontext wie der Browserchat erzeugt. Systemprompt und tatsächliche Laufzeiteinstellungen gemeinsam testen.

Websuche, Bildgenerierung, Codeausführung und nicht benötigte Werkzeuge deaktivieren. Es gibt hier insbesondere kein OpenSanctions-Tool. Linknennung ist keine Live-Prüfung. Quellenkarten der Oberfläche sind getrennt vom Antworttext konfiguriert; ein Prompt kann deren Anzeige nicht garantiert verhindern.

## 6. Testen

Fachfrage, Off-Topic-Witz, hypothetisches Beispiel, Drei-Rückfragen-Grenze, Sprachwechsel, lokalen Kontakt und fehlende lokale Fakten testen. Positive Kontakt-Tests nur auf einem isolierten Profil mit der synthetischen Fixture durchführen, nicht auf dem realen Profil.

Den Plan unter `evaluation/` verwenden. Modellantworten, Wissensabruf und Abweichungen getrennt protokollieren. Erfolgreiche Unit-Tests bewerten nicht das Sprachmodell.

## 7. Produktiver Betrieb

Erst nach dokumentierter fachlicher Freigabe aller ausgewählten KFs in der eigenen Arbeitsfassung und erfolgreichen Laufzeittests `--mode production` verwenden. Die öffentliche Vorlage bleibt Draft; alle Statuswerte pauschal umzustellen ersetzt keine Prüfung. Weitere Betriebsentscheidungen: Zugriffsschutz, externe Modellanbieter, Speicher-/Löschfristen, Monitoring, Quellenpflege und Rückkehr zum vorherigen geprüften Stand.

## Offizielle Referenzen

- Models: https://docs.openwebui.com/features/workspace/models/
- Knowledge: https://docs.openwebui.com/features/workspace/knowledge/
- RAG: https://docs.openwebui.com/features/rag/
- Lizenz: https://github.com/open-webui/open-webui/blob/main/LICENSE

Die Dokumentation ist veränderlich; Angaben für die eingesetzte Version kontrollieren.
