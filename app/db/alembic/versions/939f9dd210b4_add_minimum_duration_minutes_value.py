"""add minimum duration_minutes value

Revision ID: 939f9dd210b4
Revises: 01155ea2455c
Create Date: 2025-04-14 14:51:49.194718

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '939f9dd210b4'
down_revision: Union[str, None] = '01155ea2455c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
