# Einrichtungsleitfaden für nachnutzende Einrichtungen

**Dateien, individuelle Angaben und noch offene Betriebsaufgaben**

Stand: 26.10.2026 | Dokumentversion 1.2 | Quellstand 1.0.0

Diese Anleitung ergänzt das Repository und die allgemeine [Einrichtung in acht Schritten](setup.md). Sie beschreibt den tatsächlich enthaltenen Paketbau und die von einer Einrichtung noch einzurichtende Laufzeit. Die angegebenen Repositorypfade beziehen sich auf Version 1.0.0. Das Repository ist eine Ausgangsbasis und kein betriebsfertiges System; die hier beschriebenen Aufgaben sind der vorgesehene Weg von der Basis zum Betrieb. Neue Beispielpfade für betriebliche Unterlagen oder Automatisierung sind ausdrücklich als Vorschläge gekennzeichnet; solche Dateien wurden nicht als funktionsfähige Integration mitgeliefert.

## Das Wichtigste vorab

- **Für eine unkonfigurierte Erprobung** muss noch keine institutionelle Kontaktdatei angelegt werden. Der Bot soll lokale Angaben dann als unbekannt behandeln.
- **Für bestätigte institutionelle Auskünfte** werden beim mitgelieferten Verfahren Kontakte und Verfahren zentral in einer neu anzulegenden Datei gepflegt: `.local/institution.json`.
- **Für den späteren Betrieb** kommen die fachliche Prüfung des Wissens, eine eingerichtete KI-Plattform mit Modell und Wissenszugriff sowie tatsächliche Verhaltenstests hinzu. Diese Aufgaben werden durch das Befüllen der Kontaktdatei nicht erledigt.
- **Ein automatischer Deploy ist nicht enthalten.** Die vorhandenen Skripte erzeugen und prüfen Dateien. Eine manuelle Übernahme in eine vorhandene geeignete Plattform ist möglich; dafür ist kein zusätzliches Deployskript vorgeschrieben.

## Orientierung im Dokument

1. Welche Dateien die Einrichtung bearbeiten muss
2. Die zentrale JSON-Konfiguration und ihre Felder
3. Lokale Vorlagen und ihre Zuordnung zur Konfiguration
4. Fachliche Prüfung, offene lokale Festlegungen und Freigabe
5. Paketbau und automatisch erzeugte Dateien
6. Manuelle Einrichtung und tatsächliche Modelltests
7. Noch fehlende Bausteine für eine Automatisierung
8. CI und betriebliche Unterlagen
9. Angaben bei einem eigenen Fork oder Quellrelease
10. Abnahmeliste für die Einrichtung

## 1. Welche Dateien muss die Einrichtung bearbeiten?

### 1.1 Was wirklich individualisiert werden muss

| Datei oder Ort | Einordnung | Konkrete Aufgabe |
|---|---|---|
| `.local/institution.json` | **Zentraler Pflegeort für lokale Angaben**; neu anlegen, wenn der Bot eigene institutionelle Auskünfte kennen soll | Aus `config/institution.example.json` kopieren; bestätigte Namen, Zuständigkeiten, Kontakte und kurze botrelevante Verfahren eintragen. Mit `--config` ausdrücklich an den Build übergeben. |
| Einstellungen der KI-Plattform | Für jede tatsächliche Nutzung erforderlich; keine vorgegebene Repositorydatei | Modell, vollständige Anweisungen, Wissenssammlung, Abrufverfahren, Berechtigungen und relevante Betriebsparameter einrichten. |
| Private Arbeitsfassung der 36 Laufzeit-KFs | Vor institutioneller Production fachlich prüfen | Alle 36 KFs prüfen. Nur die Dateien ändern, deren fachliche Aussagen oder lokale Verfahrensbezüge für die Einrichtung angepasst werden müssen. Danach lokale Freigabe und Prüfdaten dokumentieren. |
| Private Kopie von `evaluation/TEST_PROTOCOL.md` | Nachweis der eigenen Tests | Tatsächliches Setup, Antworten, Quellenabruf, Kriterienverletzungen und Ergebnisse dokumentieren. Der öffentliche Ausgangsbogen bleibt unverändert. |

### 1.2 Dateien mit besonderem lokalen Prüf- oder Anpassungsbedarf

| Datei | Was die Einrichtung lokal klären soll | Typischer Pflegeort |
|---|---|---|
| `knowledge/export_control/KF-03f_US_Reexportkontrolle_Grundlagen_v1.0-public.1.md` | Zuständigkeit für vertiefte US-Fragen, verwendete Screeningwege, Dokumentation, Einbindung externer Expertise/Vertragsprüfung und Umgang mit den dort benannten Rechtskonflikten | Kurze botrelevante Aussagen in `.local/institution.json` unter `procedures[]`; ausführliche Regeln in privater Betriebsdokumentation |
| `knowledge/export_control/KF-03h_US_Reexportkontrolle_Red_Flags_v1.1-public.2.md` | Falls vorhanden: lokale Prüfwerkzeuge, Stop-Regeln, Vertragsbausteine, Prüfreihenfolgen und Dokumentationswege | Nur dann lokal dokumentieren, wenn solche Regeln institutionell festgelegt sind; die KF selbst muss dafür normalerweise nicht geändert werden |
| `knowledge/research_security/KF-07e_Gastforschende_Stipendien_und_Zugriffssteuerung_v1.1-public.2.md` | Zuständigkeiten, Zugriffsarten/-stufen, Standardzugang, Genehmigungen, Logging, Laufzeiten, Offboarding, Aufbewahrung und Eskalation | Lokale Verfahren; bei einem vorhandenen institutionellen Zugriffskonzept ggf. auch die lokale KF-Fassung anpassen |
| `knowledge/research_security/KF-07f_Daten_Software_Cloud_und_IT_Zugaenge_v1.1-public.2.md` | Zugelassene Cloud-/Kollaborationsdienste, externe Accounts, VPN, HPC, Lizenzserver, Zuständigkeiten, besonders schutzbedürftige Inhalte, Logging und Löschung | Lokale Verfahren bzw. private IT-/Betriebsdokumentation; KF nur bei tatsächlichem fachlichem Widerspruch ändern |
| `knowledge/export_control/KF-04_Verfahren_Exportkontrolle_v1.3-public.1.md` | Prüfen, ob die generische Prozesslogik zur Einrichtung passt | Normalerweise **nicht individualisieren**; nur bei institutionellem Widerspruch die lokale KF-Fassung ändern |
| `knowledge/research_security/KF-08_Verfahren_Forschungssicherheit_v1.3-public.1.md` | Prüfen, ob die generische Prozesslogik zur Einrichtung passt | Normalerweise **nicht individualisieren**; nur bei institutionellem Widerspruch die lokale KF-Fassung ändern |
| `knowledge/core/KF-98_Weiterfuehrende_Informationen_und_Anlaufstellen_v1.6-public.2.md` | Zentrale externe Quellen prüfen | **Keine lokalen Kontakte eintragen.** Institutionelle Kontakte ausschließlich über `.local/institution.json` pflegen |

