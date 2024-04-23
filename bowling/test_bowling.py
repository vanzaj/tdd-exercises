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


def test_heart_break(game):
    game.rolls([9, 0] * 10)
    assert game.score() == 90

def test_all_spares(game):
    game.rolls([5, 5] * 10 + [5])
    assert game.score() == 150

@pytest.mark.skip('bug')
def test_perfect_game(game):
    game.rolls([10]*12)
    assert game.score() == 300

