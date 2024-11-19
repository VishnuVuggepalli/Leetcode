class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        Map<Integer, Integer> freqCount = new HashMap<>();

        for(int num =0; num < nums.length; num++){
            freqCount.put(nums[num],freqCount.getOrDefault(nums[num],0)+1);
            //minHeap.offer(nums[num]);
        }
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(
            (a,b) -> freqCount.get(b)-freqCount.get(a));
        
        minHeap.addAll(freqCount.keySet());

        for(int resCount =0 ; resCount<k; resCount++){
            res[resCount] = minHeap.poll();
        }
        return res;
    }
}