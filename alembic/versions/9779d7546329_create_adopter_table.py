"""create adopter table

Revision ID: 9779d7546329
Revises: dc311d44d7db
Create Date: 2024-10-05 17:24:53.392636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9779d7546329'
down_revision: Union[str, None] = 'dc311d44d7db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "adopters",
        sa.Column("id", sa.Integer, autoincrement=True, primary_key=True),
        sa.Column("previews_adoptions", sa.Integer, server_default="0", nullable=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("note", sa.Text, server_default=None, nullable=True),
        sa.Column("suited", sa.Enum("Yes", "No", "In progress"), server_default="In progress", nullable=False)
    )


def downgrade() -> None:
    op.drop_table("adopters")
