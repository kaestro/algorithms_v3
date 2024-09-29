#include <vector>

class Solution {
public:
    int smallestRangeI(std::vector<int>& nums, int k) {
        if (nums.size() == 1) return 0;

        int min = *std::min_element(nums.begin(), nums.end());
        int max = *std::max_element(nums.begin(), nums.end());

        if (max - min <= 2 * k) return 0;
        return max - min - 2 * k;
    }
};
