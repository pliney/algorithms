import sys
from random import random as rnd
from time import time as tm


# def quick_sort(array, part_func = partition, max_size = 10):
#     rec_quick_sort(array, 0, len(array)-1, max_size, part_func)


def rec_quick_sort(array, l_index, r_index, max_size, part_func):


    if r_index - l_index < max_size:
        insertion_sort(array, l_index, r_index)
    elif l_index < r_index:
        s = part_func(array, l_index, r_index)
        rec_quick_sort(array, l_index, s - 1, max_size, part_func)
        rec_quick_sort(array, s + 1, r_index, max_size, part_func)


def hoare_partition_med3(a, l_index, r_index):
    mid = (r_index + l_index) / 2
    if a[l_index] > a[mid]:
        swap(a, l_index, mid)
    if a[mid] > a[r_index]:
        swap(a, mid, r_index)
    if a[l_index] > a[r_index]:
        swap(a, l_index, r_index)
    pivot_i = mid
    pivot = a[pivot_i]
    l_scan = l_index
    r_scan = r_index
    swap(a, pivot_i, l_index)
    finished = False
    while True:
        while True:
            l_scan += 1
            if(a[l_scan] >= pivot):
                break
        while True:
            r_scan -= 1
            if(a[r_scan] <= pivot):
                break


        if r_scan < l_scan:
            break
        else:
            swap(a, l_scan, r_scan)

    # swap(a, l_scan, r_scan)
    swap(a, l_index, r_scan)
    return r_scan


def hoare_partition(array, l_index, r_index):
    pivot_i = l_index
    pivot = array[pivot_i]
    l_scan = l_index
    r_scan = r_index+1
    while True:
        while l_scan < r_index:
            l_scan += 1
            if(array[l_scan] >= pivot):
                break
        while True:
            r_scan -= 1
            if(array[r_scan] <= pivot):
                break

        if r_scan > l_scan:
            swap(array, l_scan, r_scan)
        else:
            break

    swap(array, l_index, r_scan)
    return r_scan

def select_pivot_value(a, l_index, r_index):
    mid = (r_index + l_index) / 2
    if a[l_index] > a[mid]:
        swap(a, l_index, mid)
    if a[mid] > a[r_index]:
        swap(a, mid, r_index)
    if a[l_index] > a[r_index]:
        swap(a, l_index, r_index)

    return mid

def lomuto_partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            swap(a, i, j)
    swap(a, i+1, r)
    return i + 1

def insertion_sort(array,l_index = -1, r_index = -1):
    # if l_index == -1:
    #     l_index = 0;
    #     r_index = len(array)-1
    for i in range(l_index, r_index):
        j = i-1
        while j >= l_index:
            if (array[j] > array[j+1]):
                swap(array, j, j+1)
            else:
                j = l_index
            j -= 1

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def gen_array(num_range = 100000, size = 120000):
    a = []
    for i in range(0, size):
        a.append(int(rnd() * num_range))
    return a

def quick_sort(array, part_func = hoare_partition, max_size = 10):
    rec_quick_sort(array, 0, len(array)-1, max_size, part_func)

def time_trial(sort_function, trials = 10, **kwargs):
    totalTime = 0

    for i in range(0, trials):
        a = gen_array()
        t1 = tm()
        a.sort()
        # sort_function(a, **kwargs)
        t2 = tm()
        totalTime += (t2-t1)
    print("avg time = %f  insertion sort size = "% (totalTime / trials)) #kwargs['max_size']))
    return a



def main():
    # time_trial(quick_sort)

    # print('lumuto')
    #
    # time_trial(quick_sort, max_size=0, part_func=lomuto_partition)
    # time_trial(quick_sort, max_size=7, part_func=lomuto_partition)
    # # #
    # print('med3 hoare')
    # time_trial(quick_sort, max_size=0, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=7, part_func=hoare_partition_med3)
    # print('hoare')
    # time_trial(quick_sort, max_size=0, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=7, part_func=hoare_partition)
    print('pythonsort')
    time_trial(list.sort)


    # time_trial(quick_sort, max_size=6, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=7, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=8, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=9, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=10, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=11, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=12, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=13, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=16, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=20, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=24, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=28, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=32, part_func=hoare_partition_med3)
    # time_trial(quick_sort, max_size=36, part_func=hoare_partition_med3)

    # print('no med')
    #

    # time_trial(quick_sort, max_size=4, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=6, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=7, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=8, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=9, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=10, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=11, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=12, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=13, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=16, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=20, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=24, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=28, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=32, part_func=hoare_partition)
    # time_trial(quick_sort, max_size=36, part_func=hoare_partition)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()