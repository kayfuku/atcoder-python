#!/usr/bin/env python3
# Author:  + kei
# Date: December 17, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author: kaz_mighty + kei
    '''

    def __init__(self):
        pass

    def solve(self):
        N, M = map(int, input().split())
        edges = [[] for _ in range(N+1)]
        for _ in range(M):
            u, v = map(int, input().split())
            edges[u].append(v)
            edges[v].append(u)

        ans = N * (N - 1) // 2 - M
        colors = [0] * (N+1)
        for i in range(1, N+1):
            if colors[i] != 0:
                continue
            color_count = [0, 1, 0]
            stack = [(i, 1)]
            colors[i] = 1
            while stack:
                vertex, color = stack.pop()
                for edge in edges[vertex]:
                    if colors[edge] != 0:
                        if colors[edge] == color:
                            print(0)
                            exit()
                        continue
                    next_color = 3 - color
                    colors[edge] = next_color
                    color_count[next_color] += 1
                    stack.append((edge, next_color))
            for count in color_count:
                ans -= count * (count-1) // 2

        print(ans)


class Try:
    '''
    Author: kaz_mighty + kei
    '''

    def solve(self):
        N, M = map(int, input().split())
        g = defaultdict(set)
        for _ in range(M):
            u, v = map(int, input().split())
            g[u].add(v)
            g[v].add(u)

        def is_bipartite(v):
            color_to_num_nodes[1] = 1
            q = deque([(v, 1)])
            # Don't forget this! This is also used as visited.
            colors[v] = 1
            while q:
                cn, cc = q.popleft()
                for nei in g[cn]:
                    if colors[nei] != 0:
                        if colors[nei] == cc:
                            return False
                        continue

                    next_color = cc * (-1)
                    colors[nei] = next_color
                    color_to_num_nodes[next_color] += 1
                    q.append((nei, next_color))

            return True

        colors = [0] * (N+1)
        ans = N * (N-1) // 2 - M
        # Start from every node to explore.
        for i in range(N+1):
            if colors[i] != 0:
                continue
            color_to_num_nodes = defaultdict(int)
            if not is_bipartite(i):
                print(0)
                return
            # Subtract the number of edges of all nodes whose colors are the same.
            for num_nodes in color_to_num_nodes.values():
                ans -= num_nodes * (num_nodes-1) // 2

        print(ans)


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
