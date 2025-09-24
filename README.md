# Toggl KPI Dashboard (POC)

[English Version](README_en.md)

## Überblick
Dieses Projekt ist ein **Proof of Concept** zur Auswertung von Toggl Track Daten.  
Es zeigt, wie sich Zeiteinträge automatisch abrufen, bereinigen und in einem kleinen Dashboard visualisieren lassen.  
Das Ziel: Von Rohdaten zu KPIs und Visualisierungen in wenigen Sekunden.

![Dashboard Screenshot](docs/dashboard_example.png)

## Features
- **API-Anbindung** an Toggl Track (über persönlichen API-Key)
- **Dummy-Modus**: Projekt kann auch ohne API-Key mit Testdaten gestartet werden
- **Kennzahlen**:
  - Arbeitsstunden pro Tag
  - Stunden nach Beschreibung
  - Produktivität ($/h) basierend auf fixem Dummy-Umsatz
- **Dashboard** (matplotlib):
  - Tagesumsatz (fixer Platzhalter: $800)
  - Produktivität heute
  - Wochenübersicht (Stunden pro Tag)
  - Produktivität pro Tag (Diagramm)
- **CSV-Export** für weitere Analysen

## Installation
1. Repository klonen:
   ```bash
   git clone https://github.com/Chrisp-Codes/toggl-kpi-dashboard-poc.git
   cd toggl-kpi-dashboard-poc/src
