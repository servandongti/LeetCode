class Solution(object):
    def sol(self, n, dp):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if dp[n] != 0:
            return dp[n]
        dp[n] = self.sol(n - 1, dp) + self.sol(n - 2, dp) + self.sol(n - 3, dp)
        return dp[n]

    def tribonacci(self, n):
        dp = [0] * (n + 1)
        return self.sol(n, dp)
