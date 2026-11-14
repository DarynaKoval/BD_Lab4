"""ORM-моделі таблиць"""
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Boolean, Column, DateTime, Double, Enum, ForeignKey, Integer, String, Time

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

    astronomy = relationship("Astronomy", back_populates="weather", uselist=False)


class Astronomy(Base):
    """варіант 4: схід і захід небесних тіл"""
    __tablename__ = "astronomy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    weather_id = Column(Integer, ForeignKey("weather.id"), nullable=False, unique=True)
    sunrise = Column(Time)                                 # час
    sunset = Column(Time)                                  # час
    moonrise = Column(Time)                                # час
    moonset = Column(Time)                                 # час
    moon_phase = Column(Enum(*MOON_PHASES, name="moon_phase_enum"))  # enum
    moon_illumination = Column(Integer)                    # ціле, %
    go_outside = Column(Boolean, nullable=False)           # "Чи варто виходити на вулицю"

    weather = relationship("Weather", back_populates="astronomy")