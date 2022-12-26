#!/usr/bin/env python3
# Author: tk727 + kei
# Date: November 19, 2022
from bisect import bisect_left
import sys
input = sys.stdin.readline


def solve1():
    '''
    # Author: tk727 + kei
    # Date: November 19, 2022
    '''
    N = int(input())
    P = list(map(int, input().split()))
    li = [P[-1]]
    for i in range(N - 2, -1, -1):
        idx = bisect_left(li, P[i])
        if idx == 0:
            # Next digit is the minimum in the list.
            li.insert(0, P[i])
        else:
            k = li[idx - 1]
            li.append(P[i])
            li = list(li)
            li.sort(reverse=True)
            ans = [*P[:i]]
            ans.append(k)
            for L in li:
                if L != k:
                    ans.append(L)
            print(*ans)
            return


def solve2():
    '''
    # Author: KoD + kei
    # Date: November 19, 2022
    '''
    N = int(input())
    P = list(map(int, input().split()))

    # Find the first index from the LSD where the value is in non-increasing order to the right.
    j = N - 2
    while P[j] < P[j + 1]:
        j -= 1
    # Assert that P[j + 1:] is sorted in increasing order.

    # Find the first index from the LSD where the value is smaller than Pj.
    k = N - 1
    while P[j] < P[k]:
        k -= 1

    # Swap.
    P[j], P[k] = P[k], P[j]
    # Concat the list to the left of Pj including Pj and the reversed list of
    # the list to the right of Pj.
    print(*P[:j + 1], *P[:j:-1])


def main():
    solve2()


if __name__ == '__main__':
    main()
