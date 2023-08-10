import requests

api_key = "11325083bbb01d1d714248698ef5deee"
city_name = str(input("Enter city name: ")).lower()
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"

response = requests.get(url)

try:
    if (response.status_code == 200):
        data = response.json()
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        country = data[0]["country"]
        state = data[0]["state"]
        print(f"Latitude: {abs(lat)}")
        print(f"Longitude: {abs(lon)}")
        print(f"Country: {country}")
        print(f"State: {state}")
except:
    if (response.status_code == 200):
        data = response.json()
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        country = data[0]["country"]
        print(f"Latitude: {abs(lat)}")
        print(f"Longitude: {abs(lon)}")
        print(f"Country: {country}")
