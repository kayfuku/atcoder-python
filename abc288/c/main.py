#!/usr/bin/env python3
# Author:  + kei
# Date: February ?, 2023

from helper_classes import *
from collections import *


class Solution:
    '''
    Author:  + kei
    '''

    def solve(self):
        N, M = map(int, input().split())
        uf = UnionFind(N)
        ans = 0
        for _ in range(M):
            A, B = map(int, input().split())
            A -= 1
            B -= 1
            if uf.is_connected(A, B):
                ans += 1
            else:
                uf.unite(A, B)
                print(ans)


class Try:
    '''
    WA
    Author: kei
    '''

    def solve(self):
        N, M = map(int, input().split())
        g = defaultdict(set)
        for i in range(M):
            A, B = map(int, input().split())
            g[A].add(B)
            g[B].add(A)

        def dfs(v):
            nonlocal cnt
            seen.add(v)
            neighbors = g[v]
            for nei in neighbors:
                if nei != v and nei in seen:
                    cnt += 1
                elif not nei in seen:
                    dfs(nei)

        print(g)
        seen = set()
        cnt = 0
        dfs(1)
        print(cnt)


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
