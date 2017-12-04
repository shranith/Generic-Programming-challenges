l = [1,2,3,4,5,8,9,9,10,11,12,14]
target = 7

i = 0
j = len(l)-1
flag = 0

while i <= j:
	mid = (i+j)/2
	if target == l[mid]:
		print("Found at index", mid)
		flag = 1
		break
	elif target > l[mid]:
		i = mid+1
	elif target < l[mid]:
		j = mid-1
if flag == 0:
	print("not found")