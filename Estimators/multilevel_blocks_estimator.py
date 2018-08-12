from typing import  (
    List,
)
from Sequence import Sequence
import numpy as np
import pandas as pd


class MultilevelEstimator(object):
    """Defines a multilevel estimator"""
    def __init__(
            self,
            sequence,     # type: Sequence
    ):
        self.sequence = sequence

    def bias_linear_regression(
            self,
            num_levels,        # type: int
            start_thresh,      # type: int
            step_thresh,       # type: int
            block_size_list,   # type: List[int]
    ):
        pass
