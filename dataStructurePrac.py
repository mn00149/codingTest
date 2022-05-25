stack = []
# 5삽입 6삽입 7삽입 삭제 9삽입 6삽입 삭제
stack.append(5)
stack.append(6)
stack.append(7)
stack.pop()
stack.append(9)
stack.append(6)
stack.pop()
print(stack)
print(stack[::-1])
