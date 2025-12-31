"""aiven

Revision ID: 26a6e17bee90
Revises: bac623da9d0a
Create Date: 2025-12-31 11:38:28.832387

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26a6e17bee90'
down_revision: Union[str, Sequence[str], None] = 'bac623da9d0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
