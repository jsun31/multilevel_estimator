import numpy as np


class Sequence(object):
    """Defines a sequence object containing a sequence of floats
    along with methods that deal with estimation"""
    def __init__(
            self,
            sequence,      # type: np.array
            theta=None,    # type: float
            alpha=None,    # type: float
    ):
        # (...) -> None
        self.sequence = sequence
        self.theta = theta
        self.alpha = alpha

        self.length = len(sequence)
        self.sorted_sequence = np.sort(sequence)[::-1]

        # to be updated by record_exceedance function
        self.exceedance_records = {}

        # to be updated by MultilevelEstimator
        self.regression_results = {}
        self.alpha_hat = {}

    def __getitem__(
            self,
            index,      # type: int
    ):
        return self.sequence[index]

    def __repr__(
            self
    ):
        return str(self.sequence)

    def record_exceedance(
            self,
            thresh_ind,     # type: int
            block_size,     # type: int
    ):
        num_blocks = np.floor(self.length / block_size).astype(int)

        if (thresh_ind, block_size) not in self.exceedance_records:
            threshold = self.sorted_sequence[thresh_ind]
            max_by_block = [max(self.sequence[block_ind * block_size : (block_ind + 1) * block_size])
                            for block_ind in range(num_blocks)]
            num_exceedance_blocks = sum([block_max > threshold for block_max in max_by_block])
            num_exceedance = thresh_ind
            theta_naive_est = num_exceedance_blocks / num_exceedance

            self.exceedance_records[(thresh_ind, block_size)] = (num_blocks, num_exceedance_blocks,
                                                                 num_exceedance, theta_naive_est)

