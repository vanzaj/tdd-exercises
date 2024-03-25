class BowlingGame():

  def pin_to_int(self, pin):
    if pin == '-':
      return 0
    return int(pin)

  def line(self, pins):
    pins = [self.pin_to_int(p) for p in pins]
    self._frames = list(zip(pins[::2], pins[1::2]))

  def score(self):
    score = 0
    for (a, b) in self._frames:
      score += a + b
    return score
