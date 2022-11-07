class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        m = (l+h) >> 1
        while l < h:
            if nums[m] >= nums[0]:
                l = m+1
            else:
                h = m
            m = (l+h) >> 1
        return min(nums[0], nums[l])
