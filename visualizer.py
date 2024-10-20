import matplotlib.pyplot as plt
import pandas as pd

class WeatherVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_weather(self):
        # Check if there's valid data
        if not self.data:
            print("No valid weather data to visualize.")
            return
        
        # Create a DataFrame from the fetched data
        df = pd.DataFrame(self.data)

        # Check if the DataFrame is empty
        if df.empty:
            print("No data available for visualization.")
            return
        
        # Set the city names as the index for better display
        df.set_index('city', inplace=True)

        # Create a bar plot
        plt.figure(figsize=(12, 6))  # Increased figure size
        bars = plt.bar(df.index, df['temperature'], color='skyblue')

        # Add data labels on top of each bar
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.2, round(yval, 1), ha='center', va='bottom', fontsize=10)

        plt.title('Current Temperature in Cities', fontsize=16)  # Increased title font size
        plt.xlabel('Cities', fontsize=14)  # Increased label font size
        plt.ylabel('Temperature (°C)', fontsize=14)  # Increased label font size
        plt.xticks(rotation=45, fontsize=12)  # Rotate city names and set font size
        plt.yticks(fontsize=12)  # Set font size for y-ticks
        plt.grid(axis='y')  # Add grid for better readability
        plt.tight_layout()  # Adjust layout to make room for rotated labels
        plt.show()
