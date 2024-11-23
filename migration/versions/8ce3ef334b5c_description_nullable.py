"""description nullable

Revision ID: 8ce3ef334b5c
Revises: 1b8db8759f45
Create Date: 2024-11-22 22:02:26.656537

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8ce3ef334b5c"
down_revision: Union[str, None] = "1b8db8759f45"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("task", "description", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("task", "description", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
