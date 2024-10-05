"""create user table

Revision ID: ab45033f2a84
Revises: 32fdc07746bd
Create Date: 2024-10-04 19:51:36.207660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab45033f2a84'
down_revision: Union[str, None] = '32fdc07746bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("first_name", sa.String(20), nullable=False),
        sa.Column("last_name", sa.String(20), nullable=False),
        sa.Column("birthdate", sa.DateTime, nullable=False),
        sa.Column("cf", sa.String(16), nullable=False),
        sa.Column("address", sa.String(30), nullable=False),
        sa.Column("city", sa.String(30), nullable=False),
        sa.Column("cap", sa.Integer, nullable=True, server_default=None),
        sa.Column("state", sa.String(20), nullable=True, server_default=None),
        sa.Column("telephone", sa.Integer, nullable=True, server_default=None),
        sa.Column("email", sa.String(30), nullable=True, server_default=None),
        sa.Column("documents", sa.Integer, nullable=True, server_default=None)
    )
# first_name, last_name, birthday, sex, cf, street, cap, city, state, telephone, email, documents

def downgrade() -> None:
    op.drop_table("users")
