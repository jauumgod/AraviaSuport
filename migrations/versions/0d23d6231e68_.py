"""empty message

Revision ID: 0d23d6231e68
Revises: 81d580ef6118
Create Date: 2023-11-08 17:37:32.626919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d23d6231e68'
down_revision = '81d580ef6118'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###
