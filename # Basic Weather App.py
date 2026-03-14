# Basic Weather App
# Python Project

import requests

# Enter your API key here
API_KEY = "YOUR_API_KEY"

def get_weather(city):
    # API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if city exists
        if data["cod"] != 200:
            print("City not found. Please try again.")
            return

        # Extract weather information
        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # Display weather information
        print("\n------ Weather Information ------")
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {condition}")
        print(f"Wind Speed: {wind_speed} m/s")
        print("---------------------------------")

    except requests.exceptions.RequestException:
        print("Error connecting to weather service.")


def main():
    print("Welcome to the Basic Weather App\n")

    while True:
        city = input("Enter city name (or type 'exit' to quit): ")

        if city.lower() == "exit":
            print("Thank you for using the Weather App!")
            break

        if city.strip() == "":
            print("Please enter a valid city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()