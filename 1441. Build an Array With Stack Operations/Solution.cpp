class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) 
    {
        vector<string> ret;
        int val = target.front();
        target.erase(target.begin());
        for(int start = 1; start <= n; start++)
        {
            ret.push_back("Push");
            if(val != start)
                ret.push_back("Pop");
            else{
                if(target.empty())
                break;
                val = target.front();
                target.erase(target.begin());
            }
        }
        returSn(ret);
    }
};