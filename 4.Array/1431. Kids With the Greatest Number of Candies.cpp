class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> out;
        int r=*max_element(candies.begin(),candies.end())-extraCandies;
        for(int i:candies)
            out.push_back(i>=r);
        return out;
    }
};