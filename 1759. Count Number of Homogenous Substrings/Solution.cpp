class Solution {
public:
    int countHomogenous(string s) {
        int left = 0;
        long long ret = 0;

        for(int right = 0; right < s.size(); right++){
            if(s[left] == s[right]){
                ret += right - left + 1;
            }
            else{
                ret += 1;
                left = right;
            }
        }
        return((int) (ret % (1000000007)));
    }
};