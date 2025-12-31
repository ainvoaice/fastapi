"""reports

Revision ID: 358bba366abb
Revises: 26a6e17bee90
Create Date: 2025-12-31 12:28:36.701811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '358bba366abb'
down_revision: Union[str, Sequence[str], None] = '26a6e17bee90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