Die beiden Dateien unter `local_templates/` sind Sammel- und Erklärungshilfen. Sie werden nicht als lokale Konfiguration eingelesen und müssen nicht ausgefüllt werden.

### 1.3 Nur bei Bedarf anzupassen

| Datei oder Ort | Einordnung | Konkrete Aufgabe |
|---|---|---|
| `bot/Description.md` und `bot/prompts/Starter-Prompts.md` | Optional | Anzeigename, Beschreibung und Einstiegsfragen an die Zielgruppe anpassen. |
| `templates/anfragevorbereitung_forschende.md` | Optional | Als Handreichung anpassen. Die Vorlage wird nicht automatisch in das Buildpaket oder in die Oberfläche übernommen. |
| `bot/prompts/System.md` und `bot/prompts/Guardrails.md` | Prüfen; normalerweise nicht institutionell umschreiben | Rolle, Sprache, Grenzen und Antwortverhalten prüfen. Kontakte und Verfahren nicht hier duplizieren. |
| `config/knowledge-manifest.json` und `config/public-files.json` | Nur bei geänderter Dateiauswahl oder zusätzlichen Quelldateien | Pfade und Auswahl konsistent halten. Die Listen sind keine institutionellen Kontaktformulare. |
| `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CITATION.cff`, `VERSION`, `CHANGELOG.md` | Nur bei eigenem Fork oder eigener Veröffentlichung | Eigene Repositoryadressen, Meldewege, Versionierung und Veröffentlichungsangaben pflegen. Für die reine lokale Botnutzung nicht erforderlich. |

Die öffentlichen KFs bleiben `draft`. Für die eigene freigegebene Betriebsfassung einen getrennten privaten Arbeitsstand verwenden. Die Herkunftsangaben zur Universität Kassel und zu Nina Felgen benennen die Projektentstehung; sie legen keine Zuständigkeiten an der nachnutzenden Einrichtung fest.

## 2. Die zentrale Konfiguration im Detail

### Datei anlegen und ausdrücklich verwenden

Im Repository einen lokalen Ordner `.local` anlegen und `config/institution.example.json` als `.local/institution.json` hineinkopieren. Die öffentliche Beispieldatei bleibt neutral. `.local/` wird standardmäßig nicht von Git erfasst und nicht in das öffentliche Quellarchiv aufgenommen.

Die Datei wird **nicht automatisch gefunden**. Auch wenn sie existiert, übernimmt der Build ihre Angaben nur mit dem Parameter:

```bash
python scripts/build_bundle.py --mode review --config .local/institution.json --out dist/review-institution-01
```

### Alle acht Schlüssel beibehalten

Das Format akzeptiert genau die folgenden acht Schlüssel auf oberster Ebene. Namen und Datentypen nicht ändern; keine zusätzlichen Modell-, Server- oder Zugangsdatenfelder ergänzen.

| Schlüssel | Datentyp | Was einzutragen ist |
|---|---|---|
| `schema_version` | Ganzzahl | Unverändert `1`. |
| `institution_name` | Zeichenfolge | Tatsächlicher Name der Einrichtung; bei `facts_reviewed: true` darf er nicht leer sein. |
| `facts_reviewed` | Wahrheitswert | Zunächst `false`; erst nach tatsächlicher Bestätigung der eingetragenen Fakten `true`. Keine Zeichenfolge `"true"`. |
| `facts_reviewed_on` | Datum als Zeichenfolge oder `null` | Bei bestätigten Fakten vollständiges tatsächliches Prüfdatum in der Form `YYYY-MM-DD`; sonst `null`. Kein zukünftiges Datum. |
| `contacts` | Liste | Bestätigte Kontakte nach dem unten beschriebenen Schema. `[]` ist zulässig, wenn keine Kontakte vorliegen. |
| `procedures_reviewed` | Wahrheitswert | Eigene Bestätigung der Verfahrensaussagen; nur zusammen mit bestätigten Fakten auf `true` setzen. |
| `procedures_reviewed_on` | Datum als Zeichenfolge oder `null` | Tatsächliches Datum der Verfahrensprüfung; bei `procedures_reviewed: true` erforderlich. |
| `procedures` | Liste von Zeichenfolgen | Kurze, bestätigte Verfahrensaussagen. Ohne bestätigte Verfahren `[]` verwenden und das Verfahrens-Flag auf `false` lassen. |

