class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int pairs = 0;
        int N = words.length;
        for(int i =0; i < N-1 ;i ++){
            for(int j = i+1 ; j < N ; j++){
                if((words[i].length() <= words[j].length()) && isPrefixandSuffix(words[i],words[j])){
                    pairs ++;
                }
            }
        }
        return pairs;
    }
    public boolean isPrefixandSuffix(String word1, String word2){
        return word2.startsWith(word1) && word2.endsWith(word1);
    }
}