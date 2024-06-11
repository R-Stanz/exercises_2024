class Solution {
	public int[] relativeSortArray(int[] arr1, int[] arr2) {
		List<Integer> ls = new ArrayList<Integer>();
		for (Integer i : arr1) {
			ls.add(i);
		}

		int[] answer = new int[arr1.length];
		int marker = 0;
		for (Integer i : arr2) {
			int occurences = Collections.frequency(ls, i);
			for (int u = 0; u < occurences; u++) {
				answer[marker] = i;
				marker += 1;
				ls.remove(i);
			}
		}

		Collections.sort(ls);

		for (Integer i : ls) {
			answer[marker] = i;
			marker += 1;
		}

		return answer;
	}
}
