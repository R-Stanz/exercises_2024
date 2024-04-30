/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
	private String searchWholeTree(TreeNode currentNode, String smallestStr, String currentStr) {
		if (currentStr.length() == 0)
			currentStr += (char) ((int) 'a' + currentNode.val);

		if (currentNode.left != null) {
			String leftNodeStr = ((char) ((int) 'a' + currentNode.left.val)) + currentStr;
			smallestStr = this.searchWholeTree(currentNode.left, smallestStr, leftNodeStr);
		}
		if (currentNode.right != null) {
			String rightNodeStr = ((char) ((int) 'a' + currentNode.right.val)) + currentStr;
			smallestStr = this.searchWholeTree(currentNode.right, smallestStr, rightNodeStr);
		}
		else if ((currentNode.left == null) && (currentNode.right == null)) {
			if ((smallestStr.compareTo(currentStr) > 0) || (smallestStr.length() == 0))
				return currentStr;
		}
		return smallestStr;
	}
	public String smallestFromLeaf(TreeNode root) {
		return this.searchWholeTree(root, "", "");
	}
}
