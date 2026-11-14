"""ORM-моделі таблиць"""
from sqlalchemy import Column, DateTime, Double, Enum, Integer, String, Time
from sqlalchemy.orm import DeclarativeBase

WIND_DIRECTIONS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                   "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

MOON_PHASES = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
               "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]


class Base(DeclarativeBase):
    pass


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(100), nullable=False)          # текст
    location_name = Column(String(100), nullable=False)    # текст
    last_updated = Column(DateTime, nullable=False)        # дата
    temperature_celsius = Column(Double)                   # дробне
    condition_text = Column(String(100))                   # текст
    wind_kph = Column(Double)                              # дробне
    wind_degree = Column(Integer)                          # ціле
    wind_direction = Column(Enum(*WIND_DIRECTIONS, name="wind_direction_enum"))  # enum

    # варіант 4: схід і захід небесних тіл
    sunrise = Column(Time)                                 # час
    sunset = Column(Time)                                  # час
    moonrise = Column(Time)                                # час
    moonset = Column(Time)                                 # час
    moon_phase = Column(Enum(*MOON_PHASES, name="moon_phase_enum"))  # enum
    moon_illumination = Column(Integer)                    # ціле, %