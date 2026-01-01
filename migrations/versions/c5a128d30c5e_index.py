"""index

Revision ID: c5a128d30c5e
Revises: e986db83be2c
Create Date: 2026-01-01 10:40:23.822412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5a128d30c5e'
down_revision: Union[str, Sequence[str], None] = 'e986db83be2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
