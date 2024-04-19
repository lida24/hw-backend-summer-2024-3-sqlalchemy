"""Update table themes

Revision ID: 2af1e9ea6c80
Revises: 2b60ba1f53a3
Create Date: 2024-04-19 17:57:45.229842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2af1e9ea6c80'
down_revision: Union[str, None] = '2b60ba1f53a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('title', sa.String(length=120), nullable=False))
    op.add_column('answers', sa.Column('is_correct', sa.Boolean(), nullable=False))
    op.create_unique_constraint(None, 'answers', ['title'])
    op.add_column('questions', sa.Column('title', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'questions', ['title'])
    op.add_column('themes', sa.Column('title', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'themes', ['title'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'themes', type_='unique')
    op.drop_column('themes', 'title')
    op.drop_constraint(None, 'questions', type_='unique')
    op.drop_column('questions', 'title')
    op.drop_constraint(None, 'answers', type_='unique')
    op.drop_column('answers', 'is_correct')
    op.drop_column('answers', 'title')
    # ### end Alembic commands ###
