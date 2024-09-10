class Vertex:
    def __init__(self, color, parent):
        self.color = color
        self.parent = parent
        self.d = 0
        self.f = None

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

class Graph:
    def __init__(self, num_vertex, num_edges):
        self.num_vertex = num_vertex
        self.num_edges = num_edges
        self.vertex_list = []
        self.time = 0
        self.init_matrix()

    def init_matrix(self):
        self.matrix = [[0 for col in range(self.num_vertex)] for row in range(self.num_vertex)]
    
    def add_edge(self, edge, weight = 1):
        self.matrix[edge.u][edge.v] = weight
    
    def get_neighbor(self, u):
        adj = []
        for v in self.matrix[u]:
            if v == 1:
                adj.append(v)
        return adj
    
    def dfs(self):
        for _ in range(self.num_vertex):
            v = Vertex('white', None)
            self.vertex_list.append(v)
        for u in self.vertex_list:
            if u.color == 'white':
                self.dfs_visit(self, u)

    def dfs_visit(self, u):
        self.time += 1
        u.d = self.time
        u.color = 'gray'
        for v in self.get_neighbor(u):
            if v.color == 'white':
                v.parent = u
                self.dfs_visit(self, v)
        u.color = 'black'
        self.time += 1
        u.f = self.time



    
