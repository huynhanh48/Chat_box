"""'update__moduls'

Revision ID: 989dc44f29b4
Revises: 1d2b237e86ff
Create Date: 2024-12-10 15:27:32.603421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '989dc44f29b4'
down_revision = '1d2b237e86ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('file__session', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.String(length=60), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('file__session', schema=None) as batch_op:
        batch_op.drop_column('author')

    # ### end Alembic commands ###
