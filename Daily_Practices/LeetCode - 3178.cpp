class Solution {
public:
    int numberOfChild(int n, int k) {
        int lap = k / (n - 1);
        int remnant = k % (n - 1);
        int ans;

        if (lap % 2 == 1) {
            ans = n - remnant - 1;
        } else {
            ans = remnant;
        }

        return ans;
    }
};
