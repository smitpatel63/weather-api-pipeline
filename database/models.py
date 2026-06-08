from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WeatherData(Base):

    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True)

    city = Column(String, nullable=False)

    temperature = Column(Float)

    humidity = Column(Integer)

    weather = Column(String)

    fetched_at = Column(DateTime)