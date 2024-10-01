#include <vector>
#include <map>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {

        map<int, int>mp;
        int n = barcodes.size();
        vector<int>res(n);
        priority_queue<pair<int, int>>pq;

        for(const auto &i : barcodes){
            mp[i]++;
        }

        for(const auto &i : mp){
            pq.push(make_pair(i.second, i.first)); // Freq, element
        }

        int i = 0;

        while(!pq.empty()){

            auto temp = pq.top();
            pq.pop();

            while(temp.first--){
                if(i >= n) i = 1;
                res[i] = temp.second;
                i += 2;
            }
        }

        return res;
    }
};

int main() {
    Solution s;
    std::vector<int> barcodes{1, 1, 1, 2, 2, 3};
    std::vector<int> result = s.rearrangeBarcodes(barcodes);
    return 0;
}
