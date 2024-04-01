import requests
from datetime import datetime

# Function to fetch current weather data for a given city
def get_weather_data(city, api_key):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

# Function to fetch forecast data for a given city
def get_forecast_data(city, api_key):
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching forecast data.")
        return None

# Function to fetch weather data based on geolocation
def get_weather_by_geolocation(latitude, longitude, api_key):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude},{longitude}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data based on geolocation.")
        return None

# Function to fetch historical weather data for a given city and date
def get_historical_weather_data(city, date, api_key):
    url = f"https://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={date}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching historical weather data.")
        return None

# Function to fetch weather alerts for a given city
def get_weather_alerts(city, api_key):
    url = f"https://api.weatherapi.com/v1/alert.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("No weather alerts for this location.")
        return None

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

# Function to display weather data
def display_weather_data(data):
    if data:
        print("\nCurrent Weather Conditions:")
        print("---------------------------")
        print(f"Location: {data['location']['name']}, {data['location']['country']}")
        print(f"Local Time: {data['location']['localtime']}")
        print(f"Temperature: {data['current']['temp_c']}°C / {celsius_to_fahrenheit(data['current']['temp_c'])}°F")
        print(f"Weather: {data['current']['condition']['text']}")
        print(f"Humidity: {data['current']['humidity']}%")
        print(f"Wind Speed: {data['current']['wind_kph']} km/h")
    else:
        print("No weather data available.")

# Main function
def main():
    api_key = "b13989793f184149a91141538230103"  # Replace with your Weather API key
    city = input("Enter city name: ")
    
    # Fetch and display current weather data
    current_weather_data = get_weather_data(city, api_key)
    display_weather_data(current_weather_data)

    # Fetch and display forecast data
    forecast_data = get_forecast_data(city, api_key)
    if forecast_data:
        print("\nWeather Forecast:")
        print("-----------------")
        for day in forecast_data['forecast']['forecastday']:
            date = day['date']
            avg_temp_c = day['day']['avgtemp_c']
            avg_temp_f = celsius_to_fahrenheit(avg_temp_c)
            condition = day['day']['condition']['text']
            print(f"Date: {date}, Average Temperature: {avg_temp_c}°C / {avg_temp_f}°F, Weather: {condition}")
    else:
        print("No forecast data available.")

    # Fetch and display weather alerts
    weather_alerts = get_weather_alerts(city, api_key)
    if weather_alerts:
        print("\nWeather Alerts:")
        print("---------------")
        for alert in weather_alerts['alerts']:
            print(f"Alert: {alert['event']}, {alert['headline']}, {alert['description']}")
    else:
        print("No weather alerts for this location.")

    # Fetch and display historical weather data for yesterday
    yesterday = datetime.now().strftime("%Y-%m-%d")
    historical_weather_data = get_historical_weather_data(city, yesterday, api_key)
    if historical_weather_data:
        print("\nHistorical Weather Data (Yesterday):")
        print("-------------------------------------")
        print(f"Date: {yesterday}")
        print(f"Max Temperature: {historical_weather_data['forecast']['forecastday'][0]['day']['maxtemp_c']}°C")
        print(f"Min Temperature: {historical_weather_data['forecast']['forecastday'][0]['day']['mintemp_c']}°C")
    else:
        print("No historical weather data available.")

    # Fetch and display weather data based on geolocation (latitude and longitude)
    # Note: Requires geolocation coordinates as input
    #latitude = input("Enter latitude: ")
    #longitude = input("Enter longitude: ")
    #weather_by_geolocation = get_weather_by_geolocation(latitude, longitude, api_key)
    #display_weather_data(weather_by_geolocation)

if __name__ == "__main__":
    main()
