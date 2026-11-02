import pymysql


class CourseModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from course"
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
        id = CourseModel.next_pk(self)
        name = data['name']
        description = data['description']
        duration = data['duration']

        course_exist = self.find_by_name(name)

        if len(course_exist) > 0:
            raise Exception("course name already exist")


        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "insert into course values(%s, %s, %s, %s)"
        data = (id, name, description, duration)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        name = data['name']
        description = data['description']
        duration = data['duration']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="advance_python")
        cursor = connection.cursor()
        sql = "update course set description = %s, duration = %s, name = %s where id = %s"
        data = (name, description, duration, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("course updated successfully")

    def delete(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", database="advance_python")
        cursor = connection.cursor()
        sql = "delete from course where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def get(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", database="advance_python")
        cursor = connection.cursor()
        sql = "select * from course where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "name", "description", "duration")
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_name(self, name):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", database="advance_python")
        cursor = connection.cursor()
        sql = "select * from course where name = %s"
        data = (name)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "name", "description", "duration")
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        id = data.get('id', 0)
        name = data.get('name', '')
        description = data.get('description', '')
        duration = data.get('duration', '')
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from course where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if description != '':
            sql += " and description like '" + description + "%'"
        if duration != '':
            sql += " and duration like '" + duration + "%'"

        if page_size > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "name", "description", "duration")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list