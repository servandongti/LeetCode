class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i == rows or j == cols:
                return float('inf')
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0

            top = dfs(i - 1, j)
            bot = dfs(i + 1, j)
            right = dfs(i, j + 1)
            left = dfs(i, j - 1)

            return top + bot + right + left + 1

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    result = dfs(i, j)
                    if result != float('inf'):
                        count += result
        return count
