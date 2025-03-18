class Solution {
    public boolean divideArray(int[] nums) {
        int[] freqCount = new int[1001];
        int N = nums.length;
        int count = 0;
        for(int num : nums){
            freqCount[num] += 1;
            if(freqCount[num] == 2){
                count ++;
                freqCount[num] = 0;
            }
            
        }

        // Arrays.stream(freqCount).forEach(System.out::println);

        return (count == N / 2) ? true : false; 
    }
}