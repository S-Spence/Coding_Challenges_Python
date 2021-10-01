"""Leetcode problem: https://leetcode.com/problems/number-of-islands/submissions/"""



class Solution:
    
    def search(self, grid: List[List[str]], row: int, col: int):
        """Implement recursive dfs search algorithm"""
        grid[row][col] = "0"
        
        # Surrounding land to check
        surrounding = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
        
        for r, c in surrounding:
            # Check that search is within bounds
            if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r]):
                # If there is another piece of land, call search again
                if grid[r][c] == "1":
                    self.search(grid, r, c)
            
            
    def numIslands(self, grid: List[List[str]]) -> int:
        """Count the number of islands represented by 1s surrounded on adjacent sides by 0"""
        islands = 0 # count islands
        
        # Iterate through rows and columns
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    self.search(grid, r, c)
                    islands += 1
        return islands
        