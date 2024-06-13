class Solution {
	public List<String> generateParenthesis(int n) {
		List<String> ls = new ArrayList<String>();
		GenerateSequences(ls, n, 0, 0, "");
		return ls;
	}

	private void GenerateSequences(List<String> ls, int maxCount, int countOpen, int countClose, String sequence) {
		if (maxCount > countOpen) {
			GenerateSequences(ls, maxCount, countOpen + 1, countClose, sequence + "(");
		}
		if (countClose < countOpen) {
			GenerateSequences(ls, maxCount, countOpen, countClose + 1, sequence + ")");
		}
		if (countClose == maxCount) {
			ls.add(sequence);
		}
	}
}
