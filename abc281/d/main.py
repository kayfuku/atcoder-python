#!/usr/bin/env python3
# Author:  + kei
# Date: December 10, 2022

# from helper_classes import *
from itertools import combinations
from collections import *


class Solution:

    def solve(self):
        '''
        Author: atcoder + kei
        '''
        N, K, D = map(int, input().split())
        A = list(map(int, input().split()))
        # dp[i][j][k]: maximum of sums of j number of elements selected from
        # a1, a2, ... ai where (the cumsum) % D = k.
        dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]
        dp[0][0][0] = 0
        for i in range(N):
            ni = i + 1
            for j in range(K + 1):
                for r in range(D):
                    now = dp[i][j][r]
                    if now == -1:
                        continue
                    # not use ai
                    nj = j
                    nr = r
                    dp[ni][nj][nr] = max(dp[ni][nj][nr], now)
                    if j + 1 <= K:
                        # use ai
                        nj = j + 1
                        nr = (r + A[i]) % D
                        dp[ni][nj][nr] = max(dp[ni][nj][nr], now + A[i])

        # print(dp)
        print(dp[N][K][0])

    def solve2(self):
        '''
        Author: Kiri8128 + kei
        '''
        N, K, D = map(int, input().split())
        A = [int(a) for a in input().split()]
        X = [[-1] * D for _ in range(K + 1)]
        X[0][0] = 0
        for a in A:
            nX = [x[:] for x in X]
            for j, x in enumerate(X):
                for k, xx in enumerate(x):
                    if j < K and xx >= 0:
                        nk = (k + a) % D
                        nj = j + 1
                        nX[nj][nk] = max(nX[nj][nk], xx + a)
            X = nX

        print(X[K][0])


class Try:
    '''
    TLE
    Author: kei
    '''

    def __init__(self):
        pass

    def solve(self):
        N, K, D = map(int, input().split())
        A = list(map(int, input().split()))

        def backtrack(start, cnt, sum_):
            nonlocal ans
            if cnt == K:
                if sum_ % D == 0:
                    ans = max(ans, sum_)
                return 0

            if start == N:
                return

            for i in range(start, N):
                sum_ += A[i]
                backtrack(i + 1, cnt + 1, sum_)
                sum_ -= A[i]

        ans = -1
        backtrack(0, 0, 0)
        print(ans)


class Bot:
    '''
    TLE
    '''

    def solve(self):
        N, K, D = map(int, input().split())
        A = list(map(int, input().split()))
        # A の K 個の項の組み合わせをすべて取得する
        comb = combinations(A, K)
        # D の倍数の最大値を保存する変数
        max_multiple = -1
        # 組み合わせをすべて調べる
        for c in comb:
            # 組み合わせの和を計算する
            sum_c = sum(c)
            # 組み合わせの和が D の倍数であるかどうかを判定する
            if sum_c % D == 0:
                # D の倍数である場合、max_multiple を更新する
                max_multiple = max(max_multiple, sum_c)

        print(max_multiple)


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()

    # b = Bot()
    # b.solve()


if __name__ == '__main__':
    main()
