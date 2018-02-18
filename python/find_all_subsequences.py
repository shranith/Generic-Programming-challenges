'''
Find all subsequences in a given string
Time Complexity O(2^n)
'''
subsequences_list = set()

def find_all_subsequences(str1, str2):
	global subsequences_list
	if str2 == "":
		subsequences_list.add(str1)
		return
	subsequences_list.add(str1)
	subsequences_list.add(str2)
	find_all_subsequences(str1+str2[0], str2[1:])
	find_all_subsequences(str1, str2[1:])

find_all_subsequences("","abcde")
subsequences_list = list(subsequences_list)
subsequences_list.sort()
print(subsequences_list)



