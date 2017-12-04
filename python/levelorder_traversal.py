import Queue 


class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

q = Queue.Queue()


def levelorder(root):
	if root == None:
		return
	print(root.val)

	if root.left == None and root.right == None:
		print(root.val)
		return
	if root.left != None:
		q.put(root.left)
	if root.right !=None:
		q.put(root.right)

	while not q.empty():
		r = q.get()
		print(r.val)
		if r.left !=None:
			q.put(r.left)
		if r.right != None:
			q.put(r.right)
	return

def main():
	root = Node(5)
	root.left = Node(3)
	root.left.left = Node(2)
	root.left.right = Node(4)
	root.right = Node(8)
	root.right.left = Node(7)
	root.right.right = Node(9)


	levelorder(root)


if __name__ == '__main__':
	main()