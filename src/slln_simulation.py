import numpy as np
import matplotlib.pyplot as plt

n = 10000
X = np.random.uniform(0, 1, n)
cumulative_mean = np.cumsum(X) / np.arange(1, n + 1)

plt.plot(cumulative_mean)
plt.axhline(0.5)
plt.xlabel("n")
plt.ylabel("Mean")
plt.title("SLLN Simulation")
plt.savefig("../results/figures/slln_convergence.png")
plt.show()
