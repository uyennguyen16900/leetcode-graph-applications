class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        fresh_oranges = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        minutes = 0
        while len(queue) > 0:
            k = len(queue)
            while k > 0:
                x, y = queue.pop(0)

                right = (x, y+1)
                left = (x, y-1)
                down = (x+1, y)
                up = (x-1, y)
                if self.isValid(right, grid):
                    queue.append(right)
                    grid[right[0]][right[1]] = 2
                    fresh_oranges -= 1
                    

                if self.isValid(left, grid):
                    queue.append(left)
                    grid[left[0]][left[1]] = 2
                    fresh_oranges -= 1
                    

                if self.isValid(down, grid):
                    queue.append(down)
                    grid[down[0]][down[1]] = 2
                    fresh_oranges -= 1
                    

                if self.isValid(up, grid):
                    queue.append(up)
                    grid[up[0]][up[1]] = 2
                    fresh_oranges -= 1
                    
                
                k -= 1
            if len(queue) > 0:
                minutes += 1
        
        if fresh_oranges == 0:
            return minutes
        else:
            return -1
            
    def isValid(self, coordinate, grid):
        x, y = coordinate
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1:
            return True
        else:
            return False
    