std::vector<int> vietasFormulas(std::vector<int> roots) {
    
    std::vector<int>result,newresult;
    result.push_back(1);
    result.push_back(-1*roots[0]);
    int i,j;
        
    for(i = 2;i<=roots.size();i++)
    {
            newresult = result;
            newresult.insert(newresult.begthubin(),0);
            for(j = 0;j<newresult.size();j++)
            {
                newresult[j] = newresult[j]* (roots[i-1]*-1);
            }
            for(j = 0;j<result.size();j++)
            {
                newresult[j] = newresult[j]+ result[j];
            }
            result = newresult;
    }
    return result;
    
}

int main()
{
std::vector<int> roots,result;
roots.push_back(1);
roots.push_back(-4);
roots.push_back(0);
roots.push_back(5);
roots.push_back(-4);
roots.push_back(2);
result = vietasFormulas(roots);
for(int i = 0;i<result.size();i++)
std::cout<<result[i]<<" ";
}
