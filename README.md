# GRAD-E1489: Algorithmic Game Theory and Governance
# Instructor: Prof. Asya Magazinnik, PhD

## Term paper - Nicolas Reichardt, 245611

---

## Stochastic Multi-Armed Bandit Algorithms

A Python implementation of classical stochastic multi-armed bandit algorithms from scratch, developed as part of a term paper for the Algorithmic Game Theory and Governance course at Hertie School. 

For theoretical background, mathematical formulations, and detailed analysis, see the accompanying [paper](ADD THE PAPER HERE) ADD PAPER LINK HERE

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
├── bandit_algorithms.ipynb           
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

The implementations are evaluated on a 3-armed Bernoulli bandit with probabilities `[0.2, 0.5, 0.7]`, where arm 3 is optimal. Each algorithm runs for 5,000 iterations, tracking:

- **Instantaneous reward**: Reward obtained at each time step
- **Cumulative reward**: Total reward accumulated over time
- **Optimal arm selection rate**: Frequency of choosing the best arm

See the Jupyter notebook for complete experiments and visualizations.

---

## AI use statement:

Generative AI tools like GitHub Copilot and Claude were consulted for proofreading, LaTeX formatting, and general coding/linting support. All final answers were developed and verified by the author.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.