# src/kpi_daily.py
import pandas as pd

def normalize(entries):
    """Wandelt rohe API-Einträge in ein DataFrame mit Datum & Stunden um."""
    df = pd.DataFrame(entries)
    if df.empty:
        return df
    df["start"] = pd.to_datetime(df["start"])
    df["date"] = df["start"].dt.date
    df["hours"] = df["duration"] / 3600
    return df

def kpi_by_day(df: pd.DataFrame):
    """Summiert Stunden pro Tag."""
    return df.groupby("date")["hours"].sum().reset_index()

def kpi_by_description(df: pd.DataFrame):
    """Summiert Stunden nach Beschreibung."""
    return df.groupby("description")["hours"].sum().reset_index()

if __name__ == "__main__":
    print("Dieses Modul ist nur für KPI-Berechnung gedacht. Bitte über main.py aufrufen.")
