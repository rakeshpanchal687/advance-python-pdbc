from course_model import CourseModel


def test_add():
    data = {}
    # data['id'] = 'C'
    data['name'] = 'C'
    data['description'] = 'C programming fundamental'
    data['duration'] = '6 month'
    course = CourseModel()

    try:
        course.add(data)
    except Exception as e:
        print(e)

def test_update():
    data = {}
    data['id'] = '3'
    data['name'] = 'Python'
    data['description'] = 'Python programming advance'
    data['duration'] = '7 month'
    course = CourseModel()
    course.update(data)

def test_delete():

    course = CourseModel()
    course.delete(5)


def test_get():
    course = CourseModel()
    list = course.get(2)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['duration'], )

def test_find_by_name():
    course = CourseModel()
    list = course.find_by_name('c')
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['duration'], )


def test_search():
    data = {}
    # data['name'] = 'abc'
    data['page_no'] = 1
    data['page_size'] = 0
    model = CourseModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['duration'], )


test_add()
# test_update()
# test_get()
# test_find_by_name()
# test_delete()
# test_search()