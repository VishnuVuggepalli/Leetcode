class Solution {
    public List<String> stringMatching(String[] words) {
        ArrayList<String> matchingSubStrings = new ArrayList<String>();
        int N = words.length;
        for(int left  = 0; left < N; left ++){
            for(int right = 0; right < N; right ++){
                if (left != right && words[right].contains(words[left])){
                    matchingSubStrings.add(words[left]);
                    break;
                }
            }
        }
        return matchingSubStrings;
    }
}