#!/usr/bin/env python3
# Author:  + kei
# Date: January 7, 2023

# from helper_classes import *
from math import sqrt
from collections import *


class Solution:
    '''
    Author: tk727 + kei
    '''

    def solve(self):
        # min(p, q) <= 3 * 10**6
        primes = [1] * (3*10**6)
        primes[0] = primes[1] = 0
        prime_set = set()
        for i in range(2, 3*10**6):
            if primes[i]:
                prime_set.add(i)
                # Set 0 for number that is a product of i.
                for j in range(i**2, 3*10**6, i):
                    primes[j] = 0

        T = int(input())
        for _ in range(T):
            N = int(input())
            for p in prime_set:
                if N % p == 0:
                    # TODO:
                    if N % (p**2) == 0:
                        print(p, N // (p**2))
                        break
                    else:
                        K = int(sqrt(N//p))
                        for k in range(K-2, K+3):
                            if p * (k**2) == N:
                                print(k, p)
                            break


class Try:
    '''
    NG
    Author: kei
    '''

    def prime_factorize(self, n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    def solve(self):
        T = int(input())
        for t in range(T):
            N = int(input())
            a = []
            p = q = 0
            cnt = 0
            n = N
            while n % 2 == 0:
                cnt += 1
                q = 2
                if cnt == 2:
                    p = 2
                    q = 0
                    break
                n //= 2
            f = 3
            c = defaultdict(int)
            cnt = 0
            while f * f <= n:
                if n % f == 0:
                    a.append(f)
                    if q == 0 and p == 2:
                        q = f
                        break
                    if q == 2:
                        p = f
                        break

                    if N % f == 0:
                        if N % f**2 == 0:
                            p = f
                            q = N % f**2
                        else:
                            # TODO:
                            pass
                        break

                    n //= f
                else:
                    f += 2

            print(p, q)


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
