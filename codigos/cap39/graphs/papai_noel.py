from queue import PriorityQueue

def prim(graph: list, size: int):
    res = 0
    visited = [False] * size
    C = [float('inf')] * size
    Q = PriorityQueue()
    visited[0] = True
    for neighbor, weight in graph[0]:
        Q.put((weight, neighbor))
    
    C[0] = 0

    while not Q.empty():
        weight, u = Q.get()
        if not visited[u]:
            visited[u] = True
            res += weight
            for neighbor, w in graph[u]:
                if (not visited[neighbor]) and (w < C[neighbor]):
                    Q.put((w, neighbor))
                    C[neighbor] = w
    return res

def main():
    while True:
        M,N = map(int, input().strip().split())

        if M == 0 and N == 0:
            break

        # criar o grafo G
        G = [[] for _ in range[M]]
        for n in range(N):
            u, v, d = map(int, input().strip().split())

            G[u].append((v, d))
            G[v].append((u, d))

        result = prim(G, M)
        print(result)

main()
