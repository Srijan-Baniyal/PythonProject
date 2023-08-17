import requests


def LatAndLong(city_name):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid=5979ac965bd6b9af8edf18bfb013c660"
    response = requests.get(url)

    try:
        if (response.status_code == 200):
            data = response.json()
            lat = data[0]["lat"]
            long = data[0]["lon"]
            country = data[0]["country"]
            state = data[0]["state"]
            print(f"Latitude: {abs(lat)}")
            print(f"Longitude: {abs(long)}")
            print(f"Country: {country}")
            print(f"State: {state}")
            return lat, long
    except:
        data = response.json()
        lat = data[0]["lat"]
        long = data[0]["lon"]
        country = data[0]["country"]
        print(f"Latitude: {abs(lat)}")
        print(f"Longitude: {abs(long)}")
        print(f"Country: {country}")
        print(f"State: Not a state")
        return lat, long


def AirPollution(lat, long):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={long}&appid=5979ac965bd6b9af8edf18bfb013c660"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        return data["list"][0]["main"]["aqi"], data["list"][0]["components"]
    else:
        print("Look like something went wrong in my end try again")


def StatsAirYearlyProgression(lat, lon):
    url = f"http://history.openweathermap.org/data/2.5/aggregated/year?lat={lat}&lon={lon}&appid=5979ac965bd6b9af8edf18bfb013c660"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        return data
    else:
        print("Look like something went wrong in my end try again")
