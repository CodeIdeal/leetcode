#! /usr/bin/env python
# -*- coding: utf-8 -*-

def solution1(x, y):
    return bin(x^y).count("1")


def solution2(x, y):
    b_res = x^y
    n = 0
    while b_res > 0:
        if b_res & 1 == 1:
            n += 1
        b_res = b_res >> 1
    return n


def solution3(x, y):
        b_res = x^y
        n = 0
        while b_res > 0:
            n += b_res & 1
            b_res >>= 1
        return n

print(solution3(3, 4))