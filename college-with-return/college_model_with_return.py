import pymysql

class collegeModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = collegeModel.next_pk(self)
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_no = data['phone_no']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "insert into college values(%s, %s, %s, %s, %s, %s)"
        data = (id, name, address, state, city, phone_no)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_no = data['phone_no']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "update college set name = %s, address = %s, state = %s, city = %s, phone_no = %s where id = %s"
        data = (name, address, state, city, phone_no, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')


    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "delete from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
        cursor = connection.cursor()

        sql = "SELECT * FROM college WHERE id = %s"
        data = (id,)

        cursor.execute(sql, data)
        result = cursor.fetchall()
        list = []
        columnName = ['id', 'name', 'address', 'state', 'city', 'phone_no']

        for x in result:
            list.append({columnName[i]: x[i]for i, _ in enumerate(x)})
        cursor.close()
        connection.close()
        return list

    def findByname(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()

        sql = "SELECT * FROM college WHERE name = %s"
        data = (name,)

        cursor.execute(sql, data)
        result = cursor.fetchall()
        list = []

        columnName = ['id', 'name', 'address', 'state', 'city', 'phone_no']

        for x in result:
            list.append({ columnName[i]: x[i] for i, _ in enumerate(x) })

        cursor.close()
        connection.close()

        return list

    def search(self, param):
        id = param.get('id', 0)
        name = param.get('name', '')
        address = param.get('address', '')
        state = param.get('state', '')
        city = param.get('city', '')
        phone_no = param.get('phone_no', '')
        page_no = param.get('pageNo', 0)
        page_size = param.get('pageSize', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if address != '':
            sql += " and address like '" + address + "%'"
        if state != '':
            sql += " and state like '" + state + "%'"
        if city != '':
            sql += " and city like '" + city + "%'"
        if phone_no != '':
            sql += " and phone_no like '" + phone_no + "%'"
        if page_size > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "name", "address", "state", "city", "phone_no")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
