'''
168. Excel Sheet Column 
Difficulty: Easy
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
Credits:
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        思路：实际上就是将10进制数(每位0-9)->26进制（每位0-25,对应A-Z）
        --------------------------------------------------------------
        举例1：输入52，从0计数就是51；51 ->26进制： 
        当前个位:51%26 = 25 ->"Z"  更新 51->51/26 = 1
        当前个位:1%26  = 1 ->"A"  更新 1->1/26 = 0
        因此最终结果为 AZ
        ------------------------------------------------------------
        举例2：输入53，从0计数就是52；52 ->26进制： 
        当前个位:52%26 = 0 ->"A"  更新 52->52/26 = 2
        当前个位:2%26  = 2 ->"B"  更新 2->2/26 = 0
        因此最终结果为 BA
        
        """
        res =""
        while n:
            res = chr((n-1)%26+ord('A'))+res
            n = (n-1)/26
        return res
