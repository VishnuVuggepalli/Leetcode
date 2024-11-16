class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        int subLeft = 0;
        Set<Character> unqChar = new HashSet<Character>();
        for(int subRight =0; subRight < s.length(); subRight ++)
        {
            int tempLen =0;
            while(unqChar.contains(s.charAt(subRight))){
                    unqChar.remove(s.charAt(subLeft));
                    subLeft++;
                }
                unqChar.add(s.charAt(subRight));
                tempLen++;
            maxLength = Math.max(maxLength, subRight-subLeft+1);
        }
        return maxLength;
    }
}