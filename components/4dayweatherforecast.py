import requests

api_key = "11325083bbb01d1d714248698ef5deee"
city_name = str(input("Enter city name: ")).lower()
url=f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}"

