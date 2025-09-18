from pytest_bdd import (
    given,
    when,
    then,
    scenarios,
    parsers,
)

scenarios("../bdd-features/bank.feature")


@given(parsers.parse("I have {total:d} dollars in my account"), target_fixture="balance")
def given_cucumbers(total):
    return {"total": total}


@when(parsers.parse("I withdraw {amount:d} dollars"))
def eat_cucumbers(balance, amount):
    balance["amount"] = -amount


@then(parsers.parse("I should have {total:d} dollars in my account"))
def should_have_left_cucumbers(balance, total):
    assert balance["total"] + balance["amount"] == total
