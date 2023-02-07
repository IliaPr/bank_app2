from datetime import datetime
import json


def executed_operations(filename):
    with open(filename, 'r') as file:
        operations = json.load(file)
    operation = []
    for oper in operations:
        if not (oper.get('from') and oper.get('state')):
            continue
        if oper['state'] == 'EXECUTED':
            date = datetime.strptime(oper['date'], '%Y-%m-%dT%H:%M:%S.%f')
            date = date.strftime('%d.%m.%Y %H:%M:%S')
            operation.append({'date': date,
                          'description': oper['description'],
                          'from': oper['from'],
                          'to': oper['to'],
                          'operationAmount': oper['operationAmount']
                          })

    return operation