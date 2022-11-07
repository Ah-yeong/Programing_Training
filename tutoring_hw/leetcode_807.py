grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

result = 0
row_max = []
col_max = []
for i in range(len(grid)):
    row_max.append(max(grid[i]))

for i in range(len(grid[0])):
    m = -1
    for j in range(len(grid)):
        m = max(m, grid[j][i])
    col_max.append(m)
        
print(row_max)
print(col_max)
            
for i in range(len(grid)):
    for j in range(len(grid[0])):
        m = min(row_max[i], col_max[j])
        if m > grid[i][j]:
            result += m - grid[i][j]