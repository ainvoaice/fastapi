"""reports

Revision ID: 3cd665853dda
Revises: e579f51379ad
Create Date: 2025-12-31 12:32:17.139445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cd665853dda'
down_revision: Union[str, Sequence[str], None] = 'e579f51379ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
