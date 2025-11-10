import time
import numpy as np
from scipy.stats import rv_continuous
import matplotlib.pyplot as plt

class my_super_puper_dist(rv_continuous):
    def _pdf(self, x):
        return 3 * x**2 * np.exp(-x**3) * (x >= 0)

dist = my_super_puper_dist(a = 0)  
for n in [100, 500, 1000, 10000, 50000]:

    start_time = time.time()
    samples = dist.rvs(size = n)
    end_time = time.time()

    print(f"")
    print(f"Generation of {n} numbers was finished")
    print(f"Time: {(end_time - start_time):.5f} seconds")

    time_per_sample = ((end_time - start_time) / n) * 1_000_000
    print(f"Average time for one number: ~{time_per_sample:.2f} μs")
    
    plt.hist(samples, bins = 60, density = True, color="Pink")
    plt.title(f"PART 1. n = {n}")
    plt.savefig(f'plot_{n}.png')
    plt.close()
