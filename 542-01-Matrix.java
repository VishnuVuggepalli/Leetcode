class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int R = mat.length;
        int C = mat[0].length;
        Queue<int[]> indexes = new LinkedList<>();
        for(int i =0; i < R; i++){
            for(int j =0 ; j < C; j++){
                if(mat[i][j] == 0)  indexes.offer(new int[]{i,j});
                else mat[i][j] = Integer.MAX_VALUE;
            }
        }

        int [][] direction = {{0,1},{1,0},{0,-1},{-1,0}};
        while(!indexes.isEmpty()){
            int[] cur = indexes.poll();
            int x = cur[0];
            int y = cur[1];
            for(int[] dir: direction){
                int nx = x + dir[0];
                int ny = y + dir[1];
                if(nx >= 0 && ny >= 0 && nx < R && ny < C && mat[nx][ny] > mat[x][y] + 1){
                    mat[nx][ny] = mat[x][y] + 1;
                    indexes.offer(new int[]{nx,ny});
                }
            }              
        }
        return mat;
    }
}