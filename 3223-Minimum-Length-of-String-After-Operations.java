class Solution {
    public int minimumLength(String s) {
        int[] charCount = new int[26];
        int minLength = 0;
        for(char c : s.toCharArray()){
            charCount[c - 'a'] += 1;
        }

        for(int count : charCount){
            if (count == 0) continue;
            if (count % 2 == 0) minLength += 2;
            else    minLength ++;
            
        }
        return minLength;
        // int N = s.length();
        // for(char c : s.toCharArray()){
        //     charCount.put(c, charCount.getOrDefault(c,0) + 1);
        //     if (charCount.get(c) == 3){
        //         N -= 2;
        //         charCount.replace(c, 1);
        //     }
        // }
        // return N;
    }
}