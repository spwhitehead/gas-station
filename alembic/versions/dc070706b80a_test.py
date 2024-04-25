"""test

Revision ID: dc070706b80a
Revises: 4e6546af4a2a
Create Date: 2024-04-25 09:54:36.314980

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc070706b80a'
down_revision: str | None = '4e6546af4a2a'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
