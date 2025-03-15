class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        int cur = nums[0];
        int prev = 0;
        for (int i = 1; i < N; i++){
            int pick = prev + nums[i];
            int notPick = cur;
            prev = cur;
            cur = Math.max(pick, notPick);
        }
        return cur;
    }
}