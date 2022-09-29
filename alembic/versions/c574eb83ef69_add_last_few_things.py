"""add last few things

Revision ID: c574eb83ef69
Revises: 002467a24734
Create Date: 2022-09-29 16:01:30.152610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c574eb83ef69'
down_revision = '002467a24734'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
