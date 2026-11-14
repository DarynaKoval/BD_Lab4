import os
from pathlib import Path
from urllib.parse import quote

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

PG_PASSWORD = quote(os.getenv("POSTGRES_PASSWORD", ""), safe="")
MYSQL_PASSWORD = quote(os.getenv("MYSQL_PASSWORD", ""), safe="")

POSTGRES_URL = f"postgresql+psycopg2://postgres:{PG_PASSWORD}@localhost:5432/weather_v4"
MYSQL_URL = f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost:3306/weather_v4?charset=utf8mb4"

if os.getenv("DB") == "mysql":
    DATABASE_URL = MYSQL_URL
else:
    DATABASE_URL = POSTGRES_URL

CSV_PATH = PROJECT_ROOT / "GlobalWeatherRepository.csv"