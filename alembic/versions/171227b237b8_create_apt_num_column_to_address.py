"""Create apt_num column to Address

Revision ID: 171227b237b8
Revises: bf9b76281273
Create Date: 2022-12-26 17:54:43.002695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "171227b237b8"
down_revision = "bf9b76281273"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
