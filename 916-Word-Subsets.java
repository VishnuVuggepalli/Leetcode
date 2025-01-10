class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] freq = new int[26];
        for(String s: words2){
            int[] count = new int[26];
            for(char ch: s.toCharArray()){
                count[ch - 'a'] += 1;
                freq[ch - 'a'] = Math.max(freq[ch - 'a'], count[ch-'a']);
            }
        }

        List<String> res = new ArrayList<>();
        for(String word : words1){
            int i = 0;
            int[] count  = new int[26];
            for(char c : word.toCharArray()){
                count[c - 'a']++;
            }
            for (i = 0 ; i < 26 ;i++){
                if (freq[i] > count[i]){
                    break;
                }
            }
            if (i == 26) {
                res.add(word);
            }
        }
        return res;
    }
}