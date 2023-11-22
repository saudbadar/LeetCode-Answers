class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        queue<pair<int, int>> BFS;
        BFS.push({0,0});
        vector<int> ret;
        
        while(!BFS.empty()){
            auto [row, col] = BFS.front();
            BFS.pop();
            ret.push_back(nums[row][col]);
            if(col == 0 && (row + 1) < nums.size()){
                BFS.push({row + 1, col});
            }
            if((col + 1) < nums[row].size()){
                BFS.push({row, col + 1});
            }
        }
        return(ret);
    }
};