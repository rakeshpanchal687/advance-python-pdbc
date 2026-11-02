from role_model import RoleModel


def test_add():
    data = {}
    # data['id'] =
    data['name'] = 'Accountant'
    data['description'] = 'Manages financial records'
    role = RoleModel()
    role.add(data)


def test_update():
    data = {}
    data['id'] = 2
    data['name'] = 'Admin'
    data['description'] = 'administrator'
    role = RoleModel()
    role.update(data)


def test_delete():
    role = RoleModel()
    role.delete(1)


def test_get():
    role = RoleModel()
    role.get(2)


def test_search():
    data = {}
    # data['name'] = 'abc'
    # data['roll_no'] = 101
    data['page_no'] = 1
    data['page_size'] = 0
    model = RoleModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], )

# test_add()
# test_update()
# test_get()
# test_search()
