import numpy as np


class Sequence(object):
    """Defines a sequence object containing a sequence of floats
    along with methods that deal with estimation"""
    def __init__(self, sequence, theta=None, alpha=None):
        self.sequence = sequence   # type: np.array
        self.theta = theta         # type: float
        self.alpha = alpha         # type: float