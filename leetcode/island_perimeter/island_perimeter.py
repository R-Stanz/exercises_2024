class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row_max_limit = len(grid) - 1
        for row in range(row_max_limit + 1):
            col_max_limit = len(grid[0]) - 1
            for col in range(col_max_limit + 1):
                point = grid[row][col]
                if (point == 1):

                    if (row == 0):
                        perimeter += 1
                    if (row == row_max_limit):
                        perimeter += 1
                    if (col == 0): 
                        perimeter += 1
                    if (col == col_max_limit):
                        perimeter += 1

                    if ((row - 1 >= 0) and (grid[row - 1][col] == 0)):
                        perimeter += 1
                    if ((row + 1 <= row_max_limit) and (grid[row + 1][col] == 0)):
                        perimeter += 1
                    if ((col - 1 >= 0) and (grid[row][col - 1] == 0)):
                        perimeter += 1
                    if ((col + 1 <= col_max_limit) and (grid[row][col + 1] == 0)):
                        perimeter += 1

        return perimeter
