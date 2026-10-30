import pymysql


class RoleModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from role"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()

        return pk + 1

    def add(self, data):
        id = RoleModel.next_pk(self)
        name = data['name']
        description = data['description']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "insert into role values(%s, %s, %s)"
        data = (id, name, description)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        name = data['name']
        description = data['description']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="advance_python")
        cursor = connection.cursor()
        sql = "update role set name = %s, description = %s where id = %s"
        data = (name, description, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("college updated successfully")

    def delete(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "delete from role where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def get(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from role where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        list = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_name(self, name):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from role where name = %s"
        data = (name)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        list = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        id = data.get('id', 0)
        name = data.get('name', '')
        description = data.get('description', '')
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from role where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if description != '':
            sql += " and description like '" + description + "%'"

        if page_size > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
