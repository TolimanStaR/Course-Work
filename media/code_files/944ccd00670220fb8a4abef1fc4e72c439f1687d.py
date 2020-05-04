import heapq

uptime = list(map(int, input().split()))
parstime = list(map(int, input().split()))
stans = list(map(int, input().split()))

s, n, e = map(int, input().split())

graph = {}
for i in range(e):
    x, y, w = map(int, input().split())
    if x in graph:
        graph[x].append((y, w))
    else:
        graph[x] = [(y, w)]

    if y in graph:
        graph[y].append((x, w))
    else:
        graph[y] = [(x, w)]

keys = {i: float('inf') for i in range(n + 1)}
que = [(0, s)]
visited = {s}
while que:
    new_point = heapq.heappop(que)
    point = new_point[1]
    wp = new_point[0]
    for p in graph[point]:
        if p[0] not in visited:
            if wp + p[1] < keys[p[0]]:
                keys[p[0]] = wp + p[1]
                heapq.heappush(que, (keys[p[0]], p[0]))
    visited.add(point)

for stan, ut, pt,  in zip(stans, uptime, parstime):
    if keys[stan] + ut > pt:
        print("No")
    else:
        print("Yes", keys[stan])
