import sys

N = int(sys.stdin.readline())
stack = []

result = 0

for _ in range(N):
    word = sys.stdin.readline()
    cnt_A = 0
    cnt_B = 0
    cnt = 0

    for i in range(len(word)-1):
        if cnt_A == 0 and word[i]=='A':
            stack.append(word[i])
            cnt_A = 1
        elif cnt_B == 0 and word[i]=='B':
            stack.append(word[i])
            cnt_B = 1
        else:
            if len(stack) != 0:
                if word[i] == stack.pop():
                    cnt += 1
                    if word[i] == 'A':
                        cnt_A = 0
                    else:
                        cnt_B = 0
                else:
                    break
            else:
                break

    if cnt == (len(word)-1)/2:
        result += 1

print(result)
    
