#include <string>
#include <vector>
#include <memory>

using namespace std;

class Solution {
public:
    int maxProduct(string s) {
        unique_ptr<vector<int>> palindromic_masks = get_palindromic_masks(s);
        int max_product = max_product_of_two_palindromic_subsequences(*palindromic_masks);

        return max_product;
    }

private:
    unique_ptr<vector<int>> get_palindromic_masks(const string& s) {
        int n = s.size();
        unique_ptr<vector<int>> palindromic_masks = make_unique<vector<int>>();
        for (int mask = 1; mask < (1 << n); ++mask) {
            string subseq = "";
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    subseq += s[i];
                }
            }

            if (is_palindrome(subseq)) {
                palindromic_masks->push_back(mask);
            }
        }

        return palindromic_masks;
    }

    int max_product_of_two_palindromic_subsequences(const vector<int>& palindromic_masks) {
        int max_product = 0;
        for (int i = 0; i < palindromic_masks.size(); ++i) {
            for (int j = i + 1; j < palindromic_masks.size(); ++j) {
                if ((palindromic_masks[i] & palindromic_masks[j]) == 0) {
                    int product = bit_count(palindromic_masks[i]) * bit_count(palindromic_masks[j]);
                    max_product = max(max_product, product);
                }
            }
        }

        return max_product;
    }

    bool is_palindrome(const string& s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (s[l++] != s[r--]) return false;
        }
        return true;
    }

    int bit_count(unsigned int x) {
        int count = 0;
        while (x) {
            count += x & 1;
            x >>= 1;
        }
        return count;
    }
};
