class Pair {
    char c; 
    int val;
    public Pair(char c, int val){
        this.c = c;
        this.val = val;
    }
}
class Solution {
    public String longestDiverseString(int a, int b, int c) {
        StringBuilder longest = new StringBuilder();
        PriorityQueue<Pair> Q = new PriorityQueue<>((x,y) -> y.val - x.val);

        if(a>0) Q.offer(new Pair('a',a));
        if(b>0) Q.offer(new Pair('b',b));
        if(c>0) Q.offer(new Pair('c',c));

        
        while(!Q.isEmpty()){
            Pair biggest = Q.poll();
            if(longest.length() >= 2 && longest.charAt(longest.length() - 1) == biggest.c  && longest.charAt(longest.length() - 2) == biggest.c){
                if(Q.isEmpty()) break;
                Pair second = Q.poll();
                longest.append(second.c);
                second.val --;
                if(second.val > 0)  Q.offer(second);
                Q.offer(biggest);
            }
            else{
                longest.append(biggest.c);
                biggest.val --;
                if(biggest.val >0)  Q.offer(biggest);
            }
        }
        return longest.toString();
    }
}