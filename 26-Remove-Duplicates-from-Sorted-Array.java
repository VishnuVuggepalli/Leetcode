import java.util.*;
class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        int j = 0;
        int count =0;
        Set<Integer> numsSet = new HashSet<>();
        
        while(i<nums.length){
            if(!numsSet.contains(nums[i])){
                numsSet.add(nums[i]);
                nums[j] = nums[i];
                j ++;
                count ++;
            }
            i++;
        }
        return count;
    }
}