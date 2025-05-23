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
    public TreeNode invertTree(TreeNode root) {
        invertHelper(root);
        return root;
    }

    public void invertHelper(TreeNode root){
        if(root != null){
            TreeNode helper = root.right;
            root.right = root.left;
            root.left = helper;
            invertHelper(root.left);
            invertHelper(root.right);
        }
    }
}