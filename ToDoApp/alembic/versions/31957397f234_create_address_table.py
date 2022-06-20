"""Create address table

Revision ID: 31957397f234
Revises: dd124e008177
Create Date: 2022-06-20 14:40:35.439316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31957397f234'
down_revision = 'dd124e008177'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'address',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False,
            primary_key=True
        ),
        sa.Column(
            'address1',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'address2',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'city',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'state',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'country',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'postalcode',
            sa.String(),
            nullable=False
        )
    )


def downgrade() -> None:
    op.drop_table('address')
