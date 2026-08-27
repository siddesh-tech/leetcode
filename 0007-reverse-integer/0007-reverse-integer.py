class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign = -1
        else:
            sign = 1
        temp = x 
        x = abs(x)
        res = 0 
        while x >0 :
            digit = x % 10 
            x //=10
            if res>214748364 or (res == 214748364 and digit > 7):
                return 0
            res = res* 10 +digit
            
        return res*sign