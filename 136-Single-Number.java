class Solution {
    public int singleNumber(int[] nums) {
        int res =0;
        for (int found =0 ; found < nums.length; found ++){
            res ^= nums[found];
        }
        return res;
    }
}