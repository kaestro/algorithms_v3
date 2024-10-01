#include <vector>
#include <map>

class Solution {
public:
    std::vector<int> rearrangeBarcodes(std::vector<int>& barcodes) {
        if (barcodes.size() == 1) {
            return barcodes;
        }

        std::map<int, int> barcode_count;
        for (int barcode : barcodes) {
            barcode_count[barcode]++;
        }

        auto it = barcode_count.begin();

        std::vector<int> result;
        result.reserve(barcodes.size());

        while (it != barcode_count.end()) {
            result.push_back(it->first);
            it->second--;
            if (it->second == 0) {
                it = barcode_count.erase(it);
                if (it == barcode_count.end() && !barcode_count.empty()) {
                    it = barcode_count.begin();
                }
            } else {
                if (it != barcode_count.begin()) {
                    it--;
                } else {
                    it++;
                }
            }
        }

        return result;
    }
};

int main() {
    Solution s;
    std::vector<int> barcodes{1, 1, 1, 2, 2, 3};
    std::vector<int> result = s.rearrangeBarcodes(barcodes);
    return 0;
}
