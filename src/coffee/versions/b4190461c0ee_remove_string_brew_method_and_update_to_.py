"""Remove string brew method and update to enum

Revision ID: b4190461c0ee
Revises: d99d8c74b698
Create Date: 2021-04-23 23:47:36.676953

"""
from alembic import op
from sqlalchemy import String, Column


# revision identifiers, used by Alembic.
revision = 'b4190461c0ee'
down_revision = 'd99d8c74b698'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('recipes',
        Column('origin', String, index=True)
    )


def downgrade():
    op.drop_column('recipes', 'origin')
