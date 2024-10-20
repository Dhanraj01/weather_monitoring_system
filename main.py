import time
import requests
from visualizer import WeatherVisualizer

API_KEY = 'ba4ab86356d1639a452998c797de7923'
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

class WeatherFetcher:
    def __init__(self):
        self.visualizer = None

    def fetch_weather_data(self):
        weather_data = []
        
        print("Fetching weather data...")
        for city in CITIES:
            try:
                WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=ba4ab86356d1639a452998c797de7923&units=metric"
                response = requests.get(WEATHER_URL)
                response.raise_for_status()  # Raise an error for bad responses
                data = response.json()

                if data['cod'] == 200:  # Check if the response is successful
                    city_weather = {
                        'city': data['name'],
                        'temperature': data['main']['temp'],
                        'humidity': data['main']['humidity'],
                        'description': data['weather'][0]['description']
                    }
                    weather_data.append(city_weather)
                    print(f"Fetched data for {city}: {city_weather}")
                else:
                    print(f"Error fetching data for {city}: {data['cod']}")
            except Exception as e:
                print(f"Error fetching data for {city}: {e}")

        return weather_data

    def visualize_weather(self, weather_data):
        self.visualizer = WeatherVisualizer(weather_data)
        self.visualizer.plot_weather()

def main():
    weather_fetcher = WeatherFetcher()
    
    while True:
        weather_data = weather_fetcher.fetch_weather_data()
        if weather_data:
            weather_fetcher.visualize_weather(weather_data)
        else:
            print("No weather data available for visualization.")
        time.sleep(300)  # Wait for 5 minutes

if __name__ == "__main__":
    main()
