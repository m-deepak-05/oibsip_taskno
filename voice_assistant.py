import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import subprocess
import smtplib
import wikipedia
import requests
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to recognize speech and return it as text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        return ""

# Function to open applications
def open_application(command):
    app_name = command.replace('open', '').strip()
    try:
        if os.name == 'nt':  # Windows
            os.system(f'start {app_name}')
        elif os.name == 'posix':  # MacOS/Linux
            subprocess.Popen(['open', '-a', app_name])
    except Exception as e:
        speak(f"Failed to open {app_name}. {str(e)}")

# Function to open websites
def open_website(command):
    website_name = command.replace('open', '').replace('website', '').strip()
    if not website_name.startswith('http://') and not website_name.startswith('https://'):
        website_name = 'http://' + website_name
    webbrowser.open(website_name)

# Function to get current date and time
def get_date_time():
    now = datetime.now()
    date = now.strftime("%B %d, %Y")
    time = now.strftime("%H:%M:%S")
    return date, time

# Function to send email
def send_email(subject, body, to_email):
    try:
        email = 'your_email@example.com'
        password = 'your_password'
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, to_email, text)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Failed to send email. {str(e)}")

# Function to get weather updates
def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] == 200:
        main = data["main"]
        temperature = main["temp"]
        weather_description = data["weather"][0]["description"]
        weather_info = f"The temperature in {city} is {temperature}°C with {weather_description}."
        speak(weather_info)
    else:
        speak("City not found.")

# Function to answer general knowledge questions
def answer_question(question):
    try:
        summary = wikipedia.summary(question, sentences=2)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for this question. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find an answer to that question.")

# Function to control smart home devices (dummy implementation)
def control_smart_home(command):
    speak(f"Executing smart home command: {command}")

# Main function to handle voice commands
def handle_command(command):
    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'what is your name' in command:
        speak("I am your voice assistant.")
    elif 'how are you' in command:
        speak("I'm just a program, but I'm here to help you!")
    elif 'open' in command and 'website' in command:
        open_website(command)
    elif 'open' in command:
        open_application(command)
    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif 'date' in command:
        date, _ = get_date_time()
        speak(f"Today's date is {date}.")
    elif 'time' in command:
        _, time = get_date_time()
        speak(f"The current time is {time}.")
    elif 'send email' in command:
        speak("What is the subject of the email?")
        subject = listen()
        speak("What should the body of the email say?")
        body = listen()
        speak("What is the recipient's email address?")
        to_email = listen()
        send_email(subject, body, to_email)
    elif 'set a reminder' in command:
        reminder = command.replace('set a reminder', '').strip()
        # Here you can implement actual reminder functionality using sched or APScheduler
        speak(f"Reminder set for: {reminder}")
    elif 'weather in' in command:
        city = command.replace('weather in', '').strip()
        get_weather(city)
    elif 'answer' in command:
        question = command.replace('answer', '').strip()
        answer_question(question)
    elif 'control' in command:
        control_smart_home(command)
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't catch that. Can you please repeat?")

# Main loop to continuously listen for commands
def main():
    speak("Voice assistant activated. How can I help you?")
    while True:
        command = listen()
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
