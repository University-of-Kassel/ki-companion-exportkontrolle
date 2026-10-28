# Changelog

## 1.0.0 - vorbereitet am 2026-10-26

Erste öffentliche Version der Forschendenedition. Alle Wissensdateien sind Entwürfe zur eigenständigen Prüfung durch nachnutzende Einrichtungen.

- Ein Forschendenbot: Systemprompt v6.3-public.3 und Guardrails v1.1-public.3 mit Themenbegrenzung, Plausibilitätsprüfung, Antwort in der Sprache der letzten Nachricht, höchstens drei entscheidenden Rückfragen und Trennung bestätigter lokaler Fakten von isoliertem synthetischem Testkontext.
- 39 KF-Dateien mit `status: draft` und einheitlichem 13-Felder-Header: 36 fachliche Wissensdateien zu Exportkontrolle und Forschungssicherheit, zwei lokale Vorlagen und KF-15 als Evaluationsmaterial.
- Das Suffix `-public.N` kennzeichnet den Anpassungsstand gegenüber der jeweiligen Quellfassung; Quellversion und Anpassungsdatum stehen im Kommentar nach dem YAML-Kopf. Vorhandene `last_reviewed`-Angaben bezeichnen den übernommenen fachlichen Prüfstand, keine neue Prüfung.
- Institutionelle Angaben über eine private JSON-Konfiguration nach dem Muster von `config/institution.example.json`; ohne bestätigte Konfiguration bleiben lokale Angaben unbekannt.
- Offline-Hilfsskripte für Validierung, Review- und Production-Paketbau (Production ist bei Draft-KFs gesperrt), Export des Evaluationsplans und Quellpaketierung aus der Einzeldateiliste `config/public-files.json`.
- 45 Golden Questions als Testdefinitionen, synthetische Test-Fixture nur mit `--allow-test-fixture` und plattformneutrales Testprotokoll.
- Plattformunabhängige Einrichtungsanleitung, Einrichtungsleitfaden und optionales Open-WebUI-Beispiel; technische Prüfung per GitLab-CI und GitHub-Workflow.
- Apache License 2.0; Herkunft in `NOTICE` und `CREDITS.md`. Original-PDFs und vollständige Fremdwerke sind nicht enthalten.

Nicht durchgeführt: Live-Deploy, Modell-/Judge-Evaluation sowie eine vollständige neue Rechtsstands-, Quellen- und Fremdrechteprüfung. Ein erfolgreicher CI-Lauf ersetzt diese Punkte nicht.
