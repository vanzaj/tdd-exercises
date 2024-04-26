import pytest
from statement import statement


@pytest.fixture
def plays():
    return {
        "hamlet": {"type": "tragedy", "name": "Hamlet"},
        "pies": {"type": "comedy", "name": "Lord of Pies"},
        "foobar": {"type": "neither", "name": "FooBar"},
    }


@pytest.fixture
def invoice():
    def _make_invoice(playID, audience):
        return {
            "customer": "BigCo",
            "performances": [{"playID": playID, "audience": audience}],
        }

    return _make_invoice


def test_statement_for_two_plays(invoice, plays):
    inv = invoice("hamlet", 1)
    inv["performances"].append({"playID": "pies", "audience": 1})
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Hamlet: $400.00 (1 seats)
 Lord of Pies: $303.00 (1 seats)
Amount owed is $703.00
You earned 0 credits
"""
    )


def test_statement_for_two_plays_with_many_attendies(invoice, plays):
    inv = invoice("hamlet", 31)
    inv["performances"].append({"playID": "pies", "audience": 31})
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Hamlet: $410.00 (31 seats)
 Lord of Pies: $548.00 (31 seats)
Amount owed is $958.00
You earned 8 credits
"""
    )


def test_statement_comedy_1pax(invoice, plays):
    inv = invoice("pies", 1)
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Lord of Pies: $303.00 (1 seats)
Amount owed is $303.00
You earned 0 credits
"""
    )


def test_statement_comedy_21pax(invoice, plays):
    inv = invoice("pies", 21)
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Lord of Pies: $468.00 (21 seats)
Amount owed is $468.00
You earned 4 credits
"""
    )


def test_statement_unknown_type(invoice, plays):
    inv = invoice("foobar", 1)
    with pytest.raises(ValueError):
        x = statement(inv, plays)
