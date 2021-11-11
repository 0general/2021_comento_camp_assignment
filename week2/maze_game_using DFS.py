import random
import time


def dfs():
    while stack:
        x, y = stack[-1]
        flag = True
        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 'X':
                visited[nx][ny] = True
                if graph[nx][ny] == 'E':
                    print("찾았습니다!")
                    return
                stack.append((nx, ny))
                flag = False
        if flag:
            stack.pop()


# 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# n X n 행렬
n = 20  # 1000
visited = [[False]*n for _ in range(n)]
visited[0][0] = True
stack = [(0, 0)]
graph = []
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
dfs()
end = time.time() - start
print("dfs 미로 탐색 소요 시간 : ", end)
