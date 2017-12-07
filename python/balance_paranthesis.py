def balance(string):
	open_brackets = ['(','[','{']
	close_brackets = [')',']','}']
	bracket_map = {'(':')', '{':'}', '[':']'}

	stack_list = []
	for char in string:
		if char in open_brackets or char in close_brackets:
			if char in open_brackets:
				stack_list.append(char)
			elif char in close_brackets:
				if bracket_map[stack_list.pop()] != char:
					return False

	if len(stack_list) != 0:
		return False
	return True



def main():
	while 1:
		s = input("Enter a string:\n")
		if s == "exit":
			break
		print(balance(s))




if __name__ == '__main__':
	main()
