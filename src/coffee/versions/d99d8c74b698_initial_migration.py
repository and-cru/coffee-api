"""Initial migration

Revision ID: d99d8c74b698
Revises: 
Create Date: 2021-04-23 18:20:12.827766

"""
from alembic import op
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String


# revision identifiers, used by Alembic.
revision = 'd99d8c74b698'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'brewers',
        Column('id', Integer, primary_key=True, index=True, autoincrement=True),
        Column('name', String, unique=True, index=True)
    )

    op.create_table(
        'recipes',
        Column('id', Integer, primary_key=True, index=True, autoincrement=True),
        Column('title', String, index=True),
        Column('bean_type', String, index=True),
        Column('description', String, index=True),
        Column('brew_method', String, index=True),
        Column('taste_notes', String, index=True),
        Column('tags', String, index=True),
        Column('brew_time', Float, index=True),
        Column('views', Integer, index=True, default=0),
        Column('brewer_id', Integer, ForeignKey("brewers.id"))
    )


def downgrade():
    op.drop_table('recipes')
    op.drop_table('brewers')
