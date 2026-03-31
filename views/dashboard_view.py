import tkinter as tk


class DashboardView(tk.Frame):
    def __init__(self, parent, model):
        super().__init__(parent, bg="#F5F5F5")
        self.model = model

        # Статус автомобіля
        tk.Label(self, text="Vehicle Status: Healthy", font=("Arial", 16, "bold"),
                 fg="green", bg="#F5F5F5").pack(pady=10)

        # Панель датчиків (контейнер)
        stats_frame = tk.Frame(self, bg="#F5F5F5")
        stats_frame.pack(fill="x", padx=20)

        # Налаштування колонок для рівномірного розподілу
        stats_frame.columnconfigure(0, weight=1)
        stats_frame.columnconfigure(1, weight=1)
        stats_frame.columnconfigure(2, weight=1)

        # Створення карток датчиків
        self.create_gauge(stats_frame, "RPM", "800", 0)
        self.create_gauge(stats_frame, "Temp", "90°C", 1)
        self.create_gauge(stats_frame, "Battery", "14.2V", 2)

        # Кнопка сканування
        tk.Button(self, text="START FULL SCAN", bg="red", fg="white",
                  font=("Arial", 14, "bold"), relief="flat", cursor="hand2").pack(pady=30, padx=40, fill="x", ipady=10)

    def create_gauge(self, parent, title, value, col):
        # Картка окремого датчика
        f = tk.Frame(parent, bd=1, relief="solid", padx=10, pady=10, bg="white")
        f.grid(row=0, column=col, padx=5, sticky="nsew")

        tk.Label(f, text=title, fg="gray", bg="white", font=("Arial", 10)).pack()
        tk.Label(f, text=value, font=("Arial", 14, "bold"), bg="white").pack()