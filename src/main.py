# main.py
import datetime as dt
import tkinter as tk
from tkinter import messagebox

from api import get_time_entries
from kpi_daily import normalize, kpi_by_day, kpi_by_description
from dashboard import show_dashboard

# --- Dummy-Datenfunktion ---
def get_dummy_entries(start, end):
    return [
        {"start": "2025-09-22T06:00:00+00:00", "duration": 4*3600, "description": "Projekt A"},
        {"start": "2025-09-22T12:00:00+00:00", "duration": 2*3600, "description": "Projekt B"},
        {"start": "2025-09-22T14:00:00+00:00", "duration": 3*3600, "description": "Meeting"},
        {"start": "2025-09-23T06:00:00+00:00", "duration": 4*3600, "description": "Projekt A"},
        {"start": "2025-09-23T06:00:00+00:00", "duration": 4*3600, "description": "Projekt A"},
        {"start": "2025-09-24T12:00:00+00:00", "duration": 6*3600, "description": "Projekt C"},
    ]

def ask_mode():
    root = tk.Tk()
    root.withdraw()  # Kein leeres Fenster offen lassen
    use_dummy = messagebox.askyesno("Datenquelle wählen", "Dummy-Daten verwenden?")
    root.destroy()
    return use_dummy

def main():
    # Zeitraum: letzte 7 Tage
    end = dt.datetime.now(dt.UTC)
    start = end - dt.timedelta(days=7)

    use_dummy = ask_mode()

    if use_dummy:
        print("Dummy-Daten werden genutzt.")
        entries = get_dummy_entries(start, end)
    else:
        print("Live-API wird abgefragt.")
        entries = get_time_entries(start, end)

    df = normalize(entries)
    if df.empty:
        print("Keine Daten gefunden.")
        return

    daily = kpi_by_day(df)
    kpi_desc = kpi_by_description(df)

    print("Stunden pro Tag:")
    print(daily)

    print("Stunden nach Beschreibung:")
    print(kpi_desc)

    show_dashboard(df, daily, revenue=800)

if __name__ == "__main__":
    main()
