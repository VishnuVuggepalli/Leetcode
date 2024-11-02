class Solution {
    public int countPairs(int[] nums, int k) {
        int i,j;
        int count =0;
        for (i=0; i < nums.length ;i++){
            for (j =i ; j < nums.length;j++){
                if((i < j) && (nums[i] == nums[j]) && ( (i * j) % k ==0)){
                    count ++;
                }
            }
        }
        return count;
    }
}