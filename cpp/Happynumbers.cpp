/*A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
*/
#include<vector>
class Solution {
public:
    bool isHappy(int n) {
        if(n==1)
        return true;
    vector<int>myvector;
    myvector.push_back(n);
     std::vector<int>::iterator it;
    while(true)
    {
        n = sumofsquares(n);
        if(n==1)
            return true;
       

    it = find (myvector.begin(), myvector.end(), n);
    if (it != myvector.end())
        return false;
    else
        myvector.push_back(n);

        
    }
    }
    int sumofsquares(int n)
    {
        int sum=0;
        string s = to_string(n);
        cout<<s<<endl;;
        for(int i = 0;i<s.length();i++)
        {
            cout<<int(s[i])<<endl;
            sum+=(int(s[i])-48)*(int(s[i])-48);
        }
        cout<<sum<<endl;
        return sum;
    }

};
