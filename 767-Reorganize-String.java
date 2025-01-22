class Solution {
    public String reorganizeString(String s) {
        int N = s.length();
        Map<Character, Integer> countMap = new HashMap<>();
        for(char c: s.toCharArray()){
            countMap.put(c,countMap.getOrDefault(c,0) + 1);
        }


        Queue<Map.Entry<Character,Integer>> pq = new PriorityQueue<>((a,b) -> Integer.compare(b.getValue(), a.getValue()));
        pq.addAll(countMap.entrySet());
        Map.Entry<Character, Integer> prev = null;
        String ordS = "";


        while(!pq.isEmpty()){
            Map.Entry<Character,Integer> cur = pq.poll();
            ordS += "" + cur.getKey();
            cur.setValue(cur.getValue() -1 );

            if(prev != null && prev.getValue() > 0)    pq.offer(prev);

            prev = cur;
        }
        if(s.length() != ordS.length()) return "";
        return ordS;
    }
}