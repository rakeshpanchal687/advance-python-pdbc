from college_model import collegeModel

def test_add():
    data = {}
    data['id']=7
    data['name']='rakesh'
    data['address']= 'main road'
    data['city']='bhopal'
    data['state']='up'
    data['phone_no']=9131085107


    model = collegeModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)
    # model.add(data)

def test_update():
    data = {}
    data['id'] = 7
    data['name'] = 'raj'
    data['address'] = 'main road'
    data['city'] = 'bhopal'
    data['state'] = 'up'
    data['phone_no'] = 9131085107
    model = collegeModel()
    model.update(data)

def test_delete():

    model = collegeModel()
    model.delete(7)


test_add()
# test_update()
# test_delete()
