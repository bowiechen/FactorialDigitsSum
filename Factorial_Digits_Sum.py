from math import factorial as fac
import sys
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
        raise TypeError('lhs can only accept type Counter!')


def pretty_print(counter):
    if isinstance(counter, Counter):
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
        raise TypeError('lhs can only accept type Counter!')



def main():
    if len(sys.argv) >= 2:
        counter = Counter(int(sys.argv[1]))
        while not counter.overflow:
            counter.increment()
            if lhs(counter) == rhs(counter):
                pretty_print(counter)
    else:
        print('Missing argument!')



if __name__ == '__main__':
    main()
