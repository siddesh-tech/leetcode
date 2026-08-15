class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber >0:
            columnNumber -=1
            reminder = columnNumber % 26
            result += chr(reminder+65)
            columnNumber //= 26
        return result[::-1]
          
            