class Pair{
    int i;
    int val;
    Pair(int val , int i){
        this.val = val;
        this.i = i;
    }
}

class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        List<Pair> pairs = new ArrayList<>();
        for(int i=0; i < nums.length;i++){
            pairs.add(new Pair(nums[i],i));
        }
        pairs.sort(Comparator.comparingInt(p -> p.val));
        // for(Pair p : pairs){
        //     System.out.println(p.i + " " + p.val);
        // }
        List<List<Pair>> res = new ArrayList<>();
        res.add(new ArrayList<>(Arrays.asList(pairs.get(0))));
        //System.out.println();

        for(int i = 1; i< nums.length ; i++){
            if(pairs.get(i).val - pairs.get(i-1).val <= limit)  res.get(res.size()-1).add(pairs.get(i));
            else    res.add(new ArrayList<>(Arrays.asList(pairs.get(i))));
        }
        for(List<Pair> group : res){
            List<Pair> sorted = new ArrayList<>(group);
            // System.out.println("Before Sort");
            // for(Pair p : sorted){
            //     System.out.println(p.i + " " + p.val);
            // }
            //System.out.println("After Sort");
            sorted.sort(Comparator.comparingInt(p -> p.i));
            // for(Pair p : sorted){
            //     System.out.println(p.i + " " + p.val);
            // }

            for(int i =0; i < group.size(); ++i)
                nums[sorted.get(i).i] = group.get(i).val; 
        }
        return nums;
    }
}