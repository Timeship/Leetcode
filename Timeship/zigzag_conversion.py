#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def convert(self, s, numbers):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numbers == 1:
            return s
        res = ["" for i in range(numbers)]
        i = 0
        s = list(s)
        gap = numbers-2
        while i<len(s):
            for j in range(0,numbers):
                if i<len(s):
                    res[j]+=s[i]
                    i+=1
            for j in range(gap,0,-1):
                if i<len(s):
                    res[j]+=s[i]
                    i+=1
        return "".join(res)

if __name__=='__main__':
    test = Solution()
    print(test.convert("PAYPALISHIRING",3))
