class OperationAmount:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def get_amount(self):
        if self.amount is not None:
            return self.amount
        return ""

