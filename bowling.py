class BowlScorer():
    def __init__(self):
        self._rolls = [0 for i in range(21)]
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def get_score(self):
        score = 0
        rollIndex = 0

        for frameIndex in range(10):
            if self.is_spare(rollIndex):
                score += self.spare_score(rollIndex)
                rollIndex += 2
            elif self.is_strike(rollIndex):
                score += self.strike_score(rollIndex)
                rollIndex += 1
            else:
                score += self.frame_score(rollIndex)
                rollIndex += 2


        return score

    def is_strike(self, rollIndex):
        return self._rolls[rollIndex] == 10

    def is_spare(self, rollIndex):
        return self._rolls[rollIndex] + self._rolls[rollIndex + 1] == 10

    def strike_score(self, rollIndex):
        return 10 + self._rolls[rollIndex + 1] + self._rolls[rollIndex + 2]

    def spare_score(self, rollIndex):
        return 10 + self._rolls[rollIndex + 2]

    def frame_score(self, rollIndex):
        return self._rolls[rollIndex] + self._rolls[rollIndex + 1]