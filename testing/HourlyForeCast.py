import requests

api_key = "11325083bbb01d1d714248698ef5deee"

city_name = str(input("Enter city name: ")).lower()
lat = str(input("Enter latitude: "))
lon = str(input("Enter longitude: "))

url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)

if (response.status_code == 200):
    data = response.json()
    print(data)
