class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int first = m - 1;
        int second = n - 1;
        int right= m + n - 1;

        while (second >= 0){
 
            if (first >= 0 && nums2[second] < nums1[first]){
               nums1[right] = nums1[first];
               first --;
            }
            else{
                nums1[right] = nums2[second];
                second --;
            }
            //System.out.println(nums1[right]);
            right --;
            
        }
    }
}