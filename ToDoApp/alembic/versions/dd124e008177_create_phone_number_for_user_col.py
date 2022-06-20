"""create phone number for user col

Revision ID: dd124e008177
Revises:
Create Date: 2022-06-20 14:29:05.549326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd124e008177'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column(
            'phone_number',
            sa.String(),
            nullable=True
        )
    )


def downgrade() -> None:
    op.drop_column(
        'users',
        'phone_number'
    )
