'''
171. Excel Sheet Column Number 
Difficulty: Easy
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
Credits:
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        思路：将26进制转为10进制数:
        举个例子:
        AB
        B->2*(26^0) = 2
        A->1*(26^1) = 26
        res = 2+26 =28
        """
        res = 0
        for index,c in enumerate(reversed(s)):
            res += (ord(c)-ord('A')+1)*int(math.pow(26,index))
        return res
