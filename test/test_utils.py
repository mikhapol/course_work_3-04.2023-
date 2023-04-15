from main.classes.Class_Operations import Operation
from main.utils import load_file_json, load_operation_json, status_executed, sort_date, first_five_operations, \
    str_operations


def test_load_file_json():
    load = load_file_json()

    assert load is not None
    assert load[0].get('id') == 441945886
    assert len(load) >= 101


def test_load_operation_json():
    load = load_operation_json(load_file_json())

    assert load is not None
    assert load[0].get_date_form() == '26.08.2019'
    assert load[0].get_id() == 441945886
    assert load[1].state == "EXECUTED"
    assert load[2].get_date_form() == "30.06.2018"
    assert load[3].description == "Открытие вклада"
    assert load[4].from_operation == "Счет 19708645243227258542"
    assert load[5].to_operation == "Счет 74489636417521191160"
    assert len(load) >= 101

    assert load[0].operationAmount.amount == "31957.58"
    assert load[0].operationAmount.currency.name == "руб."


def test_status_executed():
    load = status_executed(load_operation_json(load_file_json()))

    assert load is not None
    assert load[0].get_date_form() == '26.08.2019'
    assert load[0].id == 441945886
    assert load[1].state == "EXECUTED"
    assert load[2].get_date_form() == "30.06.2018"
    assert load[3].description == "Открытие вклада"
    assert load[4].from_operation == "Счет 19708645243227258542"
    assert load[5].to_operation == "Счет 74489636417521191160"
    assert len(load) >= 85


def test_sort_date():
    load = sort_date(status_executed(load_operation_json(load_file_json())))

    assert load is not None
    assert len(load) >= 85
    assert load[0].date > load[1].date
    assert load[1].date > load[2].date
    assert load[2].date > load[3].date
    assert load[len(load) - 2].date > load[len(load) - 1].date


def test_sort_date_not_exception():
    load = load_operation_json(load_file_json())

    assert load is not None
    assert load[0].get_date_form() == '26.08.2019'
    assert load[0].id == 441945886
    assert load[1].state == "EXECUTED"
    assert load[2].get_date_form() == "30.06.2018"
    assert load[3].description == "Открытие вклада"
    assert load[4].from_operation == "Счет 19708645243227258542"
    assert load[5].to_operation == "Счет 74489636417521191160"
    assert len(load) >= 101

    load_sort = sort_date(load)

    assert load_sort is not None
    assert len(load_sort) >= 85
    assert load_sort[0].date > load_sort[1].date
    assert load_sort[1].date > load_sort[2].date
    assert load_sort[2].date > load_sort[3].date
    assert load_sort[len(load_sort) - 1].date is None
    assert len(load_sort) >= 101


def test_first_five_operations():
    load = first_five_operations(sort_date(status_executed(load_operation_json(load_file_json()))))

    assert load is not None
    assert len(load) == 5
    assert load[0].date > load[1].date
    assert load[1].date > load[2].date
    assert load[2].date > load[3].date
    assert load[len(load) - 2].date > load[len(load) - 1].date
    assert load[1].state == "EXECUTED"


def test_real_first_five_operations():
    test_list = [Operation(1, "EXECUTED", None, None, None, None, None),
                 Operation(2, "EXECUTED", None, None, None, None, None),
                 Operation(3, "EXECUTED", None, None, None, None, None)]
    load = first_five_operations(status_executed(test_list))

    assert load is not None
    assert len(load) == 3
    assert load[1].state == "EXECUTED"
    assert load[2].state == "EXECUTED"
    assert load[0].id == 1


def test_str_operations():
    str = str_operations(first_five_operations(sort_date(status_executed(load_operation_json(load_file_json())))))

    assert str is not None
    print("\n")
    print(str)
