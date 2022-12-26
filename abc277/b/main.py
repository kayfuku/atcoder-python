#!/usr/bin/env python3

def main():
    N = int(input())
    set_1 = set('HDCS')
    set_2 = set('A23456789TJQK')
    set_s = set()
    for i in range(N):
        s = input()
        if (s[0] not in set_1) or (s[1] not in set_2) or (s in set_s):
            print('No')
            return

        set_s.add(s)

    print('Yes')


main()
