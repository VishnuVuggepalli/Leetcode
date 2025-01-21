class Solution {
    public long gridGame(int[][] grid) {
        long topSum =0 ;
        int N = grid[0].length;
        for(int i =0; i< N ; i++){
            topSum += grid[0][i];
        }
        long minValue = Long.MAX_VALUE;
        long botSum = 0;
        for(int i = 0 ; i < N;i ++){
            topSum -= grid[0][i];
            minValue = Math.min(minValue, Math.max(topSum, botSum));
            botSum += grid[1][i];
        }
        return minValue;
    }
}