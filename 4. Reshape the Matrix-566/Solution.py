#! /usr/bin/env python
# -*- coding: utf-8 -*-


# input:  nums = [[1, 2, 3, 4,   5,  6]
#                 [7, 8, 9, 10, 11, 12]]
#         r = 3
#         c = 4
# output: new_nums = [[1, 2, 3, 4]
#                     [5, 6, 7, 8]
#                     [9,10,11,12]] 


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = 0
        ele = []
        for i in nums:
            n += len(i)
            for j in i:
                ele.append(j)
        if(r*c == n):
            new_array = []
            for i in range(r):
                new_ele = []
                for j in range(c):
                    new_ele.append(ele[j+i*c])
                new_array.append(new_ele)
            return new_array
        else:
            return nums


nums = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

print(Solution().matrixReshape(nums,4,3))