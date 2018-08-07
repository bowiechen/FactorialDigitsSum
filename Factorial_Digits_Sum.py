from math import factorial as fac
import sys
import argparse
from Counter import Counter

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


def main():
    args = parser.parse_args()
    counter = Counter(args.digits, args.allow_zero)
    while not counter.overflow:
        counter.increment()
        if lhs(counter) == rhs(counter):
            pretty_print(counter)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('digits', type=int, default='5', help='how many digits to calculate')
    parser.add_argument('-z', '-0', '--allow_zero', help='allow zeros to be part of the calculation', action='store_true')
    main()
