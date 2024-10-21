#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int pairSum(ListNode* head) {
        vector<long long> partial_sums;
        long long sum = 0;
        while (head != nullptr) {
            sum += head->val;
            partial_sums.push_back(sum);
            head = head->next;
        }
        int n = partial_sums.size();

        long long max_twin_sum = partial_sums[0] + partial_sums[n-1] - partial_sums[n-2];
        for (int i = 1; i < n/2; ++i) {
            long long twin_sum = (partial_sums[i] - partial_sums[i-1]) + (partial_sums[n-1-i] - partial_sums[n-1-i-1]);
            max_twin_sum = max(max_twin_sum, twin_sum);
        }

        return static_cast<int>(max_twin_sum);
    }
};
