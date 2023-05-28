def greedy_search(arr):
    
    n = len(arr)
    sorted_arr = []
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        sorted_arr.append(arr[min_idx])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return sorted_arr

arr = [4, 2, 1, 7, 5, 0, 9]
sorted_arr = greedy_search(arr)
print(sorted_arr)