class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int x = 0;
        int M = nums1.length, N = nums2.length;
        if ((M & 1) == 0 && (N & 1) == 0) return x;
        if ((M & 1) == 1 && (N & 1) == 1){
            for(int i = 0; i < M; i++){
                x ^= nums1[i];
            }
    
            for(int i = 0; i < N; i++){
                x ^= nums2[i];
            }

            return x;
        }
        if ( (M & 1) == 0){
            for(int i = 0; i < M; i++){
                x ^= nums1[i];
            }
            return x;
        }
        for(int i = 0; i < N; i++){
            x ^= nums2[i];
        }

        return x;
    }
}