#!/usr/bin/env python3

def main():
    NX = list(map(int, input().split()))
    P = list(map(int, input().split()))

    N = NX[0]
    X = NX[1]
    for i, p in enumerate(P):
        if p == X:
            print(i + 1)


main()
