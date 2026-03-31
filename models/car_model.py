class CarModel:
    def __init__(self):
        self._dtc_errors = []

    def add_error(self, error):
        self._dtc_errors.append(error)

    def get_all_errors(self):
        return self._dtc_errors
