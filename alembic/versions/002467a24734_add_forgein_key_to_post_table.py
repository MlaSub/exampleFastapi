"""add forgein-key to post table

Revision ID: 002467a24734
Revises: 76b58251014e
Create Date: 2022-09-29 15:54:36.945421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002467a24734'
down_revision = '76b58251014e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
