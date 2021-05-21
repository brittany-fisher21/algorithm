def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1] = arr[j+1], arr [j]

arr = [3, 1, 4, 2]
arr = [1, 3, 4, 2]
arr = [1, 3, 2, 4]
arr = [1, 2, 3, 4]

bubbleSort(arr)

print("sorted array is:")
for i in range (len(arr)):
    print("d%" %arr[i]),

    #didn't work

