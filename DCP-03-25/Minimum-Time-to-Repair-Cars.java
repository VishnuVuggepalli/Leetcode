class Solution {
    public long repairCars(int[] ranks, int cars) {
        long low = 1, high = (long)1e16;
        long minTime = 0L;
        while(low <= high){
            long mid = low + (high - low) / 2 ;
            int curCars = 0;
            for(int rank : ranks){
                curCars += (int)Math.sqrt(mid / (long)rank);
                if(curCars > cars)  break;
            }
            if (curCars >= cars){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
            minTime = low;
        }

        return minTime;
    }
}