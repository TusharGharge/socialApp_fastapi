"""add column in created tables

Revision ID: 44706ff9d772
Revises: 5bb5576933b3
Create Date: 2022-11-29 10:51:14.519983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "44706ff9d772"
down_revision = "5bb5576933b3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("post", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("post", "content")
    pass
