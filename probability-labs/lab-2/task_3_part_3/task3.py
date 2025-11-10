import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

def ratio_of_uniforms(n):
    samples = []
    u_max, v_min, v_max = 0.53, 0, 0.65
    while len(samples) < n:
        u = uniform.rvs(scale = u_max)
        v = uniform.rvs(loc = v_min, scale = v_max-v_min)
        x_c = v / u
        if u <= x_c * np.exp(-x_c**3 / 2):
            samples.append(x_c)
    return np.array(samples)

for n in [100, 500, 1000, 10000, 50000]:
    start_time = time.time()
    samples = ratio_of_uniforms(n)
    end_time = time.time()

    print(f"\nGeneration of {n} numbers was finished")
    print(f"Time: {(end_time - start_time):.5f} seconds")

    time_per_sample = ((end_time - start_time) / n) * 1_000_000
    print(f"Average time for one number: ~{time_per_sample:.2f} μs")
    plt.hist(samples, bins=60, density=True, color="lightgreen")
    plt.title(f"Ratio of Uniforms. n = {n}")
    plt.savefig(f'plot_ratio_{n}.png')
    plt.close()