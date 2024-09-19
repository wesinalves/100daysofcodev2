from queue import PriorityQueue

def prim(graph: list, size: int):
    res = 0
    visited = [False] * size
    Q = PriorityQueue()
    visited[0] = True
    for neighbor, weigth in graph[0]:
        Q.put((weigth, neighbor))
    
    while not Q.empty():
        weigth, u = Q.get()
        if not visited[u]:
            visited[u] = True
            res += weigth
            for neighbor, w in graph[u]:
                if not visited[neighbor]:
                    Q.put((w, neighbor))
    return res

def main():
    G = []
    V = []
    while True:
        M,N = map(int, input().strip().split())
        
        if M == 0 and N == 0:
            break
        
        # implementar o grafo G
        G = [[] for _ in range(M)]
        for n in range(N):
            u,v,d = map(int, input().strip().split())

            G[u].append((v, d))
            G[v].append((u, d))
        
        # invocar o algoritmo de prim
        result = prim(G, M)
        print(result)

main()