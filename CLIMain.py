import CustomFunction as cf
import APIfunction as AP

print("Welcome to SkySync AI . I'm your weather assistant . Choose the Following Options: \n 1.Air Pollution \n 2.Geolocation \n 3.Statistical Weather Data , \n 4.History Bulk \n 5.Just History \n 6.Road Risk \n 7.(5 Day / 3hr weather Forecast)\n 8.Current Weather Data \n 9.Global Weather Alerts \n 10.Daily Forecasts 16 Days ")

firstStage = cf.options()

if (firstStage == 1):
    print(f"Ok you have entered Air Pollution option")
    np = cf.UserInput()
    lat, long = AP.LatAndLong(np)
    aqi, othSubstances = AP.AirPollution(lat, long)
    if (aqi == 1):
        print(f"Air quality of {np} is {aqi} which is Good")
    elif (aqi == 2):
        print(f"Air quality of {np} is {aqi} is Fair")
    elif (aqi == 3):
        print(f"Air quality of {np} is {aqi} Moderate")
    elif (aqi == 4):
        print(f"Air quality of {np} is {aqi }Poor")
    elif (aqi == 5):
        print(f"Air quality of {np} is {aqi} Very Poor")        
elif (firstStage == 2):
    print("2")
elif (firstStage == 3):
    print("3")
elif (firstStage == 4):
    print("4")
elif (firstStage == 5):
    print("5")
elif (firstStage == 6):
    print("6")
elif (firstStage == 7):
    print("7")
elif (firstStage == 8):
    print("8")
elif (firstStage == 9):
    print("9")
elif (firstStage == 10):
    print("10")
else:
    print("You are entering wrong option try again")
