# Author: algo-method + kei
# Date: December 27, 2022
from typing import *
from helper_classes import *
from collections import defaultdict, deque
from sortedcontainers import SortedList, SortedSet, SortedDict
import bisect
import heapq
from functools import cache
from pprint import pprint
import unittest


class Solution:
    '''
    '''

    def solve(self):
        M, N = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(M)]

        INF = float('inf')
        dp = [[INF for _ in range(1 << M)] for _ in range(N+1)]

        # 0 ~ 2^M-1 の塗り方のうち、条件を満たさない塗り方をあらかじめ調べておく
        is_ban = [False for _ in range(1 << M)]
        for bit in range(1 << M):
            for i in range(M-1):
                if (bit & 1 << i) == 0 and (bit & 1 << (i+1)) == 0:
                    is_ban[bit] = True

        # i 行目を塗り方 p で塗るときの、黒マスに書かれた総和
        sum_Acol = [[0 for _ in range(1 << M)] for _ in range(N)]
        for i in range(N):
            for p in range(1 << M):
                tmp = 0
                for j in range(M):
                    if p & 1 << j:
                        tmp += A[j][i]
                sum_Acol[i][p] = tmp

        # DP 初期条件
        full = (1 << M) - 1   # M 行すべて黒く塗るときの塗り方に対応する番号
        dp[0][full] = 0

        # DP テーブルの更新
        for i in range(0, N):
            for p in range(1 << M):
                # i 行目の塗り方 p が条件に反する塗り方ならば、スキップ
                if is_ban[p]:
                    continue

                # i-1 行目の塗り方 bit1 が条件に反する塗り方ならば、スキップ
                for bit1 in range(1 << M):
                    if is_ban[bit1]:
                        continue

                    # p OR bit1 が 11…1 ならば、dp[i][p] を更新する
                    if bit1 | p == full:
                        dp[i+1][p] = min(dp[i+1][p], dp[i][bit1] + sum_Acol[i][p])

        # 答えを出力する
        ans = min(dp[N])
        print(ans)


class Try:
    '''
    WA
    '''

    def solve(self):
        M, N = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(M)]

        INF = float('inf')
        # dp[i][j][p]: min points at (i, j) with paint(p=1) or not paint(p=0)
        dp = [[[INF] * 2 for _ in range(N)] for _ in range(M)]
        dp[0][0][0] = INF
        dp[0][0][1] = grid[0][0]
        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                if i - 1 >= 0:
                    dp[i][j][0] = min(dp[i][j][0], dp[i-1][j][1])
                    dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][1], dp[i-1][j][0])
                if j - 1 >= 0:
                    dp[i][j][0] = min(dp[i][j][0], dp[i][j-1][1])
                    dp[i][j][1] = min(dp[i][j][1], dp[i][j-1][1], dp[i][j-1][0])

                dp[i][j][1] += grid[i][j]

        print(min(dp[M-1][N-1][0], dp[M-1][N-1][1]))


class Bot:

    def solve(self):
        print()


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        Change input and expected output as needed.
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
                # Change to the method name to be tested.
                result = s.topKFrequent(input1, input2)
                self.assertEqual(result, expected)

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     # Binary Tree
    #     #     6
    #     #    /  \
    #     #   3    12
    #     #  / \   / \
    #     # 1   4 9  14

    #     n1 = TreeNode(6)
    #     n2 = TreeNode(3)
    #     n3 = TreeNode(12)
    #     n4 = TreeNode(1)
    #     n5 = TreeNode(4)
    #     n6 = TreeNode(9)
    #     n7 = TreeNode(14)

    #     n1.left = n2
    #     n1.right = n3
    #     n2.left = n4
    #     n2.right = n5
    #     n3.left = n6
    #     n3.right = n7

    #     s = Solution()
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         (n1, n6, n7, n3),
    #         (n1, n3, n5, n1),
    #         (n1, n4, n5, n1),  # Fail
    #     ]
    #     s = Solution()
    #     for input1, input2, input3, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
    #                           expected=expected.val):
    #             result = s.solve(input1, input2, input3)
    #             self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()

    # In the terminal,
    # - To create new directories for problem {problem id}
    # $ acc new {problem id}
    # - To test using sample inputs
    # $ oj t -c "python main.py"
    # - To submit the solution
    # $ acc s
    # - To update the template
    # $ sublime `acc config-dir`/python/main.py


if __name__ == '__main__':
    main()
