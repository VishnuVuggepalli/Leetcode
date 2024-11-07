class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
            Arrays.sort(nums);

            for(int i =0 ;i < nums.length -1; i++){
                if(i > 0 && nums[i] == nums[i-1]){
                    continue;
                }
                int k = nums.length-1;
                int j = i+1;
                while(j < k){
                    //System.out.println(i + \ \ + j);
                    if(nums[j] + nums[k] > (-1 * nums[i]))
                    {
                        k--;
                    }
                    else if(nums[j] + nums[k] < (-1 * nums[i])){
                        j++;
                    }
                    else{
                        res.add(Arrays.asList(nums[i],nums[j],nums[k])); 
                        j++;
                        while(nums[j] == nums[j-1] && j < k){
                            j++;
                        }
                    }
                }
            }
        return res;
    }
}