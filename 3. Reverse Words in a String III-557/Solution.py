#! /usr/bin/env python
# -*- coding: utf-8 -*-


Input = "Let's take LeetCode contest"
Output = "s'teL ekat edoCteeL tsetnoc"


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        output = ""
        for i,word in enumerate(words):
            word = word[::-1]
            output += word
            if i != len(words) - 1:
                output += " "
        return output


class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        result = []
        for word in words:
            word = word[::-1]
            result.append(word)
        return " ".join(result)


print(Solution().reverseWords(Input))