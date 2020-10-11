import requests
import json

url = "https://api.weather.gov/gridpoints/EWX/155,90/forecast"

response = requests.request("GET", url)

response_body = json.loads(response.text)

forecast_days = response_body['properties']['periods']

print("\n" +"*"*56)
print("*"*20 + "WEATHER FORECAST" + "*"*20)
print("*"*56 + "\n")

for i in forecast_days:
    time_frame = i['name']
    forecast = i['detailedForecast']
    print("Forecast for " + time_frame + " --- " + forecast + "\n")

