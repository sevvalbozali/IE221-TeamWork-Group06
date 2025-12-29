import numpy as np
import matplotlib.pyplot as plt

n = 10000
inside = 0
pi_vals = []

for i in range(1, n+1):
    x, y = np.random.uniform(0,1,2)
    if x*x + y*y <= 1:
        inside += 1
    pi_vals.append(4*inside/i)

plt.plot(pi_vals)
plt.axhline(np.pi)
plt.xlabel("Number of points (n)")
plt.ylabel("Pi estimate")
plt.title("Monte Carlo Estimation of Pi")
plt.savefig("../results/figures/pi_estimation.png")
plt.show()
