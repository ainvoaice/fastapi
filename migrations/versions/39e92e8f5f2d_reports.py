"""reports

Revision ID: 39e92e8f5f2d
Revises: c5ea063d58e5
Create Date: 2025-12-31 12:39:33.830660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39e92e8f5f2d'
down_revision: Union[str, Sequence[str], None] = 'c5ea063d58e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
