class Solution {
    public boolean dfs(int[][] graph,int i, Map<Integer, Boolean> tentative){
        if(tentative.containsKey(i)){
            return tentative.get(i);
        }
        tentative.put(i,false);
        int[] outgoing = graph[i];
        for(int index:outgoing){
            if (dfs(graph, index, tentative) == false)    return false;
        }
        tentative.put(i,true);
        return true;

    }
    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<Integer> safeNodes = new ArrayList<>();
        Map<Integer,Boolean> tentative = new HashMap<>();
        int N = graph.length;

        for(int i =0; i < N; i++){
            if(dfs(graph,i,tentative) == true){
                safeNodes.add(i);
            }
        }
        return safeNodes;
    }
}