**Technisch vorhanden ist nicht gleich inhaltlich befüllt:** Alle acht Schlüssel gehören zur Struktur. Kontakte, Personen und Verfahren müssen aber nicht erfunden oder künstlich vervollständigt werden. Bei `facts_reviewed: false` wird keine der eingetragenen institutionellen Angaben als bestätigter lokaler Kontext übernommen. Ein ausgefüllter Name allein aktiviert die Konfiguration nicht.

### Kontakte: genau sechs Schlüssel pro Eintrag

| Schlüssel | Inhalt und Umgang mit fehlenden Angaben |
|---|---|
| `area` | Eine der Kategorien `export_control`, `research_security`, `data_protection`, `information_security` oder `general`. Die passende tatsächliche Zuständigkeit wählen. |
| `office` | Bestätigte Bezeichnung der Anlaufstelle; sonst `""`. |
| `unit` | Bestätigte Organisationseinheit; sonst `""`. |
| `email` | Vollständige bestätigte E-Mail-Adresse; sonst `""`. |
| `url` | Vollständige bestätigte URL einschließlich `https://` oder `http://`; sonst `""`. Keine Zugangsdaten in der URL. |
| `people` | `[]` oder eine Liste von Objekten mit genau `name` und `role`. Beide Werte müssen für jede genannte Person bestätigt und nicht leer sein. |

Mehrere Zuständigkeitsbereiche können als getrennte Kontakte erfasst werden. Ein Kontakt, der ausschließlich aus `area` und sonst leeren Werten besteht, wird nicht als konkrete Kontaktangabe übernommen. Telefonnummern, Anschriften oder zusätzliche Kontaktfelder unterstützt das aktuelle Schema nicht; dafür wäre eine bewusste Erweiterung von Parser, Dokumentation und Tests nötig.

## 3. Lokale Vorlagen richtig verstehen

Die beiden Dateien unter `local_templates/` sind Erläuterungen und Sammelhilfen. **Der mitgelieferte Builder liest ihre Textkörper nicht als institutionelle Konfiguration ein.** Ihre Platzhalter müssen deshalb nicht zusätzlich ausgefüllt werden. Eine Änderung nur dort erreicht den Bot nicht.

| Vorhandene Vorlage | Funktion |
|---|---|
| `local_templates/KF-04b_Lokaler_Kontext_v1.3-public.1.md` | Zeigt, welche lokalen Fakten benötigt werden und wie damit umzugehen ist. |
| `local_templates/KF-04a_Lokaler_Kontext_v1.5-public.1.md` | Hilft beim Sammeln tatsächlich geltender lokaler Verfahren. |

### Zuordnung der Platzhalter zur JSON-Datei

| Platzhalter in der Vorlage | Tatsächlicher Pflegeort in `.local/institution.json` |
|---|---|
| `INSTITUTION_NAME` | `institution_name` |
| `EXPORT_CONTROL_OFFICE` | `contacts[].office` beim Kontakt mit `area: export_control` |
| `EXPORT_CONTROL_UNIT` | `contacts[].unit` beim passenden Kontakt |
| `EXPORT_CONTROL_EMAIL` | `contacts[].email` beim passenden Kontakt |
| `EXPORT_CONTROL_URL` | `contacts[].url` beim passenden Kontakt |
| `PERSON_ROLE_ASSIGNMENT` | `contacts[].people[]` mit den Feldern `name` und `role` |
| `LOCAL_INQUIRY_PROCESS` | Eine bestätigte Aussage als Element von `procedures[]` |
| `LOCAL_ACCESS_REVIEW_PROCESS` | Eine bestätigte Aussage als Element von `procedures[]` |
| `LOCAL_DOCUMENTATION_PROCESS` | Eine bestätigte Aussage als Element von `procedures[]` |
| `LOCAL_ESCALATION_PROCESS` | Eine bestätigte Aussage als Element von `procedures[]` |

Die vier Verfahrensplatzhalter sind **keine zusätzlichen JSON-Schlüssel**. Die vorhandene Konfiguration speichert Verfahrensaussagen als einfache Textliste. Es müssen auch nicht alle vier Bereiche befüllt werden. Ungeklärte Abläufe bleiben offen.

### Typische Fehler vermeiden

- Unbekannte optionale Kontaktwerte als `""` und unbekannte Listen als `[]` belassen. `null` ist hier für die noch nicht gesetzten Datumsfelder vorgesehen.
- Vor einer Faktenbestätigung alle verbliebenen Platzhalter in den zu übernehmenden Fakten ersetzen oder den unbekannten Wert leeren. Sonst bricht der Build ab.
- Verfahrensprüfung gesondert bestätigen. Eine bekannte Anlaufstelle belegt keinen bestimmten Genehmigungs-, Dokumentations- oder Eskalationsprozess.
- Synthetische Werte aus `evaluation/fixtures/institution.test.json` nur im getrennten Testprofil mit `--allow-test-fixture` verwenden. Sie sind keine Ersatzkontakte für eine reale Einrichtung.
- Keine API-Schlüssel oder Falldaten in die lokale Faktenkonfiguration aufnehmen. Den Zugriff auf Datei und erzeugtes Paket auf die zuständigen Betreibenden beschränken.

### Wenn sich Kontakte oder Verfahren ändern

Die betroffene Bestätigung zurücksetzen, Werte ändern, prüfen und neu datieren. Danach ein neues Paket bauen und **`System.compiled.md` in der Plattform ersetzen**. Der lokale Kontext wird in diesen Systemprompt eingebettet. Nur die Wissenssammlung neu zu laden aktualisiert die Kontakte und Verfahren nicht. Kontakte auch nicht parallel in Prompts oder KF-98 pflegen.

## 4. Fachliches Wissen und lokale Freigabe

