"""reports

Revision ID: 75762afdac74
Revises: 3cd665853dda
Create Date: 2025-12-31 12:34:57.408636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75762afdac74'
down_revision: Union[str, Sequence[str], None] = '3cd665853dda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
