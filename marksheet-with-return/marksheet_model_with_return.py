import pymysql


class MarksheetModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet"
        cursor.execute(sql)
        result = cursor.fetchall()
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
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
        data = (id, roll_no, name, physics, chemistry, maths)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "update marksheet set roll_no = %s, name = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
        data = (roll_no, name, physics, chemistry, maths, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advance_python')
        cursor = connection.cursor()

        sql = "SELECT * FROM marksheet WHERE id = %s"
        data = (id,)

        cursor.execute(sql, data)
        result = cursor.fetchall()

        res = []  # Ye line zaroori hai

        columnName = ['id', 'roll_no', 'name','physics', 'chemistry', 'maths' ]

        for x in result:
            res.append({columnName[i]: x[i]for i, _ in enumerate(x)})
        cursor.close()
        connection.close()
        return res

    def findByRoll(self, roll_no):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()

        sql = "SELECT * FROM marksheet WHERE roll_no = %s"
        data = (roll_no,)

        cursor.execute(sql, data)
        result = cursor.fetchall()

        res = []  # YAHI LINE MISSING THI

        columnName = ['id', 'roll_no', 'name', 'physics', 'chemistry', 'maths']

        for x in result:
            res.append({
                columnName[i]: x[i]
                for i, _ in enumerate(x)
            })

        cursor.close()
        connection.close()

        return res

    def search(self, param):
        id = param.get('id', 0)
        roll_no = param.get('roll_no', '')
        name = param.get('name', '')
        physics = param.get('physics', 0)
        chemistry = param.get('chemistry', 0)
        maths = param.get('maths', 0)
        page_no = param.get('page_no', 0)
        page_size = param.get('page_size', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from marksheet where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if roll_no != 0:
            sql += " and name like '" + roll_no + "%'"
        if name != '':
            sql += " and name = '" + name + "%'"
        if physics != 0:
            sql += " and physics = " + str(physics)
        if chemistry != 0:
            sql += " and chemistry = " + str(chemistry)
        if maths != 0:
            sql += " and maths = " + str(maths)

        if page_size > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "roll_no", "name", "physics", "chemistry", "maths")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res
