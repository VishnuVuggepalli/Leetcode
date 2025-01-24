class Solution {
    public void filled(int[][] image, int sr, int sc, int color, int cur){
        if(sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length)    return;
        if(image[sr][sc] != cur) return;

        image[sr][sc] = color;
        filled(image, sr+1, sc, color, cur);
        filled(image, sr, sc+1, color, cur);
        filled(image, sr, sc-1, color, cur);
        filled(image, sr-1, sc, color, cur);
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {

        if(image[sr][sc] == color) return image;
        filled(image,sr,sc,color,image[sr][sc]);
        return image;
        // int R = image.length;
        // int C = image[0].length;
        // Queue<int[]> indexesQ = new LinkedList<>();
        // indexesQ.offer(new int[]{sr,sc,image[sr][sc]});

        // int[][] filled = image.clone();

        // int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
        // boolean[][] visited = new boolean[R][C];
        // while(!indexesQ.isEmpty()){
        //     int[] cur = indexesQ.poll();
        //     for(int[] dir:directions){
        //         int nx = cur[0] + dir[0];
        //         int ny = cur[1] + dir[1];
        //         int val = cur[2];

        //         if(nx < 0 || ny < 0 || nx >= R || ny>= C || visited[nx][ny])    continue;
                
        //         filled[cur[0]][cur[1]] = color;
        //         visited[cur[0]][cur[1]] = false;
        //         if(image[nx][ny] == val)    indexesQ.offer(new int[]{nx,ny,image[nx][ny]});
        //     }
        // }
        // return filled;
    }
}