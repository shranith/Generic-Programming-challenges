import queue

class Node:
	def __init__(self,val):
		self.val = val
		self.childNodes = []

def dfs(root):
	if root == None:
		return
	print(root.val)
	childNodes = root.childNodes
	for eachNode in childNodes:
		traverse(eachNode)
	return


def bfs(root):
	q = queue.Queue()
	print(root.val)
	for eachNode in root.childNodes:
		q.put(eachNode)
	q.put(None)
	while 1:
		r = q.get()
		if r == None:
			if q.empty():
				break
			q.put(None)
			print("\n")
		else:
			print(r.val)
			l = r.childNodes
			for eachNode in l:
				q.put(eachNode)
	return




def main():
	root = Node(0)
	c1 = Node(1)
	c2 = Node(2)
	c3 = Node(3)

	root.childNodes.append(c1)
	root.childNodes.append(c2)
	root.childNodes.append(c3)

	c1.childNodes.append(Node(4))
	c1.childNodes.append(Node(5))
	c1.childNodes[1].childNodes.append(Node(10))
	c1.childNodes.append(Node(6))
	c1.childNodes.append(Node(7))
	c2.childNodes.append(Node(8))
	c3.childNodes.append(Node(9))

	# dfs(root)

	bfs(root)





if __name__ == '__main__':
	main()