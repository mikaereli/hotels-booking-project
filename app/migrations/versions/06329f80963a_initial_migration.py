"""Initial migration

Revision ID: 06329f80963a
Revises: dbc8e852aad7
Create Date: 2025-02-11 18:34:05.224380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06329f80963a'
down_revision: Union[str, None] = 'dbc8e852aad7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('bookings_room_id_fkey', 'bookings', type_='foreignkey')
    op.create_foreign_key(None, 'bookings', 'rooms', ['room_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bookings', type_='foreignkey')
    op.create_foreign_key('bookings_room_id_fkey', 'bookings', 'hotels', ['room_id'], ['id'])
    # ### end Alembic commands ###
