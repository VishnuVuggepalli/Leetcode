class Solution {
    public int[] plusOne(int[] digits) {
        if(digits[digits.length - 1] == 9){
            int carry =1;
            for(int dig = digits.length -1 ;dig >= 0; dig --){
                if (digits[dig] == 9){
                    digits[dig] = 0;
                    if (dig == 0){
                        int[] res = Arrays.copyOf(digits, digits.length + 1);
                        res[0] = 1;
                        return res;
                    }
                }
                else{
                    digits[dig] += carry;
                    return digits;
                }
            }
        }
        digits[digits.length - 1] += 1;
        return digits;
    }
}