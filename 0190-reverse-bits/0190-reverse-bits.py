class Solution:
    def reverseBits(self, n: int) -> int:
        n = f"{n:032b}"
        b = n[::-1]
        return int(b,2)