from utils import sort_by_executed, sort_by_data



def test_executed_operations():
    assert sort_by_executed.executed_operations('ops.json') == [{'date': '26.08.2019 10:50:58', 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}}]

#def test_executed_operations_2():
    #assert sort_by_executed.executed_operations('ops_empty.json') ==

def test_sort_by_data():
    assert sort_by_data.sort_by_data([{'date': '26.08.2019 10:50:58'}, {'date': '21.09.2011 10:50:58'}, {'date': '24.08.2019 10:50:58'}]) == [{'date': '26.08.2019 10:50:58'}, {'date': '24.08.2019 10:50:58'}, {'date': '21.09.2011 10:50:58'}]

