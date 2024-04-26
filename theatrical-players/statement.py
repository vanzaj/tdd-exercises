from math import floor


class Calculator:
    def __init__(self, invoice, plays):
        self.customer = invoice["customer"]
        self.performances = invoice["performances"]
        self.plays = plays

    def get_play_for(self, perf):
        return self.plays[perf["playID"]]

    @property
    def total_cost(self):
        result = 0
        for perf in self.performances:
            result += APerformance(perf, self.get_play_for(perf)).cost
        return result

    @property
    def total_volume_credits(self):
        result = 0
        for perf in self.performances:
            result += APerformance(perf, self.plays[perf["playID"]]).volume_credits
        return result


class APerformance:
    def __init__(self, perf, play):
        self.perf = perf
        self.play = play

    @property
    def name(self):
        return self.play["name"]

    @property
    def type(self):
        return self.play["type"]

    @property
    def audience(self):
        return self.perf["audience"]

    @property
    def cost(self):
        result = 0
        if self.type == "tragedy":
            result = 40000
            if self.audience > 30:
                result += 1000 * (self.audience - 30)
        elif self.type == "comedy":
            result = 30000
            if self.audience > 20:
                result += 10000 + 500 * (self.audience - 20)
            result += 300 * self.audience
        else:
            raise ValueError(f"unknown type: {self.type}")
        return result

    @property
    def volume_credits(self):
        result = max(self.audience - 30, 0)
        if self.type == "comedy":
            result += floor(self.audience / 5)
        return result


def usd(cents):
    return f"${cents/100:0,.2f}"


def render_plain_text(calculator):
    result = f"Statement for {calculator.customer}\n"
    for perf in calculator.performances:
        aperf = APerformance(perf, calculator.get_play_for(perf))
        result += f" {aperf.name}: {usd(aperf.cost)} ({aperf.audience} seats)\n"

    result += f"Amount owed is {usd(calculator.total_cost)}\n"
    result += f"You earned {calculator.total_volume_credits} credits\n"
    return result


def statement(invoice, plays):
    calc = Calculator(invoice, plays)
    return render_plain_text(calc)
