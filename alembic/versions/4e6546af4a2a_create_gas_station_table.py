"""create gas station table

Revision ID: 4e6546af4a2a
Revises: 
Create Date: 2024-04-25 09:29:10.862217

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e6546af4a2a'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("gas_station", 
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("name", sa.Text, nullable=False),
                    sa.Column("location", sa.String))


def downgrade() -> None:
    op.drop_table("gas_station")