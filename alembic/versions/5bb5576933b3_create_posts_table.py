"""create posts table

Revision ID: 5bb5576933b3
Revises:
Create Date: 2022-11-29 10:17:12.006764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5bb5576933b3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
