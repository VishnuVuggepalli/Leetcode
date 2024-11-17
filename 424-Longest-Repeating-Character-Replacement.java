class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> comb = new HashMap<>();
        int left =0;
        int longest =0;
        int maxF =0;
        for(int right =0; right < s.length() ; right ++){
            comb.put(s.charAt(right), comb.getOrDefault(s.charAt(right),0) +1 );

            maxF = Math.max(maxF , comb.get(s.charAt(right)));
            while(right - left +1 -maxF>k){
                comb.put(s.charAt(left), comb.get(s.charAt(left)) -1 );
                left++;
            }
            longest = Math.max(longest, right- left +1);
            System.out.println(\long \ + longest + \ comb \ + comb);
        }
        return longest;
    }
}