class ServiceLocator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ServiceLocator, cls).__new__(cls)
            cls._instance._services = {}
            cls._instance._initialize_services()
        return cls._instance

    def _initialize_services(self):
        from models.car_model import CarModel
        from intents.car_intent import CarIntent
        from utils.obd_scanner import OBDScanner

        # Реєстрація компонентів
        self._services['model'] = CarModel()
        self._services['scanner'] = OBDScanner()

        # Впорскування моделі в Intent (Dependency Injection через конструктор)
        self._services['intent'] = CarIntent(self._services['model'])

    def get_car_intent(self):
        return self._services['intent']

    def get_car_model(self):
        return self._services['model']