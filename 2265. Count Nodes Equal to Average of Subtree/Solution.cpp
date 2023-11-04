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
    int matchingSubtreeCount = 0;

    pair<int, int> calculateSubtreeValues(TreeNode* node){
        if(node == nullptr)
            return{0, 0};
        auto leftSubtree = calculateSubtreeValues(node->left);
        auto rightSubtree = calculateSubtreeValues(node->right);

        int sumOfValues = leftSubtree.first + rightSubtree.first + node->val;
        int numberOfNodes = leftSubtree.second + rightSubtree.second + 1;

        if((sumOfValues / numberOfNodes) == node->val)
            matchingSubtreeCount++;
        
        return{sumOfValues, numberOfNodes};
    }
    int averageOfSubtree(TreeNode* root) {
        calculateSubtreeValues(root);
        return matchingSubtreeCount;
    }
};