class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum =0;
        for(int itr =0 ; itr< nums.length ; itr = itr+2){
            sum += nums[itr];
        }
        return sum;
    }
}