class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer> numIndex = new HashMap<>();
        for(int left =0 ; left < nums.length; left++){
            if(numIndex.containsKey(nums[left])){
                if(Math.abs(left - numIndex.get(nums[left])) <= k){
                    return true;
                }
            }
            numIndex.put(nums[left], left);
        }
        return false;
        //     int right = left + k;
        //     Set<Integer> setNums = new HashSet<>();
        //     for(int inside = left ; inside <=right ; inside ++){
        //         if(setNums.contains(nums[inside])) return true;
        //         setNums.add(nums[inside]);
        //     }
        // }
        // return false;
        //     for(int right = nums.length-1; right > left ; right --){
        //         if((nums[left] == nums[right]) && (Math.abs(left -right) <= k)) return true;
        //     }
        // }
        // return false;
    }
}