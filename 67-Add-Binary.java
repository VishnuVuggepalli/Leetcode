class Solution {
    public String addBinary(String a, String b) {
        int carry =0;
        int first = a.length() -1 ;
        int second = b.length() -1;
        StringBuilder sb = new StringBuilder();

        while(first >= 0 || second >= 0){
            int sum = carry;

            if(first >= 0) sum += a.charAt(first--) -'0';
            if(second >= 0 ) sum += b.charAt(second--) - '0';
            sb.append(sum % 2);
            carry = sum /2;
        }
        if (carry != 0) sb.append(carry);

        return sb.reverse().toString();

    }
}