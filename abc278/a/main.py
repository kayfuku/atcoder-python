#!/usr/bin/env python3
# Author: tk727 + kei
# Date: November 19, 2022

# from helper_classes import *
from collections import *
import sys
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    A = deque(list(map(int, input().split())))
    for _ in range(K):
        A.append(0)
        A.popleft()

    print(*A)


def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K >= N:
        ans = [0] * N
        print(*ans)
        return

    ans = A[K:]
    for i in range(K):
        ans.append(0)
    print(*ans)


def main():
    # solve()
    solution()


if __name__ == '__main__':
    main()
