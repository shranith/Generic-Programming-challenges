number_to_char_map = {}
number_to_char_map['2'] = ['A','B','C']
number_to_char_map['3'] = ['D','E','F']
number_to_char_map['4'] = ['G','H','I']
number_to_char_map['5'] = ['J','K','L']
number_to_char_map['6'] = ['M','N','O']
number_to_char_map['7'] = ['P','Q','R']
number_to_char_map['8'] = ['S','T','U', 'V']
number_to_char_map['9'] = ['W','X','Y','Z']



number = list('2443')



def main():

	final_strings = []
	for value in number_to_char_map[number.pop(0)]:
		final_strings.append(value)
	# print(final_strings)

	print(phone_keyboard(number,final_strings))
	# print(final_strings)

def phone_keyboard(number , final_strings):
	if len(number) == 0:
		return final_strings
	char = number.pop(0)
	tmp_str_list = []
	for value in number_to_char_map[char]:
		for each_string in final_strings:
			tmp_str_list.append(each_string+value)
	# final_strings = []
	final_strings = tmp_str_list
	return phone_keyboard(number,final_strings)

main()