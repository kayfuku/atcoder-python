#!/usr/bin/env python3
# Author:  + kei
# Date: November 19, 2022
import sys
input = sys.stdin.readline


def solve():
    S = input()
    ans = -1
    for i, c in enumerate(S):
        if c == 'a':
            ans = i + 1

    print(ans)


def main():
    solve()


if __name__ == '__main__':
    main()
