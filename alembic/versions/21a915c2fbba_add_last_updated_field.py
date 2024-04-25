"""add last updated field

Revision ID: 21a915c2fbba
Revises: dc070706b80a
Create Date: 2024-04-25 10:35:02.136306

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21a915c2fbba'
down_revision: str | None = 'dc070706b80a'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("gas_station", sa.Column("last_updated", sa.DateTime))

def downgrade() -> None:
    op.drop_column("gas_station", "last_updated")