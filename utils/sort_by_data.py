from datetime import datetime

def sort_by_data(operation):
    list_of_operations = sorted(operation, key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y %H:%M:%S'), reverse=True)
    return list_of_operations
def last_five_ops(list_of_operations):
    for ops in list_of_operations[0:5]:
        date = ops['date']
        desc = ops['description']
        card_bill_from = ops['from']
        if 'Счет' in card_bill_from:
            bill_name = 'Счет '
            sender = bill_name + '*' * len(card_bill_from[:-4]) + card_bill_from[-4:]
        else:
            card_number = card_bill_from.split()[-1]
            private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
            chunks, chunk_size = len(private_number), len(private_number) // 4
            spaces = " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
            card_name = card_bill_from.split()
            card_name2 = card_name[:-1]
            full_card_name = ' '.join(card_name2)
            sender = full_card_name + ' ' + spaces
        bill_to = ops['to']
        stars ='Счет ' + '*' * len(bill_to[:-4]) + bill_to[-4:]
        summ = ops['operationAmount']['amount']
        curr = ops['operationAmount']['currency']['name']
        print(f'{date} {desc}\n{sender} -> {stars}\n{summ} {curr}\n')
