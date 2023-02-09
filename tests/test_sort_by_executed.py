import json.decoder

import pytest

from utils import sort_by_executed, sort_by_data



def test_executed_operations():
    assert sort_by_executed.executed_operations('ops.json') == [{'date': '26.08.2019 10:50:58', 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}}]

def test_executed_operations_2():
    with pytest.raises(KeyError):
        sort_by_executed.executed_operations('ops_empty.json')

def test_executed_operations_3():
    with pytest.raises(json.decoder.JSONDecodeError):
        sort_by_executed.executed_operations('ops_emp.json')

def test_sort_by_data():
    assert sort_by_data.sort_by_data([{'date': '26.08.2019 10:50:58'}, {'date': '21.09.2011 10:50:58'}, {'date': '24.08.2019 10:50:58'}]) == [{'date': '26.08.2019 10:50:58'}, {'date': '24.08.2019 10:50:58'}, {'date': '21.09.2011 10:50:58'}]

def test_last_five_ops():
    assert sort_by_data.last_five_ops([{'date': '26.08.2019 10:50:58', 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}}]) == print(f'26.08.2019 10:50:58 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет ****************9589\n31957.58 руб.\n')
    assert sort_by_data.last_five_ops([]) == None
