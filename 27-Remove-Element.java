class Solution {
    public int removeElement(int[] nums, int val) {
        int swap =0;
        for(int fast =0; fast < nums.length; fast ++){
            if(nums[fast] != val){
                nums[swap] = nums[fast];
                swap ++;
            }
        }
        return swap;
    }
}