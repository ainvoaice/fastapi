"""aiven

Revision ID: bac623da9d0a
Revises: ce3902d87b94
Create Date: 2025-12-31 11:10:37.538549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision: str = 'bac623da9d0a'
down_revision: Union[str, Sequence[str], None] = 'ce3902d87b94'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ---- groups -------------------------------------------------
    op.create_table(
        "groups",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("gen_random_uuid()"),
            primary_key=True,
        ),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
    )

    op.create_index(
        "ix_groups_active",
        "groups",
        ["is_deleted"],
        postgresql_where=sa.text("is_deleted = false"),
    )

    # ---- users --------------------------------------------------
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("gen_random_uuid()"),
            primary_key=True,
        ),
        sa.Column("name", sa.String(150), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("group_id", sa.UUID(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["groups.id"],
            name="fk_users_group_id_groups",
            ondelete="SET NULL",
        ),
        sa.UniqueConstraint("email", name="uq_users_email"),
    )

    op.create_index(
        "ix_users_active",
        "users",
        ["is_deleted"],
        postgresql_where=sa.text("is_deleted = false"),
    )

    op.create_index(
        "ix_users_group_id",
        "users",
        ["group_id"],
    )


def downgrade() -> None:
    # reverse order, exact undo
    op.drop_index("ix_users_group_id", table_name="users")
    op.drop_index("ix_users_active", table_name="users")
    op.drop_table("users")

    op.drop_index("ix_groups_active", table_name="groups")
    op.drop_table("groups")