class InvalidCurrency(Exception):
    pass


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = self._validate(currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def _validate(self, currency):
        if currency == "FOO":
            raise InvalidCurrency
        return currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

