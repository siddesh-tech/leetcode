class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis = []
        for num in nums1:
            if num in nums2:
                    lis.append(num)
                    nums2.remove(num)
        return lis
