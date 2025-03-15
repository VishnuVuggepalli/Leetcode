class Solution {
    public int minCapability(int[] nums, int k) {
        int low = 1, high = (int)1e9;
        while(low < high){
            int mid = (low + high) / 2;
            int count  = 0;
            for (int i =0; i < nums.length; i++){
                if(nums[i] <= mid){
                    count ++;
                    i ++;
                }
            }
            if (count >= k){
                high = mid;
            }
            else{
                low = mid + 1;
            }
        }
        return low;
    }
}