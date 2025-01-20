class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int[] indexMap = new int[arr.length+1];
        for(int i = 0; i < arr.length; i++){
            indexMap[arr[i]] = i;
        }
        int nearest = Integer.MAX_VALUE;
        int R = mat.length;
        int C = mat[0].length;
        for(int row = 0; row < R; row ++){
            int farthestRow = -1;
            for(int col =0 ; col < C; col++){
                farthestRow = Math.max(indexMap[mat[row][col]] , farthestRow);
            }
            nearest = Math.min(nearest, farthestRow);
        }
        for(int col = 0; col < C; col ++){
            int farthestCol = -1;
            for(int row =0 ; row < R; row++){
                farthestCol = Math.max(indexMap[mat[row][col]] , farthestCol);
            }
            nearest = Math.min(nearest, farthestCol);
        }

        return nearest;
    }
}