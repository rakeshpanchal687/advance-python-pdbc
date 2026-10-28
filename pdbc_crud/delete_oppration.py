import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
cursor = connection.cursor()
sql = "delete from mark_sheet where id = 10"
cursor.execute(sql)
connection.commit()
connection.close()
print('data deleted successfully')