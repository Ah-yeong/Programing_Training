import sys
N, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
gap = []

for i in range(N-1):
    gap.append(num[i+1] - num[i])
    
gap.sort()
result = 0
for i in range(N-K): # 0 ~ N-2-(K-1)까지
    result += gap[i]

print(result)

