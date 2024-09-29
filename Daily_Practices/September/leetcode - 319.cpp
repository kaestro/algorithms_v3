class Solution {
public:
    int bulbSwitch(int n) {
        if (n == 0) return 0;

        int initial_bulbs = (1 << n) - 1;
        int bulbs = initial_bulbs;
        for (int i = 2; i <= n; ++i) {
            decltype(bulbs) filter = 1 << (i - 1);
            while (filter < initial_bulbs) {
                filter <<= i;
                filter |= (1 << (i - 1));
                if (filter > initial_bulbs) {
                    filter >>= i;
                    break;
                }
            }

            bulbs ^= filter;
        }

        int result{0};
        while (bulbs) {
            result += bulbs & 1;
            bulbs >>= 1;
        }

        return result;
    }
};

int main() {
    Solution s;
    int result = s.bulbSwitch(6);
    return 0;
}
