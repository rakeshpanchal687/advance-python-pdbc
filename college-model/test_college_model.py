from college_model import collegeModel

def test_add():
    data = {
        'id': '7',
        'name': 'John Doe',
        'address': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'phone_no': '9131085107',
    }
    model = collegeModel()
    model.add(data)

def test_update():
    data = {
        'id': '7',
        'name': 'rakesh',
        'address': '1255 Main road',
        'city': 'dubai',
        'state': 'mp',
        'phone_no': '8358090606'
    }
    model = collegeModel()
    model.update(data)

def test_delete():

    model = collegeModel()
    model.delete(7)


# test_add()
# test_update()
test_delete()
