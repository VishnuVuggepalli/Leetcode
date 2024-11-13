class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[nums.length * 2];
        int end = nums.length * 2;
        int start =0;
        while(start < end){
            for(int i  =0 ; i < nums.length; i++){
                ans[start] = nums[i];
                start++;
            }
        }
        return ans;
    }
}