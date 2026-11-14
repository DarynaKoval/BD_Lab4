"""створення таблиці weather"""
from alembic import op
import sqlalchemy as sa

revision = "001"
down_revision = None
branch_labels = None
depends_on = None

WIND_DIRECTIONS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                   "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

MOON_PHASES = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
               "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]


def upgrade():
    op.create_table(
        "weather",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("country", sa.String(100), nullable=False),
        sa.Column("location_name", sa.String(100), nullable=False),
        sa.Column("last_updated", sa.DateTime, nullable=False),
        sa.Column("temperature_celsius", sa.Double),
        sa.Column("condition_text", sa.String(100)),
        sa.Column("wind_kph", sa.Double),
        sa.Column("wind_degree", sa.Integer),
        sa.Column("wind_direction", sa.Enum(*WIND_DIRECTIONS, name="wind_direction_enum")),
        sa.Column("sunrise", sa.Time),
        sa.Column("sunset", sa.Time),
        sa.Column("moonrise", sa.Time),
        sa.Column("moonset", sa.Time),
        sa.Column("moon_phase", sa.Enum(*MOON_PHASES, name="moon_phase_enum")),
        sa.Column("moon_illumination", sa.Integer),
    )
    op.create_index("ix_weather_country_date", "weather", ["country", "last_updated"])


def downgrade():
    op.drop_table("weather")
    # у PostgreSQL enum - окремі типи, їх треба видалити окремо
    if op.get_bind().dialect.name == "postgresql":
        op.execute("DROP TYPE IF EXISTS wind_direction_enum")
        op.execute("DROP TYPE IF EXISTS moon_phase_enum")