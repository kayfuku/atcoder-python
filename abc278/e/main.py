#!/usr/bin/env python3
# Author:  + kei
# Date: November 23, 2022

# from helper_classes import *
from collections import Counter
from collections import *
from sys import stdin
input = stdin.readline


class Solution:

    def __init__(self):
        pass

    def solve(self):
        """
        Author: kaz_mighty + kei
        """
        H, W, N, h, w = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(H)]
        count_all = Counter()
        # Count for all cells.
        for a_i in A:
            # update() adds up instead of replacing.
            count_all.update(a_i)

        # Print line by line.
        for i in range(H - h + 1):
            count = count_all.copy()
            # Col 0
            for y in range(i, i + h):
                for x in range(0, w):
                    a_yx = A[y][x]
                    count[a_yx] -= 1
                    if count[a_yx] == 0:
                        del count[a_yx]

            ans = [len(count)]

            # Col 1 to W - w
            for j in range(W - w):
                for y in range(i, i + h):
                    # Come up.
                    count[A[y][j]] += 1
                    # Hide out.
                    a_yx = A[y][j + w]
                    count[a_yx] -= 1
                    if count[a_yx] == 0:
                        del count[a_yx]
                ans.append(len(count))

            print(*ans)


class Try:

    def solve():
        N = map(int, input().split())


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
