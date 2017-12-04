l = [(1,9), (2,3),(3,4), (5,7),(8,9)]


current_tuple = l.pop(0)
print(current_tuple)
return_list = []
while len(l) !=0:
	next_tuple = l.pop(0)
	e1 = current_tuple[1]
	e2 = next_tuple[1]
	b1 = current_tuple[0]
	b2 = next_tuple[0]

	if e1 < b2:
		return_list.append(current_tuple)
		current_tuple = next_tuple
	elif e1 >= b2:
		if e1 < e2:
			current_tuple = (current_tuple[0], e2)

return_list.append(current_tuple)
print(return_list)