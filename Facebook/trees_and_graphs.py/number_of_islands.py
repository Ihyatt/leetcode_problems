# Number of Islands

"""
Input:
11000
11000
00100
00011

Output: 3


00000
00000
00100
00011

islands = 1

00000
00000
00000
00011

islands = 2

00000
00000
00000
00000

islands = 3
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.dfs(grid, i, j)
                    
        return num_islands
    
    def dfs(self, grid, r, c):
        grid[r][c] = "0"
        if c + 1 <= len(grid[0]) - 1 and grid[r][c + 1] == "1": #traverse right
            self.dfs(grid, r, c + 1)
        if r + 1 <= len(grid) - 1 and grid[r + 1][c] == "1": #traverse up
            self.dfs(grid, r + 1, c)
        if c - 1 >= 0 and grid[r][c - 1] == "1": #traverse left
            self.dfs(grid, r, c - 1)
        if r - 1 >= 0 and grid[r - 1][c] == "1": #traverse right
            self.dfs(grid, r - 1, c)
