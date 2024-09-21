import sys

white = []
black = []

for _ in range(31):
    w, b = map(int, sys.stdin.readline().split())

    white.append(w)
    black.append(b)

white.sort(reverse=True)
black.sort(reverse=True)

print(white)
print(black)

cnt_w = 0
cnt_b = 0
team = []

while True:
    if len(team) == 30:
        break

    if cnt_w >= 15:
        team.append(black[cnt_b])
        cnt_b += 1
    elif cnt_b >= 15:
        team.append(white[cnt_w])
        cnt_w += 1
    else:
        if white[cnt_w] >= black[cnt_b]:
            team.append(white[cnt_w])
            cnt_w += 1
        else:
            team.append(black[cnt_b])
            cnt_b += 1

print(sum(team))

