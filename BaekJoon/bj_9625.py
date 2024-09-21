import sys

K = int(sys.stdin.readline())
AB = []
AB.append("A")

for _ in range(K):
    for i in len(AB):
        if(AB[i] == "A"):
            AB[i] == "B"
        else:
            AB.insert(i, "A")
            i += 1

cnt1 = cnt2= 0

for i in AB:
    if(i == "A"):
        cnt1 += 1
    else:
        cnt2 += 1

print(cnt1, cnt2)

