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
    
    def add_edges(self, u: Vertex, v: Vertex, non_direct = True):
        #vertex_u = Vertex(u, 'white', None)
        #vertex_v = Vertex(v, 'white', None)
        # insert u if not in list
        uids = [x.id for x in self.vertex_list[u.id]]
        if u.id not in uids:
            self.vertex_list[u.id].append(u)
        if v.id not in uids:
            self.vertex_list[u.id].append(v)

        if non_direct:
            # works for non direct graph only
            vids = [y.id for y in self.vertex_list[v.id]]
            if v.id not in vids:
                self.vertex_list[v.id].append(v)
            if u.id not in vids:
                self.vertex_list[v.id].append(u)
        
    def get_neighbor(self, u: Vertex):
        # the first vertex is out
        return self.vertex_list[u.id][1:]
    
    def dfs(self):
        for adj in self.vertex_list:
            u = adj[0]
            if u.color == 'white':
                self.dfs_visit(u)
    
    def dfs_from_source(self, s: int):
        self.time = 0
        u = self.vertex_list[s][0]
        if u.color == 'white':
            self.dfs_visit(u)

    def dfs_visit(self, u: Vertex):
        self.time += 1
        #u.d = self.time
        self.vertex_list[u.id][0].d = self.time
        self.vertex_list[u.id][0].color = 'gray'
        adjs = self.get_neighbor(u)
        for v in adjs:
            if v.color == 'white':
                self.vertex_list[v.id][0].parent = u
                self.dfs_visit(v)
        self.vertex_list[u.id][0].color = 'black'
        self.time += 1
        self.vertex_list[u.id][0].f = self.time

if __name__ == "__main__":
    # G = Graph(16, 15)
    # G.add_edges(0, 4)
    # G.add_edges(2, 3)
    # G.add_edges(6, 2)
    # G.add_edges(8, 9)
    # G.add_edges(8, 12)
    # G.add_edges(10, 9)
    # G.add_edges(14, 15) 
    # G.add_edges(14, 10)
    # G.add_edges(6, 5)
    # G.add_edges(10, 11)
    # G.add_edges(11, 7)
    # G.add_edges(4, 8)
    # G.add_edges(0, 1)
    # G.add_edges(1, 2)
    # G.add_edges(12, 13)

    G = Graph(6, 8)
    vertex0 = Vertex(0, 'white', None)
    vertex1 = Vertex(1, 'white', None)
    vertex2 = Vertex(2, 'white', None)
    vertex3 = Vertex(3, 'white', None)
    vertex4 = Vertex(4, 'white', None)
    vertex5 = Vertex(5, 'white', None)

    G.add_edges(vertex0, vertex1, False)
    G.add_edges(vertex0, vertex3, False)
    G.add_edges(vertex1, vertex4, False)
    G.add_edges(vertex2, vertex4, False)
    G.add_edges(vertex2, vertex5, False)
    G.add_edges(vertex3, vertex1, False)
    G.add_edges(vertex4, vertex3, False)
    G.add_edges(vertex5, vertex5, False)


    G.dfs_from_source(0)
    #G.dfs()

    print(G.time)
    print(G.vertex_list[0][0].d)
    print(G.vertex_list[0][0].f)
    print(G.vertex_list[0][0].color)

    # for v in range(G.num_vertex):
    #     for u in G.vertex_list[v]:
    #         print(f'{u.id} -> ', end='\t')
    #     print()



    
