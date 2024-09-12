from graph import Graph, Vertex

T = int(input())

for _ in range(T):
    s = int(input())
    v, e = input().split(' ')
    
    v = int(v)
    e = int(e)
    
    G = Graph(v, e)
    
    vertex_array = []
    for i in range(G.num_vertex):
        vertex_array.append(Vertex(i, 'white', None))

    for i in range(e):
        u, v = input().split(' ')
        u = int(u)
        v = int(v)
        G.add_edges(vertex_array[u], vertex_array[v])


    G.dfs_from_source(s)

    print(G.time - 2)