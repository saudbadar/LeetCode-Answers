class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int length = arr.size();
        arr[0] = 1;

        for(int i = 1; i < length; ++i){
            if(arr[i] - arr[i - 1] > 1){
                arr[i] = arr[i - 1] + 1;
            }
        }
        return(arr.back());
    }
};