### Was vor Production zu prüfen ist

`config/knowledge-manifest.json` nennt die **36 fachlichen Laufzeit-KFs**. Jede davon muss in der institutionellen Arbeitsfassung fachlich geprüft sein, bevor sie für Production ausgewählt wird. Die beiden lokalen Vorlagen und KF-15 unter `evaluation/scenarios/` gehören nicht zum Laufzeitwissen.

Die Prüfung umfasst insbesondere fachliche Richtigkeit, Aktualität, den vorgesehenen Rechtsraum, lokale Passung und die verwendeten Quellen. Der Bestand hat seinen Schwerpunkt in Deutschland/EU. Eine andere Einrichtung oder ein anderer Staat wird durch das Ersetzen des Namens nicht automatisch fachlich abgedeckt.

### Lokale Verfahren: vier besonders relevante KFs und drei Dateien mit bewusst anderer Funktion

Die detaillierte Änderungsmatrix steht bereits in Abschnitt 1.2. Für die fachliche Übernahme gelten zusätzlich folgende Leitlinien:

- **KF-03f, KF-07e und KF-07f** enthalten ausdrückliche lokale Festlegungen und sind damit konkrete Arbeitsaufträge an die Einrichtung.
- **KF-03h** verweist auf mögliche lokale Prüf- und Eskalationsregeln. Dort ist nur dann eine lokale Dokumentation nötig, wenn solche Regeln tatsächlich bestehen.
- **KF-04 und KF-08** sind bewusst generische Verfahrensmodelle. Sie sollen nicht einfach mit lokalen Kontakten oder Detailprozessen überschrieben werden; Änderungen sind nur bei einem tatsächlichen institutionellen Widerspruch sinnvoll.
- **KF-98** bleibt das zentrale Register für allgemeine externe Quellen. Lokale Kontakte gehören dort ausdrücklich nicht hinein.

Bestätigte Zuständigkeiten und kurze botrelevante Abläufe in der lokalen JSON-Konfiguration pflegen. Vollständige Dienstanweisungen, IT-Regelwerke, Rollenmodelle und umfangreiche Prozessbeschreibungen gehören in die dafür vorgesehenen privaten Systeme oder Betriebsunterlagen. Nur Informationen in `procedures[]` aufnehmen, die der Bot für seine Orientierung tatsächlich benötigt.

Passt die allgemeine fachliche Darstellung einer KF selbst nicht, die betreffende Datei in der lokalen Arbeitsfassung überarbeiten. Alle übrigen KFs bleiben ebenfalls Gegenstand der Übernahmeprüfung, müssen aber nicht allein wegen der institutionellen Nachnutzung verändert werden.

### Welche Metadaten sich lokal ändern können

| Angabe | Vorgehen |
|---|---|
| `status` | Erst nach tatsächlicher lokaler Prüfung für die betroffene Laufzeit-KF von `draft` auf `approved` setzen. |
| `last_reviewed` | Tatsächlichen Prüfstand dokumentieren; bei neuer Prüfung das vollständige Datum verwenden. Ein altes Datum ist kein neuer Prüfnachweis. |
| `review_cycle` | Zulässig sind `null`, `monthly`, `quarterly`, `semiannual`, `annual` und `event_driven`. Den passenden Pflegezyklus festlegen. |
| `version` und Dateiname | Bei inhaltlicher Änderung konsistent fortschreiben; Versionsangabe, Dateiname und Manifeste müssen zusammenpassen. |
| Freigabeentscheidung | Prüfer:in, Umfang, Quellenstand und Entscheidung zusätzlich in einem privaten Nachweis festhalten; dafür ist im vorhandenen KF-Schema kein eigenes Signaturfeld vorgesehen. |

Die Reihenfolge und Anzahl der 13 YAML-Kopffelder beibehalten. Keine frei erfundenen Versionssuffixe oder zusätzlichen Felder einfügen: Der vorhandene Validator akzeptiert ein festes Schema. Einzelheiten stehen in `docs/knowledge-maintenance.md`.

### Was der Code tatsächlich erzwingt

Der Production-Build blockiert, sobald eine der ausgewählten Laufzeit-KFs nicht `approved` ist. Er erzwingt dagegen **keinen vorhandenen Kontakt**, **keine bestätigte lokale Konfiguration** und **kein nichtleeres oder frisches KF-Prüfdatum**. Auch eine erfolgreiche Paketbildung ohne `--config` ist nach lokaler KF-Freigabe technisch möglich; konkrete lokale Angaben bleiben dann unbekannt.

Die Einrichtung muss ihre inhaltlichen Abnahmebedingungen deshalb selbst dokumentieren. Ein Statuswert und ein erfolgreicher Build belegen keine abgeschlossene fachliche Prüfung oder ausreichende Modellqualität.

Eine separate lokale Datei zum Überschreiben der KF-Freigabestatus ist nicht implementiert. `facts_reviewed` und `procedures_reviewed` in der JSON-Datei bestätigen ausschließlich lokale Daten; sie geben keine fachlichen KFs frei.

### Öffentliche Vorlage und Betriebsfassung getrennt halten

Die öffentliche Vorlage bleibt bei **39 Draft-KFs**. Für den internen freigegebenen Stand den normalen Validator verwenden:

```bash
python scripts/validate_repository.py
```

`--public-release` und `scripts/package_release.py` verlangen dagegen durchgängig Draft-Status. Auch beide mitgelieferten CI-Workflows prüfen die öffentliche Fassung. Eine freigegebene Betriebsfassung benötigt deshalb einen passenden internen Prüfablauf. Die öffentlichen Jobs nicht ungeprüft als Production-Workflow übernehmen.

### Die zwei Dateilisten

