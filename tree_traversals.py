class Node:
	def __init__(self,data):

		self.val = data
		self.left = None
		self.right = None


def inorder(root):
	if root == None:
		return
	inorder(root.left)
	print(root.val)
	inorder(root.right)

def preorder(root):
	if root == None:
		return
	print(root.val)
	preorder(root.left)
	preorder(root.right)

def postorder(root):
	if root == None:
		return
	postorder(root.left)
	postorder(root.right)
	print(root.val)



def main():
	root = Node(5)
	root.left = Node(3)
	root.left.left = Node(2)
	root.left.right = Node(4)
	root.right = Node(8)
	root.right.left = Node(7)
	root.right.right = Node(9)


	inorder(root)
	preorder(root)
	postorder(root)




if __name__ == '__main__':
	main()