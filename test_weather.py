from services.weather_service import fetch_weather

data = fetch_weather("Ahmedabad")

city = data["name"]

temperature = data["main"]["temp"]

humidity = data["main"]["humidity"]

weather = data["weather"][0]["main"]

print("City:", city)
print("Temperature:", temperature)
print("Humidity:", humidity)
print("Weather:", weather)