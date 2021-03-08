"""added columns

Revision ID: 1f1e2c7c249e
Revises: 3df2b571f85d
Create Date: 2021-03-05 16:31:23.011293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f1e2c7c249e'
down_revision = '3df2b571f85d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.Integer(), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
