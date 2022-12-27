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
        N = int(input())
        A = [list(map(int, input().split())) for _ in range(2)]

        INF = float('inf')
        # dp[i][p]: Min points to paint cells in the first i columns with paint way p
        # p = 0: not paint any cell (this is not allowed in this problem)
        # p = 1: paint top cell only
        # p = 2: paint bottom cell only
        # p = 3: paint top and bottom cells
        dp = [[INF] * 4 for _ in range(N)]
        dp[0][1] = A[0][0]
        dp[0][2] = A[1][0]
        dp[0][3] = A[0][0] + A[1][0]

        for i in range(1, N):
            # p = 1 requires p = 2 or p = 3 in the previous column
            dp[i][1] = min(dp[i-1][2], dp[i-1][3]) + A[0][i]
            # p = 2 requires p = 1 or p = 3 in the previous column
            dp[i][2] = min(dp[i-1][1], dp[i-1][3]) + A[1][i]
            # p = 3 requires p = 1, p = 2, or p = 3 in the previous column
            dp[i][3] = min(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + A[0][i] + A[1][i]

        ans = min(dp[N-1][1], dp[N-1][2], dp[N-1][3])
        print(ans)


class Try:

    def solve(self):
        N = int(input())
        A = []
        for _ in range(N):
            A.append(list(map(int, input().split())))

        INF = float('inf')
        dp = [[INF] * N for _ in range(2)]
        for i in range(N):
            dp[i][0] = A[i][0]

        print(min(dp[0][N-1], dp[1][N-1]))


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
