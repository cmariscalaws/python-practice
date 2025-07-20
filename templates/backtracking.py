# backtracking
def backtracking(arr, i, n):
    if i == n:
        print(arr)
        return
    for j in range(i, n):
        arr[i], arr[j] = arr[j], arr[i]
        backtracking(arr, i + 1, n)
        arr[i], arr[j] = arr[j], arr[i]
arr = [1, 2, 3, 4, 5]