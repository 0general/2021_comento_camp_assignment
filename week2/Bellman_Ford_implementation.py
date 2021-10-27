def Bellman_Ford(edges, s):
    # initialize
    s = node[s]
    for v in range(n):
        d[v] = INF
    d[s] = 0

    # main
    for i in range(n):
        for edge in edges:
            now, next, cost = edge
            now = node[now]
            next = node[next]
            if d[now] != INF and d[next] > d[now] + cost:
                d[next] = d[now] + cost
    for edge in edges:
        now, next, cost = edge
        now = node[now]
        next = node[next]
        if d[next] > d[now] + cost:
            return False
    return True


INF = int(1e9)
n, m = 5, 8
node = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
edges = [('A', 'B', -1),
         ('A', 'C', 4),
         ('B', 'C', 3),
         ('B', 'D', 2),
         ('B', 'E', 2),
         ('D', 'B', 1),
         ('D', 'C', 5),
         ('E', 'D', -3)]


for start in node:
    d = [INF]*n
    pos = Bellman_Ford(edges, start)
    if pos:
        for v in node:
            if v != start:
                if d[node[v]] != INF:
                    print("between %s and %s shortest distance : %d" %
                          (start, v, d[node[v]]))
                else:
                    print("between %s and %s shortest distance : INFINITY" %
                          (start, v))
    else:
        print("Starting at node %s contains negative-weight." % (start))
