# from math import factorial as fac
import sys
import argparse
from multiprocessing import Process, Queue
from Counter import Counter

def fac(x):
    if x == 0 or x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 6
    if x == 4:
        return 24
    if x == 5:
        return 120
    if x == 6:
        return 720
    if x == 7:
        return 5040
    if x == 8:
        return 40320
    if x == 9:
        return 362880

def lhs(counter):
    if isinstance(counter, Counter):
        return counter.get_value()
    else:
        raise TypeError('lhs can only accept type Counter!')


def rhs(counter):
    if isinstance(counter, Counter):
        retval = 0
        for i in counter.get_list():
            retval += fac(i)
        return retval
    else:
        raise TypeError('rhs can only accept type Counter!')


def pretty_print(counter):
    if isinstance(counter, Counter):
        # leading character should not be zero.
        if counter.get_list()[0] == 0:
            return
        print('=== SOLUTION ===')
        solution_str = ''
        solution_str += str(counter.get_value())
        solution_str += ' = '
        for i in counter.get_list():
            solution_str += str(i)
            solution_str += '! + '
        solution_str = solution_str[:-3]
        print(solution_str)
    else:
        raise TypeError('pretty_print can only accept type Counter!')


def brute_force(init_val, end_val, digits, allow_zero):
    counter = Counter(digits, init_val, allow_zero)
    while not counter.overflow and counter.get_value() < end_val:
        counter.increment()
        if lhs(counter) == rhs(counter):
            pretty_print(counter)


def multicore_helper(init_val, end_val, digits, allow_zero, queue=None):
    if queue is None:
        brute_force(init_val, end_val, digits, allow_zero)
    else:
        queue.put(brute_force(init_val, end_val, digits, allow_zero))

def multicore(digits, allow_zero, core_count=1):
    if core_count != int(core_count) or core_count <= 0:
        core_count = 1 # encountered invalid stuff

    if core_count > 1:
        print('TODO')
        print('[INFO] Using ' + str(core_count) + ' cores.')
        queue = Queue()
        delta = int(pow(10, digits) / core_count)
        lo = 0
        hi = lo + delta
        for i in range(core_count):
            proc = Process(target=multicore_helper, args=(lo, hi, digits, allow_zero, queue))
            proc.start()
            lo = hi
            hi += delta
    else:
        print('[INFO] Using ' + str(core_count) + ' core.')
        end_val = ''
        for i in range(digits):
            end_val += str(9)
        multicore_helper(0, int(end_val), digits, allow_zero)



def main():
    args = parser.parse_args()
    multicore(args.digits, args.allow_zero, args.multicore)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digits', type=int, default='5', help='how many digits to calculate')
    parser.add_argument('-z', '-0', '--allow_zero', help='allow zeros to be part of the calculation', action='store_true')
    parser.add_argument('-m', '--multicore', type=int, default=1, help='how many cores to use. if an invalid integer is given, \'1\' is used')
    main()
