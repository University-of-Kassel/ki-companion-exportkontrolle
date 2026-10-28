# Architektur der öffentlichen Edition

Stand: 22.10.2026 | Dokumentversion 1.1

Der Quellbestand liegt vollständig in einem Repository. Es gibt genau einen Forschendenbot, keinen externen Knowledge-Pull, kein Submodul, keinen zweifachen Profil-Deploy und keine fest eingebaute institutionelle Modell-ID. Plattform und Modell werden von der betreibenden Einrichtung ausgewählt.

```text
System.md + Guardrails.md + bestaetigte lokale Konfiguration
                       |
                       v
               System.compiled.md
                       |
                       +-----------------------------+
                                                     |
Wissensmanifest + ausgewaehlte fachliche KFs            |
                       |                             |
                       v                             v
              knowledge/*.md              verbindliche Anweisungen
                       |                             |
                       +---------------+-------------+
                                       |
                                       v
                     eigene KI-Umgebung + Sprachmodell
                   kontrollierter Kontext / Wissensabruf
```

Der Offline-Paketbau ist eine Hilfsfunktion. Alternativ kann eine Einrichtung dieselben Bausteine mit einer eigenen Integration bereitstellen. In beiden Fällen müssen Auswahl, Rollenbegrenzung, lokale Faktenbindung, Draft-Kennzeichnung und institutionelle Freigabe erhalten bleiben. [Allgemeine Einrichtung](setup.md).

Lokale Fakten werden beim mitgelieferten Build in den Systemkontext aufgenommen, damit ihre Verfügbarkeit nicht allein von einem semantischen Retrieval-Treffer abhängt. Das garantiert keine fehlerfreie Modellantwort. Lokale Prozessregeln werden unabhängig von Kontaktangaben bestätigt.

## Getrennte Artefakte

**Öffentliches Quellarchiv:** generische Dateien, Lizenz, Dokumentation und Tests. Alle 39 KFs sind Drafts zur eigenständigen Prüfung. `scripts/package_release.py` verwendet eine explizite Pfadliste; `.local/`, `dist/`, Git-Historie, Original-PDFs und private Dateien werden nicht aufgenommen.

**Lokales Vorbereitungspaket:** zusammengesetzter Systemprompt, 36 ausgewählte Wissensdateien und Prüfsummenmanifest. Es kann reale Kontakte enthalten und bleibt privat. Es ist weder ein GitHub-Release-Anhang noch ein universelles Importformat.

**Review-Modus:** Drafts werden als Testmaterial aufgenommen, nicht freigegeben. **Production-Modus:** bricht bei jeder noch nicht freigegebenen ausgewählten KF ab. Freigaben gelten nur für die geprüfte lokale Arbeitsfassung; die öffentliche Vorlage bleibt Draft. Der Build prüft technische Voraussetzungen, nicht die Qualität einer fachlichen Entscheidung.

## Laufzeitgrenzen

Die Skripte rufen keine Modell-API auf, führen kein Screening aus und deployen nichts auf einem Server. Laufzeitplattform, Modellzugang, Wissensabruf, gegebenenfalls Embeddings, Zugriffsschutz und Datenverarbeitung werden getrennt eingerichtet. Die JSON-Einstellungsreferenz ist **kein getestetes Importformat** und enthält keine plattformspezifische Bindung.

[Open WebUI](openwebui.md) ist ausschließlich ein optionales Beispiel. Es wird nicht benötigt, um die Quelldateien zu verwenden oder ein Vorbereitungspaket zu bauen. Keine der Plattformvarianten wurde in diesem Bearbeitungsschritt live getestet.

Der Build dokumentiert SHA-256-Prüfsummen der Quellen. Für einen Release und den späteren lokalen Deploy denselben getesteten Quellenstand festhalten. Interne Infrastruktur, Tokens, Fallakten und personenbezogene Originaldateien gehören nicht in die Veröffentlichung.
