import json
from datetime import datetime

from data.conf import FILE_JSON
from main.classes.Class_Currency import Currency
from main.classes.Class_OperationAmount import OperationAmount
from main.classes.Class_Operations import Operation


def load_file_json():
    """Считывает файл па пути FILE_JSON, и преобразует формат JSON в объект Python.
    Возвращает информацию из файла формата JSON в виде объекта Python"""
    with open(FILE_JSON, 'r', encoding='utf-8') as file:
        return json.load(file)


# получит список слов с внешнего ресурса, выберет случайное слово, создаст экземпляр класса basicword,
# вернет этот экземпляр.
def load_operation_json(operations_json):
    result = []
    for operation in operations_json:
        result.append(Operation(operation.get('id'),
                                operation.get('state'),
                                # 2019-08-26T10:50:58.294041
                                time_operation_format(operation.get('date')),
                                OperationAmount(mapper_amount(operation.get('operationAmount')),
                                                mapper_currency(operation.get('operationAmount'))),
                                operation.get('description'),
                                operation.get('from'),
                                operation.get('to'), ))
    return result


def time_operation_format(date):
    if date is not None:
        return datetime.fromisoformat(date)
    return None


def mapper_currency(operationAmount):
    if operationAmount is not None:
        if operationAmount.get('currency') is not None:
            return Currency(operationAmount.get('currency').get('name'),
                            operationAmount.get('currency').get('code'))
    return None


def mapper_amount(operationAmount):
    if operationAmount is not None:
        return operationAmount.get('amount')
    return None


def status_executed(operations):
    """Возвращает список с выполненными статусами"""
    operations_executed = []
    for operation in operations:
        if operation.state == "EXECUTED":
            operations_executed.append(operation)
    return operations_executed


def sort_date(operations):
    """Сортирует список по дате"""
    return sorted(operations, key=lambda x: (x.date is not None, x.date), reverse=True)


def first_five_operations(operations):
    """Вернёт первые пять операций"""
    return operations[:5]


def str_operations(operations):
    result = ""
    for operation in operations:
        result += operation.get_date_form() + " " + operation.description + "\n"
        result += operation.get_from_operation() + " -> " + operation.get_to_operation() + "\n"
        result += operation.operationAmount.get_amount() + " " + operation.operationAmount.currency.get_name() + "\n\n"
    return result
