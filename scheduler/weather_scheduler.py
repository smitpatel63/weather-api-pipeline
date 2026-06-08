from apscheduler.schedulers.blocking import BlockingScheduler

from services.weather_service import fetch_weather
from services.weather_db_service import save_weather

cities = [
    "Ahmedabad",
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Surat",
    "Pune",
    "Hyderabad"
]

def collect_weather():

    print("Fetching weather data...")

    for city in cities:

        try:
            data = fetch_weather(city)

            save_weather(data)

            print(f"{city} saved successfully")

        except Exception as e:

            print(f"Error for {city}: {e}")

    print("All cities updated")


scheduler = BlockingScheduler()

scheduler.add_job(
    collect_weather,
    trigger="interval",
    minutes=10
)

print("Scheduler Started...")

collect_weather()

scheduler.start()