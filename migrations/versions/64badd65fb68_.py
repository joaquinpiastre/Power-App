"""empty message

Revision ID: 64badd65fb68
Revises: 458bafd56829
Create Date: 2023-11-16 20:01:23.512081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64badd65fb68'
down_revision = '458bafd56829'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instructors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('specialty', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('gym_classes', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'instructors', ['instructor_name'], ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gym_classes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('instructors')
    # ### end Alembic commands ###
