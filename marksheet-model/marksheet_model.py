import pymysql


class MarksheetModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet"
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
        id = MarksheetModel.next_pk(self)
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']

        marksheet_exist = self.find_by_roll_no(roll_no)

        if len(marksheet_exist) > 0:
            raise Exception("roll no already exist")


        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
        data = (id, roll_no, name, physics, chemistry, maths)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self, data):
        id = data['id']
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "update marksheet set roll_no = %s, name = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
        data = (roll_no, name, physics, chemistry, maths, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def get(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "roll_no", "name", "physics", "chemistry", "maths")
        list = []
        for x in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_roll_no(self, roll_no):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from marksheet where roll_no = %s"
        data = (roll_no)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "roll_no", "name", "physics", "chemistry", "maths")
        list = []
        for x in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        name = data.get('name', '')
        roll_no = data.get('roll_no', 0)
        physics = data.get('physics', 0)
        chemistry = data.get('chemistry', 0)
        maths = data.get('maths', 0)
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from marksheet where 1=1"
        if name != '':
            sql += " and name like '" + name + "%'"
        if roll_no != 0:
            sql += " and roll_no = " + str(roll_no)
        if physics != 0:
            sql += " and physics like ' " + str(physics)
        if chemistry != 0:
            sql += " and chemistry like ' " + str(chemistry)
        if maths != 0:
            sql += " and maths like ' " + str(maths)
        if (page_size > 0):
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "roll_no", "name", "physics", "chemistry", "maths")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list