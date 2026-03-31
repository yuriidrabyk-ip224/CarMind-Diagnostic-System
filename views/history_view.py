import tkinter as tk

class HistoryView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Service History", font=("Arial", 18, "bold")).pack(pady=10)

        services = [("Oil Change", "12.05.2025", "5500 km"),
                    ("Brake Pads", "10.01.2026", "12000 km")]

        for service, date, mileage in services:
            card = tk.Frame(self, bd=1, relief="groove", pady=10)
            card.pack(fill="x", padx=20, pady=5)
            tk.Label(card, text=f"{service} - {date}", font=("Arial", 11, "bold")).pack(side="left", padx=10)
            tk.Label(card, text=mileage, fg="blue").pack(side="right", padx=10)