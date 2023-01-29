from collections import deque
import heapq


def bfs(start):
    global adl
    dq = deque([start])
    while len(dq):
        node = dq.popleft()
        for next_node in adl[node]:
            # 探索する条件
            if True:
                dq.append(next_node)
