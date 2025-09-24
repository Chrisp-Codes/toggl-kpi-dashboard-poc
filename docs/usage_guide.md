# Usage Guide – Toggl KPI Dashboard (POC)

Dieser Guide zeigt Schritt für Schritt, wie man das Dashboard lokal startet, 
zwischen Dummy- und Live-Daten umschaltet und die wichtigsten Funktionen nutzt.  

---

## 1. Start des Projekts
Im Projektordner (`src/`) ausführen:
```bash
python main.py
```

---

## 2. Auswahl: Dummy- oder Live-Daten
Beim Start öffnet sich ein kleines Dialogfenster:

- **Ja** → Dummy-Daten werden geladen  
- **Nein** → Die Live-API wird abgefragt  

![Dummy-Abfrage](dashboard_example.png)

---

## 3. Erste Nutzung ohne `.env`
Wenn keine `.env` vorhanden ist und du **Live-Daten** auswählst:
- Es erscheint eine Abfrage nach deinem **Toggl API-Key**.  
- Der Key wird gespeichert und automatisch in einer neuen `.env` Datei abgelegt.  
- Beim nächsten Start wird der Key automatisch geladen.  

Format der `.env`:
```env
TOGGL_API_KEY=dein_api_key_hier
```

---

## 4. Dashboard-Ansicht
Nach erfolgreichem Start öffnet sich das Dashboard (Matplotlib-Fenster).  

**Kacheln:**
- **Umsatz heute**: Platzhalter (fix $800, nur Demo)  
- **Produktivität heute**: Umsatz / gearbeitete Stunden des aktuellen Tages  
- **Wochenübersicht**: Arbeitsstunden der letzten 7 Tage (Kacheln pro Wochentag)  
- **Produktivität pro Tag**: Verlauf der Produktivität ($/h) als Diagramm  

![Dashboard Screenshot](dashboard_example.png)

---

## 5. CSV-Export
Bei jedem Lauf werden automatisch CSV-Dateien im Projektordner erstellt:  
- `time_entries_<start>_<end>.csv` (Rohdaten)  
- `kpi_daily_<start>_<end>.csv` (Stunden pro Tag)  
- `kpi_by_description_<start>_<end>.csv` (Stunden pro Beschreibung)  

Beispiel:
```csv
date,hours
2025-09-22,7
2025-09-23,9
```

---

## 6. Voraussetzungen
- Python 3.10+  
- Pakete: `requests`, `python-dotenv`, `pandas`, `matplotlib`  
- Installation über:
```bash
pip install -r requirements.txt
```

---

## 7. Typische Anwendungsfälle
- **Schnelle KPI-Übersicht**: Arbeitsstunden & Produktivität  
- **CSV-Export**: für Weiterverarbeitung in Excel/BI-Tools  
- **Dummy-Modus**: Demo ohne API-Key (ideal für Präsentationen)  

---
