class Solution {
    public int maximumCandies(int[] candies, long k) {
        int N = candies.length;
        int maxCandies = 0;
        int upperBound = 0;
        for (int c: candies){
            upperBound = Math.max(upperBound, c);
        }
        int lowerBound  = 1;
        while(lowerBound <= upperBound){
            int mid = lowerBound + (upperBound - lowerBound)/ 2;
            long sum = 0;
            for(int i = 0; i < N; i++){
                sum += candies[i] / mid;
                if (sum >= k)   break;
            }
            // System.out.println(lowerBound + " " +  upperBound + " " + sum);
            if (sum >= k){
                maxCandies = mid;
                lowerBound = mid + 1;
            }
            else{
                upperBound = mid- 1; 
            }
        }
        return maxCandies;
    }
}