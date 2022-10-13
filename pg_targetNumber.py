answer = 0

def dfs(num, s, depth, cnt, target):
    global answer
    
    if cnt == depth:
        if s == target:
            answer += 1
            
    else:        
        dfs(num, s+num[cnt], depth, cnt+1, target)
        dfs(num, s-num[cnt], depth, cnt+1, target)
            

def solution(numbers, target):
    global answer
    depth = len(numbers)
    dfs(numbers, 0, depth, 0, target)

    return answer