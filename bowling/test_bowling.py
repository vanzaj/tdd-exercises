import pytest
from bowling import BowlingGame


@pytest.fixture
def game():
    yield BowlingGame()


def test_new_bowling_game(game):
    assert isinstance(game, object)


def test_rolls(game):
    game.rolls([1, 2])
    assert game._rolls == [1, 2]
    assert game.score() == 3
