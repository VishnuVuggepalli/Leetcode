class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder res=new StringBuilder();
           int rem = 0;
           while (columnNumber > 0){
            columnNumber --;
            rem = columnNumber % 26;
            columnNumber /= 26;
            res.append((char)(rem + 65));
           } 
        return res.reverse().toString();
    }
}