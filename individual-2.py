#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = list(map(float, input().split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    s = 0
    for i in range(len(a)):
        if i % 2 != 0:
            s += a[i]

    a_first = a_last = a[0]
    i_first = i_last = 0

    for i, item in enumerate(a):
        if item < 0:
            i_first, a_first = i, item
            break
    for i, item in enumerate(a[::-1]):
        if item < 0:
            i_last, a_last = len(a) - i, item
            break

    if i_first > i_last:
        i_first, i_last = i_last, i_first

    summa = 0
    for item in a[i_first+1:i_last]:
        summa += item
    
    while abs(a[0]) >= 1:
        a.pop(0)
        a.append(0)

    print(s, summa, a)