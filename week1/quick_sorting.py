import sys
import random
import time

sys.setrecursionlimit(10**5)


def quickSort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[start]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 right -= 1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교환
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(array, start, right-1)
    quickSort(array, right+1, end)


N = 1000

# 오름차순
ls = list(range(N))
start = time.time()
quickSort(ls, 0, N-1)
end = time.time() - start
print("오름차순 배열의 퀵 정렬 실행 시간 (N = %d) : %0.5f" % (N, end))


# 내림차순
ls = list(range(N-1, -1, -1))

start = time.time()
quickSort(ls, 0, N-1)
end = time.time() - start
print("내림차순 배열의 퀵 정렬 실행 시간 : %0.5f" % (end))

# 섞인 배열
ls = []
for k in range(N):
    ls.append(random.randint(1, N))

start = time.time()
quickSort(ls, 0, N-1)
end = time.time() - start
print("균등 배열의 퀵 정렬 실행 시간 : %0.5f" % (end))
