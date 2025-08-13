"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])


        def dfs(grid, r, c):
            # out of bounds
            if (r < 0 or r >= m or c < 0 or c >= n):
                return 
            # water / already visited
            if (grid[r][c] == "0" or grid[r][c] == "v"):
                return
            
            # mark as visited
            grid[r][c] = "v"

            # top
            dfs(grid, r-1, c)
            #right
            dfs(grid, r, c+1)
            #down
            dfs(grid, r+1, c)
            #left
            dfs(grid, r, c-1)


        count = 0

        for row in range(0, m):
            for col in range(0, n):
                if grid[row][col] == "1":
                    count += 1
                    # visit the entire island
                    dfs(grid, row, col)

        return count
