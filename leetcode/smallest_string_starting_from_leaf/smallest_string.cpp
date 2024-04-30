/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
	string search_whole_tree(TreeNode* current_node, string smallest_str = "", string current_str = "") {
		if (current_str == "")
			current_str += char((int) 'a' + current_node->val);

		TreeNode* current_left_node = current_node->left;
		TreeNode* current_right_node = current_node->right;

		if (current_left_node != NULL) {
			string left_node_str = char((int) 'a' + current_left_node->val) + current_str;
			smallest_str = this->search_whole_tree(current_left_node, smallest_str, left_node_str);
		}
		if (current_right_node != NULL) {
			string right_node_str = char((int) 'a' + current_right_node->val) + current_str;
			smallest_str = this->search_whole_tree(current_right_node, smallest_str, right_node_str);
		}
		if ((current_left_node == NULL) and (current_right_node == NULL)) {
			if ((current_str < smallest_str) or (smallest_str == ""))
				return current_str;
		}
		return smallest_str;
	}
	string smallestFromLeaf(TreeNode* root) {
		return this->search_whole_tree(root);
	}
};
