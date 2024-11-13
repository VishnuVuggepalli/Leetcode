class Solution {
    public int[] replaceElements(int[] arr) {
        int right = arr.length-1;
        int max = arr[arr.length-1];
        arr[arr.length -1 ]= -1;
        for(int ele = right -1; ele >=0; ele--){
            int temp = arr[ele];
            arr[ele] = max;
            if(max < temp){
                max = temp;
            }
        }
        return arr;

    //     for(ele =0 ; ele < arr.length-1; ele++){
    //         int max = Integer.MIN_VALUE;
    //         for(int second =ele +1 ; second < arr.length ; second++ ){
    //             if(max < arr[second]){
    //                 max = arr[second];
    //             }
    //         }
    //         arr[ele] = max;
    //     }
    //     arr[ele] = -1;
    //     return arr;
     }
}