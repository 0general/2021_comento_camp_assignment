import random
import time
import heapq


def dijkstra():
    h = []
    heapq.heappush(h, (0, (0, 0)))
    dist[0][0] = 0
    while h:
        d, now = heapq.heappop(h)
        x, y = now
        if dist[x][y] < d:
            continue
        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 'X':
                cost = d + 1
                if graph[nx][ny] == 'E':
                    print("찾았습니다!")
                    return
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heapq.heappush(h, (cost, (nx, ny)))


# 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# n X n 행렬
n = 20  # 1000
visited = [[False]*n for _ in range(n)]
graph = []
INF = int(1e9)
dist = [[INF]*n for i in range(n)]


code = ['O', 'X']
for i in range(n):
    if i == 0:
        graph.append(['S']+random.choices(code, weights=[10, 3], k=n-1))
    elif i == n-1:
        graph.append(random.choices(code, weights=[10, 2], k=n-1)+['E'])
    else:
        graph.append(random.choices(code, weights=[5, 1], k=n))

for i in range(n):
    print(graph[i])

start = time.time()
dijkstra()
end = time.time() - start
print("Dijkstra 미로 탐색 소요 시간 : ", end)
