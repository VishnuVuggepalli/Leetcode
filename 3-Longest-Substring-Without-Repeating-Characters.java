class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        for(int subLeft =0; subLeft + maxLength < s.length(); subLeft ++)
        {
            int tempLen =0, subRight =0;
            Set<Character> unqChar = new HashSet<Character>();
            //System.out.println(\in loop 1  \ + s.charAt(subLeft));
            for(subRight = subLeft; subLeft + (subRight - subLeft) < s.length(); subRight++){
                //System.out.println(\in loop 2  \ + s.charAt(subRight));
                if(unqChar.contains(s.charAt(subRight))){
                    //System.out.println(\in contains \ + s.charAt(subRight));
                    break;
                }
                unqChar.add(s.charAt(subRight));
                tempLen++;
            }
            if(maxLength < subRight - subLeft){
                maxLength = subRight - subLeft;
            }
        }
        return maxLength;
    }
}