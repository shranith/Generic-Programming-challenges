import sys
def main():
	num = sys.argv[1]
	print(num)
	num_str = str(num)[::-1]
	returnstring = ""
	for i in range(len(num_str)):
		returnstring+=num_str[i]
		if (i+1)%3==0 and i+1 != len(num_str):
			returnstring+=','

	print(returnstring[::-1])





main()