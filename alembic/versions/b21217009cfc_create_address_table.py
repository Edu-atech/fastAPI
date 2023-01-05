"""Create address table

Revision ID: b21217009cfc
Revises: 51c823f00568
Create Date: 2022-12-26 11:12:24.525603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b21217009cfc"
down_revision = "51c823f00568"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("address1", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("country", sa.String(), nullable=False),
        sa.Column("postalcode", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("address")
