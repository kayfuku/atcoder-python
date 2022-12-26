#!/usr/bin/env python3
# Author: + kei
# Date: November 26, 2022

# from helper_classes import *
from collections import *
from sys import stdin
input = stdin.readline


class Solution:
    '''
    Author: maki_glenscape + kei
    '''

    def solve(self):
        N, M, K = map(int, input().split())
        MOD = 998244353

        def extgcd(a, b):
            if b == 0:
                return (a, 1, 0)
            g, x, y = extgcd(b, a % b)
            return (g, y, x - a // b * y)

        def modinv(a, mod):
            return extgcd(a, mod)[1]

        # 1 / M
        minv = modinv(M, MOD)
        ans = 0
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        dp[0][0] = 1
        # Probability of being at j after spinning the wheel i times.
        for i in range(1, K + 1):
            for j in range(N + 1):
                now = (dp[i - 1][j] * minv) % MOD
                # Spin the wheel.
                for m in range(1, M + 1):
                    next = j + m
                    if next > N:
                        next -= (next - N) * 2
                    if next == N:
                        # Got to N. Cumsum of probabilities to get to N
                        # by spinning the wheel j times.
                        ans += now
                    else:
                        dp[i][next] += now

        print(ans % MOD)


class Try:

    def __init__(self):
        pass

    def solve(self):
        N, M, K = map(int, input().split())

        print()


# class Bot:
#     '''
#     RE
#     Author: ChatGPT + kei
#     '''

#     def solve(self) -> int:
#         N, M, K = map(int, input().split())
#         P = [[0] * (K + 1) for _ in range(N + 1)]

#         for j in range(K + 1):
#             P[N][j] = 1

#         for i in range(N - 1, -1, -1):
#             for j in range(K + 1):
#                 # Probability of exceeding N
#                 q = (M - (N - i)) / M
#                 P[i][j] = (1 - q) * P[i + 1][j + 1] if q >= 0 else 0
#                 P[i][j] += q * P[i - 1][j + 1]

#         return P[0][0]


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()

    # b = Bot()
    # b.solve()


if __name__ == '__main__':
    main()