`config/knowledge-manifest.json` und die KFs unter `knowledge/` müssen exakt zusammenpassen. Eine Datei lediglich aus dem Manifest zu streichen reicht nicht: Die verbleibende Datei unter `knowledge/` wird als Abweichung erkannt. Eine fachliche Reduktion erfordert außerdem eine Prüfung von Mindestbestand, Querverweisen, Rollenbeschreibung und Tests.

`config/public-files.json` zählt einzeln alle zulässigen öffentlichen Quelldateien auf. Neue oder umbenannte KFs erfordern die Anpassung beider Listen. Neue allgemeine Dokumentation benötigt nur einen Eintrag in der öffentlichen Dateiliste. **Unbekannte zusätzliche Dateien im Quellbaum können auch einen Review-Build blockieren**, weil dieser ebenfalls die Repositoryvalidierung aufruft. Private Betriebsunterlagen unter `.local/` oder außerhalb des öffentlichen Quellbaums ablegen.

## 5. Paket bauen: Was entsteht automatisch?

### Voraussetzungen und erste Prüfung

Die Hilfsskripte benötigen Python 3.11 oder neuer und die Abhängigkeit aus `requirements.txt`. Für einen unveränderten öffentlichen Ausgangsstand:

```bash
python -m pip install -r requirements.txt
python scripts/validate_repository.py --public-release
python -m unittest discover -s tests -v
```

Die Prüfung bezieht sich auf Quellen und Hilfsskripte. Sie ruft kein Modell auf. Bei einer bereits lokal freigegebenen Arbeitsfassung den normalen Validator verwenden und die auf öffentliche Draft-Quellen ausgerichteten Paket-/CI-Tests im internen Ablauf entsprechend berücksichtigen.

### Review-Pakete

Ohne lokale Angaben:

```bash
python scripts/build_bundle.py --mode review --out dist/review-unconfigured-01
```

Mit bestätigten Angaben der Einrichtung:

```bash
python scripts/build_bundle.py --mode review --config .local/institution.json --out dist/review-institution-01
```

Nur für die isolierten positiven Lokalfaktentests:

```bash
python scripts/build_bundle.py --mode review --config evaluation/fixtures/institution.test.json --allow-test-fixture --out dist/review-synthetic-01
```

Ein bestehendes Ausgabeverzeichnis wird absichtlich nicht überschrieben. Bei Wiederholungen einen neuen Namen verwenden. Der synthetische Build erhält ein eigenes Testprofil; der Schalter erzeugt selbst keine Isolation in der KI-Plattform.

### Inhalt eines erzeugten Pakets

Die folgenden Pfade liegen jeweils innerhalb des gewählten Ausgabeordners, beispielsweise `dist/review-institution-01/`.

| Datei | Was damit zu tun ist |
|---|---|
| `System.compiled.md` | Vollständig als Systemanweisungen in der Plattform bereitstellen. Enthält Systemprompt, Guardrails und den erzeugten lokalen Kontext. |
| `knowledge/KF-*.md` | Die 36 erzeugten fachlichen Wissensdateien einbinden. Die Ausgabedateien heißen nach KF-ID, etwa `KF-03g.md`; ihre Quellnamen sind länger. |
| `Description.md` | Bei Bedarf als Profilbeschreibung verwenden. |
| `Starter-Prompts.md` | Bei Bedarf als Einstiegsfragen übernehmen. |
| `model-settings.reference.json` | Als Konfigurationshilfe lesen. `base_model` ist zunächst `null`; das tatsächliche Modell wird in der Laufzeit eingerichtet. Die Datei ist kein Importformat. |
| `build-manifest.json` | Quellstand, Modus, Prüfsummen und Konfigurationsstatus für die Nachvollziehbarkeit aufbewahren. |
| `READ_ME_FIRST.txt` | Verwendungshinweise lesen. |
| `LICENSE` und `NOTICE` | Mitgeführte Lizenz- und Herkunftsinformationen; kein fachliches Laufzeitwissen. |

Diese Dateien werden erzeugt und müssen nicht vorab von Hand angelegt werden. Änderungen an den Quelldaten durch einen Neubuild übernehmen. Eine manuelle Änderung nur an generierten Dateien geht beim nächsten Build verloren und passt nicht mehr zu den gespeicherten Prüfsummen.

Das Paket bleibt privat, wenn es institutionelle Angaben enthält. Es ist nicht der öffentliche Quellrelease. Die Referenzdatei technisch einzulesen, ein Modell auszuwählen oder Daten hochzuladen muss eine eigene Integration übernehmen.

## 6. Manuelle Einrichtung und tatsächliche Tests

### Der Weg ohne zusätzliches Deployskript

