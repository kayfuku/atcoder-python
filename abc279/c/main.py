#!/usr/bin/env python3
# Author:  + kei
# Date: November 26, 2022

# from helper_classes import *
from collections import *


class Solution:

    def __init__(self):
        pass

    def solve(self):
        '''
        Author: kaz_mighty + kei
        '''
        from collections import Counter

        h, w = map(int, input().split())
        s1 = [input() for _ in range(h)]
        t1 = [input() for _ in range(h)]
        s2 = Counter()
        for col in zip(*s1):
            # Count the vertical signature (col string) among all columns.
            sig = ''.join(col)
            s2[sig] += 1
        t2 = Counter()
        for col in zip(*t1):
            sig = ''.join(col)
            t2[sig] += 1
        # Check if all the counts are equal.
        if s2 == t2:
            print('Yes')
        else:
            print('No')


class Try:

    def __init__(self):
        pass

    def solve(self):
        H, W = map(int, input().split())
        S = [input() for _ in range(H)]
        T = [input() for _ in range(H)]
        for i in range(H):
            cnt_s = Counter(S[i])
            cnt_t = Counter(T[i])
            if cnt_s != cnt_t:
                print('No')
                return

        li_cnt_s = []
        for j in range(W):
            cnt_s_col = 0
            for i in range(H):
                if S[i][j] == 1:
                    cnt_s_col += 1
            li_cnt_s.append(cnt_s_col)

        li_cnt_t = []
        for j in range(W):
            cnt_t_col = 0
            for i in range(H):
                if T[i][j] == 1:
                    cnt_t_col += 1
            li_cnt_t.append(cnt_t_col)

        cnts_s_col = Counter(li_cnt_s)
        cnts_t_col = Counter(li_cnt_t)
        if cnts_s_col == cnts_t_col:
            print('Yes')
        else:
            print('No')


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
