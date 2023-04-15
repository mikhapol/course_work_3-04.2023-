class Operation:
    def __init__(self, id, state, date, operationAmount, description, from_operation, to_operation):
        self.id = id
        self.state = state
        self.date = date
        self.operationAmount = operationAmount
        self.description = description
        self.from_operation = from_operation
        self.to_operation = to_operation

    def get_id(self):
        """???"""
        return self.id

    def get_state(self):
        """???"""
        return self.state

    def get_date_form(self):
        """Возвращает дату в требуемом формате"""
        return self.date.strftime("%d.%m.%Y")

    def get_to_operation(self):
        """Проверка на наличие данных в графе 'to':"""
        if self.to_operation is not None:
            return self.to_operation
        return ""

    def get_to_operation_mask(self):
        """Данные карты или счёта скрыты '*'"""
        if self.to_operation is not None:
            if self.to_operation.split()[-1].isdigit() is True:
                numbers = self.to_operation.split()[-1]
            if len(numbers) > 16:
                return f"Счет **{numbers[-4:]}"
            else:
                return f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
        return "Нет данных"

    def get_from_operation(self):
        if self.from_operation is not None:
            return self.from_operation
        return "Открытие вклада"

    def get_from_operation_mask(self):
        if self.from_operation is not None:
            if self.from_operation.split()[-1].isdigit() is True:
                numbers = self.from_operation.split()[-1]
            if len(numbers) > 16:
                return f"Счет **{numbers[-4:]}"
            else:
                return f'{" ".join(self.from_operation.split()[:-1])} ' \
                       f'{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}'
        return "Открытие вклада"

    def __repr__(self):
        return f"Дата: self.date={self.date}, " \
               f"self.get_from_operation()={self.get_from_operation()}, " \
               f"self.get_to_operation()={self.get_to_operation()}"
