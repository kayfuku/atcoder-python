# Author: algo-method + kei
# Date: December 23, 2022
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
    O(NS^2D) time
    '''

    def solve(self):
        N, A, B = map(int, input().split())
        P = list(map(int, input().split()))
        Q = list(map(int, input().split()))
        R = list(map(int, input().split()))

        prices = [P, Q, R]

        INF = float('inf')
        # dp[i][s][t]: day i, store s {0, 1, 2}, and how many times to visit {1, 2, 3}
        dp = [[[INF] * 4 for _ in range(3)] for _ in range(N)]
        for s in range(3):
            dp[0][s][1] = prices[s][0]

        for i in range(1, N):
            for s in range(3):
                # Update the min in all the status.
                # Case t = 1
                # Visit the store s today after visiting the different store yesterday.
                # Calc the minimum cost from all the other stores with all the status.
                min_pre_cost = INF
                for ps in range(3):
                    if ps == s:
                        continue
                    for pt in range(1, 4):
                        min_pre_cost = min(min_pre_cost, dp[i-1][ps][pt])
                # no discount
                dp[i][s][1] = min_pre_cost + prices[s][i]

                # Case t = 2
                # Visit the same store twice in a row. Get a discount A.
                dp[i][s][2] = dp[i-1][s][1] + prices[s][i] - A

                # Case t = 3
                # Visit the same store the third time in a row. Get a discount B.
                # Be careful about the previous status used.
                dp[i][s][3] = min(dp[i-1][s][2], dp[i-1][s][3]) + \
                    prices[s][i] - B

        ans = INF
        for s in range(3):
            for t in range(1, 4):
                ans = min(ans, dp[N-1][s][t])
        print(ans)


class Try:

    def solve(self):
        N, A, B = map(int, input().split())
        P = list(map(int, input().split()))
        Q = list(map(int, input().split()))
        R = list(map(int, input().split()))

        prices = [P, Q, R]
        INF = float('inf')
        dp = [[INF] * 3 for _ in range(N)]
        for i in range(N):
            for s in range(3):
                pass
        print()


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
