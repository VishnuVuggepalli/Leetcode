class Solution {
    public int[] minOperations(String boxes) {
        //char[] box = boxes.toCharArray();
        int N = boxes.length();
        int[] distances = new int[N];

        int balls = 0;
        int moves = 0;
        for(int index =0 ; index<N; index ++){
            distances[index] = balls + moves;
            moves += balls;
            if (boxes.charAt(index) == '1'){
                balls ++;
            }
        }

        balls =0;
        moves =0;
        for(int index = N-1; index >=0; index --){
            distances[index] += balls + moves;
            moves += balls;
            if (boxes.charAt(index) == '1'){
                balls ++;
            } 
        }

        return distances;
    }
}