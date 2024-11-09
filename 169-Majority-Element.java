class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int maxCount = 1;
        int maxNum = nums[0];
        for(int num =1; num < nums.length; num++){
            if(nums[num] == maxNum){
                maxCount++;
            }
            else{
                maxCount--;
            }

            if(maxCount == 0){
                maxNum = nums[num];
                maxCount = 1;
            }
        }
        return maxNum;
    }
}