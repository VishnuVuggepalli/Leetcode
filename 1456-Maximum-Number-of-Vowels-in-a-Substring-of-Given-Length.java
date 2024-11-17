class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        int right =0;
        int count =0;
        int resCount =0;
        int left =0;
        for(right = 0 ; right < k; right++){
            if(vowels.contains(s.charAt(right)))    count++;
            resCount = Math.max(resCount, count);
        }
        for (int rightCont = right; rightCont < s.length(); rightCont++){
            if(vowels.contains(s.charAt(rightCont)))    count++;
            if(vowels.contains(s.charAt(left))) {
                count--;
            }
            left++;
            //System.out.println("left : "+left+ " right " + rightCont);
            resCount = Math.max(resCount, count);
        }
        return resCount;
    }
}