from datetime import datetime

from database.db import SessionLocal
from database.models import WeatherData


def save_weather(data):

    print("Received Data:")
    print(data)

    db = SessionLocal()

    weather_record = WeatherData(
        city=data["name"],
        temperature=data["main"]["temp"],
        humidity=data["main"]["humidity"],
        weather=data["weather"][0]["main"],
        fetched_at=datetime.now()
    )

    print("Weather Object Created")

    db.add(weather_record)

    print("Added To Session")

    db.commit()

    print("Committed To Database")

    db.close()

    print("Weather data saved!")