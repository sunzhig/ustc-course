import sys
sys.path.append('..')  # fix import directory

from app import app,db,user_datastore
from app.models import Student,Course,User


print(Student.query.all())
print()
print(Student.query.filter_by(dept='11').first())
print(Course.query.all())
print(User.query.all())
