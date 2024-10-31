class Solution {
    public int countKDifference(int[] nums, int k) {
        var n = nums.length;
        var count = new HashMap<Integer,Integer>();
        var res = 0;
        for (int i =0 ;i< n; i++){
            if(count.containsKey(nums[i] -k)){
                res += count.get(nums[i] -k);
            }
            if(count.containsKey(nums[i]+ k)){
                res += count.get(nums[i]+ k);
            }
            count.put(nums[i],count.getOrDefault(nums[i],0) + 1);
            //System.out.println(count);
        }
        return res;
    }
}