class Solution {

	public HashSet<List<Integer>> getEarthCoordSet(char[][] grid){
		HashSet<List<Integer>> earthCoordSet = new HashSet();

		for (Integer line = 0; line < grid.length; line++) {
			for (Integer col = 0; col < grid[0].length; col++) {
				if (grid[line][col] == '1') {
					List<Integer> earthCoord = List.of(line, col);
					earthCoordSet.add(earthCoord);
				}
			}
		}
		return earthCoordSet;
	}
	public int numIslands(char[][] grid) {
		Integer last_line = grid.length - 1;
		Integer last_col = grid[0].length - 1;
		HashSet<List<Integer>> earthCoordSet = this.getEarthCoordSet(grid);

		int islands = 0;
		while (! earthCoordSet.isEmpty()) {

			++islands;

			List<Integer> newIslandCoord = List.of();
			//System.out.println(earthCoordSet);
			for (var coord : earthCoordSet) {
				//System.out.println(coord);
				newIslandCoord = coord;
				earthCoordSet.remove(coord);
				break;
			}

			if (earthCoordSet.isEmpty())
				return islands;

			LinkedList<List<Integer>> newIslandCoords = new LinkedList();
			newIslandCoords.add(newIslandCoord);

			while (! newIslandCoords.isEmpty()) {
				
				List<Integer> coord = newIslandCoords.poll();
				Integer line = coord.get(0);
				Integer col = coord.get(1);

				List<Integer> upperCoord = List.of(line + 1, col);
				if((line + 1 <= last_line) && (earthCoordSet.contains(upperCoord))) {
					System.out.println(coord);
					newIslandCoords.add(upperCoord);
					earthCoordSet.remove(upperCoord);
				}

				List<Integer> bottomCoord = List.of(line - 1, col);
				if((line - 1 >= 0) && (earthCoordSet.contains(bottomCoord))) {
					System.out.println(coord);
					newIslandCoords.add(bottomCoord);
					earthCoordSet.remove(bottomCoord);
				}

				List<Integer> leftCoord = List.of(line, col - 1);
				if((col - 1 >= 0) && (earthCoordSet.contains(leftCoord))) {
					System.out.println(coord);
					newIslandCoords.add(leftCoord);
					earthCoordSet.remove(leftCoord);
				}

				List<Integer> rightCoord = List.of(line, col + 1);
				if((col + 1 <= last_col) && (earthCoordSet.contains(rightCoord))) {
					System.out.println(coord);
					newIslandCoords.add(rightCoord);
					earthCoordSet.remove(rightCoord);
				}
			}
		}
		return islands;
	}
}
