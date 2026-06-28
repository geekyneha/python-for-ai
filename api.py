import requests

# We need coordinates to get weather data

def get_weather(latitude, longitude):
# Build the API URL with our parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    response = requests.get(url)
    data = response.json()
    return data['current']['temperature_2m']


paris_weather = get_weather(48.8566, 2.3522)
london_weather = get_weather(51.5074, -0.1278)
austin_weather = get_weather(30.2672, -97.7431)

print(f"paris: {paris_weather}°C")
print(f"london: {london_weather}°C")
print(f"austin: {austin_weather}°C")

