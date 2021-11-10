"""empty message

Revision ID: bafaef19aefb
Revises: ab498c68ef57
Create Date: 2021-11-10 21:06:23.658464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bafaef19aefb'
down_revision = 'ab498c68ef57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('students_info', 'roll_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('students_info', 'firstname',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('students_info', 'current_class',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('students_info', 'phone_number',
               existing_type=sa.VARCHAR(length=11),
               nullable=True)
    op.alter_column('students_info', 'birth_cirtificate_no',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('students_info', 'birth_date',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('students_info', 'gender',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('students_info', 'zip_code',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    op.alter_column('students_info', 'address',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('students_info', 'email',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('students_info', 'image_file',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('students_info', 'signature',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('students_info', 'transportation_status',
               existing_type=sa.VARCHAR(length=5),
               nullable=True)
    op.alter_column('students_info', 'graduation_status',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.create_unique_constraint(None, 'students_info', ['unique_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'students_info', type_='unique')
    op.alter_column('students_info', 'graduation_status',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('students_info', 'transportation_status',
               existing_type=sa.VARCHAR(length=5),
               nullable=False)
    op.alter_column('students_info', 'signature',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('students_info', 'image_file',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('students_info', 'email',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('students_info', 'address',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('students_info', 'zip_code',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('students_info', 'gender',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('students_info', 'birth_date',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('students_info', 'birth_cirtificate_no',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('students_info', 'phone_number',
               existing_type=sa.VARCHAR(length=11),
               nullable=False)
    op.alter_column('students_info', 'current_class',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('students_info', 'firstname',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('students_info', 'roll_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
