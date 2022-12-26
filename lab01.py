from collections import *
from sortedcontainers import SortedList
from pprint import pprint


def main():
    # experiment code

    a = [1, 2, 3]
    b = [3, 2, 1]
    p = []
    for a, b in zip(a, b):
        p.append([a, b])
    pprint(p)

    # done
    print('done')
    # oj t -c "python main.py"
    # sublime `acc config-dir`/python/main.py


if __name__ == '__main__':
    main()
