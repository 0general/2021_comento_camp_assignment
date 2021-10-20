import random
import time


def insertionSort(ls):
    n = len(ls)
    for i in range(1, n):
        temp, j = ls[i], i
        while ls[j-1] > temp:
            if j == 0:
                break
            ls[j] = ls[j-1]
            j -= 1
        ls[j] = temp


N = 10000000

# 오름차순
ls = list(range(N+1))

start = time.time()
insertionSort(ls)
end = time.time() - start

print("오름차순 배열의 삽입 정렬 실행 시간 (N = %d): %0.5f" % (N, end))


# 내림차순
ls = list(range(N, -1, -1))

start = time.time()
insertionSort(ls)
end = time.time() - start

print("내림차순 배열의 삽입 정렬 실행 시간 : %0.5f" % (end))

# 섞인 배열
ls = []
for k in range(N):
    ls.append(random.randint(1, N))

start = time.time()
insertionSort(ls)
end = time.time() - start

print("균등 배열의 삽입 정렬 실행 시간 : %0.5f" % (end))
