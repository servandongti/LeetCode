class Solution:
    def minSubArrayLen(self, target, nums):
        i = 0
        j = 0
        res = sys.maxsize
        ans = 0
        while j < len(nums):
            if nums[j] == target:
                return 1
            ans += nums[j]
            while i <= j and ans >= target:
                res = min(res, j-i+1)
                ans -= nums[i]
                i += 1
            if ans < target:
                j += 1
            j = max(j, i)
        return res if res != sys.maxsize else 0
