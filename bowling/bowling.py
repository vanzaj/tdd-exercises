class BowlingGame:
    def rolls(self, rolls):
        self._rolls = rolls

    def frame_score(self, frame):
        return sum(frame)

    def is_strike(self, frame):
        return len(frame) == 1 and self.frame_score(frame) == 10

    def is_spare(self, frame):
        return len(frame) == 2 and self.frame_score(frame) == 10

    def score(self):
        total = 0
        frame = []
        for idx, pins in enumerate(self._rolls):
            if len(frame) == 0:
                frame.append(pins)
                continue
            if self.is_strike(frame):
                frame.extend(self._rolls[idx+1:idx+3])
                print(idx, frame)
                total += self.frame_score(frame)
                frame = []
                continue
            frame.append(pins)
            if self.is_spare(frame):
                frame.append(self._rolls[idx+1])
                total += self.frame_score(frame)
                frame = []
                continue
            total += self.frame_score(frame)
            frame = []
        return total
