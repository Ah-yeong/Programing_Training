# list 시간복잡도 O(n), insert, pop -> 시간 초과
# stack 2개 사용하여 시간 단축

from sys import stdin

arr_left = list(stdin.readline().strip())
arr_right = []
M = int(stdin.readline())

for _ in range(M):
    command = stdin.readline().split()
    if command[0] == "L":
        if len(arr_left) != 0:
            arr_right.append(arr_left.pop())
    elif command[0] == "D":
        if len(arr_right) != 0:
            arr_left.append(arr_right.pop())
    elif command[0] == "B":
        if len(arr_left) != 0:
            arr_left.pop()
    elif command[0] == "P":
        arr_left.append(command[1])

arr_right.reverse()
arr_left.extend(arr_right) 

print("".join(arr_left))


