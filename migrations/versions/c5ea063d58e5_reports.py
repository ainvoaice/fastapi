"""reports

Revision ID: c5ea063d58e5
Revises: 75762afdac74
Create Date: 2025-12-31 12:35:42.562182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5ea063d58e5'
down_revision: Union[str, Sequence[str], None] = '75762afdac74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
