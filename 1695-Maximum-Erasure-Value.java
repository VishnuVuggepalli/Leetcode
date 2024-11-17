class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int sum=0;
        int left =0;
        Set<Integer> unqNum = new HashSet<>();
        int ans =0;
        for(int right =0 ; right < nums.length; right++){
            while(unqNum.contains(nums[right])){
                sum -= nums[left];
                unqNum.remove(nums[left]);
                left++;
            }
            unqNum.add(nums[right]);
            sum += nums[right];
            ans = Math.max(ans,sum);
        }
        return ans;
    }
}