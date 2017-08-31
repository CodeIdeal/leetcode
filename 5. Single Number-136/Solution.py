#! /usr/bin/env python
# -*- coding: utf-8 -*-


# input:  nums = [[1, 2, 3, 4,   5,  6]
#                 [7, 8, 9, 10, 11, 12]]
#         r = 3
#         c = 4
# output: new_nums = [[1, 2, 3, 4]
#                     [5, 6, 7, 8]
#                     [9,10,11,12]] 

from itertools import groupby

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        it = groupby((nums))
        for i,g in it:
            list_g = list(g)
            print(str(i)+str(list_g))
            if len(list_g) == 1:
                    return list_g[0]

print(Solution().singleNumber([1,2,3,4,5,6,1,2,3,4,5]))