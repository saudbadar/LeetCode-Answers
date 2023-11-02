class Solution {
public:
    int kthGrammar(int n, int k) 
    {
        bool notZero = false;
        n = pow(2, n - 1);

        while(n != 1){
            n = int(n / 2);
            if(k > n){
                k -= n;
                notZero = !notZero;
            }
        }
        return(notZero);   
    }
};