import sys

S = list(sys.stdin.readline())

temp = S[0]
cnt = 0

for i in range(1, len(S)-1):
    if temp != S[i] and S[i-1] != S[i]:
        cnt += 1

print(cnt)