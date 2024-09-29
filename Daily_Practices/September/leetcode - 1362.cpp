#include <vector>
#include <cmath> // std::abs

class Solution {
public:
    std::vector<int> closestDivisors(int num) {
        int num1 = num + 1;
        int num2 = num + 2;

        int sqrt_num1 = std::sqrt(num1);
        int sqrt_num2 = std::sqrt(num2);

        std::vector<int> result{1, num1};

        for (int i = sqrt_num1; i > 0; --i) {
            if (num1 % i == 0) {
                result = {i, num1 / i};
                break;
            }
        }

        for (int i = sqrt_num2; i > 0; --i) {
            if (num2 % i == 0) {
                if (std::abs(result[0] - result[1]) > std::abs(i - num2 / i)) {
                    result = {i, num2 / i};
                }
                break;
            }
        }

        return result;
    }
};

int main() {
    Solution s;
    std::vector<int> result = s.closestDivisors(8);
    return 0;
}
