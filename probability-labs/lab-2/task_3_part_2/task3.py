import time
import numpy as np
import matplotlib.pyplot as plt

np.random.uniform(10000);

def F_inv(u):
    return (-np.log(1 - u))**(1/3)

for n in [100, 500, 1000, 10000, 50000]:

    start_time = time.time()
    samples = F_inv(np.random.uniform(size=n))
    end_time = time.time()
    
    print(f"")
    print(f"Generation of {n} numbers was finished")
    print(f"Time: {(end_time - start_time):.5f} seconds")

    time_per_sample = ((end_time - start_time) / n) * 1_000_000
    print(f"Average time for one number: ~{time_per_sample:.2f} μs")
    
    plt.hist(samples, bins = 60, density = True, color="Lightblue")
    plt.title(f"PART 2. n = {n}")
    plt.savefig(f'plot_{n}.png')
    plt.close()