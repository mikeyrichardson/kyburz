"""remove right side numerator and denominator in problems table

Revision ID: 4a8425d30d22
Revises: 529c4e61800b
Create Date: 2015-11-22 15:10:15.771197

"""

# revision identifiers, used by Alembic.
revision = '4a8425d30d22'
down_revision = '529c4e61800b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('problems', 'right_side_denominator')
    op.drop_column('problems', 'right_side_numerator')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problems', sa.Column('right_side_numerator', sa.INTEGER(), nullable=True))
    op.add_column('problems', sa.Column('right_side_denominator', sa.INTEGER(), nullable=True))
    ### end Alembic commands ###
