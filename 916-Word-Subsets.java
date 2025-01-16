class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        List<String> subSets = new ArrayList<>();
        int[] maxFreqs = new int[26];
        for(String word : words2){
            int[] freqs = new int[26];
            for(char c: word.toCharArray()){
                if(freqs[c - 'a'] != 0) freqs[c - 'a'] += 1;
                else  freqs[c - 'a'] = 1;
                maxFreqs[c - 'a'] = Math.max(maxFreqs[c - 'a'], freqs[c - 'a']);
            }
        }
        //System.out.println(Arrays.toString(maxFreqs));
        
        for(String word : words1){
            int[] freqs = new int[26];
            for(char c : word.toCharArray()){
                if(freqs[c - 'a'] != 0) freqs[c - 'a'] += 1;
                else  freqs[c - 'a'] = 1;
            }
            boolean flag = true;
            for(int i = 0; i < maxFreqs.length; i ++){
                if (maxFreqs[i] > 0 && freqs[i] < maxFreqs[i])
                {
                    flag = false;
                    break;
                }
            }
            if(flag)    subSets.add(word);
        }
        return subSets;
    }
}