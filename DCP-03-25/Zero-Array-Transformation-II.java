class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        // Range Update using differene array
        int N = nums.length;
        int[] diffArray = new int[N+1];
        int sum = 0;
        int k = 0;

        for (int i = 0; i< N ;i ++){
            while(sum + diffArray[i] < nums[i]){
                if (k >= queries.length) return -1;
                int start = queries[k][0];
                int end = queries[k][1];
                int val = queries[k][2];

                if(end >= i){
                    diffArray[Math.max(start, i)] += val;
                    if (end + 1 <  diffArray.length){
                        diffArray[end + 1] -= val;
                    }
                }

                k ++;
            }
            sum += diffArray[i];
        }
        return k;
    }
}