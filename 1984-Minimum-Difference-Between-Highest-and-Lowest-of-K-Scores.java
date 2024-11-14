class Solution {
    public int minimumDifference(int[] nums, int k) {
        int min = Integer.MAX_VALUE;
        Arrays.sort(nums);
        int counter =0;
        while(counter < nums.length -k + 1){
            if(nums[counter + k -1] - nums[counter] < min){
                min = nums[counter + k -1] - nums[counter];
            }
            counter++;
        }
        return min ;
    }
}