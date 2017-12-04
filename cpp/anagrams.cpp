/*
  generate all the palindromes from a given string!!. 
  Helper function recursively forms different anagrams. 
*/

#include <iostream>
#include <vector>
using namespace std;
vector<string> result;
void helper(string formed, string residual)
{
	if(residual.length()==0)
		result.push_back(formed);
	for(int i =0;i<residual.length();i++)
	{
		int k = 0;
		int l = residual.length();
		string newformed = formed;
		newformed += residual[i];
		string newresidual = residual.substr(k,i-k) + residual.substr(i+1,l-i);
		helper(newformed,newresidual);
		
	}
}

int main() {
	string residual = "abc";
	string formed = "";
	helper(formed,residual);
	
	for(int i = 0 ;i< result.size();i++)
		cout<<result[i]<<" ";
	return 0;
}

