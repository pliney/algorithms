from random import random as rand
from random import randint
from time import time
import numpy as np

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

class custom_rng:
    def __init__(self):
        self._seed = time() % 3

    def set_seed(self, seed):
        self._seed = seed

    def next_rand(self, a = 22695477, c = 1, m = 2**32):
        self._seed = (self._seed * a + c) % m
        return self._seed

    def next_int(self, min, max):
        range = max-min
        return int(self.next_rand()/float(2**32) * (range+1)) + min



def test_sequence(rng):
    print(rand())
    pass

def test_distribution(rng):
    print(rand())
    pass

def sequence_loop(rng, iterations):
    for i in range(0,iterations):
        test_sequence(rng)

def gen_freq_arrays(rng, num_range, iterations):
    python_freq = [0]*(num_range)
    # python_freq = []
    i = 0
    while i < iterations:
        python_freq[int(randint(0, num_range-1))] += 1
        # python_freq.append(int(randint(0, num_range - 1)))
        i += 1

    python_arange = np.arange(0, num_range, 1)

    custom_freq = [0] * num_range
    i = 0
    while i < iterations:
        custom_freq[int(rng(0, num_range-1))] += 1
        i += 1
    custom_arange = np.arange(0, num_range, 1)
    return python_arange, python_freq, custom_arange, custom_freq

def freqency_histogram(rng, num_range, iterations = 1000000):
    x_py, y_py, x_cust, y_cust = gen_freq_arrays(rng, num_range, iterations)

    x = np.random.randn(10000)

    # the histogram of the data
    plt.hist(y_py, bins=x_py, facecolor='green', alpha=0.75)
    print(y_py)


    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
    # plt.axis([0, num_range, 0, 100])
    plt.grid(True)

    plt.show()


    # plt.plot(x_py, y_py, 'red', x_cust, y_cust, 'green')
    # plt.show()

def frequency_line_plot(rng, num_range, iterations=10000000):
    x_py, y_py, x_cust, y_cust = gen_freq_arrays(rng, num_range, iterations)

    plt.plot(x_py,y_py, 'red', x_cust,y_cust,'green')
    plt.xlabel('Integer generated')
    plt.ylabel('Frequency')
    plt.title(r'Frequency plot of python RNG and custom RNG')
    plt.legend(['python RNG', 'custom RNG'])

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.show()

def calc_chi(rng, num_range, iterations):
    py_arange, py_freq, cust_arange, cust_freq = gen_freq_arrays(rng, num_range, iterations)
    expected = iterations/num_range
    py_chi_sq = 0
    cust_chi_sq = 0
    for i in range(0, num_range):
        py_chi_sq += float((py_freq[i] - expected)**2)/expected
        cust_chi_sq += float((cust_freq[i] - expected)**2)/expected

    return py_chi_sq, cust_chi_sq

def calc_chi_avg(num_range, iterations, trials):
    tot1 = 0
    tot2 = 0
    for i in range(0, trials):
        t1, t2 = calc_chi(rng.next_int, num_range, iterations)
        tot1 += t1
        tot2 += t2

    print((tot1/trials, tot2/trials))

if __name__ == "__main__":
    # sequence_loop(rand, 20)
    rng = custom_rng()
    # frequency_line_plot(rng.next_int, 100)
    # freqency_histogram(rng.next_int, 100)

    calc_chi_avg(num_range=100,iterations=10000, trials=100)
    calc_chi_avg(num_range=100, iterations=100000, trials=100)
    calc_chi_avg(num_range=100, iterations=1000000, trials=10)
    calc_chi_avg(num_range=100, iterations=10000000, trials=10)
    # max = rng.next_int(0,10)
    # min = max
    # for i in range(0, 1000):
    #     # next = rng.next_rand()
    #     next = rng.next_int(0,10)
    #     if next > max:
    #         max = next
    #     if next < min:
    #         min = next
    #     print(next)
    # print("max num: %d" % (max))
    # print("min num: %d" % min)