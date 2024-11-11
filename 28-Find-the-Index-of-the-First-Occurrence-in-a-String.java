class Solution {
    public int strStr(String haystack, String needle) {
        for(int first = 0 ; first <= haystack.length()- needle.length(); first ++){
                    if(haystack.substring(first, first + needle.length()).equals(needle)){
                        return first;
                    }
        }
        return -1;
        //return haystack.indexOf(needle)
    }
}