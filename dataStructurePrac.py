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
