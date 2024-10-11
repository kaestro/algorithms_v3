#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        int n = points.size();
        unordered_map<int, unordered_set<int>> m;
        for (auto& p : points) {
            m[p[0]].insert(p[1]);
        }
        int res = INT_MAX;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                auto& p1 = points[i];
                auto& p2 = points[j];
                if (p1[0] == p2[0] || p1[1] == p2[1]) continue;
                if (m[p1[0]].count(p2[1]) && m[p2[0]].count(p1[1])) {
                    res = min(res, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]));
                }
            }
        }
        return res == INT_MAX ? 0 : res;
    }
};
