class Solution:
    def isPalindrome(self, x: int):
        return str(x) == str(x)[::-1]


result = Solution()
print(result.isPalindrome(12321))
