# https://www.thealgorists.com/Algo/GraphTheory/Tarjan/ArticulationPoint
# https://web.iitd.ac.in/~bspanda/biconnectedMTL776.pdf

class Graph:
	def __init__(self, v):
		self.vertices = v
		self.adj = []
		self.visited = [False] * v
		self.articulation = [False] * v
		self.parent = [None] * v
		self.depth = [None] * v
		self.low = [None] * v

	def find_articulation(self, i, dist):
		self.visited[i] = True
		self.depth[i] = dist
		self.low[i] = dist

		is_articulation = False
		child_count = 0

		for vertex in self.adj[i]:
			if not self.visited[vertex]:
				self.parent[vertex] = i
				self.find_articulation(vertex, dist + 1)
				child_count += 1
				if self.low[vertex] >= self.depth[i]:
					is_articulation = True
				self.low[i] = min(self.low[i], self.low[vertex])
			elif vertex != self.parent[i]:
				self.low[i] = min(self.low[i], self.depth[vertex])
		if (
			self.parent[i] != None and is_articulation) or (
			self.parent[i] == None and child_count > 1):
			self.articulation[i] = True

vertices = 5

graph = Graph(vertices)
graph.adj = [[1], [0, 4], [4, 3], [4, 2], [1, 2, 3]]  # adjacency list
graph.find_articulation(0,1)
print(graph.articulation)