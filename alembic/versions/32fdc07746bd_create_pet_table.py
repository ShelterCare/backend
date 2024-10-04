"""create pet table

Revision ID: 32fdc07746bd
Revises: 
Create Date: 2024-10-04 19:05:43.182841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32fdc07746bd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pet",
        sa.Column("microchip", sa.String(15), primary_key=True),
        sa.Column("name", sa.String(30), nullable=False),
        sa.Column("birth", sa.DateTime, nullable=False),
        sa.Column("death", sa.DateTime, nullable=True, server_default=None),
        sa.Column("sex", sa.Enum("M", "F", name="sex_enum"), nullable=False),
        sa.Column("breed", sa.String(20), nullable=False, server_default="Meticcio"),
        sa.Column("fur_color", sa.String(20), nullable=False),
        sa.Column("fur_length", sa.Enum("Short", "Medium", "Long", name="fur_length_enum"), nullable=False),
        sa.Column("health_record", sa.String(30), nullable=True, server_default=None),
        sa.Column("size", sa.Enum("XS", "X/M", "M", "M/L", "L", "XL", name="size_enum"), nullable=False),
        sa.Column("sterilized", sa.Boolean, nullable=True)
    )


def downgrade() -> None:
    op.drop_table("pet")
