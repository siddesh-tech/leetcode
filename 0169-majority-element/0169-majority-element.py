class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candit = None
        count = 0
        for num in nums:
            if count == 0:
                candit = num
            if candit == num :
                count += 1
            else:
                count -=1 
        return candit
        