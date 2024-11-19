class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> nums = new Stack<>();
        for(int itr =0 ; itr < tokens.length; itr++){
            switch(tokens[itr]){
                case \+\:
                    int sum = 0;
                    sum = Integer.parseInt(nums.pop()) + Integer.parseInt(nums.pop());
                    nums.push(String.valueOf(sum));
                    break;
                case \-\:
                    int diff = 0;
                    int first =0, second =0;
                    first = Integer.parseInt(nums.pop());
                    second = Integer.parseInt(nums.pop());
                    diff =  second - first;
                    nums.push(String.valueOf(diff));
                    break;
                case \*\:
                    int mul = 0;
                    mul = Integer.parseInt(nums.pop()) * Integer.parseInt(nums.pop());
                    nums.push(String.valueOf(mul));
                    break;
                case \/\:
                    int div = 0;
                    int firstD =0, secondD =0;
                    firstD = Integer.parseInt(nums.pop());
                    secondD = Integer.parseInt(nums.pop());
                    div =  secondD / firstD;
                    System.out.println(div);
                    nums.push(String.valueOf(div));
                    break;
                default:
                    nums.push(tokens[itr]);
                    break;
            }
        }
        return Integer.parseInt(nums.peek());
    }
}