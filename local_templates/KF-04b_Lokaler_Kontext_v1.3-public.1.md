---
id: "KF-04b"
title: "Lokale Fakten der betreibenden Einrichtung"
version: "1.3-public.1"
status: "draft"
last_reviewed: null
review_cycle: "event_driven"
profiles:
  - "researcher"
scope: "{{INSTITUTION_NAME}}"
document_type: "Nicht operative Vorlage; zur institutionellen Konfiguration"
related: []
knowledge_area: null
purpose: null
binding: null
---

<!-- SPDX-License-Identifier: Apache-2.0; Public adaptation 2026-10-22; source version institution-specific original replaced; editorial adaptation, not a new legal review. -->

# KF-04b - Lokale Fakten

Diese Vorlage enthält absichtlich keine realen Kontakte. Platzhalter sind keine Tatsachen und dürfen nicht an Nutzende ausgegeben werden. Die einzige lokale Faktenquelle im Laufzeitkontext wird aus der institutionell bestätigten Datei `.local/institution.json` erzeugt.

## Platzhalter

- Einrichtung: {{INSTITUTION_NAME}}
- Stelle: {{EXPORT_CONTROL_OFFICE}}
- Organisationseinheit: {{EXPORT_CONTROL_UNIT}}
- E-Mail: {{EXPORT_CONTROL_EMAIL}}
- Webseite: {{EXPORT_CONTROL_URL}}
- Personen-Rollen-Zuordnung: {{PERSON_ROLE_ASSIGNMENT}}

## Regeln

Nur vollständige bestätigte Werte exakt ausgeben; keine Rekonstruktion aus Namen, Rollen oder Domains. Unbekannte Werte auslassen. Niemals aus einem Forschungsförderungs-, IT- oder anderen Kontakt eine Exportkontrollzuständigkeit ableiten. Lokale Fakten nur nutzen, wenn sie im aktuellen Kontext vorhanden sind.
