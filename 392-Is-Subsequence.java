class Solution {
    public boolean isSubsequence(String s, String t) {
        int tItr =0, sItr =0;
        while(sItr < s.length() && tItr < t.length()){
            if(s.charAt(sItr) == t.charAt(tItr)){
                sItr++;
            }
            tItr++;
        }
        return sItr == s.length();
    }
}