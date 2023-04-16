class OperationAmount:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def get_amount(self):
        if self.amount is not None:
            return self.amount
        return ""

    def get_currency(self):
        return self.currency

    def get_currency_get_name(self):
        if self.get_currency() is not None:
            return self.get_currency().get_name()
        return ""


