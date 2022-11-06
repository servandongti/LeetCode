class Solution(object):
    def isMonotonic(self, nums):
        n = len(nums)
        p = 0
        g = 0
        for i in range(n-1):
            if(p == 0):  # checking for if it is in ascending or descending order
                if nums[i] == nums[i+1]:
                    continue
                elif nums[i] < nums[i+1]:
                    g = 1
                    p = 1
                else:
                    g = 0
                    p = 1
            else:
                if nums[i] < nums[i+1] and g == 0:
                    return False
                if nums[i] > nums[i+1] and g == 1:
                    return False
        return True
