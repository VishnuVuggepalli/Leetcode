import static java.lang.Math.abs;
class Solution {
    public int[] sortedSquares(int[] nums) {
        int left =0;
        int right = nums.length -1;
        int size = nums.length;
        int[] res = new int[size];
        Arrays.fill(res,0);

        while(left <= right){
            //System.out.println(res[size]);
            if(Math.abs(nums[left]) >= Math.abs(nums[right])){
                size --;
                res[size] = nums[left] * nums[left];
                left ++;
            }
            else if(Math.abs(nums[left]) < Math.abs(nums[right])){
                size --;
                res[size] = nums[right] * nums[right];
                right --;
            }
        }
        return res;
    }
}