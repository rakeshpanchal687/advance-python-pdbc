from faculty_model import FacultyModel
import datetime


def test_add():
    data = {}
    data['id'] = 4
    data['first_name'] = 'harsh'
    data['last_name'] = 'parmar'
    data['email'] = 'harshparmar@gamil'
    data['password'] = 'harsh@123'
    data['address'] = 'bhawarkuwa'
    data['gender'] = 'male'
    data['dob'] = datetime.date(2005, 7, 12)
    data['college_id'] = 3
    data['course_id'] = 3
    data['subject_id'] = 6
    faculty = FacultyModel()
    faculty.add(data)
    # try:
    #     faculty.add(data)
    # except Exception as e:
    #     print(e)

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
    data['college_id'] = 2
    data['course_id'] = 3
    data['subject_id'] = 5
    faculty = FacultyModel()
    faculty.update(data)


# test_update()

def test_delete():
    model = FacultyModel()
    model.delete(4)


# test_delete()

def test_get():
    model = FacultyModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['email'], '\t',
              data['password'], '\t', data['address'], '\t', data['gender']
              , '\t', data['dob'], '\t', data['college_id'], '\t', data['course_id'], '\t', data['subject_id'])


# test_get()

def find_by_email():
    model = FacultyModel()
    list = model.find_by_email('rakeshpanchal@gamil')
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['email'], '\t',
              data['password'], '\t', data['address'], '\t', data['gender']
              , '\t', data['dob'], '\t', data['college_id'], '\t', data['course_id'], '\t', data['subject_id'])


# find_by_email()

def test_search():
    data = {}
    data['pageNo'] = 1
    data['pageSize'] = 5
    model = FacultyModel()
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['email'], '\t',
              data['password'], '\t', data['address'], '\t', data['gender']
              , '\t', data['dob'], '\t', data['college_id'], '\t', data['course_id'], '\t', data['subject_id'])

test_add()
# test_update()
# test_delete()
# test_get()
# find_by_email()
# test_search()
