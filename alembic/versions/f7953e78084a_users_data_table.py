"""users_data_table

Revision ID: f7953e78084a
Revises: 
Create Date: 2024-08-23 17:55:57.864741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7953e78084a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'vpn_users',
        sa.Column('user_name', sa.String, primary_key=True),
        sa.Column('paid_or_free', sa.String),
        sa.Column('over_day', sa.String),
    )


def downgrade() -> None:
    op.drop_table('vpn_users')
