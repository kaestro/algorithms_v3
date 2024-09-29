#include <vector>

class Solution {
public:
    std::vector<int> replaceElements(std::vector<int>& arr) {
        std::vector<int> result(arr.size());
        copy(begin(arr), end(arr), begin(result));

        auto prev_it = result.begin();
        for (auto it = std::max_element(begin(result), end(result)); it != end(result); it = std::max_element(it + 1, end(result))) {
            std::fill(prev_it, it, *it);
            prev_it = it;
        }

        std::fill(prev_it, result.end(), -1);
        return result;
    }
};
