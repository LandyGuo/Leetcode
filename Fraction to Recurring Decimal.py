'''
166. Fraction to Recurring Decimal My Submissions QuestionEditorial Solution
Total Accepted: 28692 Total Submissions: 192194 Difficulty: Medium
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        思路：如果余数已经出现过，那么就表明肯定出现了循环,因此需要保存每次余数，同时为了获得最后的结果，也要保存每一次的商
        1）维护一个商数组和一个余数的字典
        2) 每当用cur_remainder/denominator 求出当前商后，用cur_remainder%denominator求出当前的余数，看余数是否出现，如果出现，则表明出现了
        循环，根据上次余数出现的位置和当前的位置之间就是循环体
        举例：
        4/333
            pos  : 0 1  2   3
            res  : 0 0  1   2  
        remainder: 4 40 67  4-》注意：这里的4在pos=0时出现过，因此pos=1到当前pos=3就是循环体(012)
        注意：当前remainder到下一步要*10，相当于除法中的补0
        注意一些边界情形：
        1）res[0]一定是整数位，如：80/5 = 16 所有的整数位都在res[0]中保存
        2）需要判断循环节的位置，如果没有循环(余数没有重复)，res[1:]如果不为空，那么res[1:]就是所有的小数部分(否则没有小数部分也就不用
        在整数部分后加".")
        3)如果有循环节，最终结果由整数部分(res[0]),小数部分(从res的下标1到循环开始的位置)，循环部分(循环节开始和终止之间的res)组成
        结果拼接方法为: 整数部分 + "." + 小数部分 + "("+ 循环部分+")"(如果小数部分为空则不加) 
        """
        if numerator ==0 or denominator==0:
            return "0" 
        result = "-" if ((numerator<0) != (denominator<0)) else ""
        numerator, denominator= abs(numerator),abs(denominator)
        res,remainders = [],{}
        cur_remainder = numerator#当前的余数，初始化为除数
        cnt = 0
        rep_from,rep_to = None,None#循环开始和结束的位置
        while cur_remainder:#当前余数为0则直接结束
            cur_res = cur_remainder/denominator#获取除法当前位结果
            cur_remainder = cur_remainder%denominator#获取当前余数
            res.append(str(cur_res))
            if cur_remainder in remainders:#判断余数是否已经存在
                rep_from,rep_to = remainders[cur_remainder]+1,cnt+1#确定循环体
                break
            else:
                remainders[cur_remainder] = cnt#记录当前pos
            cnt+=1
            cur_remainder*=10#下次循环开始之前将余数*10，相当于补0
        #对结果进行拼接
        res_0 = res[0]#整数部分
        if rep_from is None and rep_to is None:#没有循环：如果没有小数：整数部分；有小数：整数部分+"."+小数部分
            result += (res_0+"."+"".join(res[1:]) if res[1:] else res_0)
        #有循环
        else:#整数部分 + "." + 小数部分 + "("+ 循环部分+")"(如果小数部分为空则不加)
            res_1 = "".join(res[1:rep_from])#小数不循环部分
            res_2 = "".join(res[rep_from:rep_to])#小数循环部分
            result = result+res_0+"."+res_1+"("+res_2+")"#
        return result
        
