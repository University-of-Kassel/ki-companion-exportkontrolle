# Veröffentlichung und Spiegelung

Stand: 26.10.2026 | Dokumentversion 2.0 | Quellstand 1.0.0

Das Projekt wird im führenden GitLab-Repository gepflegt. Das öffentliche Repository [University-of-Kassel/ki-companion-exportkontrolle](https://github.com/University-of-Kassel/ki-companion-exportkontrolle) auf GitHub ist ein Spiegel. Änderungen fließen nur von GitLab nach GitHub. Dieses Dokument beschreibt Vorbereitung, Spiegelung und Release; es belegt keine erfolgte Veröffentlichung. Die Adresse eines nicht öffentlichen GitLab-Repositories wird in öffentlichen Dateien nicht genannt.

## Vor der ersten Spiegelung

1. **Historie prüfen.** Eine Spiegelung kann Branches, Tags und die gesamte Historie übertragen. Enthalten frühere Stände institutionelle Kontakte, interne Freigabemarkierungen, Konfigurationen, Exporte oder Zugangsdaten, darf diese Historie nicht gespiegelt werden. Dann ein Projekt mit bereinigter Historie verwenden oder die Spiegelung auf geprüfte Branches beschränken. Auch Tags und Merge-Request-Branches prüfen.
2. **Zielrepository prüfen.** Enthält das GitHub-Repository bereits Inhalte, vorher klären, wie sie mit dem GitLab-Stand zusammengeführt werden. Eine Spiegelung kann abweichende Historie überschreiben oder scheitern. Kein Force-Push ohne bewusste Entscheidung.
3. **Quellstand prüfen.** Im Arbeitsbranch ausführen:

```bash
python scripts/validate_repository.py --public-release
python -m unittest discover -s tests -v
python scripts/package_release.py --out dist/ki-companion-exportkontrolle-source.zip
```

4. **Rechte und Herkunft prüfen.** `LICENSE` enthält Apache 2.0; `NOTICE` und `CREDITS.md` nennen Universität Kassel und Nina Felgen. Bestätigte weitere Beiträge ergänzen; keine Rechte an fremden Originalen behaupten. Die Veröffentlichung erfolgt durch die Rechteinhaberin.
5. **Zugangsdaten für die Spiegelung** ausschließlich in den Einstellungen von GitLab hinterlegen, mit minimalen Rechten, nie im Repository. Den Branchschutz auf GitHub so einrichten, dass die Spiegelung schreiben darf und andere direkte Pushs auf den Hauptbranch verhindert werden.

`.local/` und `dist/` bleiben privat. Keine lokalen Einspielpakete, Konfigurationen oder Originalexporte hochladen.

## Beiträge auf GitHub

GitHub-Issues und Pull Requests sind Vorschläge. Geprüfte Änderungen werden in einen GitLab-Arbeitsbranch übernommen, dort geprüft und über GitLab zusammengeführt; anschließend wird gespiegelt. Pull Requests nicht im gespiegelten GitHub-Hauptbranch mergen. Einzelheiten stehen in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Nach der ersten Spiegelung

Den tatsächlichen Lauf des GitHub-Workflows prüfen; er benötigt keine Modell- oder Plattform-Secrets und führt keinen Deploy aus. Verantwortliche für Quellenpflege, fachliche Freigaben und technische Wartung benennen. Privates Vulnerability Reporting in GitHub aktivieren, bevor [SECURITY.md](../SECURITY.md) diesen Meldeweg als verfügbar beschreibt.

## Quellrelease

`scripts/package_release.py` nimmt nur Dateien aus `config/public-files.json` auf und erzwingt Draft-Status. Den Release `1.0.0` mit seinen Draft- und Laufzeitgrenzen kennzeichnen. Auch ein stabiler Software- oder Dokumentationsrelease begründet keine Freigabe für fremde Einrichtungen; die öffentlich angebotenen KFs bleiben Drafts zur eigenständigen Prüfung. Tag, `VERSION`, `CITATION.cff` und Changelog gemeinsam aktualisieren; `date-released` erst mit dem tatsächlichen Veröffentlichungsdatum ergänzen.

Quellrelease und institutioneller Produktiv-Deploy bleiben getrennt. Plattform, Basismodell und externe Dienste sind nicht Teil des Quellreleases. Institutionelle Freigabestände nicht in die öffentliche Vorlage zurückübernehmen. Die Publikationsprüfung muss für alle 39 KFs `draft` ausweisen.

## Zeitkritische Punkte vor dem Release

- Offener Prüfpunkt in KF-09d (DSI/Cali Fund) nach dem Ende von COP17/NP-MOP6 am 30.10.2026.
- Aktualisierung von Anhang I der Verordnung (EU) 2021/821 (Delegierte Verordnung vom 14.09.2026): nach Veröffentlichung im Amtsblatt die betroffenen KFs, insbesondere KF-01, KF-01d und KF-99, prüfen.
- Die `last_reviewed`-Angaben in den KFs müssen tatsächlichen Prüfungen entsprechen.
