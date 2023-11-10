class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        map<int, vector<int>> myMap;
        for(auto& item: adjacentPairs){
            myMap[item[0]].push_back(item[1]);
            myMap[item[1]].push_back(item[0]);
        }
        int prev = INT_MIN, size = 2;

        for(auto& item: myMap){
            if(item.second.size() == 1){
                prev = item.first;
                break;
            }
        }
        
        vector<int> ret = {prev, myMap[prev][0]};
        prev = myMap[prev][0];
        while(size != (adjacentPairs.size() + 1)){
            for(auto& temp: myMap[prev]){
                if(temp != ret[size - 2]){
                    prev = temp;
                }
            }
            ret.push_back(prev);
            size += 1;
        }
        return(ret);
    }
};