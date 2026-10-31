import pymysql


class FacultyModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from faculty"
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
        id = FacultyModel.next_pk(self)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        address = data['address']
        gender = data['gender']
        dob = data['dob']
        college_id = data['college_id']
        college_name = data['college_name']
        course_id = data['course_id']
        course_name = data['course_name']
        subject_id = data['subject_id']
        subject_name = data['subject_name']
        #
        # faculty_exist = self.find_by_email(email)
        #
        # if len(faculty_exist) > 0:
        #     raise Exception(" email already exist")

        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root",
                                        database="advance_python")
        cursor = connection.cursor()
        sql = "insert into faculty values(%s, %s, %s, %s, %s, %s, %s , %s , %s , %s, %s, %s , %s ,%s)"
        data = (id, first_name, last_name, email, password, address, gender, dob, college_id, college_name, course_id,
                course_name, subject_id, subject_name)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self, data):
        id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        address = data['address']
        gender = data['gender']
        dob = data['dob']
        college_id = data['college_id']
        college_name = data['college_name']
        course_id = data['course_id']
        course_name = data['course_name']
        subject_id = data['subject_id']
        subject_name = data['subject_name']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root",
                                        database="advance_python")
        cursor = connection.cursor()
        sql = "update faculty set first_name = %s, last_name = %s, email = %s, password = %s, address = %s, gender = %s, dob = %s, college_id = %s, college_name = %s, course_id = %s, course_name = %s, subject_id = %s, subject_name = %s where id = %s"
        data = (first_name, last_name, email, password, address, gender, dob, college_id, college_name, course_id,
                course_name, subject_id, subject_name, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root",
                                        database="advance_python")
        cursor = connection.cursor()
        sql = "delete from faculty where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def get(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root",
                                        database="advance_python")
        cursor = connection.cursor()
        sql = "select * from faculty where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = (
            "id", "first_name", "last_name", "email", "password", "address", "gender", "dob", "college_id",
            "college_name" ,"course_id", "course_name",
            "subject_id", "subject_name")
        list = []
        for x in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_email(self, email):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root",
                                        database="advance_python")
        cursor = connection.cursor()
        sql = "select * from faculty where email = %s"
        data = (email)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = (
            "id", "first_name", "last_name", "email", "password", "address", "gender", "dob", "college_id",
            "college_name", "course_id", "course_name",
            "subject_id", "subject_name")
        list = []
        for x in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        id = data.get('id',0)
        first_name = data.get('first_name','')
        last_name = data.get('last_name','')
        email = data.get('email','')
        password = data.get('password','')
        address = data.get('address','')
        gender = data.get('gender','')
        dob = data.get('dob',0)
        college_id = data.get('college_id','')
        college_name = data.get('college_name','')
        course_id = data.get('course_id','')
        course_name = data.get('course_name','')
        subject_id = data.get('subject_id','')
        subject_name = data.get('subject_name','')
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from faculty where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if first_name != '':
            sql += " and first_name like '" + first_name + "%'"
        if last_name != '':
            sql += " and last_name like '" + last_name + "%'"
        if email != '':
            sql += " and email like '" + email + "%'"
        if password != '':
            sql += " and password like '" + password + "%'"
        if address != '':
            sql += " and address like '" + address + "%'"
        if gender != '':
            sql += " and gender like '" + gender + "%'"
        if dob != 0:
            sql += " and dob = " + str(dob)
        if college_id != '':
            sql += " and college_id like '" + college_id + "%'"
        if college_name !='':
            sql += " and college_name like '" + college_name + "%'"
        if course_id != '':
            sql += " and course_id like '" + course_id + "%'"
        if course_name !='':
            sql += " and course_name like '" + course_name + "%'"
        if subject_id != '':
            sql += " and subject_id like '" + subject_id + "%'"
        if subject_name !='':
            sql += " and subject_name like '" + subject_name + "%'"
        if (page_size > 0):
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_Name = (
            "id", "first_name", "last_name", "email", "password", "address", "gender", "dob", "college_id",
            "college_name", "course_id", "course_name",
            "subject_id", "subject_name")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_Name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
