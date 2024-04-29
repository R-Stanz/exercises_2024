class Solution:
    def list_to_set(self, grid):
        set_grid = set({})
        for i in range(len(grid)):
            for u in range(len(grid[i])):
                if (grid[i][u] == "1"):
                    set_grid.add((i,u))

        return set_grid

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        last_line = len(grid) - 1 
        last_col = len(grid[0]) - 1
        grid = self.list_to_set(grid)

        while(not (not grid)):
            new_island_point = grid.pop()
            islands += 1

            if (not grid):
                return islands

            new_island_points = [new_island_point]
            while (not (not new_island_points)):
                line, col = new_island_points.pop()

                if ((line + 1 <= last_line) and ((line + 1, col) in grid)):
                    new_island_points += [(line+1, col)]
                    grid.remove((line+1,col))

                if ((line - 1 >= 0) and ((line - 1, col) in grid)):
                    new_island_points += [(line-1, col)]
                    grid.remove((line-1,col))

                if ((col - 1 >= 0) and ((line, col - 1) in grid)):
                    new_island_points += [(line, col-1)]
                    grid.remove((line,col-1))

                if ((col + 1 <= last_col) and ((line, col + 1) in grid)):
                    new_island_points += [(line, col + 1)]
                    grid.remove((line,col+1))

        return islands
