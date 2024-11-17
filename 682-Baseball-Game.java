class Solution {
    public int calPoints(String[] operations) {
      int sum =0;
      Stack<String> stack = new Stack<>();
      for(int op =0 ; op < operations.length ; op++){
        switch(operations[op]){
            case \+\: 
                int blockSum =0;
                String temp = \\;
                temp = stack.pop();
                blockSum = Integer.parseInt(temp) + Integer.parseInt(stack.peek());
                stack.push(\\ +temp);
                stack.push(\\ +blockSum);
                break;
            case \C\: 
                stack.pop();
                break;
            case \D\: 
                int doubleScore =0;
                doubleScore = Integer.parseInt(stack.peek());
                stack.push(\\ + (doubleScore * 2));
                break;
            default: 
                stack.push(operations[op]);
                break;
        }
      }
      while(!stack.isEmpty()){
        sum += Integer.parseInt(stack.pop());
      }
      return sum;
    }
}