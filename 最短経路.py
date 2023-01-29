import heapq


def dijkstra(start):
    global costs
    hq = [[0, start]]
    heapq.heapify(hq)
    costs[start] = 0
    while len(hq):
        cost, node = map(int, heapq.heappop(hq))  # [cost,idx]
        for next_cost, next_node in enumerate(adl[node]):
            sum_cost = cost+next_cost
            if sum_cost < costs[next_node]:
                costs[next_node] = sum_cost
                heapq.heappush(hq, [sum_cost, next_node])


def floyd(n):
    global dist
    for i in range(n):
        dist[i][i] = 0
    for mid in range(n):  # 中間
        for start in range(n):  # 始点
            for end in range(n):  # 終点
                dist[start][end] = min(
                    dist[start][end], dist[start][mid]+dist[mid][end])
