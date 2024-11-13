class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> setNums = new HashSet<>();

        for(int n: nums){
            if(setNums.contains(n)){
                return true;
            }
            setNums.add(n);
        }
        return false;
    }
}