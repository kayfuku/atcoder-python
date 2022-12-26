#!/usr/bin/env python3
# Author: + kei
# Date: November 19, 2022
from collections import *
from sys import stdin
input = stdin.readline


class Solution:

    def solve(self):
        pass


class Try:

    def solve(self):
        '''
        Author: kei
        '''
        H, W = map(int, input().split())
        g = [input() for _ in range(H)]
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Get cells around start cell.
        cells_around_start = []
        for r in range(H):
            for c in range(W):
                if g[r][c] == 'S':
                    for dr, dc in D:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < H and 0 <= nc < W and g[nr][nc] == '.':
                            cells_around_start.append((nr, nc))

        def is_reachable_dfs(r, c, tr, tc):
            '''
            DFS is not good for searching in huge space.
            '''
            if (r, c) == (tr, tc):
                return True

            seen.add((r, c))
            for dr, dc in D:
                nr = r + dr
                nc = c + dc
                # We're checking (nr, nc), not (r, c)!
                # Don't forget to check if it's not in 'seen'.
                if 0 <= nr < H and 0 <= nc < W and g[nr][nc] == '.' and \
                        (nr, nc) not in seen:
                    if is_reachable_dfs(nr, nc, tr, tc):
                        return True

            return False

        def is_reachable_bfs(row, col, tr, tc):
            '''
            BFS is better for searching in huge space.
            '''
            q = deque()
            q.append((row, col))
            seen.add((row, col))
            while q:
                r, c = q.popleft()
                if (r, c) == (tr, tc):
                    return True

                for dr, dc in D:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < H and 0 <= nc < W and g[nr][nc] == '.' and \
                            (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr, nc))

            return False

        for sr, sc in cells_around_start:
            for tr, tc in cells_around_start:
                # Don't forget to initialize 'seen' each time!
                seen = set()
                if (sr, sc) == (tr, tc):
                    continue

                if is_reachable_bfs(sr, sc, tr, tc):
                    print('Yes')
                    return

        print('No')
        return


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
