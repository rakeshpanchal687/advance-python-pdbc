from model.role_model import RoleModel
from user_model import UserModel
import datetime


def test_add():
    data = {}
    data['id'] = 4
    data['first_name'] = 'vijay'
    data['last_name'] = 'varma'
    data['login_id'] = 'vijay123'
    data['password'] = 'vj123'
    data['dob'] = datetime.date(2002, 12, 5),
    data['address'] = 'bhopal'
    data['role_id'] = 4
    data['role_name'] = 'college'

    role_list = RoleModel().get(data['role_id'])
    role_name = role_list[0].get('name')
    data['role_name'] = role_name

    model = UserModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)

    # model.add(data)


def test_update():
    data = {}
    data['id'] = 2
    data['first_name'] = 'Rakesh'
    data['last_name'] = 'Panchal'
    data['login_id'] = 'rakesh123'
    data['password'] = 'rakesh@123'
    data['dob'] = datetime.date(1993, 4, 8),
    data['address'] = 'indore'
    data['role_id'] = 2
    data['role_name'] = 'student'

    role_list = RoleModel().get(data['role_id'])
    role_name = role_list[0].get('name')
    data['role_name'] = role_name

    model = UserModel()
    model.update(data)


def test_delete():
    model = UserModel()
    model.delete(5)


def test_get():
    model = UserModel()
    list = model.get(4)
    for data in list:
        print(data['id'], '\t',
              data['first_name'], '\t',
              data['last_name'], '\t',
              data['login_id'], '\t',
              data['password'], '\t',
              data['dob'], '\t',
              data['address'],'\t',
              data['role_id'], '\t',
              data['role_name'])


def find_by_login_id():
    model = UserModel()
    list = model.find_by_login_id('rakesh123')
    for data in list:
        print(data['id'], '\t',
              data['first_name'], '\t',
              data['last_name'], '\t',
              data['login_id'], '\t',
              data['password'], '\t',
              data['dob'], '\t',
              data['address'], '\t',
              data['role_id'], '\t',
              data['role_name'])


def test_search():
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5
    model = UserModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t',
              data['first_name'], '\t',
              data['last_name'], '\t',
              data['login_id'], '\t',
              data['password'], '\t',
              data['dob'], '\t',
              data['address'], '\t',
              data['role_id'], '\t',
              data['role_name'])

# test_add()
# test_update()
# test_delete()
# test_get()
# find_by_login_id()
# test_search()
