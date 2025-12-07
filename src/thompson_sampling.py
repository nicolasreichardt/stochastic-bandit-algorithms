import numpy as np

class ThompsonSampling:
    def __init__(self, k):
        self.k = k
        self.alphas = np.ones(k)
        self.betas  = np.ones(k)

    def select_arm(self):
        samples = np.random.beta(self.alphas, self.betas)
        return np.argmax(samples)

    def update(self, arm, reward):
        if reward == 1:
            self.alphas[arm] += 1
        else:
            self.betas[arm] += 1
