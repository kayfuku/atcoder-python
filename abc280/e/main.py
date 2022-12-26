#!/usr/bin/env python3
# Author:  + kei
# Date: December 10, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    DP
    '''

    def solve(self):
        '''
        Author: Kiri8128 + kei
        '''
        MOD = 998244353
        N, P = map(int, input().split())
        MINV = 828542813
        # P / 100 % MOD
        p = P * MINV % MOD
        q = (1 - p) % MOD
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            dp[i] = (1 + dp[i - 1] * q + dp[i - 2] * p) % MOD
        print(dp[N])


class NoSolution(ArithmeticError):
    pass


class Try:
    '''
    '''

    def solve(self):
        '''
        WA
        '''
        n, p = map(int, input().split())
        MOD = 998244353

        def extra_GCD(a, b):
            '''
            Return (x, y) where ax + by = gcd(a, b) = z
            '''
            z1, z2 = a, b
            x1, y1 = 1, 0
            x2, y2 = 0, 1
            while z2:
                t = z1 // z2
                z1 -= t * z2
                x1 -= t * x2
                y1 -= t * y2
                z1, z2 = z2, z1
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            x1 = x1 % (b // z1)
            y1 = (z1 - a * x1) // b
            return x1, y1, z1

        def mod_div(a, b, m):
            x, y, gcd = extra_GCD(b, m)
            if gcd == 1:
                return a * x % m
            elif a % gcd == 0:
                return x * (a // gcd) % (m // gcd)
            else:
                raise NoSolution("{} / {} (mod {})".format(a, b, n))

        MINV = mod_div(1, 100, MOD)
        print(MINV)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            # Recurrence relation
            # dp[i]: Expectation of times of attack that reduces i or more stamina.
            dp[i] = (dp[i - 1] + 1 + dp[i - 2] + p * MINV) % MOD

        print(dp[n] % MOD)

    def solve2(self):
        N, P = map(int, input().split())
        MOD = 998244353

        def extra_GCD(a, b):
            '''
            ax + by = gcd(a, b) = z
            '''
            z1, z2 = a, b
            x1, y1 = 1, 0
            x2, y2 = 0, 1
            while z2:
                t = z1 // z2
                z1 -= t * z2
                x1 -= t * x2
                y1 -= t * y2
                z1, z2 = z2, z1
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            x1 = x1 % (b // z1)
            y1 = (z1 - a * x1) // b
            return x1, y1, z1

        def mod_div(a, b, n):
            x, y, gcd = extra_GCD(b, n)
            if gcd == 1:
                return a * x % n
            elif a % gcd == 0:
                return x * (a // gcd) % (n // gcd)
            else:
                raise NoSolution("{} / {} (mod {})".format(a, b, n))

        # 1 / 100
        MINV = mod_div(1, 100, MOD)

        def helper(n):
            if n <= 1:
                return n
            if n in memo:
                return memo[n]
            # P / 100 % MOD
            p = P * MINV % MOD
            q = (1 - p) % MOD
            memo[n] = (1 + q * helper(n - 1) + p * helper(n - 2)) % MOD
            return memo[n]

        memo = {}
        print(helper(N))


def main():
    # t = Try()
    # t.solve2()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
