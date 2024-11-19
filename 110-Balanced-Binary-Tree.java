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
    private boolean check = true;
    public boolean isBalanced(TreeNode root) {
        heightCheck(root);
        return check;
    }
    public int heightCheck(TreeNode root){
        if(root == null) return 0;
        int left = heightCheck(root.left);
        int right = heightCheck(root.right);

        if(left > right && left - right > 1) check = false;
        else if(left < right && right -left > 1) check = false;
        
        return Math.max(left, right) +1;
    }
}