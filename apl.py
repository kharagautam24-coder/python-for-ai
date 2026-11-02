"""
import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)
data["current"]
"""
"""
import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)
pbr_temp=get_weather(21.64,69.60)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")
print(f"Porbandar: {pbr_temp}°C")
"""

import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os


# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)
print(today)
print(timedelta(days=7))
print(week_ago)
# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
print(start_date)
print(end_date)
# Get Porbandar weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=21.64&longitude=69.60&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(response)
print(data)

# Extract the daily data
daily_data = data['daily']
print(daily_data)
# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)

#-----------------------------------

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Porbandar Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()
#--------------------------------

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/porbandar_weather.csv', index=False)
print("Data saved to data/porbandar_weather.csv")