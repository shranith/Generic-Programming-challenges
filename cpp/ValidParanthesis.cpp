#include<stack>
class Solution {
public:
    bool isValid(string s) {
        int i,j,l;
        stack<char> stac;
        l = s.length();
        for(i = 0;i<l;i++)
        {
            if(s[i] == '[' || s[i] == '{' || s[i] == '(')
                stac.push(s[i]);
            else if(s[i] == ']' || s[i] == '}' || s[i] == ')')
            {
                if(stac.size()==0)
                    return false;
                if(s[i] == ']')
                {
                    if(stac.top() != '[')
                        return false;
                        stac.pop();                }
                if(s[i] == '}')
                {
                    if(stac.top() != '{')
                        return false;
                        stac.pop();
                }
                if(s[i] == ')')
                {
                    if(stac.top() != '(')
                        return false;
                        stac.pop();
                }
            }
        }
        if(stac.size()!=0)
            return false;
        else return true;
    }
};
