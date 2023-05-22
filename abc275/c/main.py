#!/usr/bin/env python3
# Author:  + kei
# Date: November 25, 2022

# from helper_classes import *
from collections import *
from sys import stdin
input = stdin.readline


class Solution:

    def __init__(self):
        pass

    def solve(self):
        '''
        Pick up one vector and a square will be defined.
        Check if the other two points are valid.
        Author: kyopro_friends + kei
        '''
        S = [input() for _ in range(9)]
        ans = 0
        for i1 in range(9):
            for j1 in range(9):
                if S[i1][j1] == ".":
                    continue
                # P1 picked up.

                for i2 in range(9):
                    for j2 in range(9):
                        if S[i2][j2] == "." or (i1, j1) == (i2, j2):
                            continue
                        # P2 picked up, and P1 -> P2 is a vector.
                        # Calculate dx and dy.
                        dx = j2 - j1
                        dy = i2 - i1

                        # Find P3 and P4 clockwise that make up a square with P1 and P2.
                        i3 = i2 + dx
                        j3 = j2 - dy
                        i4 = i3 - dy
                        j4 = j3 - dx

                        # Check if P3 and P4 are valid.
                        if not (0 <= min(i3, i4, j3, j4) and max(i3, i4, j3, j4) < 9):
                            # Out of bound
                            continue
                        if S[i3][j3] == "#" and S[i4][j4] == "#":
                            ans += 1

        # Don't forget to divide by 4 because we consider P1 as one of four points of a square.
        print(ans // 4)


class Try:

    def __init__(self):
        pass

    def solve(self):
        g = [input() for _ in range(9)]

        print()


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
