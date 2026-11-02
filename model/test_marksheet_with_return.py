from marksheet_model_with_return import MarksheetModel
from student_model import StudentModel
import pymysql

def testAdd():
    params = {}
    params['id'] = 5
    params['roll_no'] = 105
    params['student_id']= 5
    params['name'] = 'harshit'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = MarksheetModel()
    model.add(params)

def testUpdate():
    params = {}
    params['id'] = 1
    params['roll_no'] = 101
    params['student_id']= 1
    params['name'] = 'shubham'
    params['physics'] = 55
    params['chemistry'] = 68
    params['maths'] = 75

    model = MarksheetModel()
    model.update(params)


def testDelete():
    model = MarksheetModel()
    model.delete(8)


def testGet():
    model = MarksheetModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', 
              data['roll_no'], '\t',
              data['student_id'], '\t',
              data['name'], '\t', 
              data['physics'], '\t', 
              data['chemistry'],'\t',
              data['maths'], )


def find_by_roll_no():
    model = MarksheetModel()
    list = model.find_by_roll_no('103')
    for data in list:
        print(data['id'], '\t',
              data['roll_no'], '\t',
              data['student_id'], '\t',
              data['name'], '\t',
              data['physics'], '\t',
              data['chemistry'], '\t',
              data['maths'])


def test_Search():
    params = {}
    # params['name'] = 'abc'
    # params['roll_no'] = 101
    params['pageNo'] = 1
    params['pageSize'] = 3
    model = MarksheetModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t',
              data['roll_no'], '\t',
              data['student_id'], '\t',
              data['name'], '\t',
              data['physics'], '\t',
              data['chemistry'], '\t',
              data['maths'], )

# testAdd()
# testUpdate()
# testDelete()
# testGet()
# find_by_roll_no()
test_Search()