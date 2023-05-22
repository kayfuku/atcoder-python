#!/usr/bin/env python3
# Author: tk727 + kei
# Date: November 19, 2022

# from helper_classes import *
from collections import *
import sys
input = sys.stdin.readline


class Solution:

    def __init__(self):
        self.is_confusing = [False] * 60 * 24
        for h in range(24):
            for m in range(60):
                h1 = h // 10
                h2 = h % 10
                m1 = m // 10
                m2 = m % 10
                if 0 <= h1 * 10 + m1 < 24 and 0 <= h2 * 10 + m2 < 60:
                    self.is_confusing[60 * h + m] = True

    def solve(self):
        H, M = map(int, input().split())
        start = 60 * H + M
        for k in range(start, start + 1440):
            if self.is_confusing[k % 1440]:
                print((k % 1440) // 60, (k % 1440) % 60)
                return


class Try:

    def get_next_time(self, ch, cm):
        if cm == 59:
            ch = (ch + 1) % 24
        cm = (cm + 1) % 60
        return ch, cm

    def is_confusing(self, h, m):
        h1 = h // 10
        h2 = h % 10
        m1 = m // 10
        m2 = m % 10
        con_h = h1 * 10 + m1
        con_m = h2 * 10 + m2
        return 0 <= con_h <= 23 and 0 <= con_m <= 59

    def solve(self):
        H, M = map(int, input().split())
        ch = H
        cm = M
        while not self.is_confusing(ch, cm):
            ch, cm = self.get_next_time(ch, cm)

        print(ch, cm)


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
