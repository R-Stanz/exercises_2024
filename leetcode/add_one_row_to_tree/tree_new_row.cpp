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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
	    if (depth == 1) {
		    return new TreeNode(val, root->left, NULL);
	    }

	    else if (depth == 2) {
		    root->left = new TreeNode(val, root->left, NULL);
		    root->right = new TreeNode(val, NULL, root->right);
		    return root;
	    }

	    else {
		    if (root->left != NULL)
			    root->left = this->addOneRow(root->left, val, depth-1);
		    if (root-> right != NULL)
			    root->right = this->addOneRow(root->right, val, depth-1);
		    return root;
	    }
    }
};
