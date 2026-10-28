# Abhängigkeiten und externe Quellen

Stand: 26.10.2026 | Dokumentversion 1.2. Laufzeitplattform und Basismodell werden nicht mitgeliefert.

| Komponente | Verwendung | Bedingungen |
|---|---|---|
| Python 3.11+ | Offline-Skripte | Python-eigene Lizenz |
| PyYAML 6.0.3 | Sicheres YAML-Lesen und Metadatenprüfung | MIT; nicht als Quellcode gebündelt |
| Gewählte KI-Plattform / eigene Anwendung | Kontrollierte Bereitstellung von Anweisungen und Wissen | Auswahl und Bedingungen durch die Einrichtung; nicht mitgeliefert |
| Open WebUI (optional) | Nur dokumentiertes Einrichtungsbeispiel, keine Projektvoraussetzung | Eigene Lizenz; nicht Apache-lizenziert durch dieses Projekt |
| Basismodell; gegebenenfalls Embeddings | Antworterzeugung; je nach Integrationsweg Wissensabruf | Anbieter-/Modellbedingungen; keine Gewichte enthalten |
| GitLab CI | Technische Prüfung im führenden Repository | Geeigneter Runner und Python-Umgebung erforderlich; keine Modell-Secrets |
| GitHub Actions | Zusätzliche technische Prüfung des öffentlichen Spiegels | Externe Actions; keine institutionellen Modell-Secrets erforderlich |

Apache 2.0 gilt für eigene Prompttexte, kuratierte Zusammenfassungen, Konfigurationen, Skripte, Tests und Dokumentation, soweit die Rechte bei der Rechteinhaberin liegen. Verlinkte Gesetzestexte, Behördeninformationen und Drittleitfäden verbleiben unter ihren jeweiligen Bedingungen. Keine vollständigen Fremdwerke oder Open-WebUI-Quellen sind gebündelt.

Die Bedingungen der jeweils eingesetzten Plattform und Modelle sind vor Ort zu prüfen. Wird das optionale Open-WebUI-Beispiel genutzt, betrifft dies auch Lizenz- und gegebenenfalls Branding-Anforderungen der tatsächlich eingesetzten Version. Apache 2.0 ersetzt diese nicht. Der Hinweis steht in der Dokumentation und nicht als Zusatzbedingung im Apache-Lizenztext.

## Offizielle Nachweise

- Apache 2.0: https://www.apache.org/licenses/LICENSE-2.0
- Lizenzanwendung: https://www.apache.org/licenses/LICENSE-2.0
- Open-WebUI-Lizenz: https://github.com/open-webui/open-webui/blob/main/LICENSE
- Open-WebUI-Modellkonfiguration: https://docs.openwebui.com/features/workspace/models/
- PyYAML 6.0.3: https://pypi.org/project/PyYAML/6.0.3/
- GitLab Push-Mirroring: https://docs.gitlab.com/user/project/repository/mirror/push/
- GitLab CI: https://docs.gitlab.com/ci/
- Open-WebUI-Metadaten ab v0.11.4: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
- Checkout: https://github.com/actions/checkout
- Setup-Python: https://github.com/actions/setup-python
- Upload-Artifact: https://github.com/actions/upload-artifact

Die Offline-Hilfsskripte kommunizieren nicht mit diesen Diensten. Installation von Abhängigkeiten und CI benötigen gegebenenfalls Netzwerkzugriff. Die separat einzurichtende GitLab-Spiegelung verwendet eigene Zugangsdaten; diese gehören nicht in das Repository. Keine versionsübergreifende Funktionsgarantie für externe Plattformen.
