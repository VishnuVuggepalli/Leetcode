class Solution {
    public void rotate(int[] nums, int k) {
        // // 1. can k be greater than the array length
        // // 2.  can be done by creating a new array range(0, k) + range(k, k + (arr.length - k))
        k = k % nums.length;
        // int partition1 = (nums.length - k);
        // for(int i = partition1-1 ; i >= 0; i--){
        //     int j = i+1;
        //     while(j < (i+k+1)){
        //         int temp = nums[j];
        //         nums[j] = nums[j-1];
        //         nums[j-1] = temp;
        //         j++;
        //     }
        // }
        reverse(0, nums.length - k -1 , nums);
        reverse(nums.length - k, nums.length - 1, nums);
        reverse(0, nums.length - 1, nums);
    }
    public void reverse(int start, int end, int[] nums){
        while(start < end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start ++;
            end--;
        }
    }
}