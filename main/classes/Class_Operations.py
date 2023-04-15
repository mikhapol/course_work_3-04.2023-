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
        return self.id

    def get_date_form(self):
        return self.date.strftime("%d.%m.%Y")

    def get_to_operation(self):
        if self.to_operation is not None:
            return self.to_operation
        return ""

    def get_to_operation_mask(self):
        if self.to_operation is not None:
            return self.to_operation
        return ""

    def get_from_operation(self):
        if self.from_operation is not None:
            return self.from_operation
        return "Открытие вклада"

    def __repr__(self):
        return f"Дата: self.date={self.date}, self.get_from_operation()={self.get_from_operation()}, self.get_to_operation()={self.get_to_operation()}"
