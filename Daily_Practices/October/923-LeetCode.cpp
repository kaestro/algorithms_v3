#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        const int MOD = 1e9 + 7;
        sort(arr.begin(), arr.end());
        int n = arr.size();
        long long res = 0;

        for (int i = 0; i < n; ++i) {
            int t = target - arr[i];
            int j = i + 1;
            int k = n - 1;

            while (j < k) {
                if (arr[j] + arr[k] < t) {
                    j++;
                } else if (arr[j] + arr[k] > t) {
                    k--;
                } else {
                    if (arr[j] != arr[k]) {
                        int left = 1;
                        int right = 1;
                        while (j + 1 < k && arr[j] == arr[j + 1]) {
                            left++;
                            j++;
                        }
                        while (k - 1 > j && arr[k] == arr[k - 1]) {
                            right++;
                            k--;
                        }
                        res += left * right;
                        res %= MOD;
                        j++;
                        k--;
                    } else {
                        res += (k - j + 1) * (k - j) / 2;
                        res %= MOD;
                        break;
                    }
                }
            }
        }

        return res;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};
    int target = 8;
    int res = sol.threeSumMulti(arr, target);
    return 0;
}
