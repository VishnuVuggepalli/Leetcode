class Solution {
    public int maxFrequency(int[] nums, int k) {
        int maxF =0;
        long curSum =0;

        Arrays.sort(nums);

        for(int left =0, right =0 ; right < nums.length ; ++right){
            curSum += nums[right];
            while(curSum + k < (long)nums[right] * (right - left +1)){
                curSum -= nums[left];
                left++;
            }
            maxF = Math.max(maxF, (right - left +1));
        }
        return maxF;
    }
}