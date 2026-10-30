from marksheet_model_with_return import MarksheetModel

def testAdd():
    params = {}
    # params['id'] = 8
    params['roll_no'] = 108
    params['name'] = 'abc'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = MarksheetModel()
    model.add(params)

def testUpdate():
    params = {}
    params['id'] = 8
    params['roll_no'] = 108
    params['name'] = 'ooo'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = MarksheetModel()
    model.update(params)


def testDelete():
    model = MarksheetModel()
    model.delete(8)


def testRead():
    model = MarksheetModel()
    model.read()


def testGet():
    model = MarksheetModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',data['maths'], )


def testFindByroll_no():
    model = MarksheetModel()
    list = model.findByRoll(103)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t', data['maths'], )


def test_Search():
    params = {}
    # params['name'] = 'abc'
    # params['roll_no'] = 101
    params['pageNo'] = 1
    params['pageSize'] = 3
    model = MarksheetModel()
    list = model.search(params)
    for obj in list:
        print(obj['id'], '\t', obj['roll_no'], '\t', obj['name'], '\t', obj['physics'], '\t', obj['chemistry'], '\t',
              obj['maths'], )


# testAdd()
# testUpdate()
# testRead()
# testGet()
# testFindByroll_no()
test_Search()