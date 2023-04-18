from src.classes.Class_Operations import Operation
from src.main import main
from src.utils import load_file_json, load_operation_json, status_executed, sort_date, first_five_operations, \
    str_operations, status_canceled


def test_load_file_json():
    """Тест на получение данных из файла json"""
    load = load_file_json()

    assert load is not None
    assert load[0].get('id') == 441945886
    assert len(load) >= 101


def test_load_operation_json():
    """Тест на приём нужной информации из json"""
    load = load_operation_json(load_file_json())

    assert load is not None
    assert load[0].get_date_form() == '26.08.2019'
    assert load[0].get_id() == 441945886
    assert load[1].get_state() == "EXECUTED"
    assert load[2].get_date_form() == "30.06.2018"
    assert load[3].get_description() == "Открытие вклада"
    assert load[4].get_from_operation() == "Счет 19708645243227258542"
    assert load[5].get_to_operation() == "Счет 74489636417521191160"
    assert len(load) >= 101
    assert load[0].get_operation_amount().amount == "31957.58"
    assert load[0].get_operation_amount().currency.name == "руб."
    assert load[-1].get_id() == 667307132


def test_status_executed():
    """Тестирование функции status_executed"""
    load = status_executed(load_operation_json(load_file_json()))

    assert load is not None
    assert load[0].get_date_form() == '26.08.2019'
    assert load[0].get_id() == 441945886
    assert load[1].get_state() == "EXECUTED"
    assert load[2].get_date_form() == "30.06.2018"
    assert load[3].get_description() == "Открытие вклада"
    assert load[4].get_from_operation() == "Счет 19708645243227258542"
    assert load[5].get_to_operation() == "Счет 74489636417521191160"
    assert len(load) >= 85


def test_status_canceled():
    """Тестирование функции status_canceled"""
    load = status_canceled(load_operation_json(load_file_json()))

    assert load is not None
    assert load[0].get_date_form() == '12.09.2018'
    assert load[0].get_id() == 594226727
    assert load[1].get_state() == "CANCELED"
    assert load[2].get_date_form() == "23.11.2018"
    assert load[3].get_description() == "Перевод организации"
    assert load[4].get_from_operation() == "Visa Gold 6527183396477720"
    assert load[5].get_to_operation() == "Счет 19213886662094884261"
    assert len(load) <= 15


def test_sort_date():
    """Тестирование функции sort_date"""
    load = sort_date(status_executed(load_operation_json(load_file_json())))

    assert load is not None
    assert len(load) >= 85
    assert load[0].date > load[1].date
    assert load[1].date > load[2].date
    assert load[2].date > load[3].date
    assert load[len(load) - 2].date > load[len(load) - 1].date


def test_load_operation_json_not_exception():
    """Тестирование всего списка без исключения отменённых операций"""
    load = load_operation_json(load_file_json())

    assert load is not None
    assert load[0].get_date_form() == '26.08.2019'
    assert load[0].get_id() == 441945886
    assert load[1].get_state() == "EXECUTED"
    assert load[2].get_date_form() == "30.06.2018"
    assert load[3].get_description() == "Открытие вклада"
    assert load[4].get_from_operation() == "Счет 19708645243227258542"
    assert load[5].get_to_operation() == "Счет 74489636417521191160"
    assert len(load) >= 101

    # Тестирование всего списка отсортированного по дате
    load_sort = sort_date(load)

    assert load_sort is not None
    assert len(load_sort) >= 101
    assert load_sort[0].date > load_sort[1].date
    assert load_sort[1].date > load_sort[2].date
    assert load_sort[2].date > load_sort[3].date
    assert load_sort[len(load_sort) - 1].date is None


def test_first_five_operations():
    """Тестирование функции first_five_operations"""
    load = first_five_operations(sort_date(status_executed(load_operation_json(load_file_json()))))

    assert load is not None
    assert len(load) == 5
    assert load[0].date > load[1].date
    assert load[1].date > load[2].date
    assert load[2].date > load[3].date
    assert load[len(load) - 2].date > load[len(load) - 1].date
    assert load[1].get_state() == "EXECUTED"


