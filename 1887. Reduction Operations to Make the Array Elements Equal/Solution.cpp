class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.rbegin(), nums.rend());
        int count = 0, sum = 0, prev = 50001;
        for(int val: nums){
            if(val != prev)
                count += sum;
            sum++;
            prev = val;
        }
        return(count);
    }
};