class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 4 direct top, right, down, left
        self.dX = [0, 0, -1, 1]
        self.dY = [-1, 1, 0, 0]

        #  O(1) visited
        visited = [[False]*len(grid[0]) for i in range(len(grid))]

        # check [x][y] is in matrix ?
        def inMatrix(x, y, m, n):
            if x < 0 or y < 0:
                return False
            if x >= m or y >= n:
                return False
            return True

        def bfs(grid, visited, start):
            queue = [start]
            visited[start[0]][start[1]] = True

            close = True  # flag: is closed islands

            while queue:
                curr = queue.pop()

                # new direct
                for i in range(4):
                    x = curr[0] + self.dX[i]
                    y = curr[1] + self.dY[i]

                    # not in matrix = not closed islands
                    if not inMatrix(x, y, len(grid), len(grid[0])):
                        close = False

                        # add land to queue
                    elif not visited[x][y]:
                        visited[x][y] = True

                        if not grid[x][y]:  # grid[x][y] == 0
                            queue.append([x, y])
            return close

        m = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    visited[i][j] = True

                    if not grid[i][j]:
                        if bfs(grid, visited, [i, j]):
                            m += 1
        return m
