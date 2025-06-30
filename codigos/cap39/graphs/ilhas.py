from queue import PriorityQueue

def dijkstra(graph: list, size: int, start: int):
    D = [float('inf')] * size
    P = [None] * size
    visited = [False] * size

    Q = PriorityQueue()
    Q.put((0, start))
    D[start] = 0

    lower = float('inf')
    higher = -float('inf')

    while not Q.empty():
        weight, u = Q.get()
        if not visited[u]:
            visited[u] = True
            if u != start:
                if weight < lower:
                    lower = weight
                if weight > higher:
                    higher = weight
                
            for neighbor, w in graph[u]:
                # relax vertex
                if ((w + D[u] < D[neighbor])):
                    Q.put((w + D[u], neighbor))
                    D[neighbor] = w + D[u]
                    P[neighbor] = u
    
    return higher - lower

def main():
    
    N, M = map(int, input().strip().split())
    G = [[] for _ in range(N)]
    for m in range(M):
        u, v, d = map(int, input().strip().split())

        G[u - 1].append((v - 1, d))
        G[v - 1].append((u - 1 , d))

    s = int(input())

    result = dijkstra(G, N, s-1)
    print(result)

main()