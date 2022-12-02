"""crerate user tabloes

Revision ID: e5d1fab78c68
Revises: 44706ff9d772
Create Date: 2022-11-29 10:59:55.246762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e5d1fab78c68"
down_revision = "44706ff9d772"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("user")
    pass
