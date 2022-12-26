#!/usr/bin/env python3
# Author:  + kei
# Date: December 3, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author: Kiri8128 + kei
    '''

    def __init__(self):
        pass

    def solve(self):

        def get_prime_factors(N):
            i, n, ret, d, sq = 2, N, {}, 2, 99
            while i <= sq:
                k = 0
                while n % i == 0:
                    n, k, ret[i] = n // i, k + 1, k + 1
                if k > 0 or i == 97:
                    sq = int(n ** (1 / 2) + 0.5)
                if i < 4:
                    i = i * 2 - 1
                else:
                    i, d = i + d, d ^ 6
            if n > 1:
                ret[n] = 1
            return ret

        def calc(p, a):
            # TODO: ??
            def chk(n):
                s = 0
                while n:
                    s += n
                    n //= p
                return s

            # Find minimum n where chk(n) is equal to a.
            # Binary Search leftmost
            l = 0
            r = a
            while l <= r:
                m = (l + r) // 2
                if chk(m) >= a:
                    r = m - 1
                else:
                    l = m + 1
            # l holds the minimum.

            # TODO: ??
            return p * l

        ans = 0
        K = int(input())
        for p, a in get_prime_factors(K).items():
            # Find minimum Ni for each prime number pi where Ni! is a product of pi^a.
            ni = calc(p, a)
            # Take max of each minimum Ni because N! is a product of M! if N > M.
            ans = max(ans, ni)

        print(ans)


class Try:

    def __init__(self):
        pass

    def solve(self):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        print()


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
