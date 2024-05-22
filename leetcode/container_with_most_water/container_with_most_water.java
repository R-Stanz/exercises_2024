class Solution {
	public int maxArea(int[] height) {
		int maxArea = 0;
		int head = 0;
		int tail = height.length - 1;

		while (head < tail) {
			int minHeight = height[head];
			if (minHeight > height[tail])
				minHeight = height[tail];

			int tmpArea = minHeight * (tail - head);

			if (minHeight == height[head])
				head += 1;
			else
				tail -= 1;
			
			if (maxArea < tmpArea)
				maxArea = tmpArea;
		}
		
		return maxArea;
	}
}
