def main():
	l = [1,2,3,4,5,6,7,8,9,9,9,2]
	print(len(l))
	window_size = 4
	summer = 0
	for i in range(window_size):
		summer+=l[i]
	avg = summer/window_size

	result_list = []
	result_list.append(avg)

	for i in range(1, len(l)-window_size+1):
		summer -= l[i-1]
		summer += l[i+window_size-1]
		result_list.append(summer/window_size)

	print(result_list)
	print(len(result_list))




main()