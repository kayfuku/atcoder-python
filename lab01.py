from collections import *
from sortedcontainers import SortedList
from pprint import pprint


def main():
    # experiment code

    a = [1, 2, 3]
    b = [1]
    for ai, bi in zip(a, b):
        print(ai, bi)

    # done
    print('done')
    # oj t -c "python main.py"
    # code `acc config-dir`/python/main.py


if __name__ == '__main__':
    main()
