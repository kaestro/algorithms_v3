#include <vector>

using namespace std;

class Solution {
public:
    int maximizeTheProfit(int n, vector<vector<int>>& offers) {
        vector<int> dp(n + 1, 0); // dp[i]는 길이가 i인 길의 최대 이익
        vector<vector<pair<int, int>>> offersEndingAt(n); // offersEndingAt[i]는 길의 끝이 i인 제안들(시작, 금액)

        // Group offers by their end positions
        for (const auto& offer : offers) {
            int start = offer[0];
            int end = offer[1];
            int gold = offer[2];
            offersEndingAt[end].emplace_back(start, gold);
        }

        // Dynamic Programming to calculate maximum profit
        for (int i = 0; i < n; ++i) {
            dp[i + 1] = dp[i]; // Initialize dp[i+1] with dp[i]
            for (const auto& [start, gold] : offersEndingAt[i]) {
                dp[i + 1] = max(dp[i + 1], dp[start] + gold); // dp[i+1]은 start에서 끝나는 제안의 금액 + dp[start] 중 최대값
            }
        }

        return dp[n];
    }
};
