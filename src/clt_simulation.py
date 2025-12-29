import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, probplot

mu = 0.5
sigma = (1/12) ** 0.5
m = 1000
n_values = [2, 5, 10, 30, 50]

plt.figure()
for n in n_values:
    sums = np.sum(np.random.uniform(0,1,(m,n)), axis=1)
    Z = (sums - n*mu) / (sigma*np.sqrt(n))
    plt.hist(Z, bins=30, density=True, alpha=0.5, label=f"n={n}")

x = np.linspace(-4,4,1000)
plt.plot(x, norm.pdf(x))
plt.legend()
plt.savefig("../results/figures/clt_histograms.png")
plt.show()

plt.figure()
probplot(Z, dist="norm", plot=plt)
plt.savefig("../results/figures/clt_qqplots.png")
plt.show()
