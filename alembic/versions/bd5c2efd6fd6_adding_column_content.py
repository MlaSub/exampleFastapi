"""adding column content

Revision ID: bd5c2efd6fd6
Revises: 3b9a5a2e09de
Create Date: 2022-09-02 22:50:34.559765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd5c2efd6fd6'
down_revision = '3b9a5a2e09de'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
