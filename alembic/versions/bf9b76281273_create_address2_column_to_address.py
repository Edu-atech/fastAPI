"""Create address2 column to address

Revision ID: bf9b76281273
Revises: 6ceebdbf66c5
Create Date: 2022-12-26 16:19:04.018352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bf9b76281273"
down_revision = "6ceebdbf66c5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("address2", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "address2")
