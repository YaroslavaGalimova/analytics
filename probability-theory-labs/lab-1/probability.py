import math
import scipy.stats
from decimal import Decimal, getcontext

def factorial(n):
    f = 1
    while n > 1:
        f = f * n
        n = n - 1
    return f

def c(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def my_count(n, k, p):
    return c(n, k) * (p ** k) * ((1 - p) ** (n - k))

def pois(n, k, p):
    return ((n * p) ** k) * (math.e ** (-n * p)) / factorial(k)

def local_muivre_laplace(n, k, p):
    return (math.e**((k - n * p) / (2 * n * p * (1 - p)))) / math.sqrt(2 * n * p * (1 - p))

l = scipy.stats.laplace()
def int_muivre_laplace(n, m1, m2, p):
    sqr = math.sqrt(n * p * (1 - p))
    return l.cdf((m2 - n * p) / sqr) - l.cdf((m1 - n * p) / sqr)

def format_number(num):
    if isinstance(num, str):
        return num
    try:
        d = Decimal(str(num))
        return '{0:f}'.format(d).rstrip('0').rstrip('.') if '.' in '{0:f}'.format(d) else '{0:f}'.format(d)
    except:
        return str(num)

def sum(n, m1, m2, p, f):
    result = 0
    for i in range(m1, m2 + 1):
        try:
            result += f(n, i, p)
        except OverflowError:
            return "error"
    return result

n_vars = [100, 1000, 10000]
p_vars = [0.001, 0.01, 0.1, 0.25, 0.5]

for n in n_vars:
    for p in p_vars:
        d = math.sqrt(n*p*(1-p))
        np = math.floor(n*p)
        k_vars = [[math.floor(n / 2 - d), math.floor(n / 2 + d)], [0, 5], [np, np]]
        for k in k_vars:
            print("n: {:s}, p: {:s}, k{:s}".format(str(n), str(p), str(k)))
            print("my: " + format_number(sum(n, k[0], k[1], p, my_count)))
            print("pois: " + format_number(sum(n, k[0], k[1], p, pois)))
            print("local: " + format_number(sum(n, k[0], k[1], p, local_muivre_laplace)))
            print("int: " + format_number(int_muivre_laplace(n, k[0], k[1], p)))
            print("-"*30)