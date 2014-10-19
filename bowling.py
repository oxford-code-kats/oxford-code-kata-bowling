"http://content.codersdojo.org/code-kata-catalogue/bowling-game/"

class BowlingGame(object):
    def __init__(self):
        self._frames = []

    def _current_frame(self):
        if not self._frames:
            return self.new_frame()
        if len(self._frames) == 10:
            return self._frames[-1]
        if self._frames[-1].is_complete():
            return self.new_frame()
        return self._frames[-1]

    def new_frame(self):
        _new = Frame()
        self._frames.append(_new)
        return _new

    def score(self):
        return sum([frame.score() for frame in self._frames])

    def roll(self, count):
        current_frame = self._current_frame()
        for frame in self._frames:
            frame.add_roll(count)

class Frame(object):
    def __init__(self):
        self._pins = []
        self._score = 0
        self._extra_scoring_balls = 0

    def add_roll(self, roll):
        if not self.is_complete():
            self.score_roll(roll)
            self._pins.append(roll)
            if self.is_complete():
                # Frame is completed this roll
                if self._is_strike():
                    self._extra_scoring_balls = 2
                elif self._is_spare():
                    self._extra_scoring_balls = 1
        
        else:
            self.score_roll(roll)
    
    def score(self):
        return self._score

    def score_roll(self, roll):
        if self.is_complete():
            if not self._extra_scoring_balls:
                return
            self._score += roll
            self._extra_scoring_balls -= 1
        else:
            self._score += roll

    def _is_spare(self):
        return not self._is_strike() and sum(self._pins) == 10 

    def _is_strike(self):
        return self._pins == [10]

    def is_complete(self):
        return self._is_spare() or self._is_strike() or len(self._pins) == 2


