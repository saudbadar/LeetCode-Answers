class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n = dist.size();
        vector<double> timeToCity(n);
        
        for(int i = 0; i < n; i++){
            timeToCity[i] = static_cast<double>(dist[i]) / speed[i];
        }
        sort(timeToCity.begin(), timeToCity.end());

        for(int i = 0; i < n; i++){
            if(timeToCity[i] <= i){
                return(i);
            }
        }
        return(n);
    }
};