class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp = num 
        res = 0 
        while num >0 :
            digit = num % 10 
            res = res* 10 +digit
            num //=10
        num = res
        res = 0
        while num >0 :
            digit = num % 10 
            res = res* 10 +digit
            num //=10
        return temp == res



         
                