1. Eine geeignete institutionelle KI-Umgebung und ein konkretes Modell auswählen. Zugriff, Datenverarbeitung, Kontextgrenzen und Zuständigkeit klären. Je nach Einsatz gehören dazu Datenschutz (Rechtsgrundlage, gegebenenfalls Folgenabschätzung, Verträge mit dem Modellanbieter), die Beteiligung der Personalvertretung und die Kennzeichnung gegenüber Nutzenden, dass sie mit einem KI-System interagieren. Das Repository trifft dazu keine Aussagen und ersetzt keine entsprechende Prüfung. Ein bereits vorhandener Dienst kann genutzt werden; dieses Repository stellt keinen eigenen Modellserver bereit.
2. Ein getrenntes Review-Profil anlegen. Den vollständigen `System.compiled.md` als Systemanweisungen hinterlegen. Globale Vorgaben und Profil-Overrides auf Widersprüche prüfen.
3. Eine neue Wissenssammlung oder gleichwertige kontrollierte Kontextbereitstellung aus den **erzeugten** `knowledge/KF-*.md` einrichten. Keine lokalen Vorlagen, Testfälle, README oder Lizenzdateien als fachliches Wissen hochladen. Zum Umfang: Die 36 erzeugten Wissensdateien umfassen zusammen rund 43.000 Wörter (grob 110.000 Token), der erzeugte Systemprompt rund 5.500 Wörter (grob 10.000 Token). Das sind Näherungswerte, die vom Tokenizer abhängen. Eine vollständige Einbettung in den Modellkontext ist daher nur mit sehr großen Kontextfenstern praktikabel; üblicherweise ist ein Dokumentenabruf nötig, bei dem lange Dateien wie KF-98 an Überschriften geteilt werden.
4. Verarbeitung und Abruf prüfen. Bei semantischem Retrieval passende Embeddings und Indexierung einrichten. Kontrolle mit normalen Nutzungsrechten durchführen: Ein erfolgreicher Upload belegt noch keinen Zugriff im Chat.
5. Am tatsächlichen Modellkontext prüfen, ob die vollständigen Anweisungen, die benötigten Wissensabschnitte und lokale Angaben ankommen. Bei aufgeteilten Dokumenten relevante Herkunfts-, Versions-, Status- und Prüfangaben mitführen; ein Hinweis nur am Dateianfang erreicht spätere Abschnitte nicht zwingend.
6. Die vorgesehenen Werkzeuge und Oberflächenfunktionen konfigurieren. Wissensabruf muss für den gewählten Integrationsweg verfügbar sein. Die Edition enthält keine Websuche oder Live-Sanktionsprüfung. Sichtbare Quellenkarten, Zugriffsrechte und Protokollierung werden in der Plattform eingestellt.
7. Tatsächliche Antworten mit den Golden Questions und zusätzlichen institutionellen Kontaktprüfungen bewerten. Den Quellenabruf gesondert nachweisen. Browserchat und API getrennt prüfen, sofern beide verwendet werden.
8. Nach fachlicher Freigabe und bewerteten Tests den vorgesehenen Production-Stand bereitstellen, seine tatsächliche Konfiguration kontrollieren und die institutionelle Inbetriebnahmeentscheidung dokumentieren.

Das optionale Beispiel `docs/openwebui.md` beschreibt eine mögliche Plattform. Andere Umgebungen benötigen entsprechende Anbindungsschritte. Konkrete Oberflächenbezeichnungen, API-Payloads und Werkzeugpfade hängen von der tatsächlich eingesetzten Version ab.

### Was beim Testen noch zu tun ist

Die 45 Fälle unter `evaluation/golden_questions/` sind vorhanden. `scripts/prepare_evaluation.py` exportiert daraus einen Plan:

```bash
python scripts/prepare_evaluation.py --out dist/evaluation-plan-01.json
```

Alle Fälle bleiben dabei `not_run`. Der Befehl führt weder einen Modelltest noch eine Judge-Bewertung durch. Die Ausführung kann manuell oder über einen zusätzlich angebundenen Runner erfolgen. Bei Gesprächsfolgen mit `follows` die tatsächlichen vorherigen Botantworten verwenden.

Fälle mit `fixture: institution.test` gehören in das synthetische Testprofil. Fälle mit `fixture: unconfigured` benötigen ein Profil ohne lokale Konfiguration und ohne vorangehenden lokalen Gesprächskontext. Die synthetischen Sollwerte nicht durch reale Kontaktdaten in der öffentlichen Fixture ersetzen. Die tatsächlichen eigenen Kontakte in zusätzlichen passenden Fällen prüfen.

Für den Nachweis eine private Kopie von `evaluation/TEST_PROTOCOL.md` verwenden. Mindestens Commit/Build-Manifest, Plattformversion, konkrete Modellkennung, Einstellungen, Konfiguration, Antworten, Kriterienverletzungen und tatsächlich abgerufene Quellen festhalten. Ein guter Durchschnittswert darf harte Fehler wie falsche Kontakte oder behauptete Freigaben nicht verdecken.

### Production-Paket erst nach lokaler Fachfreigabe

```bash
python scripts/build_bundle.py --mode production --config .local/institution.json --out dist/production-01
```

Mit dem öffentlichen Draft-Bestand schlägt dieser Befehl absichtlich fehl. Auch nach erfolgreichem Build wird das Paket nicht automatisch in die Plattform übertragen. Den tatsächlich bereitgestellten Production-Kontext kontrollieren; das zuvor getestete Review-Profil allein belegt diesen Stand nicht.

## 7. Was für Automatisierung noch nicht vorhanden ist

Die folgende Liste beschreibt den Stand von Version 1.0.0. Die Dateinamen in der letzten Spalte sind **mögliche Namen in einem separaten privaten Betriebsrepository**, keine bestehenden Dateien und keine vom Quellrepo automatisch gesuchten Pfade.

