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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> levels = new ArrayList<>();
        if(root == null)    return levels;
        Queue<TreeNode> nodeLevel = new LinkedList<>();

        nodeLevel.offer(root);
        while(!nodeLevel.isEmpty()){
            int N = nodeLevel.size();
            List<Integer> level = new ArrayList<>();
            for(int i = 0; i < N; i++){
                TreeNode dummy = nodeLevel.poll();
                if(dummy.left != null){
                    nodeLevel.offer(dummy.left);
                }
                if(dummy.right != null){
                    nodeLevel.offer(dummy.right);
                }
                level.add(dummy.val);
            }
            levels.add(level);
        }
        return levels;
    }
}