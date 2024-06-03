import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = '30d4741c779ba94c470ca1f63045390a'
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        weather_label.config(text="No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        weather_label.config(text=f"The weather in {city} is: {weather}\nThe temperature in {city} is: {temp}ºF")

# GUI setup
root = tk.Tk()
root.title("Weather App")

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=20)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, font=("Helvetica", 14))
weather_label.pack(pady=20)

root.mainloop()
