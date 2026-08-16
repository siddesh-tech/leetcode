class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        count =0
        for ch in n :
            if(ch=='1'):
                count += 1
        return count