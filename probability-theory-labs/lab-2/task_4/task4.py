import numpy as np
from scipy.stats import norm

n_1 = 200000
n_2 = 38416
epsilon = 0.01

counter_1 = 0
for _ in range(100):
    sample = np.random.exponential(scale = 1, size=n_1)
    mean = np.mean(sample)
    if abs(mean - 1) <= epsilon:
        counter_1 += 1

counter_2 = 0
for _ in range(100):
    sample = np.random.exponential(scale = 1, size=n_2)
    mean = np.mean(sample)
    if abs(mean - 1) <= epsilon:
        counter_2 += 1

# Результаты
print(f"Неравенство Чебышёва в процентах (n = {n_1}): {counter_1/100:.2f}")
print(f"ЦПТ  в процентах (n = {n_2}): {counter_2/100:.2f}")