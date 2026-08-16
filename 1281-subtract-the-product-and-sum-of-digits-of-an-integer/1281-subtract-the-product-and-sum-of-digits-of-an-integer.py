class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = 0
        product = 1
        while n>0:
            res += n % 10
            product *= n%10
            n //=10
        return product - res