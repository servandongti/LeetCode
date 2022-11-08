class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def valid(guess):
            """Returns True if we can achieve guess as the 
            largest number after performing maxOperations"""
            count = 0
            for num in nums:
                if num > guess:
                    count += math.ceil(num / guess) - 1
                    if count > maxOperations:
                        return False
            return True

        high = max(nums)
        best = high
        low = 1
        while low <= high:
            g = (low + high) // 2
            if valid(g):
                best = min(best, g)
                high = g - 1
            else:
                low = g + 1

        return best
