import numpy as np

class UCB1:
    def __init__(self, k):
        self.k = k
        self.counts = np.zeros(k)
        self.values = np.zeros(k)
        self.total_pulls = 0

    def select_arm(self):
        self.total_pulls += 1
        
        # pull each arm once at the beginning
        for i in range(self.k):
            if self.counts[i] == 0:
                return i

        # UCB formula
        confidence = np.sqrt((2 * np.log(self.total_pulls)) / self.counts)
        ucb_values = self.values + confidence
        return np.argmax(ucb_values)

    def update(self, arm, reward):
        self.counts[arm] += 1
        n = self.counts[arm]
        self.values[arm] += (reward - self.values[arm]) / n
