import pytest
from bowling import BowlingGame


@pytest.fixture
def game():
    yield BowlingGame()


def test_new_bowling_game(game):
    assert isinstance(game, object)


def test_roll_one_frame(game):
    game.rolls([1, 2])
    assert game.score() == 3


def test_rolls_with_spare(game):
    game.rolls([9, 1, 2])
    assert game.score() == 12
