# weather_monitoring_system
 The Weather Monitoring System is a Python-based application that fetches current weather data for multiple cities using the OpenWeatherMap API and visualizes the data using a bar graph. The graph shows the temperature for each city, making it easier to monitor weather conditions across various locations.

Features
Fetches real-time weather data for multiple cities using the OpenWeatherMap API.
Displays weather information such as temperature, humidity, and weather description.
Visualizes temperature data in a bar chart using matplotlib.
Automatically refreshes the data every 5 minutes to keep it up-to-date.
Prerequisites
Before running the project, ensure you have the following installed on your machine:

Python 3.8+
Pip (Python package manager)
Dependencies
The project requires the following Python packages. You can install them by running the following command:

pip install -r requirements.txt
requirements.txt file content:

matplotlib
pandas
requests
Individual Package Installation
Alternatively, you can install the packages individually:

pip install matplotlib pandas requests
Getting Started

Follow the steps below to get the project running on your local machine.


2. Set up OpenWeatherMap API
The project requires an API key from OpenWeatherMap to fetch weather data.

Set the API key as an environment variable on your machine:
For Windows (Command Prompt):
set OPENWEATHER_API_KEY=API_KEY = 'ba4ab86356d1639a452998c797de7923'

3. Running the Application
After setting up the environment and installing dependencies, you can run the project:
python main.py

4. How It Works
Weather Data Fetching: The application fetches weather data for a list of predefined cities (e.g., Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) from OpenWeatherMap. The fetched data includes city name, temperature, humidity, and weather description.

Visualization: After successfully fetching data, the temperatures for all cities are visualized in a bar graph where each bar represents a city's temperature.

Automatic Refresh: The system automatically updates the weather data every 5 minutes by default (this can be modified in the code).

Project Structure
.
├── main.py               # Main entry point of the application
├── visualizer.py          # Visualization module using matplotlib
├── requirements.txt       # List of project dependencies
└── README.md              # Project documentation (this file)

main.py
Responsible for fetching weather data from the OpenWeatherMap API.
Coordinates the flow of fetching and visualizing data.
Runs in a loop to update data periodically.

visualizer.py
Handles the visualization of weather data using matplotlib.
Takes the fetched data, processes it into a Pandas DataFrame, and creates a bar chart.

Customization
Adding More Cities
To add more cities, simply modify the CITIES list in main.py:
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
You can replace the city names with any city of your choice as long as it is supported by the OpenWeatherMap API.

Change the Refresh Interval
By default, the weather data is refreshed every 5 minutes (300 seconds). You can change this value by modifying the following line in main.py:

python
time.sleep(300)  # Change 300 to any number of seconds

