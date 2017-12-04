def main():
	l = [1,2,3,3,4,5,6,7,8]
	target = 6
	i = 0
	j = len(l)-1
	pairs = []
	while i < j:
		if l[i] + l[j] == target:
			pairs.append((l[i],l[j]))
			i+=1
			j-=1
		elif l[i] + l[j] > target:
			j-=1
		elif l[i] + l[j] < target:
			i+=1
	print(pairs)


main()