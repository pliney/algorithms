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


def gen_num_arrays(rng, num_range, iterations):
    python_list = []
    i = 0
    while i < iterations:
        python_list.append(int(randint(0, num_range - 1)))
        i += 1

    i = 0
    custom_list = []
    while i < iterations:
        custom_list.append(int(rng(0, num_range - 1)))
        i += 1

    return python_list, custom_list


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

def sequence_plot(rng, num_range, iterations=10000):
    y_py, y_cust = gen_num_arrays(rng, num_range, iterations)
    x_cust = np.arange(0,iterations,1)
    plt.plot(x_cust,y_cust,'green')
    plt.xlabel('Number')
    plt.ylabel('Order')
    plt.title(r'Frequency plot of python RNG and custom RNG')
    plt.legend(['custom RNG'])

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.show()

def gap_test(rng, num_range, iterations):
    gap_matrix = []
    for k in range(num_range+1):
        gap_matrix.append([0])

    print(gap_matrix)
    i = 0

    while i < iterations:
        next = rng(0, num_range)
        # print(next)
        gap_matrix[next].append(-1)
        for j in range(0, num_range+1):
            gap_matrix[j][-1] += 1
        # print(gap_matrix)
        i += 1
    gap_analysis(gap_matrix, num_range)

def gap_analysis(a, num_range):

    p = lambda n: prob_not_k**n * prob_k
    p_list = []
    d = {}
    for row in a:
        for gap in row:
            if (gap/3) in d:
                d[gap/3] += 1
            else:
                d[gap/3] = 1
    print(d)
    chi = 0
    prob_k = 1 / float(num_range)
    prob_not_k = (1 - prob_k)
    # for gap in d:
    #     chi += ((p(gap) - (gap/float(num_range))) ** 2) / num_range
    print(chi)


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

def probs():
    i = 0
    while i < 56:
        sum = 0
        for j in range(0,4):
            sum += (.9 ** i)*.1
            i += 1
        print('i: %d  prob: %f sum' % (i, sum))

if __name__ == "__main__":
    # sequence_loop(rand, 20)
    rng = custom_rng()
    # probs()
    '''Frequency plots'''
    # frequency_line_plot(rng.next_int, 100)
    # freqency_histogram(rng.next_int, 100)

    '''Sequence plots'''
    # sequence_plot(rng.next_int, 50, 1000)
    # sequence_plot(randint, 50, 1000)

    '''Gap test'''
    gap_test(rng.next_int, 9, 100)
    gap_test(randint, 9, 100)

    '''Chi square runs'''
    # calc_chi_avg(num_range=100,iterations=10000, trials=100)
    # calc_chi_avg(num_range=100, iterations=100000, trials=100)
    # calc_chi_avg(num_range=100, iterations=1000000, trials=10)
    # calc_chi_avg(num_range=100, iterations=10000000, trials=10)


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