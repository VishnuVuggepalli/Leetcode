class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int R =  isWater.length;
        int C = isWater[0].length;
        int [][] peakMatrix = new int[R][C];

        Queue<int[]> waterXY = new LinkedList<>();

        for(int i =0 ; i < R; i ++){
            for(int j =0; j < C; j++){
                if(isWater[i][j] == 1)  waterXY.offer(new int[]{i,j});
                else    peakMatrix[i][j] = -1;
            }
        }

        int[][] direction = {{1,0},{0,1},{-1,0},{0,-1}};
        while(!waterXY.isEmpty()){
            int[] cur = waterXY.poll();
            for(int i[]: direction){
                int nx = cur[0] + i[0];
                int ny = cur[1] + i[1];

                if(nx >= 0 && ny >= 0 && nx < R && ny < C && peakMatrix[nx][ny] == -1){
                    peakMatrix[nx][ny] = peakMatrix[cur[0]][cur[1]] + 1;
                    waterXY.offer(new int[]{nx,ny});
                }
            }
        }
        return peakMatrix;
    }
}