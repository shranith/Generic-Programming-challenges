class Node:
	def __init__(self,val):
		self.val = val
		self.next = None


def reverseLinkedList(root):
	if root == None or root.next ==None:
		return root

	p = root
	q = root.next
	r = q.next
	p.next = None
	q.next = p
	while r!= None:
		p = q
		q = r
		r = r.next
		q.next = p

	return q

def traverseLinkedList(root):
	while root!=None:
		print(root.val)
		root = root.next
	return







def main():
	head = Node(1)
	head.next = Node(2)
	# head.next.next = Node(3)
	# head.next.next.next = Node(4)
	# head.next.next.next.next = Node(5)
	# head.next.next.next.next.next = Node(6)
	# head.next.next.next.next.next.next = Node(7)
	# head.next.next.next.next.next.next.next = Node(8)
	# head.next.next.next.next.next.next.next.next = Node(9)

	traverseLinkedList(head)
	head = reverseLinkedList(head)
	traverseLinkedList(head)


if __name__ == '__main__':
	main()