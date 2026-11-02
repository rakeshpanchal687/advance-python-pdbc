from model.college_model import collegeModel
from student_model import StudentModel
import datetime


def test_add():
    data = {}
    # data['id'] = 1
    data['first_name'] = 'rajvardhan'
    data['last_name'] = 'Parmar'
    data['dob'] = datetime.date(1995, 10, 31)
    data['mobile_no'] = '8463893319'
    data['email'] = 'raj12@gamil'
    data['college_id'] = 4

    college_list = collegeModel().get(data['college_id'])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name

    student = StudentModel()
    # student.add(data)

    try:
        student.add(data)
    except Exception as e:
        print(e)



# test_add()

def test_update():
    data = {}
    data['id'] = 5
    data['first_name'] = 'rajvardhan'
    data['last_name'] = 'Parmar'
    data['dob'] = datetime.date(1995, 11, 21)
    data['mobile_no'] = '9754254321'
    data['email'] = 'raj12@gamil'
    data['college_id'] = 5

    college_list = collegeModel().get(data['college_id'])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name

    student = StudentModel()
    student.update(data)


# test_update()


def test_delete():
    model = StudentModel()
    model.delete(2)

# test_delete()

def test_get():
    model = StudentModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t',
              data['first_name'], '\t',
              data['last_name'], '\t',
              data['dob'], '\t',
              data['mobile_no'], '\t',
              data['email'], '\t',
              data['college_id'],'\t',
              data['college_name'])

# test_get()

def find_by_email():
    model = StudentModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t',
              data['first_name'], '\t',
              data['last_name'], '\t',
              data['dob'], '\t',
              data['mobile_no'], '\t',
              data['email'], '\t',
              data['college_id'], '\t',
              data['college_name'])

# find_by_email()

def test_search():
    data = {}
    data['pageNo'] = 1
    data['pageSize'] = 0
    model =StudentModel()
    list = model.search(data)
    for data in list:
        print(data['id'], '\t',
              data['first_name'], '\t',
              data['last_name'], '\t',
              data['dob'], '\t',
              data['mobile_no'], '\t',
              data['email'], '\t',
              data['college_id'], '\t',
              data['college_name'])


# test_add()
# test_update()
# test_delete()
# test_get()
# find_by_email()
# test_search()

