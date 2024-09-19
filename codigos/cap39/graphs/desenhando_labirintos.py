class Vertex:
    def __init__(self, id, color, parent):
        self.id = id
        self.color = color
        self.parent = parent
        self.d = 0
        self.f = None

class Graph:
    def __init__(self, num_vertex: int, num_edges: int):
        self.num_vertex = num_vertex
        self.num_edges = num_edges
        self.vertex_list = [[] for _ in range(num_vertex)]
        self.time = 0

    def add_edges(self, u: Vertex, v: Vertex, non_direct = True):
        uids = [x.id for x in self.vertex_list[u.id]]
        if u.id not in uids:
            self.vertex_list[u.id].append(u)
        if v.id not in uids:
            self.vertex_list[u.id].append(v)
        
        if non_direct:
            vids = [y.id for y in self.vertex_list[v.id]]
            if v.id not in vids:
                self.vertex_list[v.id].append(v)
            if u.id not in vids:
                self.vertex_list[v.id].append(u)
    

    def get_neighbor(self, u: Vertex):
        return self.vertex_list[u.id][1:]
    
    def dfs(self):
        for adj in self.vertex_list:
            u = adj[0]
            if u.color == 'white':
                self.dfs_visit(u)

    def dfs_from_source(self, s: int):
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


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):

        s = int(input())
        V, A = input().split(' ')

        V = int(V)
        A = int(A)

        G = Graph(V, A)

        vertex_array = []
        for i in range(G.num_vertex):
            vertex_array.append(Vertex(i, 'white', None))

        # read edges
        for j in range(A):
            u, v = input().split(' ')
            u = int(u)
            v = int(v)
            G.add_edges(vertex_array[u], vertex_array[v])

        
        G.dfs_from_source(s)

        print(G.time)


        
