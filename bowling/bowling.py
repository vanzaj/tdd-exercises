class BowlingGame():

  def pin_to_score(self, pin):
    if pin == '-':
      return 0
    return int(pin)

  def roll(self, pins):
    self._frames = [self.pin_to_score(p) for p in pins]

  def score(self):
    return sum(self._frames)
