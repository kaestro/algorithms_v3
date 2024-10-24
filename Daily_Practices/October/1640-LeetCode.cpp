//https://leetcode.com/problems/check-array-formation-through-concatenation/
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        map<int, vector<int>> mp;
        for (auto& p : pieces) {
            mp[p[0]] = p;
        }
        vector<int> res;
        for (int i = 0; i < arr.size(); i++) {
            if (mp.find(arr[i]) != mp.end()) {
                res.insert(res.end(), mp[arr[i]].begin(), mp[arr[i]].end());
            }
        }
        return res == arr;
    }
};
