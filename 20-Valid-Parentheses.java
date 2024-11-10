class Solution {
    public boolean isValid(String s) {
        Map<Character,Character> mappings = new HashMap<>();
        mappings.put('(',')');
        mappings.put('[',']');
        mappings.put('{','}');
        Stack<Character> stack = new Stack<>();
        for(char c : s.toCharArray()){
            if(c == '(' || c == '[' || c == '{'){
                stack.push(c);
            }
            else{
                if(stack.isEmpty()) return false;
                char top = stack.pop();
                //System.out.println(top);
                if(c != mappings.get(top)){
                    return false;
                }
            }
            //System.out.println(stack);
        }
        return stack.isEmpty();
    }
}