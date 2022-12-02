"""add forehin key to user table
`
Revision ID: bd1786f23c8e
Revises: e5d1fab78c68
Create Date: 2022-11-29 11:13:08.088525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bd1786f23c8e"
down_revision = "e5d1fab78c68"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("post", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_user_fk",
        source_table="post",
        referent_table="user",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("posts_user_fk", table_name="post")
    op.drop_column("post", "owner_id")
    pass
