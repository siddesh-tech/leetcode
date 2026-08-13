class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            if(s[i] ==' '):
                continue
            else:
                count +=1
                if i==0 or s[i-1]==' ':
                    break
        return count
            

