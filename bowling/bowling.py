class BowlingGame:
    def rolls(self, rolls):
        self._rolls = rolls

    def score(self):
        return sum(self._rolls)
