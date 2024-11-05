class Solution {
    public int missingNumber(int[] nums) {
        int intendedSum =0;
        int sum =0;
        int n = nums.length;
        intendedSum = (n*(n+1))/2;
        for(int itr = 0 ;itr< nums.length; itr++){
            sum += nums[itr];
        }
        //System.out.println(intendedSum + \ \ + sum);
        return intendedSum - sum;
    }
}