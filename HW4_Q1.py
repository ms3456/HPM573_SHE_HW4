import numpy as np
from enum import Enum



class Flip(Enum):
    """flip results of a coin"""
    TAIL = 0
    HEAD = 1

class Game(object):
    def __init__(self, id, head_prob):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(self._id)
        self._headProb = head_prob
        self._flipResult = Flip.TAIL
        self._trials = []
        self._reward = -250


    def Simulate(self, n_time_steps):
        t = 0
        while t < n_time_steps:
            if self._rnd.sample() < self._headProb:
                self._flipResult = Flip.HEAD
                self._trials.append(self._flipResult)

            else:
                self._flipResult = Flip.TAIL
                self._trials.append(self._flipResult)

            t += 1


    def get_exp_value(self, n_time_steps):
        i = 2

        while i <n_time_steps:
            if self._trials[i] == Flip.HEAD and self._trials[i-1] == Flip.TAIL and self._trials[i-2] == Flip.TAIL:
                self._reward += 100
            i += 1

        return self._reward

class Realization:
    def __init__(self, id, realization_number, head_prob):
        self._realizations = []
        self._expValue = []
        n = 1
        while n <= realization_number:
            realization = Game(id * realization_number + n, head_prob)
            self._realizations.append(realization)
            n += 1

    def simulate (self, n_time_steps):
        for realization in self._realizations:
            realization.Simulate (n_time_steps)
            value = realization.get_exp_value(n_time_steps)
            if not (value is None):
                self._expValue.append(value)
        return self._expValue

    def get_ave_exp_value(self):
        return sum(self._expValue)/len(self._expValue)
