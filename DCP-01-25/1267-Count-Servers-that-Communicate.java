class Solution {
    public int countServers(int[][] grid) {
        int servers = 0;
        int R = grid.length;
        int C = grid[0].length;
        int[] x = new int[R];
        int[] y = new int[C];
        int count = 1;
        for(int i =0; i < R;i ++){
            for(int j =0 ; j < C; j++){
                if(grid[i][j] == 1){
                    x[i]++;
                    y[j]++;
                }
            }
        }
        for(int i =0; i < R;i ++){
            for(int j =0 ; j < C; j++){
                if(grid[i][j] == 1 && (x[i] > 1 || y[j] > 1)){
                    servers++;
                }
            }
        }
        return servers;
    }
}