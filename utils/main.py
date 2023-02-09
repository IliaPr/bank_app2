from sort_by_executed import executed_operations
from sort_by_data import sort_by_data, last_five_ops

#Вызов функций
executed_operations = executed_operations('operations.json')
list_of_operations = sort_by_data(executed_operations)
last_five_ops(list_of_operations)
