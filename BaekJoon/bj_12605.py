import sys

N = int(sys.stdin.readline())

for i in range(N):
    arr = list(sys.stdin.readline().rstrip().split())
    
    arr.reverse()
    print("Case #%d: %s" %(i+1, " ".join(arr)))
