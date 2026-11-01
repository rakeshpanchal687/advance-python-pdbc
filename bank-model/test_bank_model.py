from Functions.Marks import rakesh
from bank_model import BankModel

def test_add():
    data = {
        'custmer_name': 'Harsh',
        'bank_name': 'SBI',
        'account_no': '1234567890',
        'account_balance': 10000,
        'custmer_name': 'rakesh',
        'bank_name': 'HDFC',
        'account_no': '0987654321',
        'account_balance': 5000,
        'custmer_name': 'Ramesh',
        'bank_name': 'ICICI',
        'account_no': '5678901234',
        'account_balance': 2000,
    }
    model = BankModel()
    model.add(data)

def test_update():
    data = {
        'id': 2,
        'custmer_name': 'Rakesh',
        'bank_name': 'HDFC',
        'account_no': '0987654321',
        'account_balance': 100000,
    }
    model = BankModel()
    model.update(data)
def test_delete():
    id = 3
    model = BankModel()
    model.delete(id)

def find_by_Name():
    name = 'Harsh'
    model = BankModel()
    result = model.find_by_Name('harsh')
    print(result)

def test_search():
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5
    model = BankModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['custmer_name'], '\t', data['bank_name'], '\t', data['account_no'], '\t', data['account_balance'])

# test_add()
# test_update()
# test_delete()
# find_by_Name()
# test_search()
