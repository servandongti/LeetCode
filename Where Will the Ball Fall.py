class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])

        # [1] function that simulates m steps
        def move_ball(j):
            for i in range(m):
                k = j + grid[i][j]
                if not (0 <= k < n) or (grid[i][k] != grid[i][j]):
                    return -1
                j = k
            return j

        # [2] move n balls from the top to the bottom
        return [move_ball(j) for j in range(n)]
