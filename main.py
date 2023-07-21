import requests

api_key = "11325083bbb01d1d714248698ef5deee"

city = str(input("Enter city name: ")).lower()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Temperature: {round(temp - 273)} C")
    print(f"Description: {desc}")
else:
    print('Error fetching weather data')
