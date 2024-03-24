import pytest
from bowling import BowlingGame

@pytest.fixture
def game():
  yield BowlingGame()

def test_new_bowling_game(game):
  assert isinstance(game, object)

def test_roll_numbers(game):
  game.roll('123')
  assert game._frames == [1, 2, 3]


def test_score_1234(game):
  game.roll('1234')
  assert game.score() == 10

def test_miss(game):
  game.roll('8-')
  assert game.score() == 8
