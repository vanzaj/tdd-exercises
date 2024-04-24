import math

def is_comedy(play):
    return play["type"] == "comedy"


def amount_for(perf, play):
    result = 0
    if play["type"] == "tragedy":
        result = 40000
        if perf["audience"] > 30:
            result += 1000 * (perf["audience"] - 30)
    elif is_comedy(play):
        result = 30000
        if perf["audience"] > 20:
            result += 10000 + 500 * (perf["audience"] - 20)
        result += 300 * perf["audience"]
    else:
        raise ValueError(f'unknown type: {play["type"]}')
    return result


def calculate_volume_credits(nb_pax, is_comedy=False):
    if is_comedy :
        volume_credits = math.floor(nb_pax / 5)
    else:
        volume_credits = 0
    return volume_credits + max(nb_pax - 30, 0)


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(cents):
        return f"${cents/100:0,.2f}"

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = amount_for(perf, play)
        total_amount += this_amount
        result += f' {play["name"]}: {format_as_dollars(this_amount)} ({perf["audience"]} seats)\n'
        
        nb_pax = perf["audience"]
        volume_credits += calculate_volume_credits(nb_pax, is_comedy(play))


    result += f"Amount owed is {format_as_dollars(total_amount)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


