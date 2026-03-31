import tkinter as tk
from services.service_locator import ServiceLocator
from services.car_system_facade import CarSystemFacade
from utils.scan_strategies import QuickScanStrategy, DeepScanStrategy
from views.login_view import LoginView
from views.dashboard_view import DashboardView
from views.history_view import HistoryView


class CarMindApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CarMind - Smart Diagnostic")
        self.root.geometry("390x844")
        self.root.configure(bg="#1A1A1A")

        # 1. Отримуємо залежності через Service Locator (Singleton)
        self.locator = ServiceLocator()
        self.model = self.locator.get_car_model()
        self.intent = self.locator.get_car_intent()

        # 2. Створюємо Фасад для спрощення взаємодії з системами авто
        self.facade = CarSystemFacade(self.locator)

        # Контейнер для екранів
        self.container = tk.Frame(self.root, bg="#1A1A1A")
        self.container.pack(fill="both", expand=True)

        # Початковий екран
        self.show_login()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def handle_login(self):
        """Використання патерна Фасад для авторизації та запуску систем"""
        # У реальному коді тут були б дані з полів введення
        success = self.facade.full_system_boot("user@example.com", "password123")
        if success:
            self.show_dashboard()

    def show_login(self):
        self.clear_container()
        # Тепер on_success викликає наш фасадний метод
        login_screen = LoginView(self.container, on_success=self.handle_login)
        login_screen.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.clear_container()

        # Демонстрація патерна Стратегія: встановлюємо "Швидкий скан" за замовчуванням
        self.intent.set_strategy(QuickScanStrategy())

        dashboard = DashboardView(self.container, self.model)
        dashboard.pack(fill="both", expand=True)

        # Додамо кнопки для зміни стратегії прямо на головному екрані
        btn_frame = tk.Frame(self.container, bg="#1A1A1A")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Quick Mode",
                  command=lambda: self.intent.set_strategy(QuickScanStrategy()),
                  bg="#34C759", fg="white", width=12).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Deep Mode",
                  command=lambda: self.intent.set_strategy(DeepScanStrategy()),
                  bg="#FF3B30", fg="white", width=12).pack(side="left", padx=5)

        tk.Button(self.container, text="View Service History",
                  command=self.show_history, bg="#2D2D2D", fg="white",
                  relief="flat", pady=5).pack(pady=10)

    def show_history(self):
        self.clear_container()
        history = HistoryView(self.container)
        history.pack(fill="both", expand=True)

        tk.Button(self.container, text="Back to Dashboard",
                  command=self.show_dashboard, bg="#2D2D2D", fg="white",
                  relief="flat", pady=5).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = CarMindApp(root)
    root.mainloop()