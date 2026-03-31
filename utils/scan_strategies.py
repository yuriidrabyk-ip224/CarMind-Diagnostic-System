class QuickScanStrategy:
    def execute(self):
        return [("P0300", "Misfire Detected", "High")]

class DeepScanStrategy:
    def execute(self):
        return [
            ("P0300", "Misfire Detected", "High"),
            ("B1204", "Airbag Sensor", "Medium"),
            ("U0100", "Lost Comm with ECM", "High")
        ]