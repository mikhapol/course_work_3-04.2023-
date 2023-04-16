from utils import *


def main():
    """Печать всех условий необходимых для вывода по заданию"""
    print(str_operations(first_five_operations(sort_date(status_executed(load_operation_json(load_file_json()))))))


main()
