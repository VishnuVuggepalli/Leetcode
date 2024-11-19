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
    private int diameter =0;
    public int diameterOfBinaryTree(TreeNode root) {
        heightCalc(root);
        return diameter;
    }
    public int heightCalc(TreeNode root){
        if(root ==null){
            return 0;
        }
        int left = heightCalc(root.left);
        int right = heightCalc(root.right);

        diameter = Math.max(diameter, left+right);
        //System.out.println(diameter);
        return Math.max(left, right) +1;
    }
}