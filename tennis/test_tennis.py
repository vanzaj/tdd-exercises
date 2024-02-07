import unittest

from tennis import TennisGame


class TennisTest(unittest.TestCase):

    def setUp(self):
        self.game = TennisGame()

    def test_new_game(self):
        self.assertEqual("Love - All", self.game.score())
