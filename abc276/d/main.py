#!/usr/bin/env python3
# Author: tk727 + kei
# Date: November 19, 2022
import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    INF = float("inf")
    cnt = 0
    min2 = INF
    min3 = INF
    S = set()
    for ai in A:
        # Think about the prime factorization for ai.
        cnt2 = 0
        cnt3 = 0
        # Count the number of 2.
        while ai % 2 == 0:
            ai //= 2
            cnt2 += 1
        # assert that ai is not divided by 2 anymore.

        # Count the number of 3.
        while ai % 3 == 0:
            ai //= 3
            cnt3 += 1
        # assert that ai is not divided by 3 anymore.

        cnt += cnt2 + cnt3
        min2 = min(min2, cnt2)
        min3 = min(min3, cnt3)
        # for other factor that can't be divided by 2 or 3
        S.add(ai)

    # print(S)

    if len(S) != 1:
        # Two or more other factors.
        print(-1)
    else:
        # The other factor is just one. So, we can make all the numbers equal.
        print(cnt - (min2 + min3) * N)


def main():
    solve()


if __name__ == '__main__':
    main()
