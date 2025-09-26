# Toggl KPI Dashboard (POC)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-POC-orange)
![Made with ❤️](https://img.shields.io/badge/made%20with-%E2%9D%A4-red)

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
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
3. Starten:
   ```bash
   python main.py

Nutzung

Beim ersten Start ohne .env-Datei wird automatisch nach dem Toggl API-Key gefragt.
Der Key wird gespeichert und in einer .env-Datei hinterlegt.

Alternativ kann das Projekt im Dummy-Modus gestartet werden (Abfrage beim Start).

Anforderungen

Python 3.10+

Pakete: requests, python-dotenv, pandas, matplotlib

## Lizenz
Dieses Projekt steht unter der [MIT-Lizenz](https://opensource.org/licenses/MIT).

