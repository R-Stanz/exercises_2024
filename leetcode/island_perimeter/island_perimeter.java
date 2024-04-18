class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        int row_max_limit = grid.length - 1;
        for (int row = 0; row <= row_max_limit; row++) {
            int col_max_limit = grid[0].length - 1;
            for (int col = 0; col <= col_max_limit; col++) {
                int point = grid[row][col];
                if (point == 1) {

                    if (row == 0)
                        perimeter += 1;
                    if (row == row_max_limit)
                        perimeter += 1;
                    if (col == 0)
                        perimeter += 1;
                    if (col == col_max_limit)
                        perimeter += 1;

                    if ((row - 1 >= 0) && (grid[row - 1][col] == 0))
                        perimeter += 1;
                    if ((row + 1 <= row_max_limit) && (grid[row + 1][col] == 0))
                        perimeter += 1;
                    if ((col - 1 >= 0) && (grid[row][col - 1] == 0))
                        perimeter += 1;
                    if ((col + 1 <= col_max_limit) && (grid[row][col + 1] == 0))
                        perimeter += 1;
		}
	    }
	}

        return perimeter;
    }
}
