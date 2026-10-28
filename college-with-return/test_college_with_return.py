from college_model_with_return import collegeModel

def testAdd():
    params = {}
    params['id'] = 7
    params['name'] = 'abc'
    params['address'] = '123 Main St'
    params['state'] = 'CA'
    params['city'] = 'Anytown'
    params['phone_no'] = '9131085107'
    model = collegeModel()
    model.add(params)

def testUpdate():
    params = {}
    params['id'] = 7
    params['name'] = 'Rakesh'
    params['address'] = '1255 Main road'
    params['state'] = 'mp'
    params['city'] = 'dubai'
    params['phone_no'] = '8358090606'
    model = collegeModel()
    model.update(params)


def testDelete():
    model = collegeModel()
    model.delete(7)

def testGet():
    model = collegeModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'],              '\t',
              data['phone_no'], )

def testFindByname():
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


# testAdd()
# testUpdate()
# testGet()
# testFindByname()
test_Search()