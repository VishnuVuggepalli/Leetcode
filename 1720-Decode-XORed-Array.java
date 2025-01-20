class Solution {
    public int[] decode(int[] encoded, int first) {
        int N = encoded.length;
        int[] res = new int[N+1];
        res[0]= first;
        for(int i = 1; i < res.length; i ++){
            res[i] = encoded[i-1] ^ res[i-1];
        }
        return res;
    }
}