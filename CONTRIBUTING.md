# Beitragen

Nachvollziehbare fachliche Korrekturen, technische Fehlerberichte und Testfälle sind willkommen. Keine realen Fallakten, Geheimnisse oder unzulässigen personenbezogenen Daten in Issues und Pull Requests einstellen.

## GitLab und GitHub

GitLab ist das führende Repository; GitHub ist der öffentliche Spiegel. GitHub-Issues und Pull Requests dienen als Vorschläge. Die Projektbetreuung übernimmt geprüfte Änderungen in einen GitLab-Arbeitsbranch, lässt dort die Prüfungen laufen und führt sie über den GitLab-Review zusammen. Anschließend wird der neue Stand nach GitHub gespiegelt. Quelländerungen nicht unabhängig in den gespiegelten GitHub-Hauptbranch mergen; sie könnten bei der nächsten Spiegelung verloren gehen oder eine Divergenz erzeugen. [Veröffentlichungsablauf](docs/publishing.md).

## Inhalt und Prüfung

Alle KFs im öffentlichen Ausgangsrepository bleiben `draft`, auch nach redaktionellen Verbesserungen. Eine institutionelle Freigabe wird in der Arbeitsfassung der jeweiligen Einrichtung dokumentiert. Quellen nennen und Version/Prüfdatum korrekt pflegen. Redaktionelle Normalisierung ist keine Freigabe. Institutionelle Kontakte gehören in die private Konfiguration.

```bash
python scripts/validate_repository.py --public-release
python -m unittest discover -s tests -v
```

Bei neuen, entfernten oder umbenannten Dateien `config/public-files.json` aktualisieren; für fachliches Laufzeitwissen zusätzlich `config/knowledge-manifest.json`. Dateiversionen, Verweise und Tests konsistent halten. Die öffentliche Liste enthält einzelne geprüfte Dateipfade, keine pauschale Ordnerfreigabe. Lokale Arbeitsdateien gehören unter `.local/`, generierte Ausgaben unter `dist/`.

Umfang und Grenzen der Prüfung in der Änderungsbeschreibung festhalten. Technische Tests und tatsächlich ausgeführte Modelltests getrennt nennen; vorbereitete Testfälle nicht als bestanden darstellen. Geänderte Dateien und Changelog kennzeichnen. Beiträge nur mit den erforderlichen Rechten einreichen; für bewusst eingereichte Beiträge gilt die Projektlizenz, soweit nicht ausdrücklich anders vereinbart.
