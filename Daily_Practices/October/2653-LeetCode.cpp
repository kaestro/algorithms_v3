#include <deque>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
        vector<int> transformed_nums = transformNums(nums);
        vector<int> res;
        deque<int> window;
        unordered_map<int, int> count_map;
        multiset<int> sorted_window;

        for (int i = 0; i < transformed_nums.size(); ++i) {
            if (i >= k) {
                int to_remove = window.front();
                window.pop_front();
                if (--count_map[to_remove] == 0) {
                    count_map.erase(to_remove);
                }
                sorted_window.erase(sorted_window.find(to_remove));
            }

            int to_add = transformed_nums[i];
            window.push_back(to_add);
            count_map[to_add]++;
            sorted_window.insert(to_add);

            if (i >= k - 1) {
                auto it = sorted_window.begin();
                advance(it, x - 1);
                res.push_back(*it);
            }
        }

        return res;
    }

private:
    vector<int> transformNums(const vector<int>& nums) {
        vector<int> transformed_nums;
        transformed_nums.reserve(nums.size());
        for (auto num : nums) {
            if (num < 0) {
                transformed_nums.push_back(num);
            } else {
                transformed_nums.push_back(0);
            }
        }
        return transformed_nums;
    }
};;
