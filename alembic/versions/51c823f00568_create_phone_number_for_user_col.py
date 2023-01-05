"""create phone number for user col

Revision ID: 51c823f00568
Revises: 
Create Date: 2022-12-26 10:41:23.891466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "51c823f00568"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
