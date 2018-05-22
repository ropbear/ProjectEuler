class BinaryTree:
	def __init__(self,filename,size):
		self.size = size
		self.layers = self.treeify(filename)
		self.tree = self.fromList(self.layers)

	def fromList(self,layers):
		def recurse(items,i,size,max_size):
			if size == max_size:
				return []
			else:
				return [int(items[i]),recurse(items,i+size,size+1,max_size),recurse(items,i+size+1,size+1,max_size)]
		return recurse(layers,0,1,self.size)

	def treeify(self,filename):
		f = open(filename,'r')
		layers = []
		for line in f:
			layer = line.strip().split(' ')
			layers += layer
		return layers


def bruteMaxPath(tree):
	if tree == []:
		return 0
	else:
		return tree[0] + max(bruteMaxPath(tree[1]),bruteMaxPath(tree[2]))

if __name__ == "__main__":
	tree = BinaryTree("tree.txt",16)
	print(bruteMaxPath(tree.tree))
