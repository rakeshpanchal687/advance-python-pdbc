from marksheet_model import MarksheetModel

def testAdd():
    data = {
        'roll_no': '101',
        'name': 'John Doe',
        'physics': 85,
        'chemistry': 90,
        'maths': 95
    }
    model = MarksheetModel()
    model.add(data)

def testupdate():
    data = {
        'id': 21,
        'roll_no': '101',
        'name': 'John Smith',
        'physics': 88,
        'chemistry': 92,
        'maths': 96
    }
    model = MarksheetModel()
    model.update(data)


def testdelete():

    model = MarksheetModel()
    model.delete(20)

# testAdd()
# testdelete()
testdelete()
