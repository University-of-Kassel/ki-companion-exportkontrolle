# Institutionelle Anpassung

Stand: 22.10.2026 | Dokumentversion 1.1

Die folgenden Angaben beschreiben das lokale Konfigurationsformat der mitgelieferten Offline-Hilfsskripte. Es ist **keine Open-WebUI-Konfiguration** und kein universeller Plattformimport. Eine eigene technische Integration kann ein anderes Format verwenden, muss aber die getrennte Bestätigung von Fakten und Verfahren sowie den Umgang mit unbekannten Angaben beibehalten. Die Einordnung in den gesamten Ablauf steht in der [allgemeinen Einrichtungsanleitung](setup.md).

Die lokale Datei ist `.local/institution.json`, kopiert aus `config/institution.example.json`. `.local/` ist von Git und dem Quellpaket ausgeschlossen.

| Feld | Bedeutung |
|---|---|
| `schema_version` | Unverändert `1` |
| `institution_name` | Name der betreibenden Einrichtung |
| `facts_reviewed` | Erst nach Bestätigung der tatsächlichen lokalen Fakten `true` |
| `facts_reviewed_on` | Datum als `YYYY-MM-DD`, sonst `null` |
| `contacts` | Liste bestätigter Kontakte |
| `procedures_reviewed` | Gesonderte Bestätigung der Prozessangaben |
| `procedures_reviewed_on` | Datum der Verfahrensprüfung, sonst `null` |
| `procedures` | Liste bestätigter kurzer Verfahrensaussagen, sonst `[]` |

Jeder Kontakt besitzt `area`, `office`, `unit`, `email`, `url`, `people`. Leere optionale Zeichenfolgen bedeuten unbekannt. `area` ist `export_control`, `research_security`, `data_protection`, `information_security` oder `general`.

`people` ist leer oder eine Liste ausdrücklicher Zuordnungen aus `name` und `role`. Ein Personenname allein genügt nicht. Kein Kontakt wird aufgrund seiner Nennung automatisch zur Exportkontrollstelle.

Bei `facts_reviewed: false` wird **keine** eingetragene institutionelle Angabe als Fakt übernommen. Bei `true` führen verbliebene Platzhalter, ungültige Kontakte, unvollständige Personen-Rollen-Paare oder fehlende Prüfdaten zu einem Fehler. Bestätigte Verfahren setzen bestätigte institutionelle Fakten voraus.

`local_templates/` enthält Erläuterungen; beide KFs stehen auf `draft` und **werden nicht als fachliches Laufzeitwissen eingebunden**. Der Build erzeugt lokalen Kontext aus der geprüften Konfiguration. Ohne diesen Kontext sind konkrete lokale Auskünfte unbekannt.

Nur berechtigte Betreiberinnen und Betreiber dürfen die Datei bearbeiten. Review-Flags sind organisatorische Bestätigungen, keine digitale Signatur und kein Schutz gegen böswillige Administratoren. Keine API-Schlüssel, Fallakten oder besonderen personenbezogenen Daten eintragen.

Bei Änderungen die betreffende Freigabe zurücksetzen, prüfen, neu datieren, neu bauen und den Systemprompt ersetzen. Nur die Wissenssammlung neu zu laden würde den eingebetteten lokalen Kontext nicht aktualisieren. Bei einer eigenen Integration den entsprechend verwendeten lokalen Kontext erneuern.

Die Review-Flags für lokale Angaben ersetzen keine fachliche Prüfung der 36 Wissensdateien und keinen Laufzeittest. Die öffentlich gelieferten KFs bleiben unabhängig davon Drafts.
