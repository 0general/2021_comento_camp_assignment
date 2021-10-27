import heapq
INF = int(1e9)


def Dijkstra(graph, start):  # graph[i][j] = weight (from i to j)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = [0, -1]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now][0] < dist:  # visited
            continue
        for i, c in enumerate(graph[now]):
            if c != INF and i != now:
                cost = dist + c
                if cost < distance[i][0]:
                    distance[i] = [cost, now]
                    heapq.heappush(q, (cost, i))


start = 0
graph = [[0, 3, 1, 6, INF],
         [3, 0, 1, 2, 1],
         [1, 1, 0, 7, INF],
         [6, 2, 7, 0, 2],
         [INF, 1, INF, 2, 0]]
distance = [[INF, -1] for _ in range(len(graph))]  # [cost, previous node]
Dijkstra(graph, start)

for i in range(1, len(graph)):
    path = [i]
    pre = distance[i][1]
    while pre != -1:
        path.append(pre)
        pre = distance[pre][1]
    path.reverse()
    print("0번 노드에서 %d번 노드까지 최단 거리 : %d" % (i, distance[i][0]))
    print("경로 :", end=" ")
    print(*path)
