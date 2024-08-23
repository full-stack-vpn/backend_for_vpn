"""users_table

Revision ID: f33ae1dacf38
Revises: f7953e78084a
Create Date: 2024-08-23 17:59:45.404179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f33ae1dacf38'
down_revision: Union[str, None] = 'f7953e78084a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
