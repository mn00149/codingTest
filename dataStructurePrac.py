# -*- coding: utf-8 -*-

# Stack
from collections import deque
stack = []
# 5삽입 6삽입 7삽입 삭제 9삽입 6삽입 삭제
stack.append(5)
stack.append(6)
stack.append(7)
stack.pop()
stack.append(9)
stack.append(6)
stack.pop()
print(stack)  # 최하단부터 출력
print(stack[::-1])  # 최상단부터 출력
# Queue
queue = deque()
queue.append(1)
queue.append(3)
queue.append(5)
queue.append(7)
queue.append(2)
queue.popleft()
queue.append(1)
queue.popleft()
queue.popleft()
queue.reverse()
print(queue)
# 인접행렬
inf = 9999999999
AM = [
    [0, 7, 5],
    [7, 0, inf],
    [5, inf, 0]
]
graph = [[] for _ in range(3)]
graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))

# 재귀함수를 이용한 팩토리얼 구현


def factorialRecursive(n):
    if n <= 1:
        return 1
    return n*factorialRecursive(n-1)


visted = [False]*9

graph2 = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


def dfs(v, visted, graph):
    visted[v] = True
    print(v)
    for i in graph[v]:
        if not visted[i]:
            dfs(i, visted, graph)


# dfs(1, visted, graph2)


def bfs(v, visted, graph):
    queue = deque([v])
    visted[v] = True

    while(queue):
        v = queue.popleft()
        print(v)
        for i in graph[v]:
            if not visted[i]:
                queue.append(i)
                visted[i] = True


bfs(1, visted, graph2)
