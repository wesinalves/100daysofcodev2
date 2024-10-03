from queue import PriorityQueue

def dijkstra(graph: list, size: int, start: int):
    D = [float('inf')] * size
    P = [None] * size
    visited = [False] * size
    Q = PriorityQueue()
    # for neighbor, weight in graph[start]:
    #     Q.put((weight, neighbor))
    #     D[neighbor] = weight
    Q.put((0,0))
    
    D[start] = 0
    menor = float('inf')
    maior = -float('inf')
    while not Q.empty():
        weight, u = Q.get()
        if not visited[u]:
            visited[u] = True
            if u != start:
                if weight < menor:
                    menor = weight
                if weight > maior:
                    maior = weight
            for neighbor, w in graph[u]:
                # relax vertex
                if ((w + D[u]) < D[neighbor]):
                    Q.put((w + D[u], neighbor))
                    D[neighbor] = w + D[u]
                    P[neighbor] = u

    return maior - menor

def main():
    
    N, M = map(int, input().strip().split())
    #N = 4
    #M = 5

    # if M == 0 and N == 0:
    #     break

    # criar o grafo G
    # input = " \
    #         2 1 5 \n\
    #         1 3 4 \n\
    #         2 3 6 \n\
    #         4 2 8 \n\
    #         3 4 12\
    #         "
    G = [[] for _ in range(N)]
    for m in range(M):
    #for m in input.split('\n'):
        #u, v, d = map(int, m.split())
        u, v, d = map(int, input().strip().split())

        G[u - 1].append((v - 1, d))
        G[v - 1].append((u - 1 , d))

    #print(m)
    s = int(input())
    #s = 1

    result = dijkstra(G, N, s-1)
    print(result)

main()