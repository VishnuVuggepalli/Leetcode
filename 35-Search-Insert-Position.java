class Solution {
    public int searchInsert(int[] nums, int val) {
        int low = 0 ;
        int high = nums.length -1 ;
        int mid  =0;
        if (val < nums[low]){
            return low;
        }
        else if(val > nums[high]){
            //System.out.println(high);
            return high+1;
        }
        while(low <= high){
            mid = low + (high-low)/2;
            //System.out.println(low + \ \ + high + \\ + mid);
            if (val == nums[mid]){
                return mid;
            }
            else if(val < nums[mid]){
                high = mid-1;
            }
            else if(val > nums[mid]){
                low = mid+1;
            }
        }
        return low;
    }
}