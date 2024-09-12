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
        u.d = self.time
        u.color = 'gray'
        adjs = self.get_neighbor(u)
        for v in adjs:
            if v.color == 'white':
                v.parent = u
                self.dfs_visit(v)
        u.color = 'black'
        self.time += 1
        u.f = self.time

#if __name__ == "__main__":
    #for j in range (G.num_edges):
    # G.add_edges(vertex_array[0], vertex_array[1], False)
    # G.add_edges(vertex_array[0], vertex_array[3], False)
    # G.add_edges(vertex_array[1], vertex_array[4], False)
    # G.add_edges(vertex_array[2], vertex_array[4], False)
    # G.add_edges(vertex_array[2], vertex_array[5], False)
    # G.add_edges(vertex_array[3], vertex_array[1], False)
    # G.add_edges(vertex_array[4], vertex_array[3], False)
    # G.add_edges(vertex_array[5], vertex_array[5], False)

    # G.add_edges(vertex_array[0], vertex_array[4])
    # G.add_edges(vertex_array[2], vertex_array[3])
    # G.add_edges(vertex_array[6], vertex_array[2])
    # G.add_edges(vertex_array[8], vertex_array[9])
    # G.add_edges(vertex_array[10], vertex_array[9])
    # G.add_edges(vertex_array[8], vertex_array[12])
    # G.add_edges(vertex_array[14], vertex_array[15]) 
    # G.add_edges(vertex_array[14], vertex_array[10])
    # G.add_edges(vertex_array[6], vertex_array[5])
    # G.add_edges(vertex_array[10], vertex_array[11])
    # G.add_edges(vertex_array[11], vertex_array[7])
    # G.add_edges(vertex_array[4], vertex_array[8])
    # G.add_edges(vertex_array[0], vertex_array[1])
    # G.add_edges(vertex_array[1], vertex_array[2])
    # G.add_edges(vertex_array[12], vertex_array[13])

    # G.add_edges(vertex_array[1], vertex_array[2])
    # G.add_edges(vertex_array[1], vertex_array[4])
    # G.add_edges(vertex_array[4], vertex_array[7])
    # G.add_edges(vertex_array[7], vertex_array[8])
    # G.add_edges(vertex_array[4], vertex_array[1])
    # G.add_edges(vertex_array[4], vertex_array[3])

    #G.dfs_from_source(s)
    #G.dfs()

    #print(G.time - 2)
    #print(G.vertex_list[1][0].d)
    #print(G.vertex_list[1][0].f)
    #print(G.vertex_list[1][0].color)

    # for v in range(G.num_vertex):
    #     for u in G.vertex_list[v]:
    #         print(f'{u.id} -> ', end='\t')
    #     print()