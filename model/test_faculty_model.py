from faculty_model import FacultyModel
import datetime

from model.college_model import collegeModel
from model.course_model import CourseModel
from model.subject_model import SubjectModel


def do_print(data):
    print(data['id'], '\t',
          data['first_name'], '\t',
          data['last_name'], '\t',
          data['email'], '\t',
          data['password'], '\t',
          data['address'], '\t',
          data['gender'], '\t',
          data['dob'], '\t',
          data['college_id'], '\t',
          data['college_name'], '\t',
          data['course_id'], '\t',
          data['course_name'], '\t',
          data['subject_id'],
          data['subject_name'], '\t', )


def test_add():
    data = {}
    data['id'] = 5
    data['first_name'] = 'Shubham'
    data['last_name'] = 'upadhiyay'
    data['email'] = 'shubham@12gamil'
    data['password'] = 'shubham123'
    data['address'] = 'jammu'
    data['gender'] = 'male'
    data['dob'] = datetime.date(1998, 1, 5)
    data['college_id'] = 4
    data['course_id'] = 1
    data['subject_id'] = 1

    college_list = collegeModel().get(data['college_id'])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name

    course_list = CourseModel().get(data['course_id'])
    course_name = course_list[0].get('name')
    data['course_name'] = course_name

    subject_list = SubjectModel().get(data['subject_id'])
    subject_name = subject_list[0].get('name')
    data['subject_name'] = subject_name

    faculty = FacultyModel()
    # faculty.add(data)
    try:
        faculty.add(data)
    except Exception as e:
        print(e)


# test_add()

def test_update():
    data = {}
    data['id'] = 3
    data['first_name'] = 'Ruchi'
    data['last_name'] = 'jain'
    data['email'] = 'ruchijain@gamil'
    data['password'] = 'ruchi@123'
    data['address'] = 'Near railway station'
    data['gender'] = 'Female'
    data['dob'] = datetime.date(1993, 2, 12)
    data['college_id'] = 3
    data['course_id'] = 1
    data['subject_id'] = 1

    college_list = collegeModel().get(data['college_id'])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name

    course_list = CourseModel().get(data['course_id'])
    course_name = course_list[0].get('name')
    data['course_name'] = course_name

    subject_list = SubjectModel().get(data['subject_id'])
    subject_name = subject_list[0].get('name')
    data['subject_name'] = subject_name

    faculty = FacultyModel()
    faculty.update(data)


# test_update()

def test_delete():
    model = FacultyModel()
    model.delete(5)


# test_delete()

def test_get():
    model = FacultyModel()
    list = model.get(1)
    for data in list:
        do_print(data)


# test_get()

def find_by_email():
    model = FacultyModel()
    list = model.find_by_email('rakeshpanchal@gamil')
    for data in list:
        do_print(data)


# find_by_email()

def test_search():
    data = {}
    data['pageNo'] = 1
    data['pageSize'] = 0
    model = FacultyModel()
    list = model.search(data)
    for data in list:
        # college_list = collegeModel().get(data['college_id'])
        # college_name = college_list[0].get('name')
        #
        # course_list = CourseModel().get(data['course_id'])
        # course_name = course_list[0].get('name')
        #
        # subject_list = SubjectModel().get(data['subject_id'])
        # subject_name = subject_list[0].get('name')

        do_print(data)


# test_add()
# test_update()
# test_delete()
# test_get()
# find_by_email()
# test_search()
