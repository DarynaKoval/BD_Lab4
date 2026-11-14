"""колонка go_outside ("Чи варто виходити на вулицю")"""
from alembic import op
import sqlalchemy as sa

revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None

# так - якщо світло (між сходом і заходом сонця)
# так - якщо ніч, але місяць освітлений >= 75 %
# ні  - в інших випадках
FILL_SQL = """
UPDATE astronomy
SET go_outside = CASE
    WHEN (SELECT CAST(w.last_updated AS TIME) FROM weather w WHERE w.id = astronomy.weather_id)
         BETWEEN sunrise AND sunset THEN TRUE
    WHEN moon_illumination >= 75 THEN TRUE
    ELSE FALSE
END
"""


def upgrade():
    op.add_column("astronomy", sa.Column("go_outside", sa.Boolean, nullable=True))

    op.execute(FILL_SQL)

    op.alter_column("astronomy", "go_outside", existing_type=sa.Boolean, nullable=False)


def downgrade():
    op.drop_column("astronomy", "go_outside")