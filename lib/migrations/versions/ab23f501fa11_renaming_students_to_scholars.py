"""Renaming students to scholars

Revision ID: ab23f501fa11
Revises: 791279dd0760
Create Date: 2023-06-05 00:03:16.658271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab23f501fa11'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
