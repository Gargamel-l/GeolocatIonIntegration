import requests
from geopy.geocoders import Nominatim

def get_location_by_ip(ip=""):
    # Используем ipinfo.io для получения геоданных по IP
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data['loc']

def get_address_by_location(location):
    # Используем Nominatim Geocoder для получения адреса по координатам
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(location, language="en")
    return location.address

# Пример использования с вашим IP (или можно указать конкретный IP как строку)
ip = ""  # Оставьте пустым для автоматического определения IP текущего пользователя
location = get_location_by_ip(ip)
address = get_address_by_location(location)

print(f"Location coordinates: {location}")
print(f"Address: {address}")

