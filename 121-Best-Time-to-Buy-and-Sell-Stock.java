class Solution {
    public int maxProfit(int[] prices) {
        int profit =0;
        int mini = prices[0];
        for (int stock =0 ; stock < prices.length; stock++){
            mini = Math.min(mini, prices[stock]);
            profit = Math.max(profit,prices[stock] - mini);
        }
        return profit;
    }
}