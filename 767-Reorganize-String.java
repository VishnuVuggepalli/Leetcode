class Solution {
    public String reorganizeString(String s) {
        int N = s.length();
        Map<Character, Integer> countMap = new HashMap<>();
        for(char c: s.toCharArray()){
            countMap.put(c,countMap.getOrDefault(c,0) + 1);
        }
        PriorityQueue<Character> pq = new PriorityQueue<>((a,b) -> countMap.get(b) - countMap.get(a));
        pq.addAll(countMap.keySet());
        String ordS = "";
        while(pq.size() > 1){
            char c1 = pq.poll();
            char c2 = pq.poll();

            ordS += "" + c1;
            ordS += "" + c2;

            countMap.put(c1,countMap.get(c1) - 1);
            countMap.put(c2,countMap.get(c2) - 1);

            if(countMap.get(c1) > 0)    pq.add(c1);
            if(countMap.get(c2) > 0)    pq.add(c2);
        }
        while(!pq.isEmpty()){
            char last = pq.poll();
            if(countMap.get(last) > 1) return "";
            ordS += last;
        }
        return ordS;
    }
}