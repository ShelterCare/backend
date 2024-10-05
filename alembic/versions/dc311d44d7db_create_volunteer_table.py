"""create volunteer table

Revision ID: dc311d44d7db
Revises: ab45033f2a84
Create Date: 2024-10-05 16:52:21.541526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc311d44d7db'
down_revision: Union[str, None] = 'ab45033f2a84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "volunteers",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("volunteer_id", sa.String(20), nullable=True, server_default=None, unique=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("start_date", sa.DateTime, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("end_date", sa.DateTime, nullable=True),
        sa.Column("team_leader", sa.Boolean, server_default="0", nullable=False),
        sa.Column("disponibility_days", sa.Integer, server_default="1", nullable=True)
    )


def downgrade() -> None:
    op.drop_table("volunteers")
