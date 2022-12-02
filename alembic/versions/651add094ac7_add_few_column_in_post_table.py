"""add few column in post table

Revision ID: 651add094ac7
Revises: bd1786f23c8e
Create Date: 2022-11-29 11:22:11.670690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "651add094ac7"
down_revision = "bd1786f23c8e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "post",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "post",
        sa.Column(
            "create_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("post", "published")
    op.drop_column("post", "create_at")
    pass
