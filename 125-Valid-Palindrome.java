class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll(\[^a-zA-Z0-9]\, \\).trim().toLowerCase();
        if(s.length() == 0) return true;
        for(int letter = 0; letter < s.length()/2 ; letter ++){
            if(s.charAt(letter) != s.charAt(s.length() - letter -1)) return false;
        }
        return true;
    }
}