class Solution {
    public int flip(int num){
        return (num == 0) ? 1 : 0;
    }
    public int minOperations(int[] nums) {
        int flips = 0;
        int i = 0;
        while(i < nums.length -2){
            if(nums[i] == 0){
                nums[i] = flip(nums[i]);
                nums[i+1] = flip(nums[i+1]);
                nums[i+2] = flip(nums[i+2]);
                flips ++;
            }
            i ++;
        }
        return (nums[i] == 0 || nums[i+1] == 0) ? -1 : flips;
    }
}