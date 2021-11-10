import time


def MemoizationFibonacci(n):  # 1 이상의 자연수 n
    dp = [0]*(n+1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


s = time.time()
ans = MemoizationFibonacci(1)
e = time.time() - s
print("답 : ", ans, "// 걸린 시간 : ", e)
s = time.time()
ans = MemoizationFibonacci(10)
e = time.time() - s
print("답 : ", ans, "// 걸린 시간 : ", e)
s = time.time()
ans = MemoizationFibonacci(100)
e = time.time() - s
print("답 : ", ans, "// 걸린 시간 : ", e)