def test_real_first_five_operations():
    """Тестирование функции first_five_operations если список приходит из другого источника"""
    test_list = [Operation(1, "EXECUTED", None, None, None, None, None),
                 Operation(2, "CANCELED", None, None, None, None, None),
                 Operation(3, "EXECUTED", None, None, None, None, None),
                 Operation(4, "EXECUTED", None, None, None, None, None),
                 Operation(5, "EXECUTED", None, None, None, None, None),
                 Operation(6, "EXECUTED", None, None, None, None, None),
                 Operation(7, "EXECUTED", None, None, None, None, None),
                 Operation(8, "EXECUTED", None, None, None, None, None)]

    # Тестирование первых пяти из стороннего списка
    load = first_five_operations(status_executed(test_list))

    assert load is not None
    assert load[1].get_date_form() == ""
    assert load[2].get_description() == ""
    assert len(load) == 5
    assert load[0].id == 1
    assert load[1].get_state() == "EXECUTED"
    assert load[2].get_state() == "EXECUTED"


def test_get_to_operation_mask():
    """Тестирование функции get_to_operation_mask используя первые пять"""
    operation = first_five_operations(sort_date(status_executed(load_operation_json(load_file_json()))))

    assert operation is not None

    assert operation[0].get_to_operation_mask() == 'Счет **5907'
    assert operation[1].get_to_operation_mask() == 'Счет **3655'
    assert operation[2].get_to_operation_mask() == 'Счет **2869'
    assert operation[3].get_to_operation_mask() == 'Счет **8125'
    assert operation[4].get_to_operation_mask() == 'Счет **8381'


def test_get_to_operation_mask_set():
    """Тестирование функции get_to_operation_mask используя первые пять из SET"""
    operation = first_five_operations(sort_date(status_executed(load_operation_json(load_file_json()))))

    assert operation is not None

    # Использование сторонних входных данных подменяя существующие через SET
    operation[0].set_to_operation("Visa Platinum 8990922113665229")
    operation[1].set_to_operation(None)
    operation[2].set_to_operation("96527012349577388613")
    operation[3].set_to_operation("")
    operation[4].set_to_operation("Счет")

    assert operation[0].get_to_operation_mask() == 'Visa Platinum 8990 92** **** 5229'
    assert operation[1].get_to_operation_mask() == 'Перевод организации'
    assert operation[2].get_to_operation_mask() == 'Счет **8613'
    assert len(operation) == 5


def test_get_from_operation_mask():
    """Тестирование функции get_from_operation_mask"""
    operation = first_five_operations(sort_date(status_executed(load_operation_json(load_file_json()))))

    assert operation is not None

    assert operation[0].get_from_operation_mask() == 'Открытие вклада'
    assert operation[1].get_from_operation_mask() == 'Visa Classic 2842 87** **** 9012'
    assert operation[2].get_from_operation_mask() == 'Maestro 7810 84** **** 5568'
    assert operation[3].get_from_operation_mask() == 'Счет **9794'
    assert operation[4].get_from_operation_mask() == 'Открытие вклада'


def test_get_from_operation_mask_set():
    """Тестирование функции get_from_operation_mask используя SET"""
    operation = first_five_operations(sort_date(status_executed(load_operation_json(load_file_json()))))

    assert operation is not None

    # Использование сторонних входных данных подменяя существующие через SET
    operation[0].set_from_operation("Visa Platinum 8990922113665229")
    operation[1].set_from_operation(None)
    operation[2].set_from_operation("96527012349577388613")
    operation[3].set_from_operation("")
    operation[4].set_from_operation("Счет")

    assert operation[0].get_from_operation_mask() == 'Visa Platinum 8990 92** **** 5229'
    assert operation[1].get_from_operation_mask() == 'Перевод организации'
    assert operation[2].get_from_operation_mask() == 'Счет **8613'
    assert operation[3].get_from_operation_mask() == 'Перевод со счета на счет'
    assert operation[4].get_from_operation_mask() == 'Открытие вклада'


# def test_str_operations_all():
#     """Тестирование функции str_operations всего отсортированного списка"""
#     str_all = str_operations(sort_date((load_operation_json(load_file_json()))))
#
#     assert str_all is not None


def test_str_operations_main():
    """Тестирование функции str_operations первых 5 отсортированных"""
    str_main = str_operations(first_five_operations(sort_date(status_executed(load_operation_json(load_file_json())))))

    assert str_main is not None
    assert "21344.35 руб." in str_main
    assert "Счет **9794 -> Счет **8125" in str_main
    assert "19.11.2019 Перевод организации" in str_main
    assert "BYN" not in str_main


def test_main():
    assert main() is None
