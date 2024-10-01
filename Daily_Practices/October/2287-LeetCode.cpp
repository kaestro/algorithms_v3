#include <string>
#include <map>

using namespace std;

class Solution {
public:
    int rearrangeCharacters(string s, string target) {
        map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        int result = 0;
        while (true) {
            for (char c : target) {
                if (freq[c] > 0) {
                    freq[c]--;
                } else {
                    return result;
                }
            }
            result += 1;
        }


        return result;
    }
};
