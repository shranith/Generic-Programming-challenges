std::string compress(std::string s) {
	int i=0,j=1,l = s.length();
	while(1)
	{
		while(s[i]==s[j] && j<l)
			j++;
		if(j<l){
		s[i+1] = s[j];
		i++;}
		else
			break;
	}
	return s.substr(0,i+1);
}
