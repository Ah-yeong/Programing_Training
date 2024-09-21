import sys

N = int(sys.stdin.readline())
s_num =[]

for i in range(N):
    num = input()
    s_num.append(num)

def sum_num(n):
    sum = 0
    for i in n:
        if i.isdigit() == 1:
            sum += int(i)
        else:
            continue
    return sum

s_num.sort(key= lambda x:(len(x), sum_num(x), x))

for i in s_num:
    print(i)

