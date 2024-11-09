class Solution {
    public String longestCommonPrefix(String[] strs) {
        String stable =strs[0];
            for(int word =1; word < strs.length; word++){
                while(!strs[word].startsWith(stable)){
                    stable = stable.substring(0,stable.length() -1);
                    if(stable.isEmpty()) return \\;
                }
            }
        return stable;
    }
}