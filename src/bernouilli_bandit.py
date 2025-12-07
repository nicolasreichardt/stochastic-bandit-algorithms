import numpy as np

class BernoulliBandit:
    """
    A stochastic multi-armed bandit with Bernoulli rewards.
    Each arm i returns reward 1 with probability p[i], and 0 otherwise.
    """
    def __init__(self, probs):
        self.probs = np.array(probs)
        self.k = len(probs)

    def pull(self, arm):
        return 1 if np.random.rand() < self.probs[arm] else 0