| Baustein | Stand und noch erforderliche Arbeit | Beispiel für eigene Ergänzung |
|---|---|---|
| Plattformanbindung / Deployadapter | Nicht enthalten. Eine eigene Integration müsste Anweisungen, Wissen und Profile über die tatsächliche Plattform-API übertragen und anschließend prüfen. Bei manueller Übernahme ist kein Adapter erforderlich. | `scripts/deploy_runtime.py` |
| Technische Laufzeitkonfiguration | Kein betriebsfertiges Konfigurationsformat für Server, Modell, Zielprofil oder Wissenssammlung enthalten. Die erzeugte Einstellungsreferenz wird nicht automatisch ausgeführt. | `config/runtime.example.json` plus privater Werte-/Secret-Speicher |
| Wissensupload und Indexverwaltung | Kein automatischer Upload, Reindex, versionsbezogener Sammlungswechsel oder bereinigter Austausch alter Inhalte implementiert. | Im Deployadapter oder eigener Uploadkomponente |
| Metadaten je Wissensabschnitt | Der Build setzt einen Status-/Datumshinweis an den Anfang. Er überträgt keine Plattformmetadaten an jeden Retrieval-Abschnitt. Eine geeignete Zuordnung muss die Integration leisten. | Im Upload-/Retrievaladapter |
| Modelltest-Runner | Nicht enthalten. Der vorhandene Exporter erzeugt nur einen Plan; ein Runner müsste Fragen und Gesprächsfolgen an die tatsächlich konfigurierte Anwendung senden und Antworten erfassen. | `scripts/evaluate_runtime.py` |
| Automatische Judge-Bewertung | Nicht enthalten. Manuelle Bewertung ist möglich; ein zusätzlicher Judge müsste Kriterien, harte Fehler und nachvollziehbare Ergebnisse verarbeiten. | `scripts/judge_results.py` |
| Übergang von Test zu Production | Keine automatische Entscheidung anhand von Modelltests oder institutionellen Freigaben vorhanden. Abnahmekriterien und Freigabeschritt sind zusätzlich festzulegen. | Eigener Freigabejob in der Betriebs-CI |
| Rückkehr zu einem früheren Stand | Kein automatischer Rollback enthalten. Vorherige Anweisungen, Wissenssammlung, Einstellungen und Manifest müssen rekonstruierbar bleiben. | `docs/deploy-runbook.md` oder eigener Rollbackjob |
| Hosting einer neuen Plattform | Kein `Dockerfile`, keine `docker-compose.yml` und keine Serverinstallation enthalten. Das ist bei Nutzung einer vorhandenen Plattform nicht zusätzlich nötig. | Nur bei eigenem Hosting nach dessen Betriebsmodell |

### Welche Angaben eine eigene Integration üblicherweise benötigt

Zieladresse der Plattform, konkrete Modellkennung, Profil-/Sammlungskennung, Zugriffsart, notwendige Berechtigungen, Speicherorte und die gewählte Übernahmemethode müssen festgelegt werden. Zugangsdaten gehören in einen geeigneten Secret-Speicher. **In Version 1.0.0 gibt es keine dafür definierten Pflicht-Umgebungsvariablen und keinen `.env`-Lader.** Eine selbst angelegte `.env`-Datei verbindet den Bot deshalb nicht mit einer Plattform.

Für eine robuste Automatisierung zuerst den manuellen Ablauf in der konkreten Umgebung nachweisen. Danach genau diesen getesteten Ablauf automatisieren: Paket auswählen, neues Ziel vorbereiten, Inhalte übertragen, Verarbeitung und Abruf prüfen, Testresultate auswerten, Freigabe dokumentieren und kontrolliert umstellen. Ungetestete neue Wissensfassungen nicht zusätzlich in die aktive Sammlung mischen.

## 8. CI und betriebliche Unterlagen

### Die vorhandene CI richtig einordnen

`.gitlab-ci.yml` und `.github/workflows/validate.yml` prüfen das öffentliche Quellenrepository. Sie validieren Quellen, führen technische Tests aus, bauen ein unkonfiguriertes Review-Paket, exportieren den nicht ausgeführten Testplan und paketieren die öffentlichen Quellen.

Sie enthalten **keine Jobs für einen Plattform-Deploy, echte Modelltests, Judge-Bewertungen oder eine Production-Promotion**. Ein Runner oder eine GitLab-zu-GitHub-Spiegelung wird durch die Dateien ebenfalls nicht eingerichtet. Die vorhandenen Jobs übergeben keine institutionelle Konfiguration an den Build.

Für einen automatisierten institutionellen Betrieb einen getrennten Ablauf vorsehen. Dort gelten die eigenen lokalen Freigaben; der öffentliche Draft-Zwang ist nicht die passende Production-Bedingung. Auch die vorhandenen Tests der öffentlichen Quellpaketierung sind bei einer freigegebenen Betriebsfassung entsprechend einzuordnen. Die allgemeine Validierung und die Prüfung der tatsächlichen Deploy- und Evaluationsergebnisse bleiben erforderlich.

### Welche Betriebsunterlagen noch anzulegen sind

Die folgenden Inhalte werden für einen nachvollziehbaren Betrieb empfohlen. Ihre Dateinamen sind frei wählbar; Version 1.0.0 liest sie nicht automatisch ein.

| Inhalt | Was konkret dokumentiert werden sollte | Möglicher lokaler Arbeitsort |
|---|---|---|
| Betrieb und Zuständigkeiten | Fachverantwortung, technische Betreuung, Zielgruppe, Plattform-/Modellstand, Wissensabruf, Rechte, Datenverarbeitung, Fehlerkanal und Pflegezyklus. | `.local/betrieb.md` |
| Fachliche und betriebliche Freigabe | Geprüfte KF-Versionen, Prüfer:in, tatsächliche Prüfdaten, offene Punkte, akzeptierter Teststand und Entscheidung zur Inbetriebnahme. | `.local/freigabe.md` |
| Modelltests | Private Kopie der vorhandenen Protokollvorlage, tatsächliche Antworten und Ergebnisse; keine Ergebnisse vorwegnehmen. | `.local/testprotokoll.md` |
| Deploy und Rückkehr | Übernahmeschritte, Zielprofil/-sammlung, getesteter Stand, Nachkontrolle und Rückkehr zum vorherigen Stand. | `.local/deploy-runbook.md` |

`.local/` ist eine lokale Ablage und wird standardmäßig nicht mit Git versioniert. Für dauerhafte Nachweise und Zusammenarbeit eine geeignete private, gesicherte Ablage oder ein separates Betriebsrepository verwenden. Unterlagen nicht zur Umgehung der Dateiprüfung in `config/public-files.json` als öffentlich deklarieren.

