"""Initial migration

Revision ID: dbc8e852aad7
Revises: 6cf03819bf51
Create Date: 2025-02-11 18:31:50.652261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbc8e852aad7'
down_revision: Union[str, None] = '6cf03819bf51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('rooms_quantity', sa.Integer(), nullable=False))
    op.drop_column('hotels', 'room_quantity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('room_quantity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('hotels', 'rooms_quantity')
    # ### end Alembic commands ###
