#Given a string it prints out all palindromes
s = "adfdfasdfasdfdfadsfasdfaaaaaa"
# s = "racecar"

length = len(s)
palindromes = set()
i = 0
while i < length:
	m = i-1
	n = i+1
	while m >= 0 and n < length and s[m] == s[n]:
		palindromes.add(s[m:n+1])
		m-=1
		n+=1
	i+=1

i=0
while i < length:
	m = i
	n = i+1
	while m >= 0 and n < length and s[m] == s[n]:
		palindromes.add(s[m:n+1])
		m-=1
		n+=1
	i+=1




print(palindromes)





