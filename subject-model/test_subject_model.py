from subject_model import SubjectModel


def test_add():
    data = {}
    # data['id'] = 1
    data['name'] = 'git,github'
    data['description'] = 'Version control and source code management'
    data['course_id'] = 3
    subject = SubjectModel()

    try:
        subject.add(data)
    except Exception as e:
        print(e)
    # subject.add(data)


# test_add()


def test_update():
    data = {}
    data['id'] = 5
    data['name'] = 'Docker'
    data['description'] = 'Containerization and Docker images'
    data['course_id'] = 3
    subject = SubjectModel()
    subject.update(data)


# test_update()


def test_delete():
    subject = SubjectModel()
    subject.delete(6)


# test_delete()


def test_get():
    subject = SubjectModel()
    list = subject.get(2)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['course_id'], )


# test_get()


def test_find_by_name():
    subject = SubjectModel()
    list = subject.find_by_name('core java')
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['course_id'], )


# test_find_by_name()

def test_search():
    data = {}
    # data['name'] = 'core java'
    data['page_no'] = 1
    data['page_size'] = 0
    model = SubjectModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['course_id'], )

# test_add()
# test_update()
# test_delete()
# test_get()
# test_search()
