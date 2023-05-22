#!/usr/bin/env python3
# Author: lloyz23 + kei
# Date: November 17, 2022
from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    # Create a graph with Adjacency List.
    G = defaultdict(list)
    for _ in range(N):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # BFS
    q = deque([1])
    seen = set([1])
    max_ = 1
    while q:
        node = q.popleft()
        max_ = max(max_, node)

        for nei in G[node]:
            if nei in seen:
                continue
            q.append(nei)
            seen.add(nei)

    print(max_)


if __name__ == '__main__':
    main()
