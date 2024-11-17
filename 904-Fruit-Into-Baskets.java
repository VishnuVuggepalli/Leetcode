class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer,Integer> freqMap = new HashMap<>();
        int left =0 ;
        int maxF =0;
        for(int right =0 ; right < fruits.length ; right++){
            freqMap.put(fruits[right], freqMap.getOrDefault(fruits[right],0)+1);
            while(freqMap.size() > 2){
                freqMap.put(fruits[left], freqMap.get(fruits[left]) - 1);
                if(freqMap.get(fruits[left]) == 0) freqMap.remove(fruits[left]);
                left++;
            }
            maxF = Math.max(maxF, right-left+1);
        }   
        return maxF;
    }
}