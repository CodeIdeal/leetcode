# !/usr/bin/env python
# -*- coding: utf-8 -*-


# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
import re


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr, nums, strs = [], [], []
        n = 0

        for c in s:
            print("字符" + c + '-----------------------------------------------')
            if c.isdigit():
                n = n * 10 + ord(c) - ord('0')
            elif c == '[':
                nums.append(n)
                n = 0
                strs.append(curr)
                curr = []
            elif c == ']':
                strs[-1].extend(curr * nums.pop())
                curr = strs.pop()
            else:
                curr.append(c)
            print('n='+str(n))
            print('nums'+str(nums))
            print('curr'+str(curr))
            print('strs'+str(strs))

        return "".join(strs[-1]) if strs else "".join(curr)
# note

# ord()--Return the Unicode code point for a one-character string.
# 对一个数字字符'n'，ord('n') - ord('0')就是字符所对应的数字值

# n = n * 10 + ord(c) - ord('0')
# 这一行代码在遍历一个数的字符串时(eg:'321'),能实现字符串转数字的function
#
# def str2num(num_str):
#     n = 0 
#     for c in num_str:
#         n = n * 10 + ord(c) - ord('0')
#     return n

# list.extend(list) 列表的extend方法，入参也是一个list，它将参数中的所有元素添加到原list中
# 类似java中的List.addAll()函数

# 该解法是吧nums和strs两个数组当作栈来处理字符结构的多重嵌套结构
# curr则作为字符处理过程中的中间值的存储空间

    def decodeString2(self, s):
        while '[' in s:
            print(s)
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s
# 正则的解法利用了最内层的数据结构一定时 n[letters] 的形式，继而能够从内而外的解除嵌套结构


a = Solution()

print(a.decodeString2('bb3[a4[b]]dd'))


