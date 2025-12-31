"""reports

Revision ID: e579f51379ad
Revises: 358bba366abb
Create Date: 2025-12-31 12:30:51.937889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e579f51379ad'
down_revision: Union[str, Sequence[str], None] = '358bba366abb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
