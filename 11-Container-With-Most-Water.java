class Solution {
    public int maxArea(int[] height) {
        int area = 0;
        int right = height.length -1;
        int left = 0;
        while(left < right){
            int leng = Math.min(height[left], height[right]);
            int bread = right - left;
            area = Math.max(area, leng * bread);
            if(height[left]  < height[right]){
                left ++;
            }
            else{
                right --;
            }
        }
        return area;
    }
}