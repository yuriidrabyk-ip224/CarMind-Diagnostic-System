# Додай цей рядок зверху:
from utils.scan_strategies import QuickScanStrategy

class CarIntent:
    def __init__(self, model):
        self.model = model
        self.strategy = QuickScanStrategy()  # Стратегія за замовчуванням

    def set_strategy(self, strategy):
        self.strategy = strategy

    def start_scanning(self):
        # Використовуємо стратегію замість прямого виклику
        errors = self.strategy.execute()
        self.model.dtc_codes = [] # Очищуємо старі
        for err in errors:
            self.model.add_error(err)
        print(f"Сканування завершено за стратегією: {self.strategy.__class__.__name__}")