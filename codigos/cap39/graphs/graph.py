class Vertex:
    def __init__(self, id, color, parent):
        self.id = id
        self.color = color
        self.parent = parent
        self.d = 0
        self.f = None

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

class Graph:
    def __init__(self, num_vertex: int, num_edges: int):
        self.num_vertex = num_vertex
        self.num_edges = num_edges
        self.vertex_list = [[] for _ in range(num_vertex)] # adjacent list
        self.time = 0
    
    def add_edges(self, u: int, v: int):
        vertex_u = Vertex(u, 'white', None)
        vertex_v = Vertex(v, "white", None)
        # insert u if not in list
        uids = [x.id for x in self.vertex_list[u]]
        if u not in uids:
            self.vertex_list[u].append(vertex_u)
        if v not in uids:
            self.vertex_list[u].append(vertex_v)

        # works for non direct graph only
        vids = [y.id for y in self.vertex_list[v]]
        if v not in vids:
            self.vertex_list[v].append(vertex_v)
        if u not in vids:
            self.vertex_list[v].append(vertex_u)
    
    def get_neighbor(self, u: Vertex):
        # the first vertex is out
        return self.vertex_list[u.id][1:]
    
    def dfs(self):
        for adj in self.vertex_list:
            u = adj[0]
            if u.color == 'white':
                self.dfs_visit(self, u)

    def dfs_visit(self, u: Vertex):
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

if __name__ == "__main__":
    G = Graph(16, 15)
    G.add_edges(0, 4)
    G.add_edges(2, 3)
    G.add_edges(6, 2)
    G.add_edges(8, 9)
    G.add_edges(8, 12)
    G.add_edges(10, 9)
    G.add_edges(14, 15) 
    G.add_edges(14, 10)
    G.add_edges(6, 5)
    G.add_edges(10, 11)
    G.add_edges(11, 7)
    G.add_edges(4, 8)
    G.add_edges(0, 1)
    G.add_edges(1, 2)
    G.add_edges(12, 13)

    print(G.vertex_list[0])

    for v in range(G.num_vertex):
        for u in G.vertex_list[v]:
            print(f'{u.id} -> ', end='\t')
        print()



    
