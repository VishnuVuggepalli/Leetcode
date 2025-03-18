class Solution {
    public int longestNiceSubarray(int[] nums) {
        int left = 0;
        int right =  0;
        int maxLen = 1;
        int N = nums.length;
        int usedBits = 0;
        
        while(right < N){
            while((usedBits & nums[right]) != 0){
                usedBits ^= nums[left];
                left ++;
            }
            usedBits |= nums[right];
            maxLen = Math.max(maxLen, (right -left + 1));
            right ++;
        }

        return maxLen;
    }
}