"""add apt num column

Revision ID: 97a19d88eb72
Revises: 82907efb310c
Create Date: 2022-06-20 16:03:27.202803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97a19d88eb72'
down_revision = '82907efb310c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'address',
        sa.Column(
            'apt_num',
            sa.Integer(),
            nullable=True
        )
    )


def downgrade() -> None:
    op.drop_column(
        'address',
        'apt_num'
    )
