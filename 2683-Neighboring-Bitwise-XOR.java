class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int N = derived.length;
        int XORSum = 0;
        for(int i =0; i < N ; i++){
            XORSum ^= derived[i];
        }
        return XORSum == 0;
    }
}