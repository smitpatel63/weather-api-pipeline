from services.weather_service import fetch_weather
from services.weather_db_service import save_weather

data = fetch_weather("Ahmedabad")

save_weather(data)