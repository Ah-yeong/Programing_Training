def insertionSort(list):  
    for i in range(1, len(list)):  
        value = list[i]  
  
        j = i - 1  
        while j >= 0 and value < list[j]:  
            list[j + 1] = list[j]  
            j -= 1  
        list[j + 1] = value  
    return list  
  
def selectionSort(list):
    size = len(arr)
    for i in range(size):
        min_index = i
 
        for j in range(i + 1, size):
            if list[j] < list[min_index]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]
        return list
        
def mergeSort(list):
    if len(list) > 1:
        r = len(list)//2
        L = list[:r]
        M = list[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            list[k] = M[j]
            j += 1
            k += 1
            
    return list

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    return array

def countingSort(arr):
    count = [0] * (max(arr) + 1)

    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i-1]

    result = [0] * (len(arr))

    for num in arr:
        idx = count[num]
        result[idx - 1] = num
        count[num] -= 1
        
    return result

arr = [2,1,5,8,2,9,10]

print("insertion sort :", insertionSort(arr)) 
print("selection sort :", selectionSort(arr)) 
print("merge sort :", mergeSort(arr)) 
print("quick sort :", quickSort(arr, 0, len(arr) - 1))
print("counting sort :", countingSort(arr))
