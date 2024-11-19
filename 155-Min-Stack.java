class MinStack {
    Stack<Integer> stack = new Stack<>();
    Stack<Integer> minStack = new Stack<>();
    int minVal = Integer.MAX_VALUE;
    public MinStack() {
        
    }
    
    public void push(int val) {
        stack.push(val);
        if(minStack.isEmpty()) minVal = Integer.MAX_VALUE;
        if(!minStack.isEmpty() && minStack.peek() > minVal) minVal = minStack.peek();
        minVal = Math.min(minVal, val);
        minStack.push(minVal);
    }
    
    public void pop() {
        //System.out.println(\Before \ + minStack);
        minStack.pop();
        stack.pop();
        //System.out.println(\After \ + minStack);
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {

        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */