from typing import  (
    List,
)
from Sequence import (
    Sequence,
)
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
        if (num_levels, start_thresh, step_thresh, tuple(block_size_list)) not in self.sequence.regression_results:
            blocks_array = np.empty(num_levels * len(block_size_list), dtype=int)
            exceedance_array = np.empty(num_levels * len(block_size_list), dtype=int)

        return self.sequence.length


if __name__ == '__main__':
    a = Sequence(np.array([1]))
    b = MultilevelEstimator(a)
    print(b.bias_linear_regression(10, 10, 10, [10]))
