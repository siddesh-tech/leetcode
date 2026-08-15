class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=''
        for ch in s:
            if ch.isalnum():
                ss += ch.lower()
        return ss == ss[::-1]