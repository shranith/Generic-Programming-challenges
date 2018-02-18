'''
Find all substrings in a given string
Time Complexity O(n^2)
'''

def find_substrings(sentence):
	length = len(sentence)
	substring_list = set()
	for i in range(length):
		for j in range(i,length):
			substring_list.add(sentence[i:j])
	return substring_list


sentence = "abcde"
print(find_substrings(sentence))