import time


def RecursiveFibonacci(n):  # 자연수 n
    if n == 1 or n == 2:
        return 1
    else:
        return RecursiveFibonacci(n-1) + RecursiveFibonacci(n-2)


s = time.time()
ans = RecursiveFibonacci(1)
e = time.time() - s
print("답 : ", ans, "// 걸린 시간 : ", e)
s = time.time()
ans = RecursiveFibonacci(10)
e = time.time() - s
print("답 : ", ans, "// 걸린 시간 : ", e)
s = time.time()
ans = RecursiveFibonacci(100)
e = time.time() - s
print("답 : ", ans, "// 걸린 시간 : ", e)
