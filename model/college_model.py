import pymysql


class collegeModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
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

        college_exist = self.findatabaseyname(name)

        if len(college_exist) > 0:
            raise Exception("name already exist")

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
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

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')

        cursor = connection.cursor()

        sql = """ UPDATE college SET name=%s, address=%s, state=%s,city=%s,phone_no=%s WHERE id=%s"""

        values = (name, address, state, city, phone_no, id)

        cursor.execute(sql, values)
        connection.commit()
        connection.close()

        print('Data updated successfully')

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "delete from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "adress", "state", "city", "phone_no")
        list = []
        for x   in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        # connection.commit()
        connection.close()
        return list

    def findatabaseyname(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where name = %s"
        data = (name)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "adress", "state", "city", "phone_no")
        list = []
        for x in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        # connection.commit()
        connection.close()
        return list

    def search(self, data):
        name = data.get('name', '')
        address = data.get('address', 0)
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where 1=1"
        if name != '':
            sql += " and name = '" + name + "'"
        if address != '':
            sql += " and address = " + str(address)
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit " + str(pageNo) + ", " + str(pageSize)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()
