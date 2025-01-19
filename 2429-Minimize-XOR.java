class Solution {
    public int countSetBits(int num){
        int count = 0;
        while(num != 0){
            count += ((num & 1) == 1) ? 1 : 0;
            num = num >>> 1;
        }
        return count ;
    }
    public int minimizeXor(int num1, int num2) {
        int M = countSetBits(num1);
        int N = countSetBits(num2);
        if(M == N) return num1;
        int x  = num1;
        int count = 0;
        while(M != N){
            // Remove least significant - set but and unset bit / remove
            if(M > N && ((1 << count) & x) > 0){ //unset bit
                M -= 1;
                x = x ^ (1 << count); //set bit , remove least significant
            }
            if(N > M && ((1 << count) & x) == 0){
                M += 1;
                x = x | (1 << count);
            }
            count ++;
        }

        return x;
        // if (countSetBits(num1) == y ) return num1;
        // int tempCount = 0;
        // int tempX = num1--;
        // int tempY = num1++ ;
        // while(tempCount != y){
        //     if(tempX > 0 && countSetBits(tempX) == y){
        //         return tempX;
        //     }
        //     else{
        //         tempX --;
        //     }
        //     if(countSetBits(tempY) == y){
        //         return tempY;
        //     }
        //     else{
        //         tempY ++;
        //     }
        // }
        // return 0;
    }
}