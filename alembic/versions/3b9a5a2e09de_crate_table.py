"""crate table

Revision ID: 3b9a5a2e09de
Revises: 
Create Date: 2022-09-02 22:17:27.655992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b9a5a2e09de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column(
        'id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
