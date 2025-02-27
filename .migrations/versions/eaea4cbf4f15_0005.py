"""0005

Revision ID: eaea4cbf4f15
Revises: e40b11aec317
Create Date: 2025-02-03 21:14:25.616737

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "eaea4cbf4f15"
down_revision: Union[str, None] = "e40b11aec317"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("maintenance_steps", "status")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "maintenance_steps",
        sa.Column("status", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###
