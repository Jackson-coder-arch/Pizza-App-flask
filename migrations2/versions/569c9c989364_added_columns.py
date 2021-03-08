"""added columns

Revision ID: 569c9c989364
Revises: 9ede7aa094d3
Create Date: 2021-03-05 15:31:12.180356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '569c9c989364'
down_revision = '9ede7aa094d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('size', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'size')
    # ### end Alembic commands ###
