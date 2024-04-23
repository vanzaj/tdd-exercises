import pytest
from statement import statement


@pytest.fixture
def plays():
    return [
        {"type": "tragedy", "name": "Hamlet"},
        {"type": "comedy", "name": "Lord of Pies"},
        {"type": "neither", "name": "FooBar"},
    ]


@pytest.fixture
def invoice():
    def _make_invoice(playID, audience):
        return {
            "customer": "BigCo",
            "performances": [{"playID": playID, "audience": audience}],
        }

    return _make_invoice


def test_statement_tradegy_10pax(invoice, plays):
    inv = invoice(0, 10)
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Hamlet: $400.00 (10 seats)
Amount owed is $400.00
You earned 0 credits
"""
    )


def test_statement_tradegy_31pax(invoice, plays):
    inv = invoice(0, 31)
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Hamlet: $410.00 (31 seats)
Amount owed is $410.00
You earned 1 credits
"""
    )


def test_statement_comedy_1pax(invoice, plays):
    inv = invoice(1, 1)
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Lord of Pies: $303.00 (1 seats)
Amount owed is $303.00
You earned 0 credits
"""
    )


def test_statement_comedy_21pax(invoice, plays):
    inv = invoice(1, 21)
    assert (
        statement(inv, plays)
        == """Statement for BigCo
 Lord of Pies: $468.00 (21 seats)
Amount owed is $468.00
You earned 4 credits
"""
    )


def test_statement_unknown_type(invoice, plays):
    inv = invoice(2, 1)
    with pytest.raises(ValueError):
        x = statement(inv, plays)

