# Author: algo-method + kei
# Date: December 24, 2022
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
        N, M = map(int, input().split())
        W = list(map(int, input().split()))
        C = list(map(int, input().split()))

        # K: c, V: list of weights
        weights = [[] for _ in range(256)]
        for i in range(N):
            w, c = W[i], C[i]
            weights[c].append(w)

        # dp[c][w]: True if it's possible to select balls from the first c color whose
        #           weight sum is w, otherwise False.
        dp = [[False] * (M+1) for _ in range(256+1)]
        dp[0][0] = True
        for c in range(256):
            # Not use balls in color c
            dp[c+1][:] = dp[c][:]
            # Use a ball in color c
            for w in range(M+1):
                if dp[c][w] == 0:
                    continue
                for ball_w in weights[c]:
                    if w + ball_w <= M:
                        dp[c+1][w+ball_w] = True

        print('Yes' if dp[256][M] else 'No')


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
