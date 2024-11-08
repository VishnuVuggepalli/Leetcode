class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for (int row= 0 ; row < numRows; row ++){
            List<Integer> line = new ArrayList<>();
            line.add(1);
            for (int num = 1 ; num < row; num ++){
                    line.add(res.get(row-1).get(num-1) + res.get(row-1).get(num));
            }
            if(row > 0){
                line.add(1);
            }
            res.add(line);
        }
        return res;
    }
}