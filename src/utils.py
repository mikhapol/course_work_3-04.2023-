import json  # импортирование json

# импортирование функций из других файлов
from datetime import datetime
from data.conf import FILE_JSON
from src.classes.Class_Currency import Currency
from src.classes.Class_OperationAmount import OperationAmount
from src.classes.Class_Operations import Operation


# ФУНКЦИИ
def load_file_json():
    """Считывает файл па пути FILE_JSON, и преобразует формат JSON в объект Python.
    Возвращает информацию из файла формата JSON в виде объекта Python"""
    with open(FILE_JSON, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_operation_json(operations_json):
    """Создаёт питон объект (из json'а) переводит в объект класса"""
    result = []
    for operation in operations_json:
        result.append(Operation(operation.get('id'),
                                operation.get('state'),
                                time_operation_format(operation.get('date')),
                                OperationAmount(mapper_amount(operation.get('operationAmount')),
                                                mapper_currency(operation.get('operationAmount'))),
                                operation.get('description'),
                                operation.get('from'),
                                operation.get('to'), ))
    return result


def time_operation_format(date):
    """Есть дата, возвращает type data.
    В случаи отсутствии даты, возвращает None"""
    if date is not None:
        return datetime.fromisoformat(date)
    return None


def mapper_amount(operationAmount):
    """Проверяет наличие данных в amount"""
    if operationAmount is not None:
        return operationAmount.get('amount')
    return None


def mapper_currency(operationAmount):
    """Первым этапом проверяет наличие данных в operationAmount, если есть, проверяет наличие данных в currency,
    в зависимости от наличия данных возвращает информацию"""
    if operationAmount is not None:
        if operationAmount.get('currency') is not None:
            return Currency(operationAmount.get('currency').get('name'),
                            operationAmount.get('currency').get('code'))
    return None


def status_executed(operations):
    """Возвращает список с выполненными статусами"""
    operations_executed = []
    for operation in operations:
        if operation.get_state() == "EXECUTED":
            operations_executed.append(operation)
    return operations_executed


def status_canceled(operations):
    """Возвращает список с отменёнными статусами"""
    operations_canceled = []
    for operation in operations:
        if operation.get_state() == "CANCELED":
            operations_canceled.append(operation)
    return operations_canceled


def sort_date(operations):
    """Сортирует список по дате от новых к старым"""
    return sorted(operations, key=lambda x: (x.get_date() is not None, x.get_date()), reverse=True)


def first_five_operations(operations):
    """Вернёт первые пять операций методом среза"""
    return operations[:5]


def str_operations(operations):
    """Вернет запрашиваемый формат"""
    result = ""
    for operation in operations:
        result += "\n" + operation.get_date_form() + " " + operation.get_description() + "\n"
        result += operation.get_from_operation_mask() + " -> " + operation.get_to_operation_mask() + "\n"
        result += operation.get_operation_amount().get_amount() + " " \
                  + operation.get_operation_amount().get_currency_get_name() + "\n"
    return result
