class Solution {
    public String intToRoman(int num) {
        int[] ints = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roms = {\M\,\CM\,\D\,\CD\,\C\,\XC\,\L\,\XL\,\X\,\IX\,\V\, \IV\,\I\};
        int i = 0;
        StringBuilder res = new StringBuilder();
        while (num > 0){
            if(num >= ints[i]){
                res.append(roms[i]);
                num -= ints[i];
            }
            else{
                i++;
            }
            
        }

        return res.toString();
    }
}