"""create adoptions table

Revision ID: 812cc23b1d2f
Revises: 9779d7546329
Create Date: 2024-10-05 17:34:44.067371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '812cc23b1d2f'
down_revision: Union[str, None] = '9779d7546329'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "adoptions",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("adopter_id", sa.Integer, sa.ForeignKey("adopters.id"), nullable=False),
        sa.Column("pet_microchip", sa.String(15), sa.ForeignKey("pets.microchip"), nullable=False),
        sa.Column("start_date", sa.DateTime, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("end_date", sa.DateTime),
        sa.Column("end_reason", sa.Text),
        sa.Column("notes", sa.Text),
        sa.Column("volunteer_referent", sa.Integer, sa.ForeignKey("volunteers.id")),
        sa.Column("cash_offer", sa.Float)
    )


def downgrade() -> None:
    op.drop_table("adoptions")
