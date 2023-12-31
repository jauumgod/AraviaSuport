"""empty message

Revision ID: 81d580ef6118
Revises: bfc577094c45
Create Date: 2023-11-08 16:59:03.027565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81d580ef6118'
down_revision = 'bfc577094c45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chamados', schema=None) as batch_op:
        batch_op.add_column(sa.Column('problema', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('status', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chamados', schema=None) as batch_op:
        batch_op.drop_column('status')
        batch_op.drop_column('problema')

    # ### end Alembic commands ###
