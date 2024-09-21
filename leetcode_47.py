def permutation():
    if len(temp) == len(nums):
        print(temp)
        return temp

    for i in range(len(nums)):
        if visited[i] == False:
            temp.append(nums[i])
            visited[i] = True
            permutation()
            temp.pop()
            visited[i] = False

if __name__ == "__main__":
    nums = [1,1,3]

    visited = [False for _ in range(len(nums))]
    result = []
    temp = []

    result.append(permutation())
    print(result)