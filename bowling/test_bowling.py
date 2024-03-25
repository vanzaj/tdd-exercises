import pytest
from bowling import BowlingGame

@pytest.fixture
def game():
  yield BowlingGame()

def test_new_bowling_game(game):
  assert isinstance(game, object)

def test_line_to_frames(game):
  game.line('1234')
  assert game._frames == [(1, 2), (3, 4)]

def test_score_1234(game):
  game.line('1234')
  assert game.score() == 10

def test_miss(game):
  game.line('8-')
  assert game.score() == 8
