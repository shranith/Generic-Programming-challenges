class Node:
	def __init__(self,data):
		self.val =data
		self.left = None
		self.right = None

def main():
	root = Node(5)
	root.left = Node(2)
	root.right = Node(7)
	root.left.left = Node(1)
	root.left.right = Node(3)
	root.right.left = Node(6)
	root.right.right = Node(8)

	u = 1
	v = 3
	print(check_lca_bst(root,u,v))

def check_lca_bst(root, u, v):
	if root.val <= v and root.val >= u:
		return root.val
	elif u > root.val:
		return check_lca(root.right, u , v)
	return check_lca(root.left, u ,v)


if __name__ == '__main__':
	main()