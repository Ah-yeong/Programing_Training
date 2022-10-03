def sequential_search(target, data):
    for i in range(len(data)):
        if data[i] == target:
            return i+1
    return None

def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid 
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

if __name__ == "__main__":
    arr = [1,5,6,2,9,10,15,13]
    target = 9
    idx = binary_search(target, arr)
    if idx:
        print(arr[idx])
    else:
        print("찾으시는 타겟 {}가 없습니다".format(target))
        
    print("{}번째에서 데이터 탐색 종료.".format(sequential_search(target, arr)))
