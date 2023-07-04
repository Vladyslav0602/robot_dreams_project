# Exercise 1
import random
import requests
from geopy.geocoders import Nominatim

websites = [
    "http://www.google.com",
    "http://www.facebook.com",
    "http://www.twitter.com",
    "http://www.amazon.com",
    "http://www.apple.com"
]

# Випадково вибираємо сайт зі списку
random_website = random.choice(websites)

# Виконуємо запит до вибраного сайту
response = requests.get(random_website)

# Виводимо статус-код, назву сайту та довжину HTML-коду відповіді
print("Статус-код:", response.status_code)
print("Сайт:", random_website)
print("Довжина HTML-коду:", len(response.text))


# Exercise 2
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.geocode(city_name)
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None, None


def get_weather(latitude, longitude):
    response = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": "true"
        }
    )
    data = response.json()
    current_weather = data.get("current_weather", {})
    return current_weather


city_name = input("Введіть назву міста: ")
latitude, longitude = get_coordinates(city_name)

if latitude is not None and longitude is not None:
    print("Координати міста", city_name)
    print("Широта:", latitude)
    print("Довгота:", longitude)

    current_weather = get_weather(latitude, longitude)
    if current_weather:
        print("Поточна погода:")
        print("Температура:", current_weather.get("temperature"), "°C")
        print("Швидкість вітру:", current_weather.get("windspeed"), "м/с")
        print("Стан неба:", current_weather.get("weathercode"))
        print("Напрямок вітру:", current_weather.get("winddirection"))
    else:
        print("Не вдалося отримати дані погоди.")
else:
    print("Координати для міста", city_name, "не знайдені.")
