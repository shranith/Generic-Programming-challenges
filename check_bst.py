INT_MAX = 4294967296
INT_MIN = -4294967296

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

	print(check_bst(root,INT_MIN,INT_MAX ))



def check_bst(root, mini, maxi):
	if root == None:
		return True
	if root.val < mini or root.val > maxi:
		return False

	if root.left != None:
		if root.left.val > root.val:
			return False
	if root.right != None:
		if root.right.val < root.val:
			return False
	return check_bst(root.left, mini, root.val-1) and check_bst(root.right, root.val+1, maxi)






if __name__ == '__main__':
	main()