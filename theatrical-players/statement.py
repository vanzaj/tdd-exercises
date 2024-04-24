import math



def statement(invoice, plays):
    def usd(cents):
        return f"${cents/100:0,.2f}"


    def is_comedy(play):
        return play["type"] == "comedy"


    def play_for(aPerformance):
        return plays[aPerformance["playID"]]


    def amount_for(aPerformance):
        result = 0
        play = play_for(aPerformance)
        if play["type"] == "tragedy":
            result = 40000
            if aPerformance["audience"] > 30:
                result += 1000 * (aPerformance["audience"] - 30)
        elif is_comedy(play):
            result = 30000
            if aPerformance["audience"] > 20:
                result += 10000 + 500 * (aPerformance["audience"] - 20)
            result += 300 * aPerformance["audience"]
        else:
            raise ValueError(f'unknown type: {play["type"]}')
        return result


    def volume_credits_for(nb_pax, is_comedy=False):
        result = math.floor(nb_pax / 5) if is_comedy else 0
        return result + max(nb_pax - 30, 0)


    def total_volume_credits():
        result = 0
        for perf in invoice["performances"]:
            result += volume_credits_for(perf["audience"], is_comedy(play_for(perf)))
        return result

    def total_amount():
        result = 0
        for perf in invoice["performances"]:
            result += amount_for(perf)
        return result


    result = f'Statement for {invoice["customer"]}\n'
    for perf in invoice["performances"]:
        result += f' {play_for(perf)["name"]}: {usd(amount_for(perf))} ({perf["audience"]} seats)\n'

    result += f"Amount owed is {usd(total_amount())}\n"
    result += f"You earned {total_volume_credits()} credits\n"
    return result


