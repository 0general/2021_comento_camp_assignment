import sys
import random
import time

sys.setrecursionlimit(10**5)


def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    ans = []

    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    while i < len(left):
        ans.append(left[i])
        i += 1
    while j < len(right):
        ans.append(right[j])
        j += 1
    return ans


N = 10000

# 오름차순
ls = list(range(N))

start = time.time()
s = mergeSort(ls)
end = time.time() - start

print("오름차순 배열의 합병 정렬 실행 시간 (N = %d) : %0.5f" % (N, end))


# 내림차순
ls = list(range(N-1, -1, -1))

start = time.time()
s = mergeSort(ls)
end = time.time() - start
print("내림차순 배열의 합병 정렬 실행 시간 : %0.5f" % (end))

# 섞인 배열
ls = []
for k in range(N):
    ls.append(random.randint(1, N))

start = time.time()
s = mergeSort(ls)
end = time.time() - start
print("균등 배열의 합병 정렬 실행 시간 : %0.5f" % (end))
