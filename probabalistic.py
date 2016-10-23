from random import random as rng
from random import uniform as rng_r


def compute_pi(num_points=100000000):
    hits_inside = 0

    i = 0
    while i < num_points:
        x = rng_r(-1, 1)
        y = rng_r(-1, 1)
        if (x**2 + y**2) < 1:
            hits_inside += 1

    pi = 4 * float(hits_inside) / num_points
    print('pi guess: %f' %pi)


def rand_test():
    i = 0
    while True:
        x = rng()
        if x == 0 or x == 1:
            print x
            break

    print('took %d trials' %i)

if __name__ == '__main__':
    for i in range(1,12):
        print('darts = 10^%d' %i)
        compute_pi(10**i)
    # rand_test()