class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int minSum = k * threshold;
        int count = 0;
        int subArraySum =0;
        for(int temp=arr.length-1; temp>=arr.length-k; temp--){
            subArraySum += arr[temp];
            }
        if(subArraySum >= minSum){
                count++;
            }
            //System.out.println(subArraySum);
        
        for(int right = arr.length -1, left = right -k; left >= 0  ; right--, left--){ 
            subArraySum -= arr[right];
            //System.out.println("after - " + subArraySum);
            subArraySum += arr[left];
            //System.out.println("after + " + subArraySum);
            if(subArraySum >= minSum){
                count++;
            }
        }
        return count;
    }
}