class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis = []
        for num in nums1:
            for nu in nums2:
                if(num == nu):
                    lis.append(num)
                    nums2.remove(num)
        return list(set(lis))