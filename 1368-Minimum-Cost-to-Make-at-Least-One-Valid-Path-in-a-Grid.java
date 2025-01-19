class Solution {
    public int minCost(int[][] grid) {
        int M = grid.length;
        int N = grid[0].length;
        int[][] minCost = new int[M][N];
        for(int i = 0; i< M; i++){
            Arrays.fill(minCost[i], Integer.MAX_VALUE);
        }

        Deque<int[]> Q = new ArrayDeque<>();
        Q.offerFirst(new int[]{0,0});
        minCost[0][0] = 0;

        int[][] direction = {{0,1},{0,-1},{1,0},{-1,0}};
        while(!Q.isEmpty()){
            int[] arr = Q.pollFirst();
            int r = arr[0];
            int c = arr[1];

            for(int i = 0; i < 4; i++){
                int nr = r + direction[i][0];
                int nc = c + direction[i][1];
                int cost = (grid[r][c] != (i+1)) ? 1 : 0;

                if(nr >= 0 && nr< M && nc < N && nc >= 0 && minCost[r][c] + cost < minCost[nr][nc]){
                    minCost[nr][nc] = minCost[r][c] + cost;

                    if(cost == 1){
                        Q.offerLast(new int[]{nr,nc});
                    }
                    else{
                        Q.offerFirst(new int[]{nr,nc});
                    }
                }
            }
        }
        return minCost[M-1][N-1];
    }
}