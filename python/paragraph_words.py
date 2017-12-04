#Find shortest substring of a paragraph where a given a list of words are included in it.
#cases find the shortest substring which contains all the words, there may be a string which is longer and has all the words, but we have to find the string which has the smallest length
def main():
	paragraph = "A quick brown fox easily lazy jumped over lazy dog fox lazy"
	words = ["fox","lazy"]


	paragraph_list = paragraph.split(" ")

	word_map = {}
	for word in words:
		word_map[word] = 0
	length = len(words)
	count = 0
	start = 0
	end = 0

	for word_iter in range(len(paragraph_list)):
		word = paragraph_list[word_iter]
		if word in words:
			if word_map[word] == 0:
				count+=1
			word_map[word] = word_iter
			if count == length:
				func(word_map,paragraph_list)



def func(word_map,paragraph_list):
	l = word_map.values()
	length = max(l) - min(l)
	print(paragraph_list[min(l):max(l)+1])
	# print(length)

main()