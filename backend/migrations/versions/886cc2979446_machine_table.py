"""Machine table

Revision ID: 886cc2979446
Revises: 
Create Date: 2023-06-19 10:20:22.067075

"""
from alembic.op import create_table, drop_table
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, text


# revision identifiers, used by Alembic.
revision = '886cc2979446'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    create_table(
        'machines',
        Column('id', Integer, primary_key=True),
        Column('name', String(200), nullable=False, default="Machine"),
        Column('location', String(50), nullable=True),
        Column('email', String(50), nullable=False, unique=True),
        Column('number', String(200), nullable=False, unique=True),
        Column('enum', Boolean, nullable=False, default=False),
        Column('created_at', DateTime(), server_default=text('CURRENT_TIMESTAMP'), nullable=False),
        Column('edited_at', DateTime(), server_default=text('CURRENT_TIMESTAMP'), nullable=False, onupdate=text('CURRENT_TIMESTAMP')),
    )

def downgrade() -> None:
    drop_table('machines')