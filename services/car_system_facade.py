class CarSystemFacade:
    def __init__(self, locator):
        self.locator = locator

    def full_system_boot(self, email, password):
        """Фасадний метод: одна команда робить все"""
        print(f"--- System Boot Sequence Started ---")
        # 1. Емуляція логіну
        if email and password:
            # 2. Емуляція підключення до OBD-II
            print(f"Connecting to OBD-II Adapter via Bluetooth...")
            # 3. Підготовка моделі
            model = self.locator.get_car_model()
            print(f"CarModel initialized for {email}")
            return True
        return False