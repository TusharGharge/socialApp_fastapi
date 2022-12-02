"""add vote table

Revision ID: e3c941119be8
Revises: f5df1b42726d
Create Date: 2022-11-29 12:03:57.519506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e3c941119be8"
down_revision = "f5df1b42726d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "votess",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["post_id"], ["posts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "post_id"),
    )
    pass


def downgrade() -> None:
    op.drop_table("votess")
    pass
