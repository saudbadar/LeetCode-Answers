class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<int> mySet;
        for(string num: nums){
            mySet.insert(stoi(num, 0, 2));
        }
        int n = nums.size();
        for(int i = 0; i <= n; ++i){
            if(mySet.find(i) == mySet.end()){
                string ans = bitset<16>(i).to_string();
                return(ans.substr(16 - n));
            }
        }
        return("");
    }
};