class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()) return false;

        int[] str1 = new int[26], str2 = new int[26];
        for(int first =0 ; first < s1. length(); first ++){
            str1[s1.charAt(first) - 'a']++;
            str2[s2.charAt(first) - 'a']++;
        }

        for(int second = s1.length(); second < s2.length(); second++){
            if(Arrays.equals(str1,str2)) return true;
            str2[s2.charAt(second) - 'a']++;
            str2[s2.charAt(second - s1.length()) - 'a'] --;
        }
        return Arrays.equals(str1,str2);
    }
}