def encoding(string):
	result = ""
	count = 0
	prev_char = string[0]
	for char in string:
		if prev_char == char:
			count +=1
		else:
			result+=prev_char+str(count)
			prev_char = char
			count = 1
	result+=prev_char+str(count)
	return result

def main():
	while 1:
		s = input("Enter a string:\n")
		if s == "exit":
			break
		print(encoding(s))

if __name__ == '__main__':
	main()
