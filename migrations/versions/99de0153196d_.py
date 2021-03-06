"""empty message

Revision ID: 99de0153196d
Revises: 
Create Date: 2020-10-18 13:50:55.848772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99de0153196d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('real_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('message', sa.String(length=10000), nullable=False),
    sa.Column('newsletter', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('real_message')
    op.drop_table('email')
    # ### end Alembic commands ###