### Pflege nach dem Start

Bei Änderungen an Modell, Plattform, Prompt, Wissen oder lokalen Angaben die betroffenen Verhaltenstests wiederholen. Nach Aktualisierung lokaler Daten den Systemprompt erneuern; nach Wissensänderungen Sammlung und Abruf aktualisieren. Änderungen am Profil und an seinem Wissensbestand gemeinsam nachvollziehbar halten. Das Build-Manifest dokumentiert Quellen und Ausgaben, aber keinen erfolgreichen Server-Deploy.

## 9. Angaben nur für einen eigenen Fork oder Quellrelease

Diese Punkte betreffen die Pflege eines eigenen veröffentlichten Projekts. Sie sind keine zusätzlichen Laufzeit-Kontaktfelder für jede nachnutzende Einrichtung.

| Datei oder Einstellung | Wann und was anzupassen ist |
|---|---|
| `README.md` und `docs/publishing.md` | Bei eigener Projektpflege die tatsächlichen Repositoryadressen, den Veröffentlichungsweg und die Betreuung beschreiben. Der Ablauf der Spiegelung steht in `docs/publishing.md`; er betrifft die Projektpflege, nicht die Botkonfiguration. |
| `CONTRIBUTING.md` | Bei eigenen Beitragsprozessen den tatsächlichen Eingang und Bearbeitungsweg erläutern. |
| `SECURITY.md` | Einen tatsächlich verfügbaren privaten Meldeweg für das betreute Projekt konkretisieren. Die bloße Datei richtet keinen Meldekanal ein. |
| `CITATION.cff`, `VERSION`, `CHANGELOG.md` | Bei eigenem Release dessen Version und Herkunft nachvollziehbar führen. `date-released` erst mit dem tatsächlichen Veröffentlichungsdatum ergänzen. |
| `LICENSE`, `NOTICE`, `CREDITS.md` | Vorhandene Lizenz- und Herkunftsinformationen bewahren; eigene Beiträge gegebenenfalls getrennt ergänzen. Diese Dateien nicht als institutionelle Kontaktvorlagen behandeln. |
| Repository-/CI-Einstellungen | Runner, Zugriffsrechte, Freigabeschritte und gegebenenfalls eine eigene Spiegelung einrichten. Eine nachnutzende Einrichtung muss keinen Spiegel in das Projektrepository der Universität Kassel konfigurieren. |

## 10. Abnahmeliste für die Einrichtung

- [ ] Verantwortliche für Fachwissen, lokale Angaben, Betrieb und Freigabe benannt.
- [ ] Geeignete Plattform und konkretes Modell eingerichtet; tatsächlicher Kontext und Zugriffsrechte geprüft.
- [ ] Datenschutz, Beteiligung der Personalvertretung und Kennzeichnung gegenüber Nutzenden geprüft, soweit einschlägig.
- [ ] Falls lokale Auskünfte vorgesehen sind: `.local/institution.json` mit bestätigten Angaben angelegt und beim Build ausdrücklich übergeben.
- [ ] Fakten und Verfahren getrennt geprüft; unbekannte Angaben bleiben leer.
- [ ] Lokale Festlegungen aus KF-03f, KF-03h, KF-07e und KF-07f geprüft; nur botrelevante Kurzverfahren in `procedures[]` übernommen.
- [ ] KF-04 und KF-08 auf institutionelle Passung geprüft; nur bei tatsächlichem Widerspruch lokal geändert.
- [ ] Keine lokalen Kontakte in KF-98 oder in Prompts dupliziert.
- [ ] Alle vorgesehenen Laufzeit-KFs fachlich geprüft; Freigabe und Prüfdaten im privaten Arbeitsstand dokumentiert.
- [ ] Vollständigen Systemprompt und ausschließlich das vorgesehene Wissen übernommen; keine alten Wissensfassungen unkontrolliert parallel aktiv.
- [ ] Wissensabruf, relevante Metadaten und lokale Angaben im tatsächlichen Modellkontext nachgewiesen.
- [ ] Golden Questions mit den passenden Testprofilen ausgeführt; harte Fehler und offene Punkte bewertet.
- [ ] Reale institutionelle Kontaktantworten zusätzlich geprüft; synthetische Testwerte bleiben getrennt.
- [ ] Production-Stand bereitgestellt und kontrolliert; institutionelle Inbetriebnahmeentscheidung dokumentiert.
- [ ] Fehlerkanal, Pflegeablauf und Rückkehr zu einem früheren Stand festgelegt.

## Quellenbasis und Aussagegrenzen

Diese Übersicht wurde am 26.10.2026 mit den Dateien des bereitgestellten Quellstands **1.0.0** abgeglichen. Maßgeblich für die beschriebenen technischen Bedingungen sind `scripts/project.py` (insbesondere `local_context`, `read_kf`, `selected_documents`, `public_files`), `scripts/build_bundle.py`, `scripts/prepare_evaluation.py`, `scripts/package_release.py`, die beiden CI-Dateien und die Konfigurationsmanifeste. Ergänzend wurden `docs/setup.md`, `docs/configuration.md`, `docs/knowledge-maintenance.md`, `docs/publishing.md`, `evaluation/README.md`, `evaluation/TEST_PROTOCOL.md` und die beiden lokalen Vorlagen geprüft.

Die Übersicht beschreibt keine bereits erfolgte institutionelle Einrichtung. Sie liefert keinen Plattformadapter, keinen automatischen Test-Runner und keine fachliche Freigabe mit. Die technischen Prüfungen des Quellstands laufen in der CI des Projekts; sie sind von den noch erforderlichen Tests der jeweiligen Einrichtung zu unterscheiden.
