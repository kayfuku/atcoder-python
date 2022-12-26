#!/usr/bin/env python3
# Author: tk727 + kei
# Date: November 17, 2022
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    if N == 1:
        print(0)
        return

    # Sort A in place.
    A.sort()
    S = sum(A)
    sums = []
    # Note that we can't use 'sum' variable because we use sum().
    s = A[0]
    for i in range(1, N):
        if A[i] - A[i - 1] <= 1:
            s += A[i]
        else:
            # two or more gap
            sums.append(s)
            s = A[i]

    if len(sums) == 0:
        sums.append(s)
    elif (A[N - 1] + 1) % M == 0 and A[0] == 0:
        # M is equal to (the last value) + 1, and min(A) is equal to 0.
        # We can return to the first value and keep throwing the last sum away with the first sum.
        # Note that in this case, len(sums) must be two or more.
        sums[0] += s
    else:
        sums.append(s)

    print(S - max(sums))


if __name__ == '__main__':
    main()
