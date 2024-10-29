#include <map>

class Solution {
public:
    bool checkStrings(string s1, string s2) {
        map<char, int> odd_counter, even_counter;
        for (int i = 0; i < s1.size(); i += 2) {
            even_counter[s1[i]]++;
        }

        for (int i = 1; i < s1.size(); i += 2) {
            odd_counter[s1[i]]++;
        }

        for (int i = 0; i < s2.size(); i += 2) {
            if (even_counter[s2[i]] == 0) {
                return false;
            } else {
                even_counter[s2[i]]--;
            }
        }

        for (int i = 1; i < s2.size(); i += 2) {
            if (odd_counter[s2[i]] == 0) {
                return false;
            } else {
                odd_counter[s2[i]]--;
            }
        }

        return true;
    }
};
