# src/dashboard.py
import matplotlib.pyplot as plt
import pandas as pd

def show_dashboard(df: pd.DataFrame, daily: pd.DataFrame, revenue: float = 800):
    """
    Baut das Produktivitäts-Dashboard.
    Erwartet:
      - df: Rohdaten mit Spalten [start, date, hours, description]
      - daily: Aggregation Stunden pro Tag
      - revenue: Fixer Umsatz pro Tag (Dummy / Platzhalter)
    """
    latest = daily.iloc[-1]
    productivity_today = revenue / latest["hours"]

    fig, axes = plt.subplots(2, 2, figsize=(10, 7))

    # --- Titel mit Trennlinie ---
    fig.suptitle("Produktivitäts-Dashboard (POC)", fontsize=30, weight="bold")
    fig.subplots_adjust(top=0.8)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    title = fig._suptitle
    bbox = title.get_window_extent(renderer=renderer)
    bbox = bbox.transformed(fig.transFigure.inverted())
    y_line = bbox.y0 - 0.01
    fig.lines.append(
        plt.Line2D([0.1, 0.9], [y_line, y_line],
                   transform=fig.transFigure, color="black", linewidth=2)
    )

    # --- Kachel 1: Umsatz heute ---
    axes[0, 0].text(0.5, 0.5, f"$ {revenue}",
                    ha="center", va="center", fontsize=28, weight="bold")
    axes[0, 0].set_title(f"Umsatz am {latest['date']}")
    axes[0, 0].axis("off")

    # --- Kachel 2: Produktivität heute ---
    axes[0, 1].text(0.5, 0.5, f"{productivity_today:.1f} $/h",
                    ha="center", va="center", fontsize=28, weight="bold")
    axes[0, 1].set_title("Produktivität heute")
    axes[0, 1].axis("off")

    # --- Kachel 3: Wochenübersicht ---
    last7 = daily.tail(7)
    week_num = latest["date"].isocalendar()[1]
    year = latest["date"].year
    axes[1, 0].set_title(f"Wochenübersicht (KW {week_num} / {year})")
    axes[1, 0].axis("off")

    for i, row in enumerate(last7.itertuples()):
        col = i % 4
        rowpos = i // 4
        x = 0.25 + col * 0.25
        y = 0.8 - rowpos * 0.3
        dayname = row.date.strftime("%a")
        axes[1, 0].text(x, y,
                        f"{dayname}: {row.hours:.1f}h",
                        ha="center", va="center", fontsize=14,
                        bbox=dict(boxstyle="round,pad=0.3", fc="lightblue"),
                        transform=axes[1, 0].transAxes)

    # --- Kachel 4: Produktivität pro Tag ---
    last7["productivity"] = revenue / last7["hours"]
    axes[1, 1].plot(last7["date"], last7["productivity"], marker="o", color="green")
    axes[1, 1].set_title("Produktivität pro Tag")
    axes[1, 1].set_ylabel("$ / h")
    axes[1, 1].set_xticks(last7["date"])
    axes[1, 1].set_xticklabels(last7["date"].apply(lambda d: d.strftime("%d.%m")))

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    print("Dieses Modul ist nur für Visualisierung gedacht. Bitte über main.py aufrufen.")
