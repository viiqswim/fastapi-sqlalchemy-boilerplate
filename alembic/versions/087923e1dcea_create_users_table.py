"""Create users table

Revision ID: 087923e1dcea
Revises: 
Create Date: 2023-04-06 20:30:02.192615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '087923e1dcea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", name="uq_users_name"),
    )


def downgrade() -> None:
    op.drop_table("users")
