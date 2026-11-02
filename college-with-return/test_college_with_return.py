from college_model_with_return import collegeModel

def test_Add():
    params = {}
    params['id'] = 7
    params['name'] = 'abc'
    params['address'] = '123 Main St'
    params['state'] = 'CA'
    params['city'] = 'Anytown'
    params['phone_no'] = '9131085107'
    model = collegeModel()
    model.add(params)

def test_Update():
    params = {}
    params['id'] = 7
    params['name'] = 'Rakesh'
    params['address'] = '1255 Main road'
    params['state'] = 'mp'
    params['city'] = 'dubai'
    params['phone_no'] = '8358090606'
    model = collegeModel()
    model.update(params)


def test_Delete():
    model = collegeModel()
    model.delete(7)

def test_Get():
    model = collegeModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'],              '\t',
              data['phone_no'], )

def Find_By_name():
    model = collegeModel()
    list = model.findByname('star college')
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'], '\t',
              data['phone_no'], )

def test_Search():
    params = {}
    # params['name'] = 'abc'
    model = collegeModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'], '\t',
              data['phone_no'], )


test_Add()
test_Update()
test_Get()
test_Delete()
test_Search()