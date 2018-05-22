class Tree:
	def __init__(self,filename,size):
		self.layers = self.treeify(filename)
		self.tree = self.fromList(self.layers)
		self.size = size

	def fromList(self,layers):
		def recurse(items,i,size,max_size):
			if size == max_size:
				return []
			else:
				return [items[i],recurse(items,i+size,size+1,max_size),recurse(items,i+size+1,size+1,max_size)]
		return recurse(layers,0,1,6)

	def treeify(self,filename):
		f = open(filename,'r')
		layers = []
		for line in f:
			layer = line.strip().split(' ')
			layers += layer
		return layers

if __name__ == "__main__":
	tree = Tree("tree.txt",6)
