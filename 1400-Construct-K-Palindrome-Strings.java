class Solution {
    public boolean canConstruct(String s, int k) {
        if (s.length() < k) return false;
        Map<Character, Integer> alphaFreq = new HashMap<>();
        for(char c : s.toCharArray()){
            alphaFreq.put(c,alphaFreq.getOrDefault(c,0)+1);
        }
        int oddCount = 0;
        for(Map.Entry<Character, Integer> entry : alphaFreq.entrySet()){
            if (entry.getValue() % 2 != 0) oddCount++; 
        }
        return oddCount<=k;
    }
}