#!/usr/bin/env python3
# Author:  + kei
# Date: December 24, 2022

# from helper_classes import *
from collections import *
from sortedcontainers import SortedList
import bisect


class Solution:
    '''
    Author: kaz_mighty + kei
    '''

    def solve(self):
        s = input()
        stack = [set()]
        for si in s:
            if si == '(':
                stack.append(stack[-1].copy())
            elif si == ')':
                stack.pop()
            else:
                if si in stack[-1]:
                    print('No')
                    return
                stack[-1].add(si)
        print('Yes')


class Try:
    '''
    Author: kei
    '''

    def solve(self):
        S = input()
        s_list = []
        str_set = set()
        open_idx_stack = []
        for i in range(len(S)):
            if S[i] == '(':
                open_idx_stack.append(i)
            elif S[i] != ')':
                if S[i] in str_set:
                    print('No')
                    return
                str_set.add(S[i])
                s_list.append(S[i])
            else:
                last_open_idx = open_idx_stack.pop()
                del_idx = bisect.bisect(last_open_idx)
                j = del_idx
                while j < len(s_list):
                    str_set.remove(s_list[j][1])
                    s_list.pop(j)
                    j += 1

        print('Yes')


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
