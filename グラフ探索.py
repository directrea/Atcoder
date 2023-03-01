from collections import deque


def bfs(start):
    global adl
    dq = deque([start])
    while len(dq):
        node = dq.popleft()
        for next_node in adl[node]:
            # 探索する条件
            if True:
                dq.append(next_node)


def TopologicalSort(adl):
    visited = [0]*len(adl)
    indeg = [0]*len(adl)
    for v in adl:
        for node in v:
            indeg[node] += 1
    v = []
    for i in range(len(indeg)):
        if indeg[i] == 0:
            v.append(i)
    res = []
    while len(v):
        top = v.pop()
        res.append(top)
        visited[top] = 1
        for node in adl[top]:
            if visited[node]:  # 閉路がある場合
                return None
            indeg[node] -= 1
            if indeg[node] == 0:
                v.append(node)
    return res
