class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    count += self.dfs(grid, row, col)
                    
        return count
                    
    
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return 0
        grid[row][col] = '0'
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)
        return 1
        
        
        