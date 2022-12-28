# Author: algo-method + kei
# Date: December 28, 2022
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
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        INF = float('inf')
        # dp[i][k]: Max sum of the first i elements when deleting k elements to the left of
        #           A[i] inclusive.
        dp = [[-INF for _ in range(K+1)] for _ in range(N)]
        dp[0][0] = A[0]
        dp[0][1] = 0
        for i in range(1, N):
            # Case 1: Not delete A[i] (Use A[i])
            # Take max of not deleting A[i-1] or deleting K elements to the left of
            # A[i-1] inclusive.
            # Store the max sum from not deleting K elemes at i-1 or deleting K elems at i-1,
            # plus A[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][K]) + A[i]

            # Case 2: Delete A[i] (Not use A[i])
            # Store the result when deleting k (1 <= k <= K) elements to the left of A[i].
            for k in range(1, K+1):
                # Delete k elements to the left of A[i]
                # dp[i-1] has already the info. Use it.
                dp[i][k] = dp[i-1][k-1]

                # Store the max sum from not deleting K elemes at i-1 or deleting K elems at i-1.
                if k == K:
                    dp[i][k] = max(dp[i-1][k-1], dp[i-1][k])

        ans = max(dp[N-1][0], dp[N-1][K])
        print(ans)


class Try:

    def solve(self):
        S = input()
        N = int(input())
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
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
