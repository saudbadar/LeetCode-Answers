class Solution {
public:
    int countPalindromicSubsequence(string s) {
        map<char, vector<int>> myMap;
        int ret = 0;
        
        for(int i = 0; i < s.size(); ++i){
            if(myMap.count(s[i])){
                myMap[s[i]][1] = i;
            }else{
                myMap[s[i]].insert(myMap[s[i]].end(), {i, i});
            }
        }

        for(auto const& [key, val] : myMap){
            int start = val[0], end = val[1];
            
            if(start < end){
                unordered_set<char> charSet;
                for(int i = start + 1; i < end; ++i){
                    charSet.insert(s[i]);
                }
                ret += charSet.size();
            }
        }
        return(ret);
        
    }
};