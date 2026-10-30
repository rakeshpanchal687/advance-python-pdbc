import pymysql


def testDelete1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = 4"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data deleted successfully')


def testDelete2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = %s"
    data = (2)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data deleted successfully')


def testDelete3(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = %s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data deleted successfully')

# testDelete1()
# testDelete2()
testDelete3(21)