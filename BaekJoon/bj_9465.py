import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    score = [[0]*n for _ in range(2)]

    score[0][0] = sticker[0][0]
    score[1][0] = sticker[1][0]

    if n != 1:
        score[0][1] = sticker[0][1] + score[1][0]
        score[1][1] = sticker[1][1] + score[0][0]

        for i in range(2, n):
            score[0][i] =  max(score[1][i-2], score[1][i-1]) + sticker[0][i]
            score[1][i] = max(score[0][i-2], score[0][i-1]) + sticker[1][i]

    print(max(map(max,score)))
