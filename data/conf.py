import os  # Подключение модуля OS - адаптация пути к файлам в ОС.

BASE_PATH = os.path.abspath("../data")  # Применение абсолютного пути.

FILE_JSON = os.path.join(BASE_PATH, "operations.json")  # путь к файлу json с вопросами

# print(BASE_PATH)
# print(FILE_JSON)
