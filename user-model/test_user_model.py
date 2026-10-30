from user_model import UserModel
import datetime

def test_add():
    data = {
        'first_name': 'Harsh',
        'last_name': 'parmar',
        'login_id': 'harsh123',
        'password': 'password123',
        'dob': datetime.date(2005, 5, 1),
        'address': 'Indore'
    }
    model = UserModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)

    # model.add(data)

def test_update():
    data = {
        'id': 1,
        'first_name': 'Rakesh',
        'last_name': 'Panchal',
        'login_id': 'rakesh123',
        'password': 'rakesh@123',
        'dob': datetime.date(1993, 4, 8),
        'address': 'Patnipura Road'
    }
    model = UserModel()
    model.update(data)

def test_delete():
    model = UserModel()
    model.delete(7)

def test_get():
    model = UserModel()
    list = model.get(4)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t', data['password'], '\t', data['dob'], '\t', data['address'])

def find_by_login_id():
    model = UserModel()
    list = model.find_by_login_id('rakesh123')
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t', data['password'], '\t', data['dob'], '\t', data['address'])

def test_search():
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5
    model = UserModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t', data['password'], '\t', data['dob'], '\t', data['address'])

test_add()
# test_update()
# test_delete()
# test_get()
# find_by_login_id()
# test_search()