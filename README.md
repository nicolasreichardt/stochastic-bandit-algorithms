# GRAD-E1489: Algorithmic Game Theory and Governance
# Instructor: Prof. Asya Magazinnik, PhD

## Term paper - Nicolas Reichardt, 245611

---

## Stochastic Multi-Armed Bandit Algorithms

A Python implementation of classical stochastic multi-armed bandit algorithms from scratch, developed as part of a term paper for the Algorithmic Game Theory and Governance course at Hertie School. 

For theoretical background, mathematical formulations, and detailed analysis, see the accompanying [paper](PLACEHOLDER.pdf).

## Overview

This repository provides clean, educational implementations of three fundamental algorithms for solving the multi-armed bandit problem in stochastic settings:

- **ε-Greedy**: A simple algorithm that balances exploration and exploitation using a fixed probability
- **UCB1 (Upper Confidence Bound)**: An optimistic algorithm that selects arms based on confidence intervals
- **Thompson Sampling**: A Bayesian approach that maintains probability distributions over arm qualities

The implementations are designed for clarity and educational purposes, demonstrating the core mechanics of each algorithm without relying on external libraries. All algorithms are implemented from scratch in Python for a Bernoulli bandit setting.

## Repository Structure
```
stochastic-bandit-algorithms/
├── src/
│   ├── __init__.py
│   ├── bernoulli_bandit.py           # Bernoulli bandit environment
│   ├── epsilon_greedy.py             # ε-Greedy implementation
│   ├── upper_confidence_bound.py     # UCB1 implementation
│   └── thompson_sampling.py          # Thompson Sampling implementation
├── plots/                            # Saved figures and visualizations
├── bandit_algorithms.ipynb
├── PLACEHOLDER.pdf
├── requirements.txt
├── LICENSE
└── README.md

```

## Installation

Clone the repository and install the required dependencies:
```bash
git clone https://github.com/nicolasreichardt/stochastic-bandit-algorithms.git
cd stochastic-bandit-algorithms
pip install -r requirements.txt
```

### Running Experiments

The `bandit_algorithms.ipynb` notebook contains complete experiments comparing all three algorithms. It tracks:

- **Instantaneous reward**: Reward obtained at each time step
- **Cumulative reward**: Total reward accumulated over time
- **Optimal arm selection rate**: Frequency of choosing the best arm

To run the experiments:
```bash
jupyter notebook bandit_algorithms.ipynb
```

## Experimental Setup

The implementations are evaluated using comprehensive experiments that test algorithm performance across different scenarios:

### Bandit Configurations

Three difficulty levels are tested to evaluate algorithm robustness:

- **Easy**: `[0.1, 0.5, 0.9]` - Large reward differences between arms
- **Medium**: `[0.3, 0.5, 0.7]` - Moderate reward differences
- **Hard**: `[0.48, 0.50, 0.52]` - Small reward differences (challenging exploration)

### Experimental Protocol

- **Time horizon**: 5,000 iterations per experiment
- **Replications**: 50 independent runs per configuration
- **Algorithms compared**: Epsilon-Greedy (ε=0.1), UCB1, and Thompson Sampling

### Metrics Tracked

For each algorithm and configuration, the following metrics are measured:

- **Cumulative reward**: Total reward accumulated over time (with confidence intervals)
- **Optimal arm selection rate**: Frequency of choosing the best arm
- **Cumulative regret**: Difference between optimal performance and actual performance

### Sensitivity Analysis

Additional experiments explore hyperparameter sensitivity:

- **Epsilon-Greedy**: Tested with ε ∈ {0.01, 0.05, 0.1, 0.15, 0.2}
- Analysis shows impact of exploration-exploitation trade-off on performance

Results are averaged across multiple runs with standard deviation bands to show statistical reliability.

---

## AI use statement:

Generative AI tools like GitHub Copilot and Claude were consulted for proofreading, LaTeX formatting, and general coding/linting support. All final answers were developed and verified by the author.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.