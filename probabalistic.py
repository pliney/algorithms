from random import random as rfg
from random import uniform as rfg_r
from random import randint as rng
import math

'''************************Compute Pi funciton *******************************'''
def compute_pi(num_points=100000):
    hits_inside = 0

    i = 0
    while i < num_points:
        x = rfg_r(-1, 1)
        y = rfg_r(-1, 1)
        if (x**2 + y**2) < 1:
            hits_inside += 1
        i += 1

    pi = 4 * float(hits_inside) / num_points
    print('pi guess: %f' %pi)
''' ********************* Random array search functions **********************'''
def rand_array_search_trial():
    trials = 10000
    max_guesses = 5000

    total_guesses = 0
    failures = 0

    for i in range(0,trials):
        guesses = rand_array_search(max_guesses)
        total_guesses += guesses
        if guesses == max_guesses:
            failures += 1

    avg = float(total_guesses) / trials
    print('Avg # of guesses per search: %f\nTotal failed search attemps: %d' % (avg, failures))


def rand_array_search(max_guesses):
    size = 1000
    array_range = 100000
    a = []
    for i in range(0, size):
        a.append(rng(0, array_range))

    search_int = a[rng(0,size-1)]
    i = 0
    while i < max_guesses:
        search_index = rng(0,size-1)
        if a[search_index] == search_int:
            break
        i+= 1

    return i


'''******************Prime test functions**************************'''
def prime_test_loop(divisors_to_try = 100, trials = 100, prime_range = 100):
    false_positives = 0
    for i in range(0, trials):
        if prime_test(divisors_to_try, prime_range):
            false_positives += 1

    print('Out of %d different non_primes tested, %d of the numbers were not rejected' % (trials, false_positives))

def prime_test(divisors_to_try, prime_range):

    non_prime = gen_non_prime(prime_range)
    root = int(non_prime ** (.5))

    for i in range(0, divisors_to_try):
        if non_prime % rng(2,root) == 0:
            return False

    return True


def gen_non_prime(prime_range):
    return rng(2, prime_range) * rng(2, prime_range)


'''Monte Carlo Integration'''


def find_rectangle_range(function, domain=(-10, 10)):
    max_y = 0
    min_y = 0
    for x in range(domain[0], domain[1]):
        if function(x) > max_y:
            max_y = function(x)

    for x in range(domain[0], domain[1]):
        if function(x) < min_y:
            min_y = function(x)

    if min_y < 0:
        return max_y * 2, min_y * 2
    else:
        return max_y, 0


def monte_carlo_darts(f=lambda x: x ** 2, domain=(-10, 10), num_points=10000):
    y_max, y_min = find_rectangle_range(f, domain)

    area = (domain[1] - domain[0]) * (y_max - y_min)

    pos_hits = 0
    neg_hits = 0

    i = 0
    while i < num_points:
        x = rfg_r(domain[0],domain[1])
        y = rfg_r(y_min, y_max)

        if 0 < y < f(x):
            pos_hits += 1
        if f(x) < y < 0:
            neg_hits += 1

        i += 1

    integral = area * float(pos_hits - neg_hits) / num_points
    return integral

def monte_carlo_mean(f=lambda x: x**2, domain=(-10, 10), num_points=10000):
    domain_width = domain[1] - domain[0]
    total_y = 0
    i = 0
    while i < num_points:
        x = rfg_r(domain[0], domain[1])
        total_y += f(x)
        i += 1

    mean = total_y/float(num_points)

    return mean * domain_width

def monte_carlo_trial(trials=20, **kwargs):
    dart_total = 0
    for i in range(0,trials):
        dart_total += monte_carlo_darts(**kwargs)

    print('Monte carlo dart result: %f' % (float(dart_total)/trials))

    mean_total = 0
    for i in range(0,trials):
        mean_total += monte_carlo_mean(**kwargs)

    print('Monte carlo mean result: %f' % (float(mean_total) / trials))

def rand_test():
    i = 0
    while True:
        x = rfg()
        if x == 0 or x == 1:
            print x
            break

    print('took %d trials' %i)

if __name__ == '__main__':
    # '''Computing Pi'''
    # for i in range(1,12):
    #     print('darts = 10^%d' %i)
    #     compute_pi(num_points=10**i)

    '''Random array search'''
    # rand_test()
    # rand_array_search_trial()

    '''Prime exclusion test'''
    # prime_test_loop(divisors_to_try=1000, trials=10000,prime_range = 10000)

    '''Monte Carlo'''
    (monte_carlo_trial(f=lambda x: ((x-3)*(x+1)*(x-1)), num_points=50000, domain=(-2, 2)))