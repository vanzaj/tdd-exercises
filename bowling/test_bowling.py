import pytest
from bowling import Game

@pytest.fixture
def game():
  yield Game()

def test_new_bowling_game(game):
  assert isinstance(game, object)

def test_roll_numbers(game):
  game.roll('123')
  assert game._frames == [1, 2, 3]
