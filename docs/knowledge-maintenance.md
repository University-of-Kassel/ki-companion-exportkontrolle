# Wissenspflege und Freigaben

Stand: 26.10.2026 | Dokumentversion 1.2

## Explizite Auswahl

`config/knowledge-manifest.json` nennt jede Laufzeitdatei. Alle knowledge files (KFs) unter `knowledge/` müssen im Manifest stehen; Evaluation und lokale Vorlagen sind dort unzulässig. Neue Dateien werden dadurch nicht allein wegen ihrer Endung produktiv.

Die öffentliche Edition enthält 36 fachliche KFs, zwei lokale Vorlagen und KF-15 als Evaluationsmaterial.

## Freigaben

**Alle 39 veröffentlichten KFs sind `draft`: 36 fachliche Dateien, zwei lokale Vorlagen und KF-15 als Evaluationsmaterial.** Interne Freigaben werden nicht auf nachnutzende Einrichtungen übertragen. Auch sorgfältig bearbeitete oder intern verwendete Texte werden hier als Entwürfe zur eigenen Prüfung bereitgestellt.

Der Draft-Status ist eine Kennzeichnung; fachliche Inhalte, KF-Versionen und `last_reviewed` bleiben davon unberührt.

In einer **eigenen lokalen Arbeitsfassung** darf die zuständige Einrichtung nach Quellenprüfung, Anpassung und dokumentierter Entscheidung geprüfte Dateien auf `approved` setzen. Tatsächliches Prüfdatum und erforderliche Inhaltsversionen nachvollziehbar pflegen. Die öffentliche Vorlage bleibt Draft; eine Statusänderung oder ein erfolgreicher Build ersetzt keine Prüfung.

`python scripts/validate_repository.py --public-release` prüft zusätzlich, dass wirklich alle veröffentlichten KFs Draft sind. Für eine bereits lokal freigegebene Arbeitsfassung den normalen Validator ohne diese Publikationsoption verwenden. `--mode production` bleibt blockiert, solange mindestens eine ausgewählte Wissensdatei Draft ist. Bei eigener Integration ohne Build-Skript sind entsprechende organisatorische und technische Kontrollen selbst umzusetzen.

## Einheitliches Schema

Alle 39 `KF-*.md`-Dateien haben dieselben 13 Felder in dieser Reihenfolge:

```yaml
---
id: "KF-XX"
title: "Titel"
version: "1.0-public.1"
status: "draft"
last_reviewed: null
review_cycle: null
profiles:
  - "researcher"
scope: "Hochschulen und Forschungseinrichtungen; Schwerpunkt Deutschland/EU"
document_type: "Kuratierte Knowledge File"
related: []
knowledge_area: null
purpose: null
binding: null
---
```

`last_reviewed` kann einen belegten Monatsstand (`YYYY-MM`) bewahren. Keinen unbekannten Tag erfinden. Bei einer neuen tatsächlichen Prüfung das volle Datum verwenden. Die technische Publikationsanpassung ist im Kommentar der jeweiligen Datei dokumentiert, nicht als neue rechtliche Prüfung.

`-public.1` bezeichnet die öffentliche Anpassung der Quellversion. Beim nächsten Update Suffix oder fachliche Version bewusst erhöhen; Dateiname, Header und Manifest gemeinsam ändern.

## Aktualität und Tests

Gesetzliche Geltungszeitpunkte sind fachlich zu prüfen. Statische Textdateien und technische Tests garantieren keinen aktuellen Rechtsstand. KF-98 ist ein Quellenregister, kein Live-Abruf. Besonders dynamisch sind Sanktionen, Listungen, Güterlisten, US-Regeln und lokale Kontakte.

KF-09d enthält einen offenen erneuten Prüfpunkt zum DSI/Cali-Fund-Prozess nach dem 30.10.2026. Dieser wurde nicht als erledigt markiert. Diese Publikationsaufbereitung ist keine vollständige neue rechtliche Validierung aller Quellen.

Nach Änderungen: Validator und Unit-Tests ausführen, Review-Paket bauen, betroffene Golden Questions und Retrieval prüfen, fachlich freigeben und denselben Quellenstand deployen. Fremdoriginale nur nach Rechteprüfung übernehmen; bevorzugt verlinken und eigene Zusammenfassungen pflegen.
