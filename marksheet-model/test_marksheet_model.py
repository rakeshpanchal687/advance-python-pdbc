from marksheet_model import MarksheetModel


def test_add():
    data = {}
    # data['id'] = 8
    data['roll_no'] = 108
    data['name'] = 'abc'
    data['physics'] = 70
    data['chemistry'] = 67
    data['maths'] = 79

    model = MarksheetModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)

test_add()

def test_update():
    data = {}
    data['id'] = 8
    data['roll_no'] = 108
    data['name'] = 'ooo'
    data['physics'] = 70
    data['chemistry'] = 67
    data['maths'] = 79

    model = MarksheetModel()
    model.update(data)


def test_delete():
    model = MarksheetModel()
    model.delete(8)



def test_get():
    model = MarksheetModel()
    list = model.get()
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def test_find_by_roll_no():
    model = MarksheetModel()
    list = model.find_by_roll_no(103)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def test_search():
    data = {}
    # data['name'] = 'John Smith'
    # data['roll_no'] = 101
    data['page_no'] = 1
    data['page_size'] = 6
    model = MarksheetModel()
    model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t', data['maths'], )



# test_update()
# test_get()
# test_find_by_roll_no()
# test_search()