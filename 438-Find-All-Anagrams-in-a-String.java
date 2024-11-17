class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] pRes = new int[128], sRes = new int[128];
        List<Integer> indices = new ArrayList<>();
        if(p.length() > s.length()) return indices;
        for(int first =0; first < p.length(); first ++){
            pRes[p.charAt(first)] ++;
            sRes[s.charAt(first)] ++;
        }
        if(Arrays.equals(pRes,sRes)) indices.add(0);
        for(int second = p.length() ; second<s.length(); second++){
            
            sRes[s.charAt(second)]++;
            sRes[s.charAt(second - p.length())]--;
            if(Arrays.equals(pRes,sRes)) indices.add(second-p.length()+1);
        }
        return indices;
    }
}