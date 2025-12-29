import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 10000
X = np.random.uniform(0, 1, n)
cumulative_mean = np.cumsum(X) / np.arange(1, n + 1)

plt.figure()
plt.plot(cumulative_mean, label="Cumulative Mean")
plt.axhline(0.5, linestyle="--", label="μ = 0.5")
plt.xlabel("Number of observations (n)")
plt.ylabel("Cumulative Mean")
plt.title("SLLN Simulation for U[0,1]")
plt.legend()
plt.tight_layout()
plt.savefig("../results/figures/slln_convergence.png")
plt.show()

