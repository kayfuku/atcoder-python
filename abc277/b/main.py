#!/usr/bin/env python3

def main():
    N = int(input())
    set_1 = set('HDCS')
    set_2 = set('A23456789TJQK')
    set_s = set()
    for i in range(N):
        s = input()
        if (not s[0] in set_1) or (not s[1] in set_2) or (s in set_s):
            print('No')
            return

        set_s.add(s)

    print('Yes')


main()
