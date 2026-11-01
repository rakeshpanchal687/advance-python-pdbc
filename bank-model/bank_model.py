import pymysql
class BankModel:
    def next_pk(self):
        pk=0
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select max(id) from bank"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add (self, data):
        id = BankModel.next_pk(self)
        custmer_name = data['custmer_name']
        bank_name = data['bank_name']
        account_no = data['account_no']
        account_balance = data['account_balance']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "insert into bank values(%s, %s, %s, %s, %s)"
        data = (id, custmer_name, bank_name, account_no, account_balance)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self, data):
        id = data['id']
        custmer_name = data['custmer_name']
        bank_name = data['bank_name']
        account_no = data['account_no']
        account_balance = data['account_balance']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "update bank set custmer_name = %s, bank_name = %s, account_no = %s, account_balance = %s where id = %s"
        data = (custmer_name, bank_name, account_no, account_balance, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "delete from bank where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def get(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from bank where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def find_by_Name(self, name):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", database="advance_python")
        cursor = connection.cursor()
        sql = "select * from bank where custmer_name = %s"
        data = (name,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def search(self, params):
        pageNo = params['pageNo']
        pageSize = params['pageSize']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from bank where 1=1"
        if 'id' in params and params['id'] != 0:
            sql += " and id = %s" % params['id']
        if 'custmer_name' in params:
            sql += " and custmer_name like '%" + params['custmer_name'] + "%'"
        if 'bank_name' in params:
            sql += " and bank_name like '%" + params['bank_name'] + "%'"
        if 'account_no' in params:
            sql += " and account_no like '%" + params['account_no'] + "%'"
        if 'account_balance' in params:
            sql += " and account_balance = %s" % params['account_balance']
        sql += " limit %s, %s" % ((pageNo - 1) * pageSize, pageSize)
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "custmer_name", "bank_name", "account_no", "account_balance")
        list = []
        for x in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list


