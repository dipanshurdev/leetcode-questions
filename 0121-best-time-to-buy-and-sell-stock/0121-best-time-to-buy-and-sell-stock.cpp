class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mine=prices[0];
        int diff=0;
        int n=prices.size();
        
        for(int i=0;i<n;i++){
            diff=max((prices[i]-mine),diff);
            mine=min(prices[i],mine);
        }
        return diff;
    }
};