

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import json
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Speech recognition service failed.")
            return ""

def basic_commands(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {date}")
    elif "search" in command:
        search_query = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Here are the search results for {search_query}")

def get_weather(command):
    if "weather" in command:
        city = command.replace("weather in", "").strip()
        api_key = os.getenv("OPENWEATHER_API_KEY")  
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url).json()
            if response.get("main"):
                temp = response['main']['temp']
                desc = response['weather'][0]['description']
                speak(f"The weather in {city} is {desc} with a temperature of {temp}°C.")
            else:
                speak("I could not find the weather for that location.")
        except:
            speak("Failed to fetch weather data.")


def custom_commands(command):
    commands = {
        "play music": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "open github": "https://github.com"
    }
    for key in commands:
        if key in command:
            webbrowser.open(commands[key])
            speak(f"Opening {key}")


def run_assistant():
    speak("Voice assistant is ready.")
    while True:
        command = take_command()
        if command == "":
            continue
        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        basic_commands(command)
        get_weather(command)
        custom_commands(command)
if __name__ == "__main__":
    run_assistant()