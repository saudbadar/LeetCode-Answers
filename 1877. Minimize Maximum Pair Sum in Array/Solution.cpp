class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.size() - 1, ret = INT_MIN;
        while(left < right){
            ret = max(nums[left] + nums[right], ret);
            left += 1;
            right -= 1;
        }
        return(ret);
        
    }
};