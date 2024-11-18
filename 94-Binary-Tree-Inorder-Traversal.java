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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inOrder = new ArrayList<>();
        rootRes(root,inOrder);
        return inOrder;
    }

    public static void rootRes(TreeNode root, List<Integer> res){
        if(root == null){
            return;
        }
        rootRes(root.left, res);
        res.add(root.val);
        rootRes(root.right, res);
    } 

}