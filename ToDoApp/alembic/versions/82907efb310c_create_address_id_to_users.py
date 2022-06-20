"""create address_id to users

Revision ID: 82907efb310c
Revises: 31957397f234
Create Date: 2022-06-20 15:21:26.611032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82907efb310c'
down_revision = '31957397f234'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column(
            'address_id',
            sa.Integer(),
            nullable=True
        )
    )

    op.create_foreign_key(
        'address_users_fk',
        source_table="users",
        referent_table="address",
        local_cols=['address_id'],
        remote_cols=["id"],
        ondelete="CASCADE"
    )


def downgrade() -> None:
    op.drop_constraint(
        'address_users_fk',
        table_name="users"
    )

    op.drop_column('users', 'address_id')
