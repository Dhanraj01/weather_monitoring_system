import json
import os

class FileHandler:
    def __init__(self):
        self.file_path = 'data/weather_summary.json'
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def save_summary(self, daily_summary):
        try:
            with open(self.file_path, 'w') as f:
                json.dump(daily_summary, f)
            print("Weather summary saved successfully.")
        except Exception as e:
            print(f"Error saving weather summary: {e}")
