import requests
import os

class WeatherFetcher:
    def __init__(self, cities):
        self.cities = cities
        self.api_key = os.getenv("OPENWEATHER_API_KEY")  # Ensure your API key is set in the environment
        self.last_error = None

    def fetch_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            self.last_error = None
            return response.json()
        else:
            self.last_error = response.status_code  # Store the error code for logging
            return None
