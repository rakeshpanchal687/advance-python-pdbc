import pymysql


def testUpdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = 104, name = 'ppp', physics = 99, chemistry = 99, maths = 99 where id = 4"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = %s, name = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
    data = (100, 'xyy', 72, 72, 26, 2)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate3(rollNo, name, physics, chemistry, maths, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = %s, name = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
    data = (rollNo, name, physics, chemistry, maths, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate4(data):
    id = data['id']
    rollNo = data['rollNo']
    name = data['name']
    physics = data['physics']
    chemistry = data['chemistry']
    maths = data['maths']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = %s, name = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
    data = (rollNo, name, physics, chemistry, maths, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')

# testUpdate1()
# testUpdate2()
# testUpdate3(103, 'pqr', 89, 77, 67, 3)

# params = {}
# params['id'] = 4
# params['rollNo'] = 104
# params['name'] = 'klj'
# params['physics'] = 100
# params['chemistry'] = 100
# params['maths'] = 100
#
# testUpdate4(params)