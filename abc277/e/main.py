#!/usr/bin/env python3
# Author: + kei
# Date: November 18, 2022
from collections import deque
import sys
input = sys.stdin.readline


def solve():
    N, M, K = map(int, input().split())
    # Create an undirected graph with Adjacency List for each flag.
    edges = [[set() for _ in range(N)] for _ in range(2)]
    for _ in range(M):
        u, v, a = map(int, input().split())
        u -= 1
        v -= 1
        edges[a][u].add(v)
        edges[a][v].add(u)

    li = list(map(int, input().split()))
    S = set()
    for s in li:
        S.add(s - 1)

    # To store the minimum cost from the start node for each node with each state
    # Each node has two states, 0 or 1.
    # node number: index % N, state: index // N
    # index: (state) * N + (node number)
    INF = float('inf')
    bfs_cost = [INF] * (2 * N)

    # 01BFS
    q = deque()
    # The start node number is 0 with state 1, which is index N in bfs_cost, and
    # the cost is 0.
    # If the start node has a switch, then do BFS alternatively.
    bfs_cost[N] = 0
    q.append(N)
    if 0 in S:
        bfs_cost[0] = 0
        q.append(0)

    # BFS will finish if there is no more updates.
    while q:
        # current node
        cn = q.popleft()
        # a: state, 0 or 1
        a = cn // N
        # v: node number
        v = cn % N
        # Check the neighbor nodes with the current state.
        for u in edges[a][v]:
            # a * N + u represents a node with the current state.
            # bfs_cost[cn] + 1 means that we can reach the current node from the
            # start node at the cost of bfs_cost[cn] plus one more edge.
            if bfs_cost[a * N + u] > bfs_cost[cn] + 1:
                # Update the minimum cost.
                bfs_cost[a * N + u] = bfs_cost[cn] + 1
                # Keep doing BFS because the cost has been updated.
                q.append(a * N + u)

            # If the node has a switch, then update the cost for the node with the other state.
            if u in S:
                if bfs_cost[(1 ^ a) * N + u] > bfs_cost[cn] + 1:
                    # Update the minimum cost.
                    bfs_cost[(1 ^ a) * N + u] = bfs_cost[cn] + 1
                    # Keep doing BFS because the cost has been updated.
                    q.append((1 ^ a) * N + u)

    ans = min(bfs_cost[N - 1], bfs_cost[2 * N - 1])
    if ans == INF:
        print(-1)
    else:
        print(ans)


def main():
    solve()


if __name__ == '__main__':
    main()
