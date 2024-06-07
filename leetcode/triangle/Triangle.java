class Solution {
	public int minimumTotal(List<List<Integer>> triangle) {

		for (int lvl = triangle.size() - 1; lvl > 0; lvl--) {
			for (int marker = 0; marker < triangle.get(lvl-1).size(); marker++) {

				Integer min_val = triangle.get(lvl).get(marker);
				if (min_val > triangle.get(lvl).get(marker+1))
					min_val = triangle.get(lvl).get(marker+1);

				Integer newValue = triangle.get(lvl-1).get(marker) + min_val;
				triangle.get(lvl-1).set(marker, newValue);
			}
		}

		return triangle.get(0).get(0);
	}
}
