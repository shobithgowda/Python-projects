import streamlit as st
import requests
from datetime import datetime

# Function to fetch current weather data for a given city
def get_weather_data(city, api_key):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching weather data.")
        return None

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

# Function to display weather data
def display_weather_data(data):
    if data:
        st.subheader("Current Weather Conditions:")
        st.write(f"Location: {data['location']['name']}, {data['location']['country']}")
        st.write(f"Local Time: {data['location']['localtime']}")
        st.write(f"Temperature: {data['current']['temp_c']}°C / {celsius_to_fahrenheit(data['current']['temp_c'])}°F")
        st.write(f"Weather: {data['current']['condition']['text']}")
        st.write(f"Humidity: {data['current']['humidity']}%")
        st.write(f"Wind Speed: {data['current']['wind_kph']} km/h")
    else:
        st.warning("No weather data available.")

# Main function
def main():
    st.title("Weather App")
    api_key = "b13989793f184149a91141538230103"  # Replace with your Weather API key
    city = st.text_input("Enter city name:", "New York")

    if st.button("Get Weather"):
        # Fetch and display current weather data
        current_weather_data = get_weather_data(city, api_key)
        display_weather_data(current_weather_data)

if __name__ == "__main__":
    main()
