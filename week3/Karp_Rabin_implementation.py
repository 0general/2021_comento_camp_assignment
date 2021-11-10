import random

def rabin_karp(s, t):  # s is in t?
    n = len(s)
    h_s = hash(s)
    for i in range(len(t)-n+1):
        temp = t[i:i+n]
        h_t = hash(temp)
        if h_s == h_t:
            if s == temp:
                return i
    return -1


alpha = ['A', 'B', 'C', 'D', 'E']

for i in range(4):
    t = "".join(random.choices(alpha, k=26))
    s = "".join(random.choices(alpha, k=3))
    print("검사 문자열 t : %s" % (t))
    print("매칭 문자열 s : %s" % (s))
    result = rabin_karp(s, t)
    if result == -1:
        print("s는 t의 부분문자열이 아닙니다.")
    else:
        print("s는 t의 %d 번째 위치에서 등장합니다." % (result))
