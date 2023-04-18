class Operation:
    def __init__(self, id, state, date, operationAmount, description, from_operation, to_operation):
        self.id = id
        self.state = state
        self.date = date
        self.operation_amount = operationAmount
        self.description = description
        self.from_operation = from_operation
        self.to_operation = to_operation

    def get_id(self):
        return self.id

    def get_state(self):
        return self.state

    def get_date_form(self):
        """Возвращает дату в требуемом формате"""
        if self.get_date() is not None:
            return self.get_date().strftime("%d.%m.%Y")
        return ""

    def get_to_operation(self):
        if self.to_operation is not None:
            return self.to_operation
        return ""

    def set_to_operation(self, to_operation):
        self.to_operation = to_operation

    def set_from_operation(self, from_operation):
        self.from_operation = from_operation

    def get_to_operation_mask(self):
        """Данные карты или счёта скрыты '*'"""
        if (len(self.get_to_operation()) != 0) and self.get_to_operation().split()[-1].isdigit() is True:
            numbers = self.get_to_operation().split()[-1]
            if len(numbers) > 16:
                return f"Счет **{numbers[-4:]}"
            else:
                return f'{" ".join(self.get_to_operation().split()[:-1])} ' \
                       f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
        return self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        return ""

    def get_operation_amount(self):
        return self.operation_amount

    def get_date(self):
        return self.date

    def get_from_operation(self):
        if self.from_operation is not None:
            return self.from_operation
        return self.description

    def get_from_operation_mask(self):
        if (len(self.get_from_operation()) != 0) and self.get_from_operation().split()[-1].isdigit() is True:
            numbers = self.from_operation.split()[-1]
            if len(numbers) > 16:
                return f"Счет **{numbers[-4:]}"
            else:
                return f'{" ".join(self.from_operation.split()[:-1])} ' \
                       f'{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}'
        return self.description

    def __repr__(self):
        return f"Дата: self.date={self.get_date_form()}, " \
               f"self.get_from_operation()={self.get_from_operation()}, " \
               f"self.get_to_operation()={self.get_to_operation()}"
