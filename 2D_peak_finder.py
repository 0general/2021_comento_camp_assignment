
# array = [[1, 3, 2, 4, 3], [4, 6, 4, 5, 2],[7, 7, 12, 9, 1], [10, 11, 13, 2, 0]]
array = [[10, 8, 10, 10], [14, 13, 12, 11], [15, 9, 11, 21], [16, 17, 19, 20]]
n, m = len(array), len(array[0])

left, right = 0, m-1
while left <= right:
    mid = (left+right)//2
    mx = 0
    for i in range(1, n):
        if array[i][mid] > array[mx][mid]:
            mx = i
    if mid-1 >= 0:
        if array[mx][mid-1] > array[mx][mid]:
            right = mid-1
            continue
    if mid+1 < n:
        if array[mx][mid+1] > array[mx][mid]:
            left = mid + 1
            continue
    print("2D-peak : (%d, %d)" % (mx, mid))
    